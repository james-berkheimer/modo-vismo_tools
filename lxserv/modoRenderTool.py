#!/usr/bin/env python

#------------------------------------------------------------------------------
# VISMO Render Tool v1.0.0, James Berkheimer
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

# Local application imports
import vismo.render as render
import vismo.setup as setup
import vismo.tools as tools
from vismo import renderOutputData
rod = renderOutputData.RenderOutputData()

# Establishing global icon path
scriptDir = os.path.dirname(os.path.abspath(__file__))
scriptDir = os.path.dirname(scriptDir)
icon_path = scriptDir + "\\icons\\"


class RenderTool_Cmd(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add('name', lx.symbol.sTYPE_STRING)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)

    def basic_Execute(self, msg, flags):
        try:
            lx.eval("log.masterClear")
            lx.out("I am renderTool")
            self.main()

        except:
            lx.out("\n", "Failed Launch")
            lx.out(traceback.format_exc())

    def main(self, **options):
        lx._widget = RenderTool_UI
        lx._widgetOptions = options
        lx.eval('launchWidget')


class RenderTool_UI(gui.QMainWindow):
    onClose = QtCore.Signal()

    def __init__(self, parent=None, **options):
        super(RenderTool_UI, self).__init__(parent)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('VISMO RenderTool v1.1.0')
        self.resize(480, 625)

        print "Clearing Renderout arrays"
        rod.clearData
        print 'options:', options
        scene = modo.Scene()
        filename = scene.filename
        self.render_setup_widget = Render_Setup_Tab(self)
        self.render_management_widget = Render_Management_Tab(self)
        self.render_submit_widget = Render_Submit_Button(self)

        _widget = gui.QWidget()
        _layout = gui.QVBoxLayout(_widget)
        _tabs = gui.QTabWidget()
        _tabs.addTab(self.render_setup_widget, "Render Setup")
        _tabs.addTab(self.render_management_widget, "Render Management")
        _layout.addWidget(_tabs)
        _layout.addWidget(self.render_submit_widget)
        self.setCentralWidget(_widget)


