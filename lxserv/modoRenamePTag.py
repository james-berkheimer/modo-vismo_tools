# python

# Third party imports
import lx
import lxifc
import lxu.command
import modo


class RenamPTagCmdArg(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        
    def renamPtag(self):
        lx.eval("!!select.drop item")
        meshes = modo.Scene().items('mesh')
        ptags = set()
        for mesh in meshes:
            for tagType in (lx.symbol.i_POLYTAG_MATERIAL, lx.symbol.i_POLYTAG_PART):
                for index in range(mesh.geometry.PTagCount(tagType)):
                    ptag = mesh.geometry.internalMesh.PTagByIndex(tagType, index)	
                    if 'ptag' in ptag:
                        ptagInfo = ptag.split('_')
                        newptag = "_".join(ptagInfo[:-1]) + "_ptag"
                        lx.eval("select.item %s set" %(mesh.name))
                        lx.eval('poly.renameTag %s {%s} MATR' % (ptag, newptag))			
        lx.eval("!!select.drop item")    

    def basic_Execute(self, msg, flags):
        try:
            lx.out("Testing modoRenamPTag")
            self.renamPtag()
        except Exception as e:
            lx.out(e)
            lx.out("\n Rename Failed...")
    

lx.bless(RenamPTagCmdArg, "vismo.renamePTag")