=> Switches need to be perfectly symmetric (i.e activating + deactivating does a net 0). Otherwise
we run into problems for CancelSwitch (they work through activating activated switches to 
deactivate them).

This means that switches must always switch the state of walls and cannot be only activate/only 
deactivate.

Note that it's not enough to have the same behaviour when activated and deactivated.
IT MUST BE SWITCH ONLY, otherwise it could lead to inconsistencies if the switches aren't 
deactivated in the same order all the time (and is overall way too tedious.)