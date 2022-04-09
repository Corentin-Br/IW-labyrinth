from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .binary_switch import BinarySwitchSaModel

if TYPE_CHECKING:
    from ..structures.wall import WallSaModel


class WallSwitchSaModel(BinarySwitchSaModel):
    __tablename__ = "wall_switch"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)

    walls: List["WallSaModel"] = relationship("WallSaModel", secondary="wall_switch_to_wall_table", uselist=True)
    __mapper_args__ = {"polymorphic_identity": "wall_switch"}
