from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

wall_switch_to_wall_table = Table(
    "wall_switch_to_wall_table",
    Column("id", Integer, primary_key=True),
    Column("wall_switch_id", Integer, ForeignKey("wall_switch.id"), nullable=False),
    Column("wall_id", Integer, ForeignKey("wall.id"), nullable=False),
    UniqueConstraint("wall_switch_id", "wall_id"),
)
