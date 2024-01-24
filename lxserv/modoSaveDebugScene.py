# python


# Standard library imports
import os
from shutil import copyfile

# Third party imports
import lx
import lxifc
import lxu.command
import modo

# Local application imports
import vismo.tools as tools

class SaveDebugSceneCmdArg(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        
    def saveDebugScene(self):
        rootDir = "O:\\Clients"
        newRootDir = str()
        filename = modo.Scene().filename
        currSceneName = os.path.basename(filename)
        currScenePath = os.path.dirname(filename)
        currUser = tools.getUserInitials()
        newUserInitials = tools.dialog_getText("initials", "Enter User Initials")
        newRootDir = tools.dialog_getDirectory()
            
        # Make new file name and file path
        lx.out(rootDir)
        lx.out(newRootDir) 
        newScenePath = currScenePath.replace(rootDir, newRootDir)
        newSceneName = currSceneName.replace("_" + currUser, "_" + newUserInitials)
        newScenePathFull = newScenePath + "\\" + newSceneName        
               
        # Create new directory structure and copy over file with new name
        lx.out(newScenePath)
        try:
            os.makedirs(newScenePath)
        except Exception as e:
            lx.out(e)
            lx.out("Path exists!")
        lx.out(filename)
        lx.out(newScenePathFull)
        
        try:
            # copyfile(filename, newScenePathFull)
            lx.eval("scene.saveAs {%s}" % (newScenePathFull))
        except Exception as e:
            lx.out(e)
            lx.out("Failed to copy scene file")

        lx.out("Debug scene moved to: %s" % (newScenePathFull))

    def basic_Execute(self, msg, flags):
        try:
            lx.out("Running saveDebugScene")
            self.saveDebugScene()
        except Exception as e:
            lx.out(e)
            lx.out("\n Script Failed...")
    

lx.bless(SaveDebugSceneCmdArg, "vismo.saveDebugScene")