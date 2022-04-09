from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.features.feature import FeatureSaModel

if TYPE_CHECKING:
    from models.effects.player_effect import PlayerEffectSaModel


class AltarSaModel(FeatureSaModel):
    __tablename__ = "altar"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    first_player_id = Column(Integer, ForeignKey("player.id"))  # intentionally nullable

    minor_negative_effect_id = Column(Integer, ForeignKey("player_effect.id"))
    major_negative_effect_id = Column(Integer, ForeignKey("player_effect.id"))
    positive_effect_id = Column(Integer, ForeignKey("player_effect.id"))

    self_sacrifice_message = Column(String, nullable=False)
    sacrificed_other_message = Column(String, nullable=False)
    got_sacrificed_message = Column(String, nullable=False)

    minor_negative_effect: "PlayerEffectSaModel" = relationship(
        "PlayerEffectSaModel", foreign_keys=[minor_negative_effect_id]
    )
    major_negative_effect: "PlayerEffectSaModel" = relationship(
        "PlayerEffectSaModel", foreign_keys=[major_negative_effect_id]
    )
    positive_effect: "PlayerEffectSaModel" = relationship("PlayerEffectSaModel", foreign_keys=[positive_effect_id])

    __mapper_args__ = {"polymorphic_identity": "altar"}
