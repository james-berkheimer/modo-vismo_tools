#!/usr/bin/env python

#------------------------------------------------------------------------------
# VISMO Modo OBJ Import v1.0.0, James Berkheimer
#------------------------------------------------------------------------------

# Standard library imports
import traceback

# Third party imports
import lx
import lxifc
import lxu.command
import modo

# Local application imports
import vismo.tools as tools

class Modo_OBJ_Import(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.scene = modo.Scene()
        self.meshes = self.scene.selected
    
    def basic_Execute(self, msg, flags):
        objPaths = []
        # set up the dialog
        lx.eval('dialog.setup fileOpenMulti')
        lx.eval('dialog.fileTypeCustom wf_OBJ WaveFront *.obj *.obj')
        __open_path = "O:\Clients"
        sceneDir = tools.getDirectory()
        rootDir = tools.getProjectRoot()
        if sceneDir:
            projectShot = sceneDir.split('\\')[-1]
            __open_path = rootDir + "cache\\MDD\\" + projectShot
        lx.eval('dialog.result {%s}' % __open_path)
        
        # Open the dialog and see which button was pressed
        lx.eval('dialog.open')
        objPaths = lx.eval("dialog.result ?")
        if objPaths:
            lx.out("objPaths:", objPaths)
            self.importOBJ(objPaths)
        else:
            lx.out("Canceled!")
            exit
            
    def setPolyParts(self):
        print "Deleting multiple Poly Parts and renaming one to mesh name"
        for mesh in self.meshes:
            print ("Check for mesh type")
            if mesh.type == "mesh":
                print ("Get Geo")
                geo = mesh.geometry
                print ("Get Parts")
                parts = [geo.PTagByIndex(lx.symbol.i_PTAG_PART, p) for p in xrange(geo.PTagCount(lx.symbol.i_PTAG_PART))]
                print ("Loop Parts")
                for part in parts:
                    lx.eval('poly.renameTag %s {%s} PART' % (part, mesh.name))
            
    def getMetaData(self, objPath): 
        import mmap
        f = open(objPath.replace(".obj", ".vismo"))
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        animCachePath = ""
        for line in iter(s.readline, ""):
            if "SCALE" in line:
                sceneScale = line.split(" ")[1].strip()
            if "MDD:" in line:
                animCachePath = line.split(" ")[1].strip()
        return animCachePath, sceneScale      

    def importOBJ(self, objPaths):
        print "----- In importOBJ -----"
        if type(objPaths) == str:
            objPaths = [objPaths]
        for objPath in objPaths:
            mddPath, sceneScale = self.getMetaData(objPath)
            lx.eval ('loaderOptions.wf_OBJ false false false %s' %('meters'))
            lx.eval ('!scene.open "%s" import' % objPath)
            # Select import OBJ Mesh item
            objName = objPath.split('\\')[-1].split('.')[0]
            lx.eval('select.item "%s" set' % objName)
            groupName = objName + "_GRP"
            lx.eval('item.name "%s" groupLocator' % groupName)
            lx.eval("pickwalk down")
            meshName = objName + "_MSH"
            lx.eval('item.name "%s" mesh' % meshName)
            # Attach MDD to OBJ Mesh item
            if mddPath:
                lx.eval('deform.mddAdd {%s}' % mddPath)
                lx.eval("pickwalk down")
                mddName = objName + "_MDD"
                lx.eval('item.name "%s" deformMDD2' % mddName)
        print "----- Out importOBJ -----"    
        
        
################################################################################################

    
lx.bless(Modo_OBJ_Import, "vismo.OBJImport")