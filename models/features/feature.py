from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from models.structures.tile import TileSaModel


class FeatureSaModel(Base):
    __tablename__ = "feature"

    id = Column(Integer, primary_key=True)
    enabled = Column(
        Boolean, nullable=False
    )  # Determines if the feature is visible in the labyrinth/can be triggered.
    tile_id = Column(Integer, ForeignKey("tile.id"), nullable=False)
    feature_type = Column(String, nullable=False)
    image_name = Column(String, nullable=False)

    tile: "TileSaModel" = relationship("TileSaModel")

    __mapper_args__ = {"polymorphic_identity": "feature", "polymorphic_on": feature_type}