class Render_Setup_Tab(gui.QWidget):
    def __init__(self, parent):
        super(Render_Setup_Tab, self).__init__(parent)
        # we still have access to the TD SDK
        scene = modo.Scene()
        filename = scene.filename

        #--------------------------------------------------------------------------
        # Call the group box functions
        #--------------------------------------------------------------------------
        self.renderSetupTab_TopGroupBox()
        self.renderSetupTab_BottomGroupBox()

        #--------------------------------------------------------------------------
        # Set Main layout
        #--------------------------------------------------------------------------
        topLayout = gui.QHBoxLayout()
        topLayout.addStretch(1)
        mainLayout = gui.QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topGroupBox, 1, 0)
        mainLayout.addWidget(self.bottomGroupBox, 2, 0)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

    #--------------------------------------------------------------------------
    # Creating Group boxes
    #--------------------------------------------------------------------------
    def renderSetupTab_TopGroupBox(self):
        self.topGroupBox = gui.QGroupBox()
        spacer = gui.QLabel("")
        fileType = lx.eval("scene.tag string FEXT ?")
        if fileType:
            yellow_html = "<font color=yellow size=5> <u> </u> {} </font>".format(
                fileType)
        else:
            yellow_html = "<font color=yellow size=5> <u> </u> {} </font>".format(
                "None")
        render_filetype_label = gui.QLabel('File Type:')
        self.render_filetype = gui.QLabel(yellow_html)
        png08_button = Utl.createButton("&PNG 8-Bit",
                                        partial(self.fileType_set, "PNG08"),
                                        icon_path + "png08.png")
        png16_button = Utl.createButton("&PNG 16-Bit",
                                        partial(self.fileType_set, "PNG16"),
                                        icon_path + "png16.png")
        exr16_button = Utl.createButton("&EXR 16-Bit",
                                        partial(self.fileType_set, "EXR16"),
                                        icon_path + "exr16.png")
        exr32_button = Utl.createButton("&EXR 32-Bit",
                                        partial(self.fileType_set, "EXR32"),
                                        icon_path + "exr32.png")
        exrLayered_button = Utl.createButton(
            "&EXR 16-Bit Layered", partial(self.fileType_set, "Layered_EXR"),
            icon_path + "layeredexr16.png")
        output_check = gui.QLabel("Empty outputs: ")
        placeHolder_label = gui.QLabel(" ")
        helpEmail_button = Utl.createButton("", self.helpEmail,
                                            icon_path + "help.png",
                                            QtCore.QSize(50, 50))
        # versionUpScene_button = Utl.createButton("&Version Up Scene", self.versionUp_scene, icon_path + "version_UP.png", QtCore.QSize(30, 30))
        versionUpScene_button = Utl.createButton("&Make Shot Directories",
                                                 self.makeShotDirs,
                                                 icon_path + "Folder.ico",
                                                 QtCore.QSize(30, 30))
        self.output_num = gui.QLabel()
        self.check_empty_renderoutputs()
        spacer = gui.QLabel(" ")

        layout_main = gui.QVBoxLayout()
        layout_filetype = gui.QHBoxLayout()
        layout_outputCheck_Grid = gui.QGridLayout()
        layout_filetype.setAlignment(QtCore.Qt.AlignLeft)
        layout_filetype.addWidget(render_filetype_label)
        layout_filetype.addWidget(self.render_filetype)
        layout_outputCheck_Grid.addWidget(output_check, 1, 0)
        layout_outputCheck_Grid.addWidget(self.output_num, 1, 1)
        layout_outputCheck_Grid.addWidget(helpEmail_button, 1, 2)
        layout_outputCheck_Grid.addWidget(versionUpScene_button, 1, 3)
        layout_filetype_grid = gui.QGridLayout()
        layout_filetype_grid.addWidget(png08_button, 1, 0)
        layout_filetype_grid.addWidget(png16_button, 1, 1)
        layout_filetype_grid.addWidget(exr16_button, 2, 0)
        layout_filetype_grid.addWidget(exr32_button, 2, 1)
        layout_filetype_grid.addWidget(exrLayered_button, 3, 0, 1, 2)
        layout_main.addLayout(layout_filetype)
        layout_main.addLayout(layout_filetype_grid)
        layout_main.addWidget(spacer)
        layout_main.addLayout(layout_outputCheck_Grid)
        layout_main.setAlignment(QtCore.Qt.AlignTop)
        self.topGroupBox.setLayout(layout_main)

    def renderSetupTab_BottomGroupBox(self):
        self.bottomGroupBox = gui.QGroupBox()

        ############################################################
        frameWidth = lx.eval('render.res 0 ?')
        frameHeight = lx.eval('render.res 1 ?')
        frame_width_label = gui.QLabel("Width ")
        self.frame_width_box = gui.QSpinBox()
        self.frame_width_box.setMaximum(99999)
        self.frame_width_box.setValue(frameWidth)
        frame_height_label = gui.QLabel("Height")
        self.frame_height_box = gui.QSpinBox()
        self.frame_height_box.setMaximum(99999)
        self.frame_height_box.setValue(frameHeight)
        self.half_rez_button = gui.QPushButton("&Toggle Half Resolution", self)
        self.half_rez_button.setCheckable(True)
        if lx.eval("scene.tag string HREZ ?") == 'True':
            print("Half Rez is TRUE")
            self.half_rez_button.setText("&Half Resolution ON")
            self.half_rez_button.setStyleSheet(
                "background-color: rgb(240, 140, 2); color: black;")
            self.half_rez_button.setChecked(True)
        else:
            self.half_rez_button.setText("&Half Resolution OFF")
            self.half_rez_button.setStyleSheet(
                "background-color: rgb(100, 100, 100)")
            self.half_rez_button.setChecked(False)
        self.half_rez_button.clicked[bool].connect(self.halfres)
        frameH_layout = gui.QHBoxLayout()
        frameH_layout.setAlignment(QtCore.Qt.AlignLeft)
        frameW_layout = gui.QHBoxLayout()
        frameW_layout.setAlignment(QtCore.Qt.AlignLeft)
        halfRez_layout = gui.QHBoxLayout()
        halfRez_layout.setAlignment(QtCore.Qt.AlignLeft)
        frameW_layout.addWidget(frame_width_label)
        frameW_layout.addWidget(self.frame_width_box)
        frameH_layout.addWidget(frame_height_label)
        frameH_layout.addWidget(self.frame_height_box)
        halfRez_layout.addWidget(self.half_rez_button)
        rez_layout = gui.QVBoxLayout()
        rez_layout.addLayout(frameW_layout)
        rez_layout.addLayout(frameH_layout)
        rez_layout.addLayout(halfRez_layout)
        rez_layout.addStretch(1)
        top_left_group = gui.QGroupBox()
        top_left_group.setLayout(rez_layout)

        ##
        self.clamp_colors_checkbox = gui.QCheckBox("&Toggle Clamp Colors",
                                                   self)
        if lx.eval("scene.tag string CCOL ?") == 'True':
            self.clamp_colors_checkbox.setChecked(True)
        else:
            self.clamp_colors_checkbox.setChecked(False)
        self.clamp_colors_checkbox.stateChanged.connect(
            self.toggleClampColors_checked)

        self.remap_pixel_values_checkbox = gui.QCheckBox(
            "&Toggle Remap Pixel Values", self)
        if lx.eval("scene.tag string RMAP ?") == 'True':
            self.remap_pixel_values_checkbox.setChecked(True)
        else:
            self.remap_pixel_values_checkbox.setChecked(False)
        self.remap_pixel_values_checkbox.stateChanged.connect(
            self.toggleRemapPixelValues_checked)

        toggle_layout = gui.QVBoxLayout()
        toggle_layout.addWidget(self.clamp_colors_checkbox)
        toggle_layout.addWidget(self.remap_pixel_values_checkbox)

        top_right_group = gui.QGroupBox()
        top_right_group.setLayout(toggle_layout)
        ##
        add_alphas_button = Utl.createButton("&Add Alphas", self.makeAlphaOuts,
                                             icon_path + "Alpha.png")
        add_shaders_button = Utl.createButton("&Add Shaders", self.makeShaders,
                                              icon_path + "Shader.png")
        add_renderOutputs_button = Utl.createButton(
            "&Add Render Outputs", self.makeRenderOutputs,
            icon_path + "RenderOut.png")
        rename_shaderTree_button = Utl.createButton(
            "&Shader Tree Naming", self.rename_shaderTree,
            icon_path + "shaderTree.png")
        rename_cleanScene_button = Utl.createButton(
            "&Clean Scene", self.cleanup, icon_path + "trash-empty-icon.png")
        shader_layout = gui.QHBoxLayout()
        shader_layout.addWidget(add_alphas_button)
        shader_layout.addWidget(add_shaders_button)
        shader_layout.addWidget(add_renderOutputs_button)
        organizing_layout = gui.QHBoxLayout()
        organizing_layout.addWidget(rename_shaderTree_button)
        organizing_layout.addWidget(rename_cleanScene_button)
        bottom_center_layout = gui.QVBoxLayout()
        bottom_center_layout.addLayout(shader_layout)
        bottom_center_layout.addLayout(organizing_layout)
        bottom_center_group = gui.QGroupBox()
        bottom_center_group.setLayout(bottom_center_layout)
        ##
        layout_top = gui.QGridLayout()
        layout_top.addWidget(top_left_group, 0, 0)
        layout_top.addWidget(top_right_group, 0, 1)
        layout_bottom = gui.QHBoxLayout()
        layout_bottom.addWidget(bottom_center_group)
        layout = gui.QVBoxLayout()
        layout.addLayout(layout_top)
        layout.addLayout(layout_bottom)

        self.bottomGroupBox.setLayout(layout)

    #--------------------------------------------------------------------------
    # Widget Functions
    #--------------------------------------------------------------------------
    def placeHolder(self, word):
        print("I am holding place")
        print("This is my word: " + word)

    #-------------------------------------------------------------------------------
    # Modo Functions
    #-------------------------------------------------------------------------------
    def check_empty_renderoutputs(self):
        renderOutputs = modo.Scene().items('renderOutput')
        count = 0
        for output in renderOutputs:
            print("Render output:   " + output.name)
            print lx.eval("item.channel filename ? item:{%s}" % (output.name))
            if lx.eval("item.channel filename ? item:{%s}" %
                       (output.name)) == None:
                count += 1

        if count < 1:
            count_html = "<font color=black size=5> <u> </u> {} </font>".format(
                str(count))
        else:
            count_html = "<font color=red size=5> <u> </u> {} </font>".format(
                str(count))
        self.output_num.setText(count_html)

    def cleanup(self):
        lx.out("Hello")
        try:
            self.dialog(
                'Warning',
                'Cleanup image cache, event log, undo history and command history, continue?',
                'yesNo')
            result = lx.eval('dialog.result ?')
            if (result == 'ok'):
                lx.eval('!!history.clear')
                lx.eval('!!cache.purge imageStack')
                lx.eval('!!uiimage.clear')
                lx.eval('!!log.masterClear')
        except Exception as e:
            lx.out(e)
            None

    def dialog(self, title, msg, type):
        try:
            lx.eval('dialog.setup %s' % type)
            lx.eval('dialog.title "%s"' % title)
            lx.eval('dialog.msg "%s"' % msg)
            lx.eval('dialog.result ok')
            lx.eval('dialog.open')
            result = lx.eval('dialog.result ?')
            return result
        except Exception as e:
            lx.out(e)
            result = lx.eval('dialog.result ?')
            return result

    def fileType_set(self, filetype):
        print("***** In fileType_set *****")
        renderOutputs = modo.Scene().items('renderOutput')
        lx.out("Setting up {%s} environment" % (filetype))
        try:
            setup.setAlphaOutName()
            setup.setRenderEnvironment(filetype)
            setup.renderDirSetup(False)
            self.render_filetype.setText(
                "<font color=yellow size=5> <u> </u> {} </font>".format(
                    filetype))
            self.check_empty_renderoutputs()
            lx.eval("scene.tag string FEXT {%s}" % (filetype))
            print("File type set to:  " + filetype)
            print("***** Out fileType_set *****")
        except Exception as e:
            lx.out("\n")
            lx.out(
                "##################################################################################################################################################"
            )
            lx.out("Render Environment Setup Failed")
            lx.out(e)
            lx.out(
                "##################################################################################################################################################"
            )
            lx.out("\n")
            lx.eval("scene.tag string FEXT {%s}" % ("Error"))
            # set up the dialog
            lx.eval('dialog.setup error')
            lx.eval('dialog.title {Filetype set error}')
            lx.eval(
                'dialog.msg {Filetype setting failed. \nPlease send Help! email.}'
            )
            # Open the dialog
            try:
                lx.eval('dialog.open')
                userResponse = lx.eval("dialog.result ?")
            except Exception as e:
                lx.out(e)
                userResponse = lx.eval("dialog.result ?")

    def halfres(self, pressed):
        # Setting passes to none so as to not lock in this change to only one pass
        lx.eval("layer.active {} type:pass")
        try:
            if pressed == True:
                #set a scene tag to store the Resolution state.
                lx.eval("scene.tag string HREZ {True}")
                print "TRUE"
                print lx.eval("scene.tag string HREZ ?")
                self.half_rez_button.setText("&Half Resolution ON")
                self.half_rez_button.setStyleSheet(
                    "background-color: rgb(240, 140, 2); color: black;")

                width = lx.eval('render.res 0 ?')
                height = lx.eval('render.res 1 ?')
                lx.eval('render.res 0 %s' % (width / 2))
                lx.eval('render.res 1 %s' % (height / 2))
                self.frame_width_box.setValue(width / 2)
                self.frame_height_box.setValue(height / 2)

            if pressed == False:
                print "FALSE"
                lx.eval("scene.tag string HREZ {False}")
                print lx.eval("scene.tag string HREZ ?")
                self.half_rez_button.setText("&Half Resolution OFF")
                self.half_rez_button.setStyleSheet(
                    "background-color: rgb(100, 100, 100)")

                width = lx.eval('render.res 0 ?')
                height = lx.eval('render.res 1 ?')
                lx.eval('render.res 0 %s' % (width * 2))
                lx.eval('render.res 1 %s' % (height * 2))
                self.frame_width_box.setValue(width * 2)
                self.frame_height_box.setValue(height * 2)
        except Exception as e:
            lx.out(e)
            print("Failed to set Half Rez")

    def helpEmail(self):
        import os
        import modo
        send_to = ["JBerkheimer@viscira.com"]  # must be a list
        user = os.environ.get("USERNAME")
        send_from = user + "@viscira.com"
        scene = modo.Scene()
        scenepath = scene.filename
        subject = user + " Modo issue"
        text = scenepath
        scenename = scenepath.split('\\')[-1].split('.')[0]
        users_dir = "C:\\Users\\"
        lux_dir = "\\AppData\\Roaming\\Luxology\\debug\\"
        filepath = users_dir + user + lux_dir
        eventlog_file = filepath + scenename + "_log.txt"
        dirCheck = os.path.exists(filepath)
        if not dirCheck:
            os.makedirs(filepath)
        lx.eval('log.masterSave {%s}' % (eventlog_file))
        files = [eventlog_file]

        lx.eval('dialog.setup yesNoCancel')
        lx.eval('dialog.title {Email for help?}')
        lx.eval('dialog.msg {Do you want to send email?}')

        # Open the dialog and see which button was pressed
        try:
            lx.eval('dialog.open')
            userResponse = lx.eval("dialog.result ?")

        except Exception as e:
            lx.out(e)
            userResponse = lx.eval("dialog.result ?")

        if userResponse == 'ok':
            tools.send_mail(send_from, send_to, subject, text, files)

    def makeAlphaOuts(self):
        tools.makeAlphaOuts()
        self.check_empty_renderoutputs()

    def makeRenderOutputs(self):
        tools.makeRenderOutputs()
        self.check_empty_renderoutputs()

    def makeShaders(self):
        tools.makeShaders()
        self.check_empty_renderoutputs()

    def rename_shaderTree(self):
        setup.setAlphaOutName()
        setup.setMaterialName()
        setup.setShaderName()
        setup.setTextureName()

    def toggleClampColors_checked(self):
        # Setting passes to none so as to not lock in this change to only one pass
        lx.eval("layer.active {} type:pass")
        if self.clamp_colors_checkbox.isChecked() == True:
            lx.eval("scene.tag string CCOL {True}")
            lx.out("Turning ON Clamp Colors")

        if self.clamp_colors_checkbox.isChecked() == False:
            lx.eval("scene.tag string CCOL {False}")
            lx.out("Turning OFF Clamp Colors")
        self.toggleClampColor()

    def toggleClampColor(self):
        renderOutputs = modo.Scene().items('renderOutput')
        for output in renderOutputs:
            if lx.eval("scene.tag string CCOL ?") == "True":
                lx.eval("item.channel clamp true item:{%s}" % (output.name))
            if lx.eval("scene.tag string CCOL ?") == 'False':
                lx.eval("item.channel clamp false item:{%s}" % (output.name))

    def toggleRemapPixelValues_checked(self):
        # Setting passes to none so as to not lock in this change to only one pass
        lx.eval("layer.active {} type:pass")
        print "Remap"
        print self.remap_pixel_values_checkbox.isChecked()
        if self.remap_pixel_values_checkbox.isChecked() == True:
            lx.eval("scene.tag string RMAP {True}")
            lx.out("Turning ON Clamp Colors")
        if self.remap_pixel_values_checkbox.isChecked() == False:
            lx.eval("scene.tag string RMAP {False}")
            lx.out("Turning ON Clamp Colors")
        self.toggleRemapPixelValues()

    def toggleRemapPixelValues(self):
        changeList = ["Depth", "motion"]
        renderOutputs = modo.Scene().items('renderOutput')
        for output in renderOutputs:
            roType = lx.eval("item.channel effect ? item:{%s}" % (output.name))
            if roType == 'motion' or roType == 'depth':
                if self.remap_pixel_values_checkbox.isChecked() == True:
                    lx.out("Turning ON %s Remap Pixel Values" % (output.name))
                    lx.eval("item.channel remap true item:{%s}" %
                            (output.name))
                if self.remap_pixel_values_checkbox.isChecked() == False:
                    lx.out("Turning OFF Remap Pixel Values")
                    lx.eval("item.channel remap false item:{%s}" %
                            (output.name))

    def versionUp_scene(self):
        try:
            setup.saveRenderReadyVersion()
            lx.eval('dialog.title {New version saved}')
            lx.eval('dialog.msg {Your scene is now versioned up.}')
            lx.eval('dialog.result ok')
            lx.eval('dialog.open')
        except:
            lx.out("\n")

    def makeShotDirs(self):
        lx.out(
            " --------------------------------- Making directories for new Render Outputs ----------------------------------"
        )
        setup.setBaseRenderDir(False, False)
        setup.renderDirSetup(False)


