from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from models.configuration.app import Base

if TYPE_CHECKING:
    from .altar_basic_effect import AltarBasicEffectSaModel


class AltarFullEffectSaModel(Base):
    __tablename__ = "altar_full_effect"

    id = Column(Integer, primary_key=True)

    base_effects: List["AltarBasicEffectSaModel"] = relationship(
        "AltarBasicEffectSaModel", foreign_keys=["altar_basic_effect.full_condition_id"], uselist=True
    )
