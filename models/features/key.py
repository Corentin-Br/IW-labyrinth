from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.features.feature import FeatureSaModel
from models.utils.enums.games import MiniGameEnum

if TYPE_CHECKING:
    from models.structures.door import DoorSaModel


class KeySaModel(FeatureSaModel):
    __tablename__ = "key"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    door_id = Column(Integer, ForeignKey("door.id"), nullable=False)
    activated = Column(Boolean, nullable=False)
    game = Column(Enum(MiniGameEnum), nullable=False)

    door: "DoorSaModel" = relationship("DoorSaModel")

    __mapper_args__ = {"polymorphic_identity": "key"}
