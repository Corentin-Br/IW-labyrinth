from sqlalchemy import Column, Enum, ForeignKey, Integer

from models.configuration.app import Base
from models.utils.enums.items import ItemEnum


class ItemSaModel(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(Enum(ItemEnum), nullable=False)
    player_id = Column(Integer, ForeignKey("player.id"), nullable=False)
