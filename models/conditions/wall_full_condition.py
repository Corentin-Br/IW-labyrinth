from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.configuration.app import Base

if TYPE_CHECKING:
    from models.conditions.wall_basic_condition import WallBasicConditionSaModel


class WallFullConditionSaModel(Base):
    __tablename__ = "wall_full_condition"

    id = Column(Integer, primary_key=True)
    wall_id = Column(Integer, ForeignKey("wall.id"), nullable=False)

    base_conditions: List["WallBasicConditionSaModel"] = relationship("WallBasicConditionSaModel", uselist=True)
