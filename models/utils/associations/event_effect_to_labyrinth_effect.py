from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

event_effect_to_labyrinth_effect_table = Table(
    "event_effect_to_labyrinth_effect_table",
    Column("id", Integer, primary_key=True),
    Column("event_effect_id", Integer, ForeignKey("event_effect.id"), nullable=False),
    Column("labyrinth_effect_id", Integer, ForeignKey("labyrinth_effect.id"), nullable=False),
    UniqueConstraint("event_effect_id", "labyrinth_effect_id"),
)
