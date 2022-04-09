from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

player_to_item_table = Table(
    "player_to_item_table",
    Column("id", Integer, primary_key=True),
    Column("player_id", Integer, ForeignKey("player.id"), nullable=False),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False),
    UniqueConstraint("player_id", "item_id"),
)
