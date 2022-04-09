from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer

from app.configuration.database import SqliteDecimal
from models.features.feature import FeatureSaModel
from models.utils.enums.caracteristic import CaracteristicEnum


class DamageTileSaModel(FeatureSaModel):
    __tablename__ = "damage_tile"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    damage = Column(SqliteDecimal, nullable=False)
    resistance_caracteristic = Column(Enum(CaracteristicEnum))  # intentionally nullable.
    send_home = Column(
        Boolean, nullable=False
    )  # determines if the player is sent to the beginning when he walks on it.

    __mapper_args__ = {"polymorphic_identity": "damage_tile"}
