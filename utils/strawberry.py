from contextlib import ExitStack
from typing import Any, Generator, List, Optional, Sequence, Tuple, Type, TypeVar, Union

from sqlalchemy.orm import Session
from strawberry.types import Info

from app.api import get_app
from models.players.item import ItemSaModel
from utils.sqlalchemy import instances_getter

T_ = TypeVar("T_", bound=Union["ItemSaModel"])
S_ = TypeVar("S_")


def generic_resolver(
    sa_model_cl: Type[T_],
    info: Info,
    model_ids: Optional[Sequence[int]],
    attributes_to_selectin_load: List[Tuple[str, str]],
    session: Optional[Session] = None,
) -> Generator[T_, None, None]:
    if not model_ids:
        model_ids = []
    with ExitStack() as stack:
        if session is None:
            session = stack.enter_context(get_app().session())
            stack.enter_context(session.begin())
        yield from instances_getter(session, sa_model_cl, model_ids, info, attributes_to_selectin_load)


def generic_update(obj: S_, **kwargs: Any) -> S_:
    for name, value in kwargs.items():
        if value is not None:
            setattr(obj, name, value)
    return obj
