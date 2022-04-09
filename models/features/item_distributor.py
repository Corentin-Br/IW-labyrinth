from typing import TYPE_CHECKING, List

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.features.feature import FeatureSaModel

from ..utils.enums.caracteristic import CaracteristicEnum

if TYPE_CHECKING:
    from models.effects.event_effect import EventEffectSaModel

    from ..players.item import ItemSaModel
    from ..utils.hint import HintSaModel


class ItemDistributorSaModel(FeatureSaModel):
    __tablename__ = "item_distributor"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    last_item_time = Column(DateTime, nullable=False)
    self_cooldown = Column(Integer, nullable=False)  # time in seconds between two items from this feature
    self_cooldown_text = Column(String, nullable=False)
    player_cooldown = Column(
        Integer, nullable=False
    )  # time in seconds a player must wait since getting item from another feature
    player_cooldown_text = Column(String, nullable=False)

    caracteristic = Column(
        Enum(CaracteristicEnum), nullable=False
    )  # The caracteristic used to determine what level of item you get

    items: List["ItemSaModel"] = relationship("ItemSaModel", secondary="item_to_item_distributor_table", uselist=True)

    effects: List["EventEffectSaModel"] = relationship(
        "EventEffectSaModel", foreign_keys=["event_consequence.event_id"], uselist=True
    )
    hints: List["HintSaModel"] = relationship("HintSaModel", foreign_keys=["hint.event_id"], uselist=True)

    __mapper_args__ = {"polymorphic_identity": "item_distributor"}
