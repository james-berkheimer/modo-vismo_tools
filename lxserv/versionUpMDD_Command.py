#!/usr/bin/env python

#------------------------------------------------------------------------------
# VISMO Version Up Scene v1.0.0, James Berkheimer
#------------------------------------------------------------------------------

# Standard library imports
import os, glob
import traceback

# Third party imports
import lx
import lxifc
import lxu.command
import modo

# Local application imports
import vismo.tools as tools

class versionUpAllMDDs_Command(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        
    def basic_Execute(self, msg, flags):
        scene = modo.Scene()
        for deformer in scene.deformers():
            if deformer.type == 'deformMDD2':
                fileChan = deformer.channel('file')
                latestMDDFile = tools.getLatestFileVersion(fileChan.get(), ".mdd")
                fileChan.set(latestMDDFile)
        lx.eval('dialog.title {MDD Updating}')
        lx.eval('dialog.msg {All MDDs are now updated to the latest file version.}')
        lx.eval('dialog.result ok')
        lx.eval('dialog.open')   
            
lx.bless(versionUpAllMDDs_Command, "vismo.versionUpAllMDDs")

#---------------------------------------------------------------

class VersionUpSelectedMDDs_Command(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        
    def findDeformer(self, parent):
        for child in parent.children():
            if child.type == "deformMDD2":
                return child
            else:
                return self.findDeformer(child)
        
    def basic_Execute(self, msg, flags):
        scene = modo.Scene()
        selected = scene.selected
        for selection in selected:
            deformer = self.findDeformer(selection)
            print deformer
            if deformer:
                fileChan = deformer.channel('file')
                latestMDDFile = tools.getLatestFileVersion(fileChan.get(), ".mdd")
                print latestMDDFile
                fileChan.set(latestMDDFile)
        lx.eval('dialog.title {MDD Updating}')
        lx.eval('dialog.msg {The Selected MDDs are now updated to the latest file version.}')
        lx.eval('dialog.result ok')
        lx.eval('dialog.open')            
            
lx.bless(VersionUpSelectedMDDs_Command, "vismo.versionUpSelectedMDDs")

