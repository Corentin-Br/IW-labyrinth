from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from .labyrinth import LabyrinthSaModel
    from .tile import TileSaModel


class FloorSaModel(Base):
    __tablename__ = "floor"

    id = Column(Integer, primary_key=True)
    level = Column(Integer, nullable=False)
    labyrinth_id = Column(Integer, ForeignKey("labyrinth.id"), nullable=False)

    labyrinth: "LabyrinthSaModel" = relationship("LabyrinthSaModel", back_populates="floors")
    tiles: List["TileSaModel"] = relationship("TileSaModel", back_populates="tiles")
