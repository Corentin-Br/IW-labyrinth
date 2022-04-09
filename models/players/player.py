from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.sqlite import DATETIME as sqlite_datetime
from sqlalchemy.orm import relationship

from models.configuration.app import Base
from models.utils.enums.directions import DirectionEnum

from ..configuration.database import SqliteDecimal
from ..utils.associations.player_to_close_tiles import player_to_close_tiles_table
from ..utils.associations.player_to_monster_sight_tiles import player_to_monster_sight_tiles_table
from ..utils.associations.player_to_seen_tiles import player_to_seen_tiles_table

if TYPE_CHECKING:
    from ..structures.tile import TileSaModel
    from .item import ItemSaModel
    from .team import TeamSaModel


class PlayerSaModel(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    discord_id = Column(Integer, nullable=False)
    tile_id = Column(Integer, ForeignKey("tile.id"), nullable=False)
    previous_tile_id = Column(Integer, ForeignKey("tile.id"), nullable=True)
    direction = Column(Enum(DirectionEnum), nullable=False)
    adventurer_class = Column(String(32), nullable=False)
    energy = Column(SqliteDecimal, nullable=False)
    immune_count = Column(Integer, nullable=False)
    no_heal_count = Column(Integer, nullable=False)
    monster_meeting_chance = Column(SqliteDecimal, nullable=False)
    steps_since_last_monster = Column(Integer, nullable=False)
    team_id = Column(Integer, ForeignKey("team.id"), nullable=False)
    is_leader = Column(Boolean, nullable=False)
    resurrected_count = Column(Integer, nullable=False)
    time_since_last_item = Column(sqlite_datetime)

    # Bonus Attributes
    secret_discoveries = Column(Integer, default=0, nullable=False)
    dangerous_area_resistance = Column(Integer, default=0, nullable=False)
    cheaper_building = Column(Integer, default=0, nullable=False)
    powerful_monster_sight = Column(Integer, default=0, nullable=False)
    close_tile_sight = Column(Integer, default=0, nullable=False)
    resurrection = Column(Integer, default=0, nullable=False)
    event_bonus = Column(Integer, default=0, nullable=False)
    key_sight = Column(Integer, default=0, nullable=False)
    cheaper_move = Column(Integer, default=0, nullable=False)
    higher_regeneration = Column(Integer, default=0, nullable=False)
    trap_resistance = Column(Integer, default=0, nullable=False)
    monster_resistance = Column(Integer, default=0, nullable=False)

    # Vanity stats
    total_steps = Column(Integer, nullable=False)
    total_energy_used = Column(SqliteDecimal, nullable=False)
    damage_taken_from_monsters = Column(SqliteDecimal, nullable=False)
    damage_taken_by_surprise = Column(SqliteDecimal, nullable=False)
    damage_taken_from_traps = Column(SqliteDecimal, nullable=False)
    damage_taken_from_areas = Column(SqliteDecimal, nullable=False)
    deaths = Column(Integer, nullable=False)
    avoided_deaths = Column(Integer, nullable=False)
    found_chests = Column(Integer, nullable=False)
    activated_keys = Column(Integer, nullable=False)
    completed_events = Column(Integer, nullable=False)
    built_things = Column(Integer, nullable=False)
    auto_sacrifices = Column(Integer, nullable=False)
    sacrifices = Column(Integer, nullable=False)
    times_being_sacrificed = Column(Integer, nullable=False)

    current_tile: "TileSaModel" = relationship("TileSaModel", foreign_keys=["tile_id"], back_populates="players")
    previous_tile: "TileSaModel" = relationship("TileSaModel", foreign_keys=["previous_tile_id"])
    tiles_marked_by_close_sight: List["TileSaModel"] = relationship(
        "TileSaModel", secondary=player_to_close_tiles_table
    )
    tiles_marked_by_monster_sight: List["TileSaModel"] = relationship(
        "TileSaModel", secondary=player_to_monster_sight_tiles_table
    )
    tiles_walked: List["TileSaModel"] = relationship("TileSaModel", secondary=player_to_seen_tiles_table)
    team: "TeamSaModel" = relationship("TeamSaModel", back_populates="players")
    inventory: List["ItemSaModel"] = relationship("ItemSaModel")
