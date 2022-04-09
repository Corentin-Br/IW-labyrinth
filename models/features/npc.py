from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.features.feature import FeatureSaModel

if TYPE_CHECKING:
    from models.effects.exchange import ExchangeSaModel


class NpcSaModel(FeatureSaModel):
    __tablename__ = "npc"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    short_presentation_text = Column(String, nullable=False)  # Text displayed if player doesn't have an item
    too_many_people_text = Column(String, nullable=False)  # Text displayed if there are too many players.
    presentation_text = Column(String, nullable=False)

    exchanges: List["ExchangeSaModel"] = relationship(
        "ExchangeSaModel", foreign_keys=["exchange.npc_id"], uselist=True
    )
    __mapper_args__ = {"polymorphic_identity": "npc"}
