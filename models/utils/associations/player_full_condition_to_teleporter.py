from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

player_full_condition_to_teleporter_table = Table(
    "player_full_condition_to_teleporter_table",
    Column("id", Integer, primary_key=True),
    Column("player_full_condition_id", Integer, ForeignKey("player_full_condition.id"), nullable=False),
    Column("teleporter_id", Integer, ForeignKey("teleporter.id"), nullable=False),
    UniqueConstraint("player_full_condition_id", "teleporter_id"),
)
