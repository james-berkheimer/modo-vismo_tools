#!/usr/bin/env python


#------------------------------------------------------------------------------
# VISMO Version Up Scene v1.0.0, James Berkheimer
#------------------------------------------------------------------------------

# Standard library imports
import traceback

# Third party imports
import lx
import lxifc
import lxu.command
import modo

# Local application imports
import vismo.setup as setup

class VersionUpScene_Command(lxu.command.BasicCommand):
	def __init__(self):
		lxu.command.BasicCommand.__init__(self)
		self.dyna_Add('name', lx.symbol.sTYPE_STRING)
		self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)        
		
	def basic_Execute(self, msg, flags):
		try:    
			setup.saveRenderReadyVersion()        
			lx.eval('dialog.title {New version saved}')
			lx.eval('dialog.msg {Your scene is now versioned up.}')
			lx.eval('dialog.result ok')
			lx.eval('dialog.open')            
		except:
			lx.out("\n")
		
		
lx.bless(VersionUpScene_Command, "vismo.versionup")