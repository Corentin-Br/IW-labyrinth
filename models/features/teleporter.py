from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.features.feature import FeatureSaModel

if TYPE_CHECKING:
    from models.effects.teleporter_effect import TeleporterEffectSaModel


class TeleporterSaModel(FeatureSaModel):
    __tablename__ = "teleporter"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    auto_triggered = Column(Boolean, nullable=False)  # If true, the teleporter triggers without input. Meant to trap.

    effects: List["TeleporterEffectSaModel"] = relationship(
        "TeleporterEffectSaModel", uselist=True, foreign_keys=["teleporter_effect.origin_id"]
    )
    __mapper_args__ = {"polymorphic_identity": "teleporter"}
