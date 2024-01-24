#!/usr/bin/env python

#------------------------------------------------------------------------------
# VISMO Modo Mesh Export v1.0.0, James Berkheimer
#------------------------------------------------------------------------------

# Standard library imports
import traceback

# Third party imports
import lx
import lxifc
import lxu.command
import modo

class Modo_OBJ_Export(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.scene = modo.Scene()
        self.meshes = self.scene.selected
    
    def basic_Execute(self, msg, flags):
        try:
            lx.out("Testing modoMeshExport")
            self.exportOBJ()
        except Exception as e:
            lx.out(e)
            lx.out("\n Export Failed...")
            
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
            
    def exportOBJ(self):
        print "Exporting"
        lx.eval("export.selected 15 false true true")
        
        
################################################################################################


    
lx.bless(Modo_OBJ_Export, "vismo.meshOBJExport")