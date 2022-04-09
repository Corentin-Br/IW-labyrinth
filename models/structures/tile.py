from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from models.configuration.app import Base

from ..configuration.database import SqliteDecimal
from ..utils.associations.player_to_close_tiles import player_to_close_tiles_table
from ..utils.associations.player_to_monster_sight_tiles import player_to_monster_sight_tiles_table

if TYPE_CHECKING:
    from ..features.altar import AltarSaModel
    from ..players.player import PlayerSaModel
    from .area import AreaSaModel
    from .floor import FloorSaModel
    from .wall import WallSaModel


class TileSaModel(Base):
    __tablename__ = "tile"

    id = Column(Integer, primary_key=True)
    abscissa = Column(Integer, nullable=False)
    ordinate = Column(Integer, nullable=False)
    floor_id = Column(Integer, ForeignKey("floor.id"), nullable=False)
    checked = Column(Boolean, default=False, nullable=False)
    minimum_increase_in_monster_spawn = Column(SqliteDecimal, nullable=False)
    coefficient_increase_in_monster_spawn = Column(SqliteDecimal, nullable=False)
    covered_in_shadows = Column(Boolean, nullable=False)  # beacon flag.

    areas: List["AreaSaModel"] = relationship("AreaSaModel", secondary="tile_to_area_table", uselist=True)
    floor: "FloorSaModel" = relationship("FloorSaModel", back_populates="tiles")
    walls: List["WallSaModel"] = relationship("WallSaModel", back_populates="tile", uselist=True)
    current_players: List["PlayerSaModel"] = relationship("PlayerSaModel", back_populates="current_tile")
    players_close_tile_marking: List["PlayerSaModel"] = relationship(
        "PlayerSaModel", secondary=player_to_close_tiles_table
    )
    players_monsters_tile_marking: List["PlayerSaModel"] = relationship(
        "PlayerSaModel", secondary=player_to_monster_sight_tiles_table
    )

    altar: "AltarSaModel" = relationship("AltarSaModel", foreign_keys=["altar.tile_id"])
    # relationship features

    __table_args__ = (
        UniqueConstraint("abscissa", "ordinate", "floor_id"),
    )  # TODO: Check that it's like that. What about naming scheme?
