from sqlalchemy import Column, ForeignKey, Integer, String

from models.features.feature import FeatureSaModel


class WarpSaModel(FeatureSaModel):
    __tablename__ = "warp"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    identifiant = Column(Integer, nullable=False)  # It's the number player uses
    name = Column(String, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "warp"}
