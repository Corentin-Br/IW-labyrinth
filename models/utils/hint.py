from sqlalchemy import Column, Enum, ForeignKey, Integer, String, UniqueConstraint

from app.configuration.database import Base
from models.utils.enums.caracteristic import CaracteristicEnum


class HintSaModel(Base):
    __tablename__ = "hint"

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    caracteristic_required = Column(Enum(CaracteristicEnum), nullable=False)
    caracteristic_value = Column(Integer, nullable=False)
    event_id = Column(Integer, ForeignKey("event.id"), nullable=False)

    __table_args_ = UniqueConstraint("caracteristic_required", "caracteristic_value", "event_id")
