from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from models.features.feature import FeatureSaModel


class AmovibleTileSaModel(FeatureSaModel):
    __tablename__ = "amovible_tile"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    amovible_id = Column(Integer, ForeignKey("amovible.id"), nullable=False)
    order = Column(Integer, nullable=False)

    __table_args__ = (UniqueConstraint("order, amovible_id"),)
    __mapper_args__ = {"polymorphic_identity": "amovible_tile"}
