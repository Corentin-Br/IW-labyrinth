from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from models.configuration.app import Base


class FeatureSaModel(Base):
    __tablename__ = "feature"

    id = Column(Integer, primary_key=True)
    enabled = Column(
        Boolean, nullable=False
    )  # Determines if the feature is visible in the labyrinth/can be triggered.
    tile_id = Column(Integer, ForeignKey("tile.id"), nullable=False)
    feature_type = Column(String, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "feature", "polymorphic_on": feature_type}
