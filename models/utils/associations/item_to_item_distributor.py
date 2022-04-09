from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

item_to_item_distributor_table = Table(
    "item_to_item_distributor_table",
    Column("id", Integer, primary_key=True),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False),
    Column("item_distributor_id", Integer, ForeignKey("item_distributor.id"), nullable=False),
    UniqueConstraint("item_id", "item_distributor_id"),
)
