#!/usr/bin/env python

#------------------------------------------------------------------------------
# VISMO Pass Tool v1.0.0, James Berkheimer
#------------------------------------------------------------------------------

# Standard library imports
import traceback
from functools import partial
import os
import math
import re

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

# Local application imports
import vismo.tools as tools


class PassTool_Cmd(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add('name', lx.symbol.sTYPE_STRING)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)

    def basic_Execute(self, msg, flags):
        try:
            lx.eval("log.masterClear")
            lx.out("I am passTool")
            self.main()

        except Exception as e:
            lx.out(e)
            lx.out("\n", "Failed Launch")
            lx.out(traceback.format_exc())

    def main(self, **options):
        lx._widget = PassData_UI
        lx._widgetOptions = options
        lx.eval('launchWidget')


class PassData_UI(gui.QDialog):
    onClose = QtCore.Signal()

    def __init__(self, parent=None):
        super(PassData_UI, self).__init__(parent)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('VISMO Pass Tool v1.0.0')
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.resize(750, 850)
        self.scene = modo.Scene()
        #--------------------------------------------------------------------------
        # Set layouts
        #--------------------------------------------------------------------------
        self.main_layout = gui.QVBoxLayout()
        self.passes_dropdowns_layout = gui.QHBoxLayout()
        self.itemsChannels_bin = gui.QWidget()
        self.bin_layout = gui.QHBoxLayout()

        #--------------------------------------------------------------------------
        # Creating Widget Items
        #--------------------------------------------------------------------------
        self.passes_dropMenus()
        self.itemChannels_bin()
        self.populatePassGroupBox()
        self.populateRenderPassesBox()
        self.populateItemChannels()

        #--------------------------------------------------------------------------
        # Populate main layout
        #--------------------------------------------------------------------------
        self.main_layout.addLayout(self.passes_dropdowns_layout)
        self.main_layout.addWidget(self.itemsChannels_bin)
        self.setLayout(self.main_layout)

    #--------------------------------------------------------------------------
    # Main layout functions
    #--------------------------------------------------------------------------
    def passes_dropMenus(self):
        self.passGroup_label = gui.QLabel("PassGroups:")
        self.passGroup_dropdown = gui.QComboBox()
        self.rPass_label = gui.QLabel("Render Passes:")
        self.rPass_dropdown = gui.QComboBox()

        self.updateButton = gui.QPushButton("Update")

        self.passGroup_dropdown.activated[str].connect(
            self.populateRenderPassesBox)
        self.rPass_dropdown.activated[str].connect(self.populateItemChannels)

        self.passes_dropdowns_layout.addWidget(self.passGroup_label)
        self.passes_dropdowns_layout.addWidget(self.passGroup_dropdown, 1)
        self.passes_dropdowns_layout.addWidget(self.rPass_label)
        self.passes_dropdowns_layout.addWidget(self.rPass_dropdown, 1)

        self.passes_dropdowns_layout.addWidget(self.updateButton)
        self.updateButton.clicked.connect(self.updateUI)

    def itemChannels_bin(self):
        self.itemChannels_bin_tree = gui.QTreeWidget()
        self.itemChannels_bin_tree.setColumnCount(3)
        self.itemChannels_bin_tree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.itemChannels_bin_tree.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.itemChannels_bin_tree.setEditTriggers(
            gui.QAbstractItemView.NoEditTriggers)
        self.itemChannels_bin_tree.setAlternatingRowColors(True)
        self.itemChannels_bin_tree.setUniformRowHeights(False)
        self.itemChannels_bin_tree.setSelectionMode(
            gui.QAbstractItemView.ExtendedSelection)
        self.itemChannels_bin_tree.setObjectName("itemChannels_bin_tree")
        self.itemChannels_bin_tree.header().setVisible(True)
        self.itemChannels_bin_tree.header().setDefaultSectionSize(225)
        self.itemChannels_bin_tree.header().setMinimumSectionSize(25)
        self.itemChannels_bin_tree.header().setSortIndicatorShown(False)
        self.itemChannels_bin_tree.setColumnWidth(0, 350)
        self.itemChannels_bin_tree.setColumnWidth(1, 150)
        self.itemChannels_bin_tree.setColumnWidth(2, 90)
        ###########
        self.itemChannels_bin_tree.setColumnWidth(3, 50)
        ###########
        self.itemChannels_bin_tree.headerItem().setText(
            0,
            gui.QApplication.translate(
                "", "Items", None, gui.QApplication.UnicodeUTF8))
        self.itemChannels_bin_tree.headerItem().setText(
            1,
            gui.QApplication.translate(
                "", "Channels", None, gui.QApplication.UnicodeUTF8))
        self.itemChannels_bin_tree.headerItem().setText(
            2,
            gui.QApplication.translate(
                "", "Values", None, gui.QApplication.UnicodeUTF8))
        ###########
        self.itemChannels_bin_tree.headerItem().setText(
            3,
            gui.QApplication.translate(
                "", "Value Type", None, gui.QApplication.UnicodeUTF8))
        ###########

        self.bin_layout.addWidget(self.itemChannels_bin_tree)
        self.itemsChannels_bin.setLayout(self.bin_layout)

        self.itemChannels_bin_tree.itemDoubleClicked.connect(
            self.launch_ch_data_UI)

    #--------------------------------------------------------------------------
    # Utility functions
    #--------------------------------------------------------------------------
    def populatePassGroupBox(self):
        passGroups = self.scene.renderPassGroups
        passGroups = sorted(passGroups)
        for pg in passGroups:
            self.passGroup_dropdown.addItem(pg.name)
        self.passGroup_dropdown.setCurrentIndex(0)

    def populateRenderPassesBox(self):
        self.rPass_dropdown.clear()
        passGroup = self.passGroup_dropdown.currentText()
        rPassDict = self.makeRPassDict()
        self.rPass_dropdown.addItem('setup')
        for key, value in rPassDict.iteritems():
            if key.name == passGroup:
                value = sorted(value)
                for rPass in value:
                    self.rPass_dropdown.addItem(rPass)
        activePass = self.getActivePass()
        if activePass == 'setup':
            self.rPass_dropdown.setCurrentIndex(0)
        else:
            self.rPass_dropdown.setCurrentIndex(
                value.index(self.getActivePass()) + 1)

    def makeRPassDict(self):
        passGroups = self.scene.renderPassGroups
        rpassDict = {}
        rPasses = []
        for pg in passGroups:
            passes = pg.passes
            for p in passes:
                rPasses.append(p.name)
            rpassDict[pg] = rPasses
        return rpassDict

    def makeItemDict(self, channels):
        itemDict = {}
        for ch in channels:
            ch_item = ch.item
            itemDict.setdefault(ch_item.type, [])
            itemDict[ch_item.type].append(ch)
        return itemDict

    def populateItemChannels(self):
        lx.out("----- In populateItemChannels -----")
        self.itemChannels_bin_tree.clear()
        rPass = self.rPass_dropdown.currentText()
        lx.eval("layer.active %s type:pass" % (rPass))
        pg = self.passGroup_dropdown.currentText()
        channels = self.getChannels(pg)
        itemDict = self.makeItemDict(channels)
        for key, value in itemDict.iteritems():
            itemType_item = gui.QTreeWidgetItem(
                self.itemChannels_bin_tree)
            itemType_item.setSizeHint(0, QtCore.QSize(200, 35))
            myFont = gui.QFont()
            myFont.setBold(True)
            lx.out("Key:", key)
            itemFlag = key.capitalize() + " [" + str(len(value)) + "]"
            itemType_item.setText(0, itemFlag)
            itemType_item.setFont(0, myFont)
            itemType_item.setExpanded(True)
            self.itemChannels_bin_tree.addTopLevelItem(itemType_item)
            self.itemChannels_bin_tree.sortItems(0, QtCore.Qt.AscendingOrder)
            value_sorted = sorted(value)
            for i in range(len(value_sorted)):
                chanItem = gui.QTreeWidgetItem(itemType_item)
                ch_item = value[i].item
                ch_value = value[i].get(0, rPass)
                ch_type = self.getChannelType(value[i].type)
                print "   ", value[i].name
                chanItem.setText(0, ch_item.name)
                chanItem.setText(1, value[i].name)
                chanLabeslDict = self.getChanOptLablesDict(key)
                chanCmdsDict = self.getChanOptCmdsDict(key)
                index = 0
                style1 = "background-color: rgb(100, 100, 100); color: white;"
                style2 = "background-color: rgb(125, 125, 125); color: white;"
                if tools.listMatch(value[i].name, chanCmdsDict.keys()):
                    lx.out("      ", chanCmdsDict[value[i].name])
                    lx.out(ch_value)
                    index = chanCmdsDict[value[i].name].index(ch_value)
                    lx.out("      ", index)
                    boxList = chanLabeslDict[value[i].name]
                    current = chanLabeslDict[value[i].name][index]
                    tmp_comboBox = gui.QComboBox(
                        self.itemChannels_bin_tree)
                    tmp_comboBox.addItems(boxList)
                    tmp_comboBox.setStyleSheet(style1)
                    tmp_comboBox.setCurrentIndex(boxList.index(current))
                    self.itemChannels_bin_tree.setItemWidget(
                        chanItem, 2, tmp_comboBox)
                    tmp_comboBox.currentIndexChanged.connect(
                        lambda index, tmp_comboBox=tmp_comboBox, ch_item=
                        ch_item, value=value: self.setChannelValue(
                            tmp_comboBox.currentText(), ch_item.name, value[i].
                            name))

                else:
                    tmp_lineEdit = gui.QLineEdit(
                        self.itemChannels_bin_tree)
                    if "rot." in value[i].name:
                        ch_value = math.degrees(ch_value)
                        tmp_lineEdit.setText(str(ch_value))
                        tmp_lineEdit.setStyleSheet(style2)
                        tmp_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
                        self.itemChannels_bin_tree.setItemWidget(
                            chanItem, 2, tmp_lineEdit)
                    else:
                        tmp_lineEdit.setText(str(ch_value))
                        tmp_lineEdit.setStyleSheet(style2)
                        tmp_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
                        self.itemChannels_bin_tree.setItemWidget(
                            chanItem, 2, tmp_lineEdit)

                    tmp_lineEdit.returnPressed.connect(
                        lambda tmp_lineEdit=tmp_lineEdit, ch_item=ch_item,
                        value=value: self.setChannelValue(
                            tmp_lineEdit.text(), ch_item.name, value[i].name))

        ###########
                chanItem.setText(3, ch_type)

        self.itemChannels_bin_tree.setColumnWidth(0, 300)
        self.itemChannels_bin_tree.setColumnWidth(1, 200)
        self.itemChannels_bin_tree.setColumnWidth(2, 150)
        self.itemChannels_bin_tree.setColumnWidth(3, 50)
        lx.out("----- Out populateItemChannels -----")

    def getActivePass(self):
        scene = modo.Scene()
        passGroups = scene.renderPassGroups
        rpName = 'setup'
        if passGroups:
            rpasses = passGroups[0].passes
            for rp in rpasses:
                if rp.active == 1:
                    rpName = rp.name
        return rpName

    def getChannels(self, passGroup):
        passGroups = modo.Scene().renderPassGroups
        channels = []
        for pg in passGroups:
            if pg.name == passGroup:
                channels = pg.groupChannels
        return channels

    def getChanOptCmdsDict(self, item):
        coc = vismo.ChannelOptionCmds()
        attrs = vars(coc)
        classKeys = attrs.keys()
        swap = coc.swap_dot(item, 1)
        methodToCall = {'tmp': '1'}
        for i in sorted(classKeys):
            if re.match(i, swap, re.IGNORECASE):
                methodToCall = getattr(coc, i)
        return methodToCall

    def getChanOptLablesDict(self, item):
        col = vismo.ChannelOptionLabels()
        attrs = vars(col)
        classKeys = attrs.keys()
        lx.out("Item:", item)
        swap = col.swap_dot(item, 1)
        methodToCall = {'tmp': '1'}
        for i in sorted(classKeys):
            if re.match(i, swap, re.IGNORECASE):
                methodToCall = getattr(col, i)
        return methodToCall

    def getChannelType(self, type):
        ch_type = ""
        if type == 0:
            ch_type = "none"
        if type == 1:
            ch_type = "integer"
        if type == 2:
            ch_type = "float"
        if type == 3:
            ch_type = "gradient"
        if type == 4:
            ch_type = "storage"
        if type == 5:
            ch_type = "eval"
        return ch_type

    def closeEvent(self):
        pass

    def updateUI(self):
        self.populateItemChannels()

    def launch_ch_data_UI(self):
        selectedItem = self.itemChannels_bin_tree.currentItem()
        selectedItemText = selectedItem.text(0)
        selectedChannelText = selectedItem.text(1)
        lx.out("Selected Item:", selectedItem.text(0))
        self.ui = ChannelData_UI(selectedItemText, selectedChannelText)
        self.ui.show()

    def setChannelValue(self, value, itemName, channel):
        rPass = self.rPass_dropdown.currentText()
        lx.out("Channel:", channel)
        lx.out("Item:", itemName)
        lx.out("Value:", value)
        lx.out("Render Pass:", rPass)

        lx.eval("layer.active %s type:pass" % (rPass))
        lx.eval("layer.autoAdd on")
        lx.eval("channel.value %s channel:{%s:%s}" %
                (value, itemName, channel))
        lx.eval("edit.apply")
        lx.eval("layer.autoAdd off")


