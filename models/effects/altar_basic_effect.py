from sqlalchemy import Column, Enum, ForeignKey, Integer

from models.configuration.app import Base
from models.utils.enums.altar_effects import AltarEffectEnum


class AltarBasicEffectSaModel(Base):
    __tablename__ = "altar_basic_effect"

    id = Column(Integer, primary_key=True)
    function_name = Column(Enum(AltarEffectEnum), nullable=False)

    # TODO: Add columns for parameters

    full_condition_id = Column(Integer, ForeignKey("altar_full_effect.id"), nullable=False)

    # TODO: Add CheckConstraint to check that not all parameters are null.
