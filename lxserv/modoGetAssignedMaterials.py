# python

#------------------------------------------------------------------------------
# VISMO Gety Assigned Materials v1.0.0, James Berkheimer
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


class GetAssignedMaterials_Command(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add('name', lx.symbol.sTYPE_STRING)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)
    
    def basic_Execute(self, msg, flags):
        try:
            scene = modo.Scene()
            meshes = scene.selectedByType('mesh')
            for mesh in meshes:
                groupMasks = tools.getAssignedMaterials(mesh)   
                # Print their names and children's names
                lx.eval("select.drop item")
                for groupMask in groupMasks:
                    print ''
                    print 'groupMask {}:'.format(groupMask.name)
                    lx.eval("select.item %s add" %(groupMask.id))
                    for child in groupMask.children():
                        print '- child {}'.format(child.name)
        except Exception as e:
            lx.out(e)
            lx.out("\n")
            
lx.bless(GetAssignedMaterials_Command, "vismo.getAssMat")