from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

feature_switch_to_feature_table = Table(
    "feature_switch_to_feature_table",
    Column("id", Integer, primary_key=True),
    Column("feature_switch_id", Integer, ForeignKey("feature_switch.id"), nullable=False),
    Column("feature_id", Integer, ForeignKey("feature.id"), nullable=False),
    UniqueConstraint("feature_switch_id", "feature_id"),
)
