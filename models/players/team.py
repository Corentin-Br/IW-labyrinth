from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from .player import PlayerSaModel


class TeamSaModel(Base):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True)

    players: List["PlayerSaModel"] = relationship("PlayerSaModel", uselist=True, back_populates="team")
