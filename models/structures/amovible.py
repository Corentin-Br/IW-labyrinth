from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from ..features.amovible_tile import AmovibleTileSaModel


class AmovibleSaModel(Base):
    __tablename__ = "amovible"

    id = Column(Integer, primary_key=True)
    current_position = Column(Integer, nullable=False)
    switch_id = Column(Integer, ForeignKey("amovible_switch.id"))  # intentionally nullable.

    amovible_tiles: List["AmovibleTileSaModel"] = relationship(
        "AmovibleTileSaModel", foreign_keys=["amovible_tile.amovible_id"]
    )
