import strawberry
from attr import define


@strawberry.type
@define
class Item:
    id: int
    name: str
    rank: int
