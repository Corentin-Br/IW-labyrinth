from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from app.configuration.database import Base

if TYPE_CHECKING:
    from models.conditions.player_full_condition import PlayerFullConditionSaModel


class TeleporterEffectSaModel(Base):
    __tablename__ = "teleporter_effect"

    id = Column(Integer, primary_key=True)
    origin_id = Column(Integer, ForeignKey("teleporter.id"), nullable=False)
    destination_id = Column(Integer, ForeignKey("teleporter.id"), nullable=False)
    order = Column(
        Integer, nullable=False
    )  # determines the order in which the effects are checked by the Teleporter. If one condition is true, the
    # following ones aren't checked.

    alternative_conditions: List["PlayerFullConditionSaModel"] = relationship(
        "PlayerFullConditionSaModel", uselist=True, secondary="player_full_condition_to_teleporter_table"
    )

    __table_args__ = (UniqueConstraint(order, origin_id),)
