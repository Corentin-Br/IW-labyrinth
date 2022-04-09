from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

work_point_to_labyrinth_effect_table = Table(
    "work_point_to_labyrinth_effect_table",
    Column("id", Integer, primary_key=True),
    Column("work_point_id", Integer, ForeignKey("work_point.id"), nullable=False),
    Column("labyrinth_effect_id", Integer, ForeignKey("labyrinth_effect.id"), nullable=False),
    UniqueConstraint("work_point_id", "labyrinth_effect_id"),
)
