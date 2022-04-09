from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from models.effects.labyrinth_effect import LabyrinthEffectSaModel


class ExchangeSaModel(Base):
    __tablename__ = "exchange"

    id = Column(Integer, primary_key=True)
    npc_id = Column(Integer, ForeignKey("npc.id"), nullable=False)
    wanted_item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    given_item_id = Column(Integer, ForeignKey("item.id"))  # intentionally nullable
    exchange_text = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)

    effects: List["LabyrinthEffectSaModel"] = relationship(
        "LabyrinthEffectSaModel", secondary="exchange_to_labyrinth_effect_table", uselist=True
    )

    __table_args__ = (UniqueConstraint("npc_id", "rank"), UniqueConstraint("npc_id", "wanted_item_id"))
