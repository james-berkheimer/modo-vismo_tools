#!/usr/bin/env python

#------------------------------------------------------------------------------
# VISMO MDD Tool v1.0.0, James Berkheimer
#------------------------------------------------------------------------------

# Standard library imports
import traceback
from functools import partial
import os
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
    gui = QtGui
else:
    print("Importing PySide2")
    from PySide2 import QtCore, QtWidgets, QtGui
    gui = QtWidgets


class MDDTool_Cmd(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add('name', lx.symbol.sTYPE_STRING)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)

    def basic_Execute(self, msg, flags):
        try:
            lx.eval("log.masterClear")
            lx.out("I am mddTool")
            self.main()

        except Exception as e:
            lx.out(e)
            lx.out("\n", "Failed Launch")
            lx.out(traceback.format_exc())

    def main(self, **options):
        lx._widget = MainWindow
        lx._widgetOptions = options
        lx.eval('launchWidget')


class MainWindow(gui.QMainWindow):
    onClose = QtCore.Signal()

    def __init__(self, parent=None, **options):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('MDD Import Tool v1.0.0')
        self.resize(1200, 650)

        scene = modo.Scene()
        filename = scene.filename
        self.importTab_widget = Import_Tab(self)
        self.manageTab_widget = Manage_Tab(self)

        _widget = gui.QWidget()
        _layout = gui.QVBoxLayout(_widget)

        _tabs = gui.QTabWidget()
        _tabs.addTab(self.importTab_widget, "Import MDDs")
        _tabs.addTab(self.manageTab_widget, "Manage MDDs")

        _layout.addWidget(_tabs)
        self.setCentralWidget(_widget)


################################################################################################


