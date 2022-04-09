from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from models.conditions.player_basic_condition import PlayerBasicConditionSaModel


class PlayerFullConditionSaModel(Base):
    __tablename__ = "player_full_condition"

    id = Column(Integer, primary_key=True)

    base_conditions: List["PlayerBasicConditionSaModel"] = relationship("PlayerBasicConditionSaModel", uselist=True)
    # all base_conditions must be True to make the full conditio True.