class Render_Management_Tab(gui.QWidget):
    def __init__(self, parent):
        super(Render_Management_Tab, self).__init__(parent)
        # we still have access to the TD SDK

        #--------------------------------------------------------------------------
        # Call the group box functions
        #--------------------------------------------------------------------------
        self.templateGroupBox()

        #--------------------------------------------------------------------------
        # Set Main layout
        #--------------------------------------------------------------------------
        mainLayout = gui.QGridLayout()
        mainLayout.addWidget(self.tempGroupBox, 1, 0)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

    #--------------------------------------------------------------------------
    # Creating Group boxes
    #--------------------------------------------------------------------------
    def templateGroupBox(self):
        self.tempGroupBox = gui.QGroupBox()

        tmp01_button = Utl.createButton("&Placeholder...1", self.placeHolder)
        tmp02_button = Utl.createButton("&Placeholder...2", self.placeHolder)
        tmp03_button = Utl.createButton("&Placeholder...3", self.placeHolder)
        tmp04_button = Utl.createButton("&Placeholder...4", self.placeHolder)

        group1 = gui.QGroupBox()
        grp1_layout = gui.QHBoxLayout()
        grp1_layout.addWidget(tmp01_button)
        group1.setLayout(grp1_layout)

        group2 = gui.QGroupBox()
        grp2_layout = gui.QHBoxLayout()
        grp2_layout.addWidget(tmp02_button)
        group2.setLayout(grp2_layout)

        group3 = gui.QGroupBox()
        grp3_layout = gui.QHBoxLayout()
        grp3_layout.addWidget(tmp03_button)
        group3.setLayout(grp3_layout)

        group4 = gui.QGroupBox()
        grp4_layout = gui.QHBoxLayout()
        grp4_layout.addWidget(tmp04_button)
        group4.setLayout(grp4_layout)

        layout = gui.QGridLayout()
        layout.addWidget(group1, 0, 0)
        layout.addWidget(group2, 0, 1)
        layout.addWidget(group3, 1, 0)
        layout.addWidget(group4, 1, 1)

        self.tempGroupBox.setLayout(layout)

    #--------------------------------------------------------------------------
    # Widget Functions
    #--------------------------------------------------------------------------
    def placeHolder(self, word):
        print("I am holding place")
        print("This is my word: " + word)