##################################################################################
##################################################################################


class ChannelData_UI(gui.QDialog):
    onClose = QtCore.Signal()

    def __init__(self, itemName, channelName):
        gui.QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Testing')
        self.resize(250, 700)
        self.scene = modo.Scene()
        self.itemName = itemName
        self.channelName = channelName

        self.table = gui.QTableWidget()
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.resizeColumnsToContents()
        self.table.setSortingEnabled(1)

        yellow_html_item = "<font color=yellow size=5> <u> </u> {} </font>".format(
            self.itemName)
        yellow_html_channel = "<font color=yellow size=5> <u> </u> {} </font>".format(
            self.channelName)
        self.channelType_Label = gui.QLabel('Item:')
        self.item_Label = gui.QLabel(yellow_html_item)
        self.channel_Label = gui.QLabel(yellow_html_channel)
        self.main_layout = gui.QVBoxLayout()
        self.label_layout = gui.QVBoxLayout()
        self.label_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.label_layout.addWidget(self.item_Label)
        self.label_layout.addWidget(self.channel_Label)
        self.main_layout.addLayout(self.label_layout)
        self.main_layout.addWidget(self.table)
        self.setmydata()
        self.table.sortByColumn(0, QtCore.Qt.AscendingOrder)

        self.setLayout(self.main_layout)
        width = self.table.frameGeometry().width()
        height = self.table.frameGeometry().height()
        self.table.itemChanged.connect(self.setChannelValue)

    def setmydata(self):
        lx.out("In setmydata")
        item = self.itemName
        passGroups = self.scene.renderPassGroups
        rpasses = passGroups[0].passes
        channels = self.getChannels(passGroups[0], item)
        horHeaders = ['Render Pass']
        vorHeaders = []
        for ch in channels:
            if ch.name == self.channelName:
                horHeaders.append(ch.name)
        for rp in rpasses:
            vorHeaders.append(rp.name)
        self.table.setColumnCount(len(horHeaders))
        self.table.setRowCount(len(rpasses))

        chDict = self.getChannelDict(item, rpasses,
                                     passGroups[0].groupChannels)
        for rCount, rp in enumerate(rpasses):
            for cCount, value in enumerate(chDict[rp.name]):
                passItem = gui.QTableWidgetItem(rp.name)
                if value[0] == self.channelName:
                    if "rot." in self.channelName:
                        degValue = math.degrees(float(value[1]))
                        newitem = gui.QTableWidgetItem(degValue)
                        newitem.setData(QtCore.Qt.EditRole, degValue)
                    else:
                        newitem = gui.QTableWidgetItem(value[1])
                        newitem.setData(QtCore.Qt.EditRole, value[1])
                    lx.out(rCount, cCount)
                    self.table.setItem(rCount, 0, passItem)
                    self.table.setItem(rCount, 1, newitem)
        self.table.setHorizontalHeaderLabels(horHeaders)
        self.table.resizeColumnsToContents()

    def getChannels(self, passGroup, item):
        lx.out("In getChannels")
        passGroups = modo.Scene().renderPassGroups
        channels = []
        for ch in passGroup.groupChannels:
            ch_item = ch.item
            if ch_item.name == item:
                channels.append(ch)
        return channels

    def getChannelDict(self, item, rpasses, channels):
        lx.out("In getChannelDict")
        ch_dict = {}
        for rp in rpasses:
            values_list = []
            for ch in channels:
                ch_list = []
                ch_item = ch.item
                if ch_item.name == item:
                    tmp_tuple = (ch.name, str(ch.get(0, rp.name)))
                    values_list.append(tmp_tuple)
            ch_dict[rp.name] = values_list
        return ch_dict

    def setChannelValue(self):
        lx.out("In setChannelValue")
        item = self.table.currentItem()
        columnNum = item.column()
        rowNum = item.row()
        channel = self.table.horizontalHeaderItem(columnNum).text()
        value = item.text()
        rPass = self.table.item(rowNum, 0).text()
        lx.out("I'm changing the cell!!")
        lx.out("Column #:", columnNum)
        lx.out("Row #:", rowNum)
        lx.out("Channel:", channel)
        lx.out("Value:", value)
        lx.out("Render Pass:", rPass)

        lx.eval("layer.active %s type:pass" % (rPass))
        lx.eval("layer.autoAdd on")
        lx.eval("channel.value %s channel:{%s:%s}" %
                (value, self.itemName, channel))
        lx.eval("edit.apply")
        lx.eval("layer.autoAdd off")

        mainUI = PassData_UI()
        mainUI.populateItemChannels()

    def refreshMainUI(self):
        ui = PassData_UI()


lx.bless(PassTool_Cmd, "vismo.passTool")
