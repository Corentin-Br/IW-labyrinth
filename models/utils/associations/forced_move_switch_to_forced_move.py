from sqlalchemy import Column, ForeignKey, Integer, Table, UniqueConstraint

force_move_switch_to_forced_move_table = Table(
    "force_move_switch_to_forced_move_table",
    Column("id", Integer, primary_key=True),
    Column("forced_move_switch_id", Integer, ForeignKey("forced_move_switch.id"), nullable=False),
    Column("forced_move_id", Integer, ForeignKey("forced_move.id"), nullable=False),
    UniqueConstraint("forced_move_switch_id", "forced_move_id"),
)