class Render_Submit_Button(gui.QWidget):
    def __init__(self, parent):
        super(Render_Submit_Button, self).__init__(parent)
        # we still have access to the TD SDK

        #--------------------------------------------------------------------------
        # Create Submit Layout Widgets
        #--------------------------------------------------------------------------
        submitRender_button = Utl.createButton("&Submit Render",
                                               self.submitRender,
                                               icon_path + "images.png",
                                               QtCore.QSize(50, 50))
        submitRender_button.setFixedHeight(50)

        #--------------------------------------------------------------------------
        # Set Main layout
        #--------------------------------------------------------------------------
        mainButtonLayout = gui.QVBoxLayout()
        mainButtonLayout.addWidget(submitRender_button, 1)
        self.setLayout(mainButtonLayout)

    #-------------------------------------------------------------------------------
    # Submit Render
    #-------------------------------------------------------------------------------
    def submitRender(self):
        ################## Run sanity checks #######################
        if tools.checkForIssues() == False:
            renderType = lx.eval("scene.tag string FEXT ?")
            # set up the dialog
            lx.eval('dialog.setup yesNoCancel')
            lx.eval('dialog.title {Run Render Setup?}')
            lx.eval('dialog.msg {Do you want to run the render setup script?}')

            # Open the dialog and see which button was pressed
            try:
                lx.eval('dialog.open')
                userResponse = lx.eval("dialog.result ?")

            except Exception as e:
                lx.out(e)
                userResponse = lx.eval("dialog.result ?")

            # lx.out(userResponse)
            Utl.createDirs(userResponse, renderType)


