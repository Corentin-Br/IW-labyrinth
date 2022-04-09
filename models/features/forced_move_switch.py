from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .binary_switch import BinarySwitchSaModel

if TYPE_CHECKING:
    from .forced_move import ForcedMoveSaModel


class ForcedMoveSwitchSaModel(BinarySwitchSaModel):
    __tablename__ = "forced_move_switch"

    id = Column(Integer, ForeignKey("binary_switch.id"), primary_key=True)

    force_moves: List["ForcedMoveSaModel"] = relationship(
        "ForcedMoveSaModel", secondary="forced_move_switch_to_forced_move_table", uselist=True
    )
    __mapper_args__ = {"polymorphic_identity": "forced_move_switch"}
