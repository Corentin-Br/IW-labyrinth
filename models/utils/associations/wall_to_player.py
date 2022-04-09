from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

wall_to_player_table = Table(
    "wall_to_player_table",
    Column("id", Integer, primary_key=True),
    Column("player_id", Integer, ForeignKey("player.id"), nullable=False),
    Column("wall_id", Integer, ForeignKey("wall.id"), nullable=False),
    UniqueConstraint("player_id", "wall_id"),
)
