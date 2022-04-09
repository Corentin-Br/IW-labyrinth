from typing import Optional

import strawberry
from strawberry.types import Info

from app.api import get_app
from models.players.item import ItemSaModel
from schema.dataclasses.players import Item
from utils.dataclass_mapper import turn_in_dataclass
from utils.strawberry import generic_resolver, generic_update


@strawberry.input
class CreateItemInput:
    name: str
    rank: int


@strawberry.input
class UpdateItemInput:
    item_id: int
    name: Optional[str] = None
    rank: Optional[int] = None


def create_item_route(inputs: CreateItemInput) -> Item:
    with get_app().session() as session, session.begin():
        new_item = ItemSaModel(name=inputs.name, rank=inputs.rank)
        session.add(new_item)
        session.flush()
        return turn_in_dataclass(new_item, Item)


def update_item_route(info: Info, inputs: UpdateItemInput) -> Item:
    with get_app().session() as session, session.begin():
        item_orm = generic_update(
            next(generic_resolver(ItemSaModel, info, [inputs.item_id], [], session)),
            name=inputs.name,
            rank=inputs.rank,
        )
        return turn_in_dataclass(item_orm, Item)


@strawberry.type
class Mutation:
    create_item = strawberry.mutation(resolver=create_item_route)
    update_item = strawberry.mutation(resolver=update_item_route)
