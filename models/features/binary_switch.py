from sqlalchemy import Boolean, Column, ForeignKey, Integer

from models.features.feature import FeatureSaModel


class BinarySwitchSaModel(FeatureSaModel):
    __tablename__ = "binary_switch"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    activated = Column(Boolean, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "binary_switch"}
