from typing import List

import strawberry
from strawberry.types import Info

from models.players.item import ItemSaModel
from schema.dataclasses.players import Item
from utils.dataclass_mapper import turn_in_dataclass
from utils.strawberry import generic_resolver


def get_items_route(info: Info, item_ids: List[int]) -> List[Item]:
    return [turn_in_dataclass(result, Item) for result in generic_resolver(ItemSaModel, info, item_ids, [])]


@strawberry.type
class Query:
    items = strawberry.field(resolver=get_items_route)
