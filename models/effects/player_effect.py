from sqlalchemy import Column, Integer

from app.configuration.database import Base


class PlayerEffectSaModel(Base):
    __tablename__ = "player_effect"

    id = Column(Integer, primary_key=True)

    # TODO: Add columns for parameters
    # Lots of parameters columns => Big function that takes it all => mini-functions that take each parameter.
