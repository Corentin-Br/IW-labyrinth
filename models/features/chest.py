from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.features.feature import FeatureSaModel

if TYPE_CHECKING:
    from models.effects.player_effect import PlayerEffectSaModel


class ChestSaModel(FeatureSaModel):
    __tablename__ = "chest"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    opened = Column(Boolean, nullable=False)
    message = Column(String, nullable=False)
    effect_id = Column(Integer, ForeignKey("player_effect.id"), nullable=False)

    effect: "PlayerEffectSaModel" = relationship("PlayerEffectSaModel", uselist=False)

    __mapper_args__ = {"polymorphic_identity": "chest"}
