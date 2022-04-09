from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.configuration.database import Base
from models.utils.enums.caracteristic import CaracteristicEnum

if TYPE_CHECKING:
    from models.effects.labyrinth_effect import LabyrinthEffectSaModel
    from models.effects.player_effect import PlayerEffectSaModel


class EventEffectSaModel(Base):
    __tablename__ = "event_effect"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("event.id"), nullable=False)
    rank = Column(Integer, nullable=False)
    choice_text = Column(String, nullable=False)
    player_effect_id = Column(Integer, ForeignKey("player_effect.id"), nullable=False)

    player_effect: "PlayerEffectSaModel" = relationship("PlayerEffectSaModel", uselist=False)
    tile_effects: List["LabyrinthEffectSaModel"] = relationship(
        "LabyrinthEffectSaModel", secondary="event_effect_to_labyrinth_effect_table", uselist=True
    )
    caracteristic_required = Column(Enum(CaracteristicEnum), nullable=False)
    caracteristic_value = Column(Integer, nullable=False)

    __table_args_ = UniqueConstraint("rank", "event_id")
