from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

exchange_to_labyrinth_effect_table = Table(
    "exchange_to_labyrinth_effect_table",
    Column("id", Integer, primary_key=True),
    Column("exchange_id", Integer, ForeignKey("exchange.id"), nullable=False),
    Column("labyrinth_effect_id", Integer, ForeignKey("labyrinth_effect.id"), nullable=False),
    UniqueConstraint("exchange_id", "labyrinth_effect_id"),
)
