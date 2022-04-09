from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .binary_switch import BinarySwitchSaModel

if TYPE_CHECKING:
    from models.features.feature import FeatureSaModel


class FeatureSwitchSaModel(BinarySwitchSaModel):

    __tablename__ = "feature_switch"

    id = Column(Integer, ForeignKey("binary_switch.id"), primary_key=True)

    features: List["FeatureSaModel"] = relationship(
        "FeatureSaModel", secondary="feature_switch_to_feature_table", uselist=True
    )
    __mapper_args__ = {"polymorphic_identity": "feature_switch"}
