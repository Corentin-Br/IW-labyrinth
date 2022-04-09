from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .feature import FeatureSaModel

if TYPE_CHECKING:
    from ..structures.amovible import AmovibleSaModel


class AmovibleSwitchSaModel(FeatureSaModel):
    __tablename__ = "amovible_switch"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    amovible_id = Column(Integer, ForeignKey("amovible.id"), nullable=False)

    amovible: "AmovibleSaModel" = relationship("AmovibleSaModel", uselist=False)

    __mapper_args__ = {"polymorphic_identity": "amovible_switch"}
