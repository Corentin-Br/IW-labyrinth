from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

player_full_condition_to_wall_table = Table(
    "player_full_condition_to_wall_table",
    Column("id", Integer, primary_key=True),
    Column("player_full_condition_id", Integer, ForeignKey("player_full_condition.id"), nullable=False),
    Column("wall_id", Integer, ForeignKey("wall.id"), nullable=False),
    UniqueConstraint("player_full_condition_id", "wall_id"),
)
