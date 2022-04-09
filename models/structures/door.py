from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from .wall import WallSaModel


class DoorSaModel(Base):
    __tablename__ = "door"

    id = Column(Integer, primary_key=True)
    resistance = Column(Integer, nullable=False)

    walls: List["WallSaModel"] = relationship("WallSaModel", back_populates="door")
