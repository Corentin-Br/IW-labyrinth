from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from app.configuration.database import Base


class ItineraryTileSaModel(Base):
    __tablename__ = "itinerary_tile"

    id = Column(Integer, primary_key=True)
    monster_id = Column(Integer, ForeignKey("powerful_monster.id"), nullable=False)
    tile_id = Column(Integer, ForeignKey("tile.id"), nullable=False)
    rank = Column(Integer, nullable=False)

    __table_args__ = (UniqueConstraint("monster_id", "rank"),)
