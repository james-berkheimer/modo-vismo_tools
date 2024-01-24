# python

# Standard library imports
import os
from shutil import copyfile

# from lxserv import *

# Third party imports
import lx
import lxifc
import lxu.command
import modo

version = lx.eval("query platformservice appversion ?")
if version < 1501:
    print("Importing PySide")
    from PySide import QtGui
    from PySide import QtCore
else:
    print("Importing PySide2")
    from PySide2 import QtCore, QtWidgets, QtGui

# Local application imports
import vismo.tools as tools


class MakeNewShotCmdArg(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)

    def saveScene(self):
        # newShotName = tools.dialog_getShotName()
        newProjectCode = tools.dialog_getText("code", "Enter Project Code")
        newShotNumber = tools.dialog_getText("shotnum", "Enter Shot Number")
        newShotSuffix = tools.dialog_getText("suffix",
                                             "Enter Description Suffix")
        newShotPhase = tools.dialog_getText("phase", "Enter Shot Phase")
        newUserInitials = tools.dialog_getText("initials",
                                               "Enter User Initials")
        newShotName = newProjectCode + "_" + newShotNumber
        newShotDir = tools.dialog_getDirectory(
            "Select the PROJECT ANIMATION directory"
        ) + "\\" + newProjectCode + "_MODO" "\\" + newShotPhase.upper(
        ) + "\\" + newShotName

        # Make new file name and file path
        if newShotSuffix:
            newSceneName = newShotName + "-" + newShotSuffix + "_v001_" + newUserInitials.upper(
            ) + ".lxo"
        else:
            newSceneName = newShotName + "_v001_" + newUserInitials.upper(
            ) + ".lxo"
        newScenePathFull = newShotDir + "\\" + newSceneName

        # Create new directory structure and copy over file with new name
        lx.out(newShotDir)
        try:
            os.makedirs(newShotDir)
        except Exception as e:
            lx.out(e)
            lx.out("Path exists!")

        if os.path.isfile(newScenePathFull):
            if modo.dialogs.yesNo(
                    "Save scene",
                    "Scene already exists!  Do you want to overwrite?"
            ) == "yes":
                lx.eval("scene.saveAs {%s}" % (newScenePathFull))
                lx.out("New scene created in %s" % (newScenePathFull))
            else:
                exit()
        else:
            lx.eval("scene.saveAs {%s}" % (newScenePathFull))
            lx.out("New scene created in %s" % (newScenePathFull))

    def basic_Execute(self, msg, flags):
        lx.out("Running Make New Shot")
        self.saveScene()


lx.bless(MakeNewShotCmdArg, "vismo.makeNewShot")