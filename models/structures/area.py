from tokenize import String
from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.configuration.app import Base

if TYPE_CHECKING:
    from .tile import TileSaModel


class AreaSaModel(Base):
    __tablename__ = "area"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tiles: List["TileSaModel"] = relationship("TileSaModel", secondary="tile_to_area_table")
