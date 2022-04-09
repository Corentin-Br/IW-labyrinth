from sqlalchemy import Column, Integer, String

from app.configuration.database import Base


class ItemSaModel(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)
