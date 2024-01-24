# python

# Standard library imports
import traceback

# Third party imports
import lx
import lxifc
import lxu.command
import modo


class Channel2Setup_Command(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add('name', lx.symbol.sTYPE_STRING)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)        
        
    def basic_Execute(self, msg, flags):
        try:
            lx.eval("channel.wipe")
            lx.eval("group.edit add chan pass")
            lx.eval("channel.toSetup")
        except Exception as e:
            lx.out(e)
            lx.out("\n")
        
        
lx.bless(Channel2Setup_Command, "vismo.chan2setup")