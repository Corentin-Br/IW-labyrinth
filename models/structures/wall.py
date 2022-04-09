from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from models.configuration.app import Base
from models.utils.enums.directions import DirectionEnum
from models.utils.enums.symbols import SymbolEnum

from ..utils.associations.wall_to_player import wall_to_player_table

if TYPE_CHECKING:
    from ..conditions.wall_full_condition import WallFullConditionSaModel
    from ..players.player import PlayerSaModel
    from .door import DoorSaModel
    from .tile import TileSaModel


class WallSaModel(Base):
    __tablename__ = "wall"

    id = Column(Integer, primary_key=True)
    position = Column(Enum(DirectionEnum), nullable=False)
    tile_id = Column(Integer, ForeignKey("tile.id"), nullable=False)
    opened = Column(Boolean, nullable=False)
    symbol = Column(Enum(SymbolEnum))
    door_id = Column(Integer, ForeignKey("door.id"))

    __table_args__ = (UniqueConstraint("position", "tile_id"),)
    tile: "TileSaModel" = relationship("TileSaModel", back_populates="walls")
    door: "DoorSaModel" = relationship("DoorSaModel", back_populates="walls")

    allowed_players: List["PlayerSaModel"] = relationship("PlayerSaModel", secondary=wall_to_player_table)
    alternative_conditions: List["WallFullConditionSaModel"] = relationship(
        "WallFullConditionSaModel"
    )  # Each condition is itself composed of base conditions linked by AND. Each of those alternative conditions are
    # in turn linked by OR. A rough pseudo-code for checking them should be
    # for cond in wall.alternative_conditions:
    #   if all base_cond in cond.base_conditions are True:
    #       return True
    # return False
