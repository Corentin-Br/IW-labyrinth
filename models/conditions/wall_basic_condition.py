from sqlalchemy import Boolean, CheckConstraint, Column, Enum, ForeignKey, Integer, String

from models.configuration.app import Base
from models.utils.enums.directions import DirectionEnum
from models.utils.enums.wall_conditions import WallConditionEnum


class WallBasicConditionSaModel(Base):
    __tablename__ = "wall_basic_condition"

    id = Column(Integer, primary_key=True)
    inverted = Column(Boolean, nullable=False)  # NOT
    function_name = Column(Enum(WallConditionEnum), nullable=False)

    class_name = Column(String)
    direction = Column(Enum(DirectionEnum))

    full_condition_id = Column(Integer, ForeignKey("wall_full_condition.id"), nullable=False)
    __table_args__ = (CheckConstraint("num_nonnulls(class_name, direction) >= 1"),)
