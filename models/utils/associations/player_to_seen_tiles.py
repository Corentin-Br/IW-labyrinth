from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

player_to_seen_tiles_table = Table(
    "player_to_seen_tiles_table",
    Column("id", Integer, primary_key=True),
    Column("player_id", Integer, ForeignKey("player.id"), nullable=False),
    Column("tile_id", Integer, ForeignKey("tile.id"), nullable=False),
    UniqueConstraint("player_id", "tile_id"),
)
