from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

cancel_switch_to_binary_switch = Table(
    "cancel_switch_to_binary_switch",
    Column("id", Integer, primary_key=True),
    Column("cancel_switch_id", Integer, ForeignKey("cancel_switch.id"), nullable=False),
    Column("binary_switch_id", Integer, ForeignKey("binary_switch.id"), nullable=False),
    UniqueConstraint("cancel_switch_id", "binary_switch_id"),
)
