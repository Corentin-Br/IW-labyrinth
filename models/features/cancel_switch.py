from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .feature import FeatureSaModel

if TYPE_CHECKING:
    from ..structures.area import AreaSaModel
    from ..structures.tile import TileSaModel
    from .amovible_switch import AmovibleSwitchSaModel
    from .binary_switch import BinarySwitchSaModel


class CancelSwitchSaModel(FeatureSaModel):
    __tablename__ = "cancel_switch"

    id = Column(Integer, ForeignKey("feature.id"), primary_key=True)
    area_id = Column(Integer, ForeignKey("area.id"), nullable=False)  # It can always be a single area.
    tile_id = Column(Integer, ForeignKey("tile.id"), nullable=False)
    destination_tile_id = Column(Integer, ForeignKey("tile.id"), nullable=False)

    teleported_area: "AreaSaModel" = relationship("AreaSaModel", uselist=False)
    teleportation_destination: "TileSaModel" = relationship(
        "TileSaModel", foreign_keys=[destination_tile_id], uselist=True
    )

    affected_binary_switches: List["BinarySwitchSaModel"] = relationship(
        "BinarySwitchSaModel", secondary="cancel_switch_to_binary_switch_table", uselist=True
    )
    affected_amovible_switches: List["AmovibleSwitchSaModel"] = relationship(
        "AmovibleSwitchSaModel", secondary="cancel_switch_to_amovible_switch_table", uselist=True
    )
    __mapper_args__ = {"polymorphic_identity": "cancel_switch"}
