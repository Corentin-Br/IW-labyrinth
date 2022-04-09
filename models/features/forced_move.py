from sqlalchemy import Column, Enum, ForeignKey, Integer

from models.features.feature import FeatureSaModel
from models.utils.enums.directions import DirectionEnum


class ForcedMoveSaModel(FeatureSaModel):
    __tablename__ = "forced_move"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    direction = Column(Enum(DirectionEnum))  # intentionally nullable. A nullable value means "keep going".
    __mapper_args__ = {"polymorphic_identity": "forced_move"}