class Import_Tab(gui.QWidget):
    def __init__(self, parent):
        super(Import_Tab, self).__init__(parent)
        # we still have access to the TD SDK
        #Get script directory path
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        scriptDir = os.path.dirname(scriptDir)
        scene = modo.Scene()
        self.filename = scene.filename
        self.project_mdd_path = self.getProjectMDDPath()
        rightArrow_icon = "\\icons\\right-arrows37.png"
        leftArrow_icon = "\\icons\\left-arrows37.png"
        self.rightArrow_icon_path = scriptDir + rightArrow_icon
        self.leftArrow_icon_path = scriptDir + leftArrow_icon

        #--------------------------------------------------------------------------
        # Call the tab functions
        #--------------------------------------------------------------------------

        #--------------------------------------------------------------------------
        # Set layouts
        #--------------------------------------------------------------------------
        self.main_layout = gui.QVBoxLayout()
        self.projectsSplitter = gui.QSplitter()
        self.projectsSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.projectsSplitter.setObjectName("projectsSplitter")
        self.topSide = gui.QWidget()
        self.topSide.resize(100, 800)
        self.leftSide = gui.QWidget()
        self.rightSide = gui.QWidget()
        self.file_path_layout = gui.QHBoxLayout()
        self.bin_layout = gui.QVBoxLayout()
        self.bin_buttons_layout = gui.QHBoxLayout()
        self.import_layout = gui.QVBoxLayout()
        self.import_buttons_layout = gui.QHBoxLayout()

        #--------------------------------------------------------------------------
        # Creating Widget Items
        #--------------------------------------------------------------------------
        self.create_file_path_browser()
        self.create_holding_bin()
        self.create_import_bin()
        self.populateTrees(self.project_mdd_path)

        #--------------------------------------------------------------------------
        # Populate main layout
        #--------------------------------------------------------------------------
        self.projectsSplitter.addWidget(self.leftSide)
        self.projectsSplitter.addWidget(self.rightSide)
        self.main_layout.addLayout(self.file_path_layout)
        self.main_layout.addWidget(self.projectsSplitter)
        self.setLayout(self.main_layout)

    #--------------------------------------------------------------------------
    # Main layout functions
    #--------------------------------------------------------------------------

    def create_file_path_browser(self):
        self.file_path_label = gui.QLabel("Project MDD Path:")
        self.file_path_lineedit = gui.QLineEdit(self.project_mdd_path)
        self.file_path_browse_button = gui.QPushButton("Browse")
        self.file_path_browse_button = Utl.createButton(
            "Set Project MDD Path", self.browseSetProjectMDDPath)
        self.file_path_browse_button.setMinimumWidth(100)
        self.file_path_layout.addWidget(self.file_path_label)
        self.file_path_layout.addWidget(self.file_path_lineedit, 1)
        self.file_path_layout.addWidget(self.file_path_browse_button, 0)
        self.file_path_layout.setContentsMargins(8, 10, 8, 0)

    def create_holding_bin(self):
        self.holding_bin_tree = gui.QTreeWidget()
        self.holding_bin_tree.setColumnCount(2)
        self.holding_bin_tree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.holding_bin_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.holding_bin_tree.setEditTriggers(
            gui.QAbstractItemView.NoEditTriggers)
        self.holding_bin_tree.setAlternatingRowColors(True)
        self.holding_bin_tree.setUniformRowHeights(False)
        self.holding_bin_tree.setSelectionMode(
            gui.QAbstractItemView.ExtendedSelection)
        self.holding_bin_tree.setObjectName("holding_bin_tree")
        self.holding_bin_tree.header().setVisible(True)
        self.holding_bin_tree.header().setDefaultSectionSize(200)
        self.holding_bin_tree.header().setMinimumSectionSize(25)
        self.holding_bin_tree.header().setSortIndicatorShown(False)
        self.holding_bin_tree.headerItem().setText(
            0,
            gui.QApplication.translate("MDD Importer", "Objects", None,
                                       gui.QApplication.UnicodeUTF8))
        self.holding_bin_tree.headerItem().setText(
            1,
            gui.QApplication.translate("MDD Importer", "File path", None,
                                       gui.QApplication.UnicodeUTF8))

        self.add_to_bin_button = Utl.createButton("Add to Bin",
                                                  self.browseAddToBin)
        self.remove_from_bin_button = Utl.createButton("Remove from Bin",
                                                       self.removeFromOBJBin)
        self.add_for_import_button = Utl.createToolButton(
            "Add", self.moveToImportBin, self.rightArrow_icon_path)
        self.add_for_import_button.setToolTip("Move to Import Box")

        self.bin_buttons_layout.addWidget(self.add_to_bin_button)
        self.bin_buttons_layout.addWidget(self.remove_from_bin_button)
        self.bin_buttons_layout.addWidget(self.add_for_import_button)

        self.bin_layout.addWidget(self.holding_bin_tree)
        self.bin_layout.addLayout(self.bin_buttons_layout)
        self.leftSide.setLayout(self.bin_layout)

    def create_import_bin(self):
        self.import_bin_tree = gui.QTreeWidget()
        self.import_bin_tree.setColumnCount(1)
        self.import_bin_tree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.import_bin_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.import_bin_tree.setEditTriggers(
            gui.QAbstractItemView.NoEditTriggers)
        self.import_bin_tree.setAlternatingRowColors(True)
        self.import_bin_tree.setUniformRowHeights(False)
        self.import_bin_tree.setSelectionMode(
            gui.QAbstractItemView.ExtendedSelection)
        self.import_bin_tree.setObjectName("import_bin_tree")
        self.import_bin_tree.header().setVisible(True)
        self.import_bin_tree.header().setDefaultSectionSize(200)
        self.import_bin_tree.header().setMinimumSectionSize(25)
        self.import_bin_tree.header().setSortIndicatorShown(False)
        self.import_bin_tree.headerItem().setText(
            0,
            gui.QApplication.translate("MDD Importer", "Files to Import", None,
                                       gui.QApplication.UnicodeUTF8))
        self.import_bin_tree.headerItem().setText(
            1,
            gui.QApplication.translate("MDD Importer", "File path", None,
                                       gui.QApplication.UnicodeUTF8))

        self.remove_from_import_button = Utl.createToolButton(
            "Remove", self.moveToHoldingBin, self.leftArrow_icon_path)
        self.remove_from_import_button.setToolTip("Remove from Import Box")
        self.importMDDs_button = Utl.createButton("Import", self.importOBJ)

        self.import_buttons_layout.addWidget(self.remove_from_import_button)
        self.import_buttons_layout.addWidget(self.importMDDs_button)

        self.import_layout.addWidget(self.import_bin_tree)
        self.import_layout.addLayout(self.import_buttons_layout)
        self.rightSide.setLayout(self.import_layout)

    #--------------------------------------------------------------------------
    # Utility functions
    #--------------------------------------------------------------------------

    def browseAddToBin(self):
        print "----- In browseAddToBin -----"
        directory = gui.QFileDialog.getExistingDirectory(
            self, "Find Files", self.file_path_lineedit.text())
        self.file_path_lineedit.setText(directory)
        self.populateTrees(directory)
        print "----- Out browseAddToBin -----"

    def browseMDD(self):
        print "----- In browseMDD -----"
        selectedItem = self.holding_bin_tree.selectedItems()
        if len(selectedItem) > 1:
            print "Too many selected items"
        else:
            print "selected item: " + selectedItem[0].text(0)
            mddFilePath = gui.QFileDialog.getOpenFileName(
                self, "Find MDD", self.path, "MDD Files (*.mdd)")
            mddFile = mddFilePath[0].split('/')[-1]
            print "Attaching: " + mddFile
            mddItem = gui.QTreeWidgetItem()
            mddItem.setText(0, mddFile)
            print "Child: " + selectedItem[0].child(1).text(0)
            selectedItem[0].removeChild(selectedItem[0].child(0))
            selectedItem[0].addChild(mddItem)
        print "----- Out browseMDD -----"

    def browseSetProjectMDDPath(self):
        print "----- In browseSetProjectMDDPath -----"
        directory = gui.QFileDialog.getExistingDirectory(
            self, "Set project MDD path", self.file_path_lineedit.text())
        self.project_mdd_path = directory
        self.file_path_lineedit.setText(directory)
        self.populateTrees(directory)
        print "----- Out browseSetProjectMDDPath -----"

    def getFiles(self, filepath):
        print "----- In getFiles -----"
        print filepath
        currentDir = QtCore.QDir(filepath)
        fileName = "*"
        files = currentDir.entryList([fileName], QtCore.QDir.Files
                                     | QtCore.QDir.NoSymLinks)
        mdd_files = []
        obj_files = []

        for f in files:
            if ".mdd" in f:
                mdd_files.append(f)
            if ".obj" in f:
                obj_files.append(f)
        print "----- Out getFiles -----"
        return mdd_files, obj_files

    def getImportDict(self):
        print "----- In getImportDict -----"
        importDict = {}
        for item in self.getImportBinTreeList():
            valueList = [item.child(0).text(0), item.child(0).text(1)]
            importDict[item.text(0)] = valueList
        print "----- Out getImportDict -----"
        return importDict

    def getProjectMDDPath(self):
        print "----- In getProjectMDDPath -----"
        if self.filename:
            print(self.filename)
            pathInfo = self.filename.split("\\")
            index = pathInfo.index("Animation") + 1
            pathInfo = pathInfo[:index]
            shot = self.filename.split("\\")[-2]
            newpath = ""
            for i in pathInfo:
                newpath = newpath + i + "\\"
            mddPath = newpath + "cache\\MDD\\" + shot
            print "----- Out getProjectMDDPath -----"
            return mddPath

    def getHoldingBinTreeList(self):
        print "----- In getHoldingBinTreeList -----"
        root = self.holding_bin_tree.invisibleRootItem()
        treeCount = root.childCount()
        print("Tree count: " + str(treeCount))
        treeList = []
        for i in range(treeCount):
            item = root.child(i)
            print item.text(0)
            treeList.append(item)
        print "----- Out getHoldingBinTreeList -----"
        return treeList

    def getImportBinTreeList(self):
        print "----- In getImportBinTreeList -----"
        root = self.import_bin_tree.invisibleRootItem()
        treeCount = root.childCount()
        treeList = []
        for i in range(treeCount):
            item = root.child(i)
            treeList.append(item)
        print "----- Out getImportBinTreeList -----"
        return treeList

    def importOBJ(self):
        print "----- In importOBJ -----"
        importDict = {}
        importDict = self.getImportDict()
        for key, value in importDict.iteritems():
            obj_name = key
            obj_path = value[1] + "\\" + key
            mdd_path = value[1] + "\\" + value[0]
            if value[1]:
                # Import OBJ
                lx.eval('loaderOptions.wf_OBJ false false Meters')
                lx.eval('!scene.open "%s" import' % obj_path)
                # Select import OBJ Mesh item
                name = obj_name.split('.')[0]
                lx.eval('select.item "%s" set' % name)
                groupName = name + "_GRP"
                lx.eval('item.name "%s" groupLocator' % groupName)
                lx.eval("pickwalk down")
                meshName = name + "_MSH"
                lx.eval('item.name "%s" mesh' % meshName)
                # Attach MDD to OBJ Mesh item
                lx.eval('deform.mddAdd {%s}' % mdd_path)
                lx.eval("pickwalk down")
                mddName = name + "_MDD"
                lx.eval('item.name "%s" deformMDD2' % mddName)
        print "----- Out importOBJ -----"

    def moveToImportBin(self):
        print "----- In moveToImportBin -----"
        selectedItems = self.holding_bin_tree.selectedItems()
        root = self.holding_bin_tree.invisibleRootItem()
        for item in selectedItems:
            print item.text(0)
            objName = item.text(0)
            filepath = item.text(1)
            mddName = item.child(0).text(0)
            mddItem = gui.QTreeWidgetItem(self.import_bin_tree)
            mddItem.setSizeHint(0, QtCore.QSize(200, 35))
            mddItem.setText(0, objName)
            mddItem.setText(1, filepath)
            mddItem.setForeground(1, gui.QBrush(gui.QColor('#575757')))

            self.import_bin_tree.addTopLevelItem(mddItem)
            self.import_bin_tree.sortItems(0, QtCore.Qt.AscendingOrder)

            mddChildItem = gui.QTreeWidgetItem(mddItem)
            mddChildItem.setText(0, mddName)
            mddChildItem.setText(1, filepath)

            #remove the item from the OBJ tree
            (item.parent() or root).removeChild(item)
        print "----- Out moveToImportBin -----"

    def populateTrees(self, filepath):
        print "----- In populateTrees -----"
        mdd_files, obj_files = self.getFiles(filepath)
        treeList = self.getHoldingBinTreeList()
        s = set(treeList)
        items_to_add = [x for x in obj_files if x not in s]
        for obj in items_to_add:
            print "OBJ: " + obj
            objItem = gui.QTreeWidgetItem(self.holding_bin_tree)
            objItem.setSizeHint(0, QtCore.QSize(200, 35))
            objItem.setText(0, obj)
            objItem.setText(1, filepath)
            self.holding_bin_tree.addTopLevelItem(objItem)
            self.holding_bin_tree.sortItems(0, QtCore.Qt.AscendingOrder)
            tmp = []
            for mdd in mdd_files:
                if obj.split('.')[0] in mdd:
                    print "MDD: " + mdd
                    tmp.append(mdd)
            print "MDD List:"
            print tmp
            if tmp:
                tmp2 = sorted(tmp)[-1]
            else:
                tmp2 = "EMPTY"
                objItem.setForeground(0, gui.QBrush(gui.QColor(200, 0, 0)))
            mddItem = gui.QTreeWidgetItem(objItem)
            mddItem.setText(0, tmp2)
            mddItem.setText(1, filepath)
        print "----- Out populateTrees -----"

    def removeFromOBJBin(self):
        print "----- In removeFromOBJBin -----"
        selectedItems = self.holding_bin_tree.selectedItems()
        root = self.holding_bin_tree.invisibleRootItem()
        for item in selectedItems:
            (item.parent() or root).removeChild(item)
        print "----- Out removeFromOBJBin -----"

    def moveToHoldingBin(self):
        print "----- In moveToHoldingBin -----"
        selectedItems = self.import_bin_tree.selectedItems()
        root = self.import_bin_tree.invisibleRootItem()
        for item in selectedItems:
            print item.text(0)
            objName = item.text(0)
            filepath = item.text(1)
            mddName = item.child(0).text(0)
            mddItem = gui.QTreeWidgetItem(self.holding_bin_tree)
            mddItem.setSizeHint(0, QtCore.QSize(200, 35))
            mddItem.setText(0, objName)
            mddItem.setText(1, filepath)
            mddItem.setForeground(1, gui.QBrush(gui.QColor('#575757')))

            self.holding_bin_tree.addTopLevelItem(mddItem)
            self.holding_bin_tree.sortItems(0, QtCore.Qt.AscendingOrder)

            mddChildItem = gui.QTreeWidgetItem(mddItem)
            mddChildItem.setText(0, mddName)

            #remove the item from the OBJ tree
            (item.parent() or root).removeChild(item)

        print "----- Out moveToHoldingBin -----"


