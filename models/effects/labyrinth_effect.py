from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer

from app.configuration.database import Base


class LabyrinthEffectSaModel(Base):
    __tablename__ = "labyrinth_effect"

    id = Column(Integer, primary_key=True)

    closed_wall_id = Column(Integer, ForeignKey("wall.id"))
    opened_wall = Column(Integer, ForeignKey("wall.id"))
    removed_feature_id = Column(Integer, ForeignKey("feature.id"))
    activated_feature_id = Column(Integer, ForeignKey("feature.id"))

    tile_id = Column(Integer, ForeignKey("tile.id"))
    player_effect_id = Column(
        Integer, ForeignKey("player_effect.id")
    )  # all players present on the tile will receive the effect

    __table_args__ = (
        CheckConstraint(
            "(tile_id IS NOT NULL AND player_effect_id IS NOT NULL) OR (tile_id IS NULL and player_effect_id IS NULL)"
        ),
    )
