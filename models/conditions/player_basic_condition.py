from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String

from app.configuration.database import Base
from models.utils.enums.directions import DirectionEnum


class PlayerBasicConditionSaModel(Base):
    __tablename__ = "player_basic_condition"

    id = Column(Integer, primary_key=True)
    inverted = Column(Boolean, nullable=False)  # NOT

    class_name = Column(String)
    direction = Column(Enum(DirectionEnum))
    # add more parameters. They are ALL checked, and the NOT is applied to the AND of the parameters.

    full_condition_id = Column(Integer, ForeignKey("player_full_condition.id"), nullable=False)
