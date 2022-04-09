from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.configuration.database import SqliteDecimal
from models.features.feature import FeatureSaModel
from models.utils.enums.caracteristic import CaracteristicEnum

if TYPE_CHECKING:
    from models.effects.labyrinth_effect import LabyrinthEffectSaModel


class WorkPointSaModel(FeatureSaModel):
    __tablename__ = "work_point"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    find_caracteristic = Column(Enum(CaracteristicEnum), nullable=False)
    build_caracteristic = Column(Enum(CaracteristicEnum), nullable=False)
    discovered = Column(Boolean, nullable=False)
    built = Column(Boolean, nullable=False)
    cost = Column(SqliteDecimal, nullable=False)

    effects: List["LabyrinthEffectSaModel"] = relationship(
        "LabyrinthEffectSaModel", secondary="work_point_to_labyrinth_effect_table", uselist=True
    )

    __mapper_args__ = {"polymorphic_identity": "work_point"}
