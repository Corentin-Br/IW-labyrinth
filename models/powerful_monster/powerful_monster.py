from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configuration.database import Base, SqliteDecimal

if TYPE_CHECKING:
    from .itinerary import ItineraryTileSaModel


class PowerfulMonsterSaModel(Base):
    __tablename__ = "powerful_monster"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    area_id = Column(Integer, ForeignKey("area.id"), nullable=False)
    move_number = Column(Integer, nullable=False)
    damage = Column(SqliteDecimal, nullable=False)
    send_home = Column(Boolean, nullable=False)
    enabled = Column(Boolean, nullable=False)

    itinerary: List["ItineraryTileSaModel"] = relationship("ItineraryTileSaModel", uselist=True)
