from typing import Iterator, List, Optional, Sequence, Set, Tuple, Type, TypeVar, Union

from sqlalchemy import inspect, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Load, Mapper, RelationshipProperty, Session, joinedload, selectinload
from sqlalchemy.orm.scoping import ScopedSession
from sqlalchemy.orm.strategy_options import _UnboundLoad
from sqlalchemy.sql import Select
from strawberry.types import Info
from strawberry.types.nodes import FragmentSpread, InlineFragment, SelectedField, Selection

from models.players.item import ItemSaModel

# TODO: it should be Base
T_ = TypeVar("T_", bound=Union["ItemSaModel"])


def get_all_required_fields(info: Info) -> Set[str]:
    def get_required_fields(
        fields: Sequence[Selection],
        prefix: str = "",
        required_fields: Optional[Set[str]] = None,
    ) -> Set[str]:
        if not required_fields:
            required_fields = set()
        for field in fields:
            if isinstance(field, FragmentSpread):
                required_fields |= get_required_fields(field.selections, prefix, required_fields)
            elif isinstance(field, SelectedField):
                if field.selections:
                    new_prefix = f"{prefix}.{field.name}" if prefix else field.name
                    required_fields |= get_required_fields(field.selections, new_prefix, required_fields)
                else:
                    required_fields.add(prefix)
            elif isinstance(field, InlineFragment):
                raise NotImplementedError("Inline fragments can't be used.")
        return required_fields

    return get_required_fields(info.selected_fields)


def get_required_relationships(
    mapper: Mapper, required_fields: Set[str], current_path: str
) -> Set[RelationshipProperty]:
    relationships = set()
    for field in required_fields:
        if field.startswith(f"{current_path}."):  # We only want paths with additional things, so we need the dot.
            splitted_field = field.replace(f"{current_path}.", "").split(".")
            relationships.add(mapper.relationships[splitted_field[0]])
    return relationships


def generate_eagerload(
    sa_model_cl: Type[T_],
    required_fields: Set[str],
    current_load: Optional[_UnboundLoad],
    current_path: str,
    attributes_to_selectin_load: List[Tuple[str, str]],
) -> List[Load]:
    relationships = get_required_relationships(inspect(sa_model_cl), required_fields, current_path)
    if relationships in (set(), {None}):
        return [current_load.noload("*")] if current_load else []
    else:
        loads = []
        for relationship in relationships:
            if (current_path, relationship.key) in attributes_to_selectin_load:
                current_load = (
                    current_load.selectinload(relationship.class_attribute)
                    if current_load
                    else selectinload(relationship.class_attribute)
                )
            else:
                current_load = (
                    current_load.joinedload(relationship.class_attribute)
                    if current_load
                    else joinedload(relationship.class_attribute)
                )
            loads.extend(
                generate_eagerload(
                    sa_model_cl=relationship.mapper.class_,
                    required_fields=required_fields,
                    current_load=current_load,
                    current_path=f"{current_path}.{relationship.key}",
                    attributes_to_selectin_load=attributes_to_selectin_load,
                )
            )
        return loads


def generate_sql_query(
    sa_model_cl: Type[T_], model_ids: Sequence[int], info: Info, attributes_to_selectin_load: List[Tuple[str, str]]
) -> Select:
    query = select(sa_model_cl)
    if model_ids:
        query = query.where(sa_model_cl.id.in_(model_ids))
    required_fields = get_all_required_fields(info)
    loads = generate_eagerload(sa_model_cl, required_fields, None, info.field_name, attributes_to_selectin_load)
    if loads:
        query = query.options(loads)
    return query


def instances_getter(
    session: Session,
    sa_model_cl: Type[T_],
    model_ids: Sequence[int],
    info: Info,
    attributes_to_selectin_load: List[Tuple[str, str]],
) -> Iterator[T_]:
    return (
        session.execute(generate_sql_query(sa_model_cl, model_ids, info, attributes_to_selectin_load))
        .unique()
        .scalars()
    )


def create_metadata(engine: Engine) -> None:
    from app.configuration.database import Base

    with engine.begin() as _conn:
        Base.metadata.create_all(_conn)


def get_engine(session: ScopedSession) -> Engine:
    bind = session.get_bind()
    if not isinstance(bind, Engine):
        bind = bind.engine
    return bind