################################################################################################


class Manage_Tab(gui.QWidget):
    def __init__(self, parent):
        super(Manage_Tab, self).__init__(parent)
        scene = modo.Scene()
        self.filename = scene.filename
        self.project_mdd_path = self.getProjectMDDPath()

        #--------------------------------------------------------------------------
        # Set layouts
        #--------------------------------------------------------------------------
        self.main_layout = gui.QVBoxLayout()
        self.topSide = gui.QWidget()
        self.topSide.resize(100, 800)
        self.meshBin = gui.QWidget()
        self.rightSide = gui.QWidget()
        self.file_path_layout = gui.QHBoxLayout()
        self.bin_layout = gui.QVBoxLayout()
        self.bin_buttons_layout = gui.QHBoxLayout()
        self.import_layout = gui.QVBoxLayout()
        self.import_buttons_layout = gui.QHBoxLayout()

        #--------------------------------------------------------------------------
        # Creating Widget Items
        #--------------------------------------------------------------------------
        self.create_file_path_browser()
        self.scene_mesh_bin()
        self.populateMeshTree()

        #--------------------------------------------------------------------------
        # Populate main layout
        #--------------------------------------------------------------------------
        self.main_layout.addLayout(self.file_path_layout)
        self.main_layout.addWidget(self.meshBin)
        self.setLayout(self.main_layout)

    #--------------------------------------------------------------------------
    # Main layout functions
    #--------------------------------------------------------------------------

    def create_file_path_browser(self):
        self.file_path_label = gui.QLabel("Project MDD Path:")
        self.file_path_lineedit = gui.QLineEdit(self.project_mdd_path)
        self.file_path_browse_button = gui.QPushButton("Browse")
        self.file_path_browse_button = self.createButton(
            "Set Project MDD Path", self.browseSetProjectMDDPath)
        self.file_path_browse_button.setMinimumWidth(100)
        self.file_path_layout.addWidget(self.file_path_label)
        self.file_path_layout.addWidget(self.file_path_lineedit, 1)
        self.file_path_layout.addWidget(self.file_path_browse_button, 0)
        self.file_path_layout.setContentsMargins(8, 10, 8, 0)

    def scene_mesh_bin(self):
        self.mesh_bin_tree = gui.QTreeWidget()
        self.mesh_bin_tree.setColumnCount(4)
        self.mesh_bin_tree.hideColumn(2)
        self.mesh_bin_tree.hideColumn(3)
        self.mesh_bin_tree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mesh_bin_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.mesh_bin_tree.setEditTriggers(
            gui.QAbstractItemView.NoEditTriggers)
        self.mesh_bin_tree.setAlternatingRowColors(True)
        self.mesh_bin_tree.setUniformRowHeights(False)
        self.mesh_bin_tree.setSelectionMode(
            gui.QAbstractItemView.ExtendedSelection)
        self.mesh_bin_tree.setObjectName("mesh_bin_tree")
        self.mesh_bin_tree.header().setVisible(True)
        self.mesh_bin_tree.header().setDefaultSectionSize(400)
        self.mesh_bin_tree.header().setMinimumSectionSize(300)
        self.mesh_bin_tree.header().setSortIndicatorShown(False)
        self.mesh_bin_tree.headerItem().setText(
            0,
            gui.QApplication.translate("MDD Importer Name", "Scene Mesh", None,
                                       gui.QApplication.UnicodeUTF8))
        self.mesh_bin_tree.headerItem().setText(
            1,
            gui.QApplication.translate("MDD Importer Path", "MDD File path",
                                       None, gui.QApplication.UnicodeUTF8))
        self.mesh_bin_tree.headerItem().setText(
            2,
            gui.QApplication.translate("MDD Name", "MDD Name", None,
                                       gui.QApplication.UnicodeUTF8))
        self.mesh_bin_tree.headerItem().setText(
            3,
            gui.QApplication.translate("MDD Importer Updated",
                                       "MDD to update?", None,
                                       gui.QApplication.UnicodeUTF8))

        self.update_selected_button = self.createButton(
            "Update SELECTED", self.updateSelectedMDD)
        self.update_all_button = self.createButton("Update ALL",
                                                   self.updateMDD)

        self.bin_buttons_layout.addWidget(self.update_selected_button)
        self.bin_buttons_layout.addWidget(self.update_all_button)

        self.bin_layout.addWidget(self.mesh_bin_tree)
        self.bin_layout.addLayout(self.bin_buttons_layout)
        self.meshBin.setLayout(self.bin_layout)

    #--------------------------------------------------------------------------
    # Utility functions
    #--------------------------------------------------------------------------

    def browseSetProjectMDDPath(self):
        print "----- In browseSetProjectMDDPath -----"
        directory = gui.QFileDialog.getExistingDirectory(
            self, "Set project MDD path", self.file_path_lineedit.text())
        self.project_mdd_path = directory
        self.file_path_lineedit.setText(directory)
        print "----- Out browseSetProjectMDDPath -----"

    def createToolButton(self, text, member, icon=""):
        print "----- In createToolButton -----"
        if icon:
            button = gui.QToolButton()
            button.setText(text)
            button.setIcon(gui.QIcon(icon))
            button.setMinimumWidth(175)
            button.setMinimumHeight(25)

        else:
            button = gui.QPushButton(text)
        button.clicked.connect(member)
        print "----- Out createToolButton -----"
        return button

    def createButton(self, text, member, icon=""):
        print "----- In createButton -----"
        if icon:
            button = gui.QPushButton(gui.QIcon(icon), text)
        else:
            button = gui.QPushButton(text)
        button.clicked.connect(member)
        print "----- Out createButton -----"
        return button

    def findNewerVersion(self, mddFile):
        print "----- In findNewerVersion -----"
        mddName = mddFile.split('\\')[-1]
        mdd_files, obj_files = self.getFiles(self.project_mdd_path)
        tmp = [mddName]
        for mdd in mdd_files:
            if mddName.split('_v')[0] in mdd:
                tmp.append(mdd)
        tmp2 = sorted(tmp)[-1]
        print "----- Out findNewerVersion -----"
        return tmp2

    def getFiles(self, filepath):
        print "----- In getFiles -----"
        print filepath
        currentDir = QtCore.QDir(filepath)
        fileName = "*"
        files = currentDir.entryList([fileName], QtCore.QDir.Files
                                     | QtCore.QDir.NoSymLinks)
        mdd_files = []
        obj_files = []
        for f in files:
            print "File: " + f
            if ".mdd" in f:
                mdd_files.append(f)
            if ".obj" in f:
                obj_files.append(f)
        print "----- Out getFiles -----"
        return mdd_files, obj_files

    def getMeshDict(self):
        print "----- In getMeshDict Manage Tab -----"
        mddDict = {}
        sceneMeshs = modo.Scene().meshes
        for item in sceneMeshs:
            for deformer in item.deformers:
                if deformer.type == "deformMDD2":
                    deformerList = [
                        deformer.name,
                        lx.eval("item.channel file ? item:{%s}" %
                                (deformer.id))
                    ]
                    mddDict[item.name] = deformerList
        return mddDict
        print "----- Out getMeshDict Manage Tab -----"

    def getPathFromFile(self, filepath):
        tmp = filepath.split('\\')[:-1]
        path = ""
        for i in tmp:
            path = path + i + '\\'
        return path

    def getProjectMDDPath(self):
        print "----- In getProjectMDDPath -----"
        if self.filename:
            print(self.filename)
            pathInfo = self.filename.split("\\")
            index = pathInfo.index("Animation") + 1
            pathInfo = pathInfo[:index]
            # pathInfo = pathInfo[:5]
            shot = self.filename.split("\\")[-2]
            newpath = ""
            for i in pathInfo:
                newpath = newpath + i + "\\"
            mddPath = newpath + "cache\\MDD\\" + shot
            print "----- Out getProjectMDDPath -----"
            return mddPath

    def populateMeshTree(self, refresh=False):
        print "----- In populateMeshTree Manage Tab -----"
        if refresh == True:
            root = self.mesh_bin_tree.invisibleRootItem()
            treeCount = root.childCount()
            for i in range(treeCount):
                self.mesh_bin_tree.clear()
        meshInfo = self.getMeshDict()
        for meshName, mdd in meshInfo.iteritems():
            meshItem = gui.QTreeWidgetItem(self.mesh_bin_tree)
            meshItem.setSizeHint(0, QtCore.QSize(200, 35))
            meshItem.setText(0, meshName)
            latestVersion = self.getPathFromFile(
                mdd[1]) + self.findNewerVersion(mdd[1])
            meshItem.setText(1, latestVersion)
            meshItem.setText(2, mdd[0])
            meshItem.setText(3, "False")
            print("if " + mdd[1] + " != " + latestVersion)
            if mdd[1] != latestVersion:
                meshItem.setForeground(1, gui.QBrush(gui.QColor(200, 0, 0)))
                meshItem.setText(3, "True")
            self.mesh_bin_tree.addTopLevelItem(meshItem)
            self.mesh_bin_tree.sortItems(0, QtCore.Qt.AscendingOrder)
            mddItem = gui.QTreeWidgetItem(meshItem)
            mddItem.setText(0, mdd[0])
        print "----- In populateMeshTree Manage Tab -----"

    def updateMDD(self):
        print "----- In upDateMDD -----"
        root = self.mesh_bin_tree.invisibleRootItem()
        treeCount = root.childCount()
        for i in range(treeCount):
            item = root.child(i)
            print item.text(2)
            print item.text(3)
            if item.text(3) == "True":
                lx.eval('select.deformer "%s" set' % item.text(2))
                lx.eval('item.channel deformMDD2$file "%s"' % item.text(1))
                lx.eval("select.drop item")
        self.populateMeshTree(True)
        print "----- Out upDateMDD -----"

    def updateSelectedMDD(self):
        print "----- In updateSelectedMDD -----"
        selectedItems = self.mesh_bin_tree.selectedItems()
        for item in selectedItems:
            print item.text(2)
            print item.text(3)
            if item.text(3) == "True":
                lx.eval('select.deformer "%s" set' % item.text(2))
                lx.eval('item.channel deformMDD2$file "%s"' % item.text(1))
                lx.eval("select.drop item")
        self.populateMeshTree(True)
        print "----- Out updateSelectedMDD -----"


