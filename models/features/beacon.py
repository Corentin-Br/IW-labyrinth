from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.configuration.app import Base

from .feature import FeatureSaModel

if TYPE_CHECKING:
    from ..structures.area import AreaSaModel


class BeaconSaModel(FeatureSaModel):
    __tablename__ = "beacon"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    activated = Column(Boolean, nullable=False)
    area_id = Column(Integer, ForeignKey("area.id"))

    area: "AreaSaModel" = relationship("AreaSaModel")
    __mapper_args__ = {"polymorphic_identity": "beacon"}
