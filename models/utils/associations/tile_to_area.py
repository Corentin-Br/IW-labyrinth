from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

tile_to_area_table = Table(
    "tile_to_area_table",
    Column("id", Integer, primary_key=True),
    Column("tile_id", Integer, ForeignKey("tile.id"), nullable=False),
    Column("area_id", Integer, ForeignKey("area.id"), nullable=False),
    UniqueConstraint("tile_id", "area_id"),
)
