from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

cancel_switch_to_amovible_switch_table = Table(
    "cancel_switch_to_amovible_switch_table",
    Column("id", Integer, primary_key=True),
    Column("cancel_switch_id", Integer, ForeignKey("cancel_switch.id"), nullable=False),
    Column("amovible_switch_id", Integer, ForeignKey("amovible_switch.id"), nullable=False),
    UniqueConstraint("cancel_switch_id", "amovible_switch_id"),
)
