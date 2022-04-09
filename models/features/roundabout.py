from sqlalchemy import Column, Enum, ForeignKey, Integer

from models.features.feature import FeatureSaModel
from models.utils.enums.roundabout_function import RoundaboutFunctionEnum


class RoundaboutSaModel(FeatureSaModel):
    __tablename__ = "roundabout"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    function = Column(Enum(RoundaboutFunctionEnum), nullable=False)

    __mapper_args__ = {"polymorphic_identity": "roundabout"}
