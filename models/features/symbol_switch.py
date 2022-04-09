from enum import Enum

from sqlalchemy import Column, ForeignKey, Integer

from ..utils.enums.symbols import SymbolEnum
from .binary_switch import BinarySwitchSaModel


class SymbolSwitchSaModel(BinarySwitchSaModel):
    """It's a switch that opens all the wall bearing the symbol."""

    __tablename__ = "symbol_switch"

    id = Column(Integer, ForeignKey("binary_switch.id"), primary_key=True)
    symbol = Column(Enum(SymbolEnum), nullable=False)
    area_id = Column(Integer, ForeignKey("area.id"), nullable=False)

    # The walls affected by the switch will be ALL those from the area, so no need to create relationship.
    __mapper_args__ = {"polymorphic_identity": "symbol_switch"}
