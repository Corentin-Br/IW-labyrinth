from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from models.configuration.app import Base

if TYPE_CHECKING:
    from .area import AreaSaModel
    from .floor import FloorSaModel


class LabyrinthSaModel(Base):
    __tablename__ = "labyrinth"

    id = Column(Integer, primary_key=True)
    vote_enabled = Column(Boolean, nullable=False)
    name = Column(String, nullable=False)

    floors: List["FloorSaModel"] = relationship(
        "FloorSaModel", back_populates="labyrinth", uselist=True
    )
    areas: List["AreaSaModel"] = relationship(
        "AreaSaModel", back_populates="labyrinth", uselist=True
    )