#############################
class Utl(object):
    def __init__(self, parent=None):
        super(Utl, self).__init__(parent)

    @staticmethod
    def createButton(text, member, icon=""):
        print "----- In createButton -----"
        if icon:
            button = gui.QPushButton(gui.QIcon(icon), text)
        else:
            button = gui.QPushButton(text)
        button.clicked.connect(member)
        print "----- Out createButton -----"
        return button

    @staticmethod
    def createToolButton(text, member, icon=""):
        print "----- In createToolButton -----"
        if icon:
            button = gui.QToolButton()
            button.setText(text)
            button.setIcon(gui.QIcon(icon))
            button.setMinimumWidth(175)
            button.setMinimumHeight(25)
        else:
            button = gui.QPushButton(text)
        button.clicked.connect(member)
        print "----- Out createToolButton -----"
        return button

    @staticmethod
    def createComboBox(text=""):
        comboBox = gui.QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(gui.QSizePolicy.Expanding,
                               gui.QSizePolicy.Preferred)
        return comboBox

    @staticmethod
    def createMDDmddFilesTable():
        mddFilesTable = gui.QTableWidget(0, 3)
        mddFilesTable.setSelectionBehavior(gui.QAbstractItemView.SelectRows)

        mddFilesTable.setHorizontalHeaderLabels(
            ("MDD File Name", "Path", "Size"))
        mddFilesTable.setColumnWidth(0, 150)
        mddFilesTable.setColumnWidth(1, 550)
        mddFilesTable.horizontalHeader().setResizeMode(0,
                                                       gui.QHeaderView.Stretch)
        mddFilesTable.verticalHeader().hide()
        mddFilesTable.setShowGrid(False)
        return mddFilesTable

    @staticmethod
    def createOBJmddFilesTable():
        objFilesTable = gui.QTableWidget(0, 3)
        objFilesTable.setSelectionBehavior(gui.QAbstractItemView.SelectRows)

        objFilesTable.setHorizontalHeaderLabels(
            ("OBJ File Name", "Path", "Size"))
        objFilesTable.setColumnWidth(0, 150)
        objFilesTable.setColumnWidth(1, 550)
        objFilesTable.horizontalHeader().setResizeMode(0,
                                                       gui.QHeaderView.Stretch)
        objFilesTable.verticalHeader().hide()
        objFilesTable.setShowGrid(False)

        return objFilesTable


################################################################################################

lx.bless(MDDTool_Cmd, "vismo.mddTool")
