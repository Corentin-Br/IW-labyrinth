from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.features.feature import FeatureSaModel

if TYPE_CHECKING:
    from models.effects.event_effect import EventEffectSaModel

    from ..utils.hint import HintSaModel


class EventSaModel(FeatureSaModel):
    __tablename__ = "event"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    activated = Column(Boolean, nullable=False)
    presentation_text = Column(String, nullable=False)

    effects: List["EventEffectSaModel"] = relationship(
        "EventEffectSaModel", foreign_keys=["event_consequence.event_id"], uselist=True
    )
    hints: List["HintSaModel"] = relationship("HintSaModel", foreign_keys=["hint.event_id"], uselist=True)
    __mapper_args__ = {"polymorphic_identity": "event"}