class Utl(object):
    def __init__(self, parent=None):
        super(Utl, self).__init__(parent)

    #--------------------------------------------------------------------------
    # Creating GUI Functions
    #--------------------------------------------------------------------------

    @staticmethod
    def sanityCheck():
        lx.out("----------------- In sanityCheck --------------------------")
        import os
        renderOutputs = tools.getAllRenderOutputs()
        renderPasses = tools.getRenderPasses()
        overloadedString = False
        badFilePath = False
        missingFilePath = False
        shot = os.path.basename(
            lx.eval("query sceneservice scene.file ? all")).split('_')[:-1]
        shot = "_".join(shot)
        for p in renderPasses:
            for output in renderOutputs:
                filePath = output.channel('filename').get()
                fullFilePath = filePath + p.name + "_0001.png"
                if len(fullFilePath) > 260:
                    lx.out("ERROR: File path over the character limit")
                    lx.out("ERROR: " + fullFilePath)
                    lx.out("ERROR: " + str(len(fullFilePath)))
                    overloadedString = True
                if filePath:
                    # lx.out (filePath.split('\\')[-4], "!=", shot)
                    lx.out("if " + filePath.split('\\')[-4] + " != " + shot)
                    if filePath.split('\\')[-4] != shot:
                        lx.out("ERROR: Bad file path.")
                        lx.out("ERROR: " + filePath)
                        badFilePath = True
                else:
                    lx.out("ERROR: Empty output")
                    lx.out("ERROR: " + p.name)
                    missingFilePath = True
        lx.out("badFilePath: " + str(badFilePath))
        lx.out("missingFilePath: " + str(missingFilePath))
        lx.out("overloadedString: " + str(overloadedString))
        lx.out("----------------- Out sanityCheck --------------------------")
        return badFilePath, missingFilePath, overloadedString
        # return match, notmissing

    @staticmethod
    def createButton(text,
                     command,
                     icon="",
                     iconSize=QtCore.QSize(24, 24),
                     isCheckable=False):
        button = gui.QPushButton(text)
        if icon:
            button.setIcon(QtGui.QIcon(icon))
            button.setIconSize(iconSize)
        if isCheckable:
            button.setCheckable()
        button.clicked.connect(command)
        return button

    @staticmethod
    def createDirs(userResponse, renderType):
        if userResponse == 'ok':
            lx.out("Render Type: " + renderType)
            if renderType != "EXRLAYERED":
                setup.setBaseRenderDir(False)
                setup.renderDirSetup(True)
                setup.saveRenderReadyVersion()
                # Checking for potential issues with the setup
                badFilePath, missingFilePath, overloadedString = Utl.sanityCheck(
                )
                if badFilePath or missingFilePath or overloadedString:
                    lx.eval('dialog.setup warning')
                    lx.eval('dialog.title {!!Issues Found!!}')
                    lx.eval(
                        'dialog.msg {Please check the Event Log for more info.}'
                    )
                    lx.eval('dialog.result ok')
                    lx.eval('dialog.open')
                else:
                    lx.eval('dialog.title {Render Setup Complete}')
                    lx.eval(
                        'dialog.msg {Your render directories are now created\nA new scene file has been revisioned up and saved\nPlease check your directories before submiting to Deadline.}'
                    )
                    lx.eval('dialog.result ok')
                    lx.eval('dialog.open')
                    render.launchDeadline("", "", renderType)

            else:
                setup.setBaseRenderDir(True, True, False)
                setup.saveRenderReadyVersion()
                # Checking for potential issues with the setup
                badFilePath, missingFilePath, overloadedString = Utl.sanityCheck(
                )
                if badFilePath or missingFilePath or overloadedString:
                    lx.eval('dialog.setup warning')
                    lx.eval('dialog.title {!!Issues Found!!}')
                    lx.eval(
                        'dialog.msg {Please check the Event Log for more info.}'
                    )
                    lx.eval('dialog.result ok')
                    lx.eval('dialog.open')
                else:
                    lx.eval('dialog.title {Render Setup Complete}')
                    lx.eval(
                        'dialog.msg {Your render directories are now created\nA new scene file has been revisioned up and saved\nPlease check your directories before submiting to Deadline.}'
                    )
                    lx.eval('dialog.result ok')
                    lx.eval('dialog.open')
                    render.launchDeadline(tools.getRenderOutputDir(),
                                          tools.getRenderFileName())

        if userResponse == 'no':
            lx.out("No: Not running render setup")
            lx.out(
                "##################################################################################################################################################"
            )
            lx.out(
                "##################################################################################################################################################"
            )
            lx.out("\n")

            if renderType != "EXRLAYERED":
                # Checking for potential issues with the setup
                badFilePath, missingFilePath, overloadedString = Utl.sanityCheck(
                )
                if badFilePath or missingFilePath or overloadedString:
                    lx.eval('dialog.setup warning')
                    lx.eval('dialog.title {!!Issues Found!!}')
                    lx.eval(
                        'dialog.msg {Please check the Event Log for more info.}'
                    )
                    lx.eval('dialog.result ok')
                    lx.eval('dialog.open')
                else:
                    render.launchDeadline("", "", renderType)

            else:
                # Checking for potential issues with the setup
                badFilePath, missingFilePath, overloadedString = Utl.sanityCheck(
                )
                if badFilePath or missingFilePath or overloadedString:
                    lx.eval('dialog.setup warning')
                    lx.eval('dialog.title {!!Issues Found!!}')
                    lx.eval(
                        'dialog.msg {Please check the Event Log for more info.}'
                    )
                    lx.eval('dialog.result ok')
                    lx.eval('dialog.open')
                else:
                    render.launchDeadline(tools.getRenderOutputDir(False),
                                          tools.getRenderFileName(False))
        else:
            pass


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

lx.bless(RenderTool_Cmd, "vismo.renderTool")
