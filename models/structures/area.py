from tokenize import String
from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from .tile import TileSaModel


class AreaSaModel(Base):
    # It's basically acting as an association table to link lots of tiles to X, instead of needing lots of foreign
    # keys on tiles.
    __tablename__ = "area"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tiles: List["TileSaModel"] = relationship("TileSaModel", secondary="tile_to_area_table")
