#!/usr/bin/env python

##--------------------------------------##
#              DEV VERSION               #
##--------------------------------------##

# Standard library imports
import os.path
import os, shutil, glob
import time
import re
import sys, string
import subprocess

# Third party imports
import lx, lxu.select
import lxifc
import modo

# Local application imports
from vismo import renderOutputData
rod = renderOutputData.RenderOutputData()

lx.out("Loading Tools")


#####################################################################################################
# Makes
#####################################################################################################
def makeAlphaOuts():
    lx.out("----------------- In makeAlphaOuts -----------------")
    masks = modo.Scene().items('mask')
    for mask in masks:
        alphaCheck = False
        children = lx.evalN('query sceneservice mask.children ? %s' % mask.id)
        for c in children:
            if "renderOutput" in c:
                if lx.eval("item.channel effect ? item:{%s}" %
                           (c)) == "shade.alpha":
                    lx.out('"%s" already has an Alpha output!' % mask.name)
                    alphaCheck = True
        if alphaCheck is False:
            lx.out('Adding Alpha output to "%s"' % mask.name)
            lx.eval("select.drop item")
            lx.eval("select.item %s set" % (mask.id))
            lx.eval("shader.create renderOutput")
            lx.eval("shader.setEffect shade.alpha")
    lx.out("----------------- Out makeAlphaOuts -----------------")


def makeRenderOutputs():
    lx.out("----------------- In makeRenderOutputs -----------------")
    outputTypes = [
        'shade.diffuse', 'shade.luminosity', 'shade.reflection',
        'shade.specular', 'shade.subsurface', 'shade.transparency', 'depth'
    ]
    renderOutputs = modo.Scene().items('renderOutput')
    existingRenderOuts = []
    for out in renderOutputs:
        existingRenderOuts.append(
            lx.eval("item.channel effect ? item:{%s}" % (out.name)))
    for newOut in outputTypes:
        if newOut in existingRenderOuts:
            lx.out(newOut + " already exists \n")
        else:
            lx.eval("select.itemType polyRender")
            lx.eval("shader.create renderOutput")
            lx.eval("shader.setEffect {%s}" % (newOut))
    lx.out("----------------- Out makeRenderOutputs -----------------")


def makeShaders():
    lx.out("----------------- In makeShaders -----------------")
    masks = modo.Scene().items('mask')
    for mask in masks:
        shaderCheck = False
        children = lx.evalN('query sceneservice mask.children ? %s' % mask.id)
        for c in children:
            if "defaultShader" in c:
                if lx.eval("item.channel effect ? item:{%s}" %
                           (c)) == "fullShade":
                    lx.out('"%s" already has an Shader!' % mask.name)
                    shaderCheck = True
        if shaderCheck is False:
            lx.out('Adding Shader to "%s"' % mask.name)
            lx.eval("select.drop item")
            lx.eval("select.item %s set" % (mask.id))
            lx.eval("shader.create defaultShader")
    lx.out("----------------- Out makeShaders -----------------")


#####################################################################################################
# Gets
#####################################################################################################
def getAssignedMaterials(mesh):
    lx.out(
        "----------------- In getAssignedMaterials --------------------------")
    # This gets the selected mesh if any
    if mesh:
        # First collect the materials polygon tags of the mesh in question
        ptags = set()
        for tagType in (lx.symbol.i_POLYTAG_MATERIAL,
                        lx.symbol.i_POLYTAG_PART):
            for index in range(mesh.geometry.PTagCount(tagType)):
                ptag = mesh.geometry.internalMesh.PTagByIndex(tagType, index)
                ptags.add(ptag)

        groupMasks = set()
        for groupMask in modo.Scene().renderItem.childrenByType('mask'):
            tagType = groupMask.channel('ptyp').get()
            if tagType in ('Material', 'Part'):
                assignedTag = groupMask.channel('ptag').get()
                if assignedTag in ptags:
                    groupMasks.add(groupMask)

    lx.out(
        "-------------------------- Leaving getAssignedMaterials --------------------------"
    )
    return groupMasks


def getCameras():
    lx.out("----------------- In getCameras --------------------------")
    lx.eval("select.itemType camera set")
    cameras = modo.Scene().items('camera')
    lx.out("Cameras: ")
    lx.out(cameras)
    lx.out("----------------- Leaving getCameras --------------------------")
    return cameras


def getDirectory():
    lx.out("----------------- In getDirectory --------------------------")
    try:
        directory = os.path.dirname(
            lx.eval("query sceneservice scene.file ? all"))
        lx.out("Directory: " + directory)
    except Exception as e:
        lx.out(e)
        directory = None
    lx.out("----------------- Leaving getDirectory --------------------------")
    return directory


def getEndFrame():
    lx.out("----------------- In getEndFrame -----------------")
    render = modo.Scene().items('polyRender')
    endFrame = lx.eval("item.channel last ? item:{%s}" % (render[0].name))
    lx.out("----------------- Leaving getEndFrame -----------------")
    return endFrame


def getFileName(noExt=1):

    lx.out("----------------- In getFileName -----------------")
    fileName = os.path.basename(lx.eval("query sceneservice scene.file ? all"))
    lx.out("File name: " + fileName)
    if noExt == 1:
        fileName = fileName[:-4]
    lx.out("File name without extension: " + fileName)
    lx.out("----------------- Leaving getFileName -----------------")
    return (fileName)


def getFileInfo():
    lx.out("----------------- In getFileInfo --------------------------")
    lx.out("File Name: " + getFileName())
    fileInfo = getFileName().split("_")
    lx.out("----------------- Leaving getFileInfo --------------------------")
    return fileInfo


def getFileType(layeredEXR=False):
    lx.out("----------------- In getFileType --------------------------")
    renderOutputs = modo.Scene().items('renderOutput')
    for output in renderOutputs:
        if "Final Color" in output.name:
            fileType = lx.eval("item.channel format ? item:{%s}" %
                               (output.name))
    print("Final Color format: " + fileType)
    lx.out("----------------- Leaving getFileType --------------------------")
    return fileType


def getFinalColorPath(layeredEXR=False):
    lx.out("----------------- In getFinalColorPath --------------------------")
    renderOutputs = modo.Scene().items('renderOutput')
    for output in renderOutputs:
        if "Final Color" in output.name:
            filePath = lx.eval("item.channel filename ? item:{%s}" %
                               (output.name))
    print("Final Color format: " + filePath)

    lx.out(
        "----------------- Leaving getFinalColorPath --------------------------"
    )
    return filePath


def getFrameRange():
    lx.out("----------------- In getFrameRange --------------------------")
    frameRange = str(getStartFrame()) + "-" + str(getEndFrame())
    if getStepFrame() > 1:
        frameRange = frameRange + "x" + str(getStepFrame())
    lx.out("frames: " + frameRange)
    lx.out(
        "----------------- Leaving getFrameRange --------------------------")
    return frameRange


def getFrameSize():
    lx.out("----------------- In getFrameSize --------------------------")
    render = modo.Scene().items('polyRender')
    fWidth = lx.eval("item.channel resX ? item:{%s}" % (render[0].name))
    fHeight = lx.eval("item.channel resY ? item:{%s}" % (render[0].name))
    frameSize = str(fWidth) + "x" + str(fHeight)
    lx.out("----------------- Leaving getFrameSize --------------------------")
    return frameSize


def getGroups():
    lx.out("----------------- In getGroups --------------------------")
    groups = []
    for g in modo.Scene().items('group'):
        if g.type == "render":
            groups.append(g)
    lx.out("Groups: ")
    lx.out(groups)
    lx.out("----------------- Leaving getGroups --------------------------")
    return groups


def getLatestFileVersion(inputFile, fileType):
    print "----- In findNewerVersion -----"
    if "\\" in inputFile:
        mddPath = "/".join(inputFile.split('\\')[:-1])
    else:
        mddPath = "/".join(inputFile.split('/')[:-1])
    os.chdir(mddPath)
    mddfiles = glob.glob("*" + fileType)
    mddName = inputFile.split('\\')[-1]
    tmp = [mddName]
    for mdd in mddfiles:
        # print (">>>>>>>>>>>>>>> " + mdd)
        if mddName.split('_v')[0] in mdd:
            tmp.append(mdd)
    tmp2 = sorted(tmp)[-1]
    print "----- Out findNewerVersion -----"
    return mddPath + "/" + tmp2


def getMeshes():
    lx.out("----------------- In getMeshes --------------------------")
    meshes = modo.Scene().items('mesh')
    lx.out("Meshes: ")
    lx.out(meshes)
    lx.out("----------------- Leaving getMeshes --------------------------")
    return meshes


def getModoVersion():
    modoVersion = lx.eval("query platformservice appversion ?")
    return "%sxx" % str(modoVersion)[:-2]    


def getProjectCode():

    lx.out("----------------- In getProjectCode --------------------------")
    fileInfo = getFileInfo()
    show = fileInfo[0]
    lx.out(
        "----------------- Leaving getProjectCode --------------------------")
    return show


def getProjectPhase():
    lx.out("----------------- In getProjectPhase --------------------------")
    path = getDirectory()
    phases = ['\\_DVLP\\', '\\ALPHA\\', '\\BETA\\', '\\FINAL\\', '\\REF\\']
    showPhase = 'ALPHA'
    for phase in phases:
        if phase in path:
            showPhase = phase.strip('\\')
    lx.out(
        "----------------- Leaving getProjectPhase --------------------------")
    return showPhase


def getProjectRoot():
    lx.out("----------------- In getProjectRoot --------------------------")
    try:
        return getDirectory().split('Animation')[0] + "Animation\\"
    except Exception as e:
        lx.out(e)
        return "O:\Clients"
    lx.out("----------------- Out getProjectRoot --------------------------")


def getRenderFileName(versionUp=True):
    lx.out("----------------- In getRenderFileName --------------------------")
    fileInfo = getFileInfo()
    version = fileInfo[-2]
    versionNumber = version[1:]
    if versionUp == True:
        lx.out("Old Version Number: " + versionNumber)
        versionNumber = int(versionNumber) + 1
        lx.out("New Version Number: " + str(versionNumber))
    lx.out("New version number: " + str(versionNumber))
    version = "%03d" % int(versionNumber)
    version = "v" + str(version)
    lx.out("New version: " + version)
    userInitials = getUserInitials()
    renderReady = fileInfo[0] + "_" + fileInfo[1] + "_" + version + "_" + userInitials
    lx.out("Render ready file: " + renderReady)
    lx.out(
        "----------------- Leaving getRenderFileName --------------------------"
    )
    return renderReady


def getDefinedRenderOuts(name):
    lx.out("----------------- In get%sRenderOuts --------------------------" %
           (name))
    renderOuts = []
    renderOutputs = modo.Scene().items('renderOutput')
    for output in renderOutputs:
        currentType = lx.eval("item.channel effect ? item:{%s}" % (output.name))
        if currentType == rod.renderOutputTypes[rod.renderOutputNames.index(
                name)]:
            lx.out(name + "!")
            renderOuts.append(output)
    lx.out(
        "-------------------------- Leaving getDefinedRenderOuts --------------------------"
    )
    return renderOuts


def getAllRenderOutputs():
    lx.out(
        "----------------- In getAllRenderOutputs --------------------------")
    lx.out(
        "-------------------------- Leaving getAllRenderOutputs --------------------------"
    )
    return modo.Scene().items('renderOutput')


def getRenderOutputDir(exr, versionUp):
    lx.out(
        "----------------- In getRenderOutputDir --------------------------")
    directory = getDirectory()
    fileInfo = getFileInfo()
    lx.out("Directory: " + directory)
    version = fileInfo[-2]
    lx.out("File version: " + version)
    userInitials = getUserInitials()
    lx.out("userInitials: " + userInitials)
    versionNumber = version[1:]
    lx.out("versionUp: ", versionUp)
    if versionUp == True:
        versionNumber = int(versionNumber) + 1
    lx.out("New version number: " + str(versionNumber))
    version = "%03d" % int(versionNumber)
    version = "v" + str(version)
    lx.out("New version: " + version)
    projShotVers = fileInfo[0] + "_" + fileInfo[1] + "_" + version
    lx.out("New Project Shot Version: " + projShotVers)
    directory = directory + "\\" + projShotVers

    dirList = directory.split('\\')
    animIndex = dirList.index("Animation") + 1
    if dirList[animIndex] == "scenes":
        directory = directory.replace("scenes", "frames")
    else:
        dirList[animIndex] = "frames"
        phase = dirList[animIndex + 1]
        newPhase = "MODO" + "_" + fileInfo[0] + "_" + phase
        dirList[animIndex + 1] = newPhase
        directory = '\\'.join(dirList)

    if exr == True:
        directory = directory + "\EXR"
    lx.out("Directory path: " + directory)
    lx.out(
        "----------------- Leaving getRenderOutputDir --------------------------"
    )
    return directory


def getRenderOutArgs(layeredEXR=False):
    lx.out("----------------- In getRenderOutArgs --------------------------")
    outputArguments = ""
    args = []
    renderOutputs = modo.Scene().items('renderOutput')
    for output in renderOutputs:
        fileFormat = lx.eval("item.channel format ? item:{%s}" % (output.name))
        filePath = lx.eval("item.channel filename ? item:{%s}" % (output.name))
        args.append(fileFormat)
        args.append(filePath)
    outputArguments = ",".join(
        args
    )  #this turns a list of strings into a single string, separating items with commas
    print "Args: " + outputArguments
    print "OutputArgs Type: " + str(type(outputArguments))
    lx.out(
        "----------------- Leaving getRenderOutArgs --------------------------"
    )
    return outputArguments


def getRenderPasses():
    passes = []
    passGroups = modo.Scene().renderPassGroups
    for pg in passGroups:
        passes = pg.passes
    return passes


def getRenderVersion():
    lx.out("----------------- In getRenderVersion --------------------------")
    fileInfo = getFileInfo()
    version = fileInfo[-2]
    versionNumber = version[1:]
    versionNumber = int(versionNumber) + 1
    lx.out("New version number: " + str(versionNumber))
    version = "%03d" % int(versionNumber)
    version = "v" + str(version)
    lx.out("New version: " + version)
    lx.out(
        "----------------- Leaving getRenderVersion --------------------------"
    )
    return version


def getStartFrame():
    lx.out("----------------- In getStartFrame -----------------")
    render = modo.Scene().items('polyRender')
    startFrame = lx.eval("item.channel first ? item:{%s}" % (render[0].name))
    lx.out("----------------- Leaving getStartFrame -----------------")
    return startFrame


def getStepFrame():
    lx.out("----------------- In getStepFrame -----------------")
    render = modo.Scene().items('polyRender')
    stepFrame = lx.eval("item.channel step ? item:{%s}" % (render[0].name))
    lx.out("----------------- Leaving getStepFrame -----------------")
    return stepFrame


def getTextures():
    lx.out("----------------- In getTextures --------------------------")
    texturesID = []
    texturesName = []
    numTexLayers = lx.eval('query sceneservice textureLayer.N ?')
    for x in range(numTexLayers):
        texLayerType = lx.eval('query sceneservice textureLayer.type ? %s' % x)
        if "val." in texLayerType:
            texturesID.append(
                lx.eval('query sceneservice textureLayer.id ? %s' % x))
            texturesName.append(
                lx.eval('query sceneservice textureLayer.name ? %s' % x))
    lx.out("Textures: ")
    lx.out(texturesName)
    lx.out("----------------- Leaving getTextures --------------------------")
    return texturesName


def getUserInitials():
    lx.out("----------------- In getUserInitials --------------------------")
    fileInfo = getFileInfo()
    userName = fileInfo[-1]
    userInitials = userName[:6].upper()
    lx.out(
        "----------------- Leaving getUserInitials --------------------------")
    return userInitials


####################################################################################################
# Checks
#####################################################################################################


def checkForStereo():
    lx.out("----------------- In checkForStereo -----------------")
    stereoExists = False
    groups = getGroups()
    if groups:
        for group in groups:
            if group.name == "Stereo":
                lx.out("PassGroup already exists!!")
                stereoExists = True
    lx.out("----------------- Leaving checkForStereo -----------------")
    return stereoExists


def checkForDepth():
    lx.out("----------------- In checkForDepth -----------------")
    depthExists = False
    renderOutputs = modo.Scene().items('renderOutput')
    for output in renderOutputs:
        lx.out(" ")
        lx.out("--------------------------------------")
        lx.out(" ")
        lx.out("Render Output: " + output.name)
        if "depth" in lx.eval("item.channel effect ? item:{%s}" %
                              (output.name)):
            lx.out("Output type:")
            lx.out("             Depth!")
            depthExists = True
            lx.out("There is a Depth: " + str(depthExists))
    lx.out("----------------- Leaving checkForDepth -----------------")
    return depthExists


def checkLocalMDDs():
    lx.out("----------------- In checLocalkMDDs -----------------")
    foundIssue = False
    localMDDs = []
    deformers = modo.Scene().items('deformMDD2')
    if deformers == None:
        lx.out("No MDDs in scene")
    else:
        for deformer in deformers:
            print("MDD:  " + deformer.name)
            mddFile = lx.eval("item.channel file ? item:{%s}" %
                              (deformer.name))
            if mddFile == None:
                lx.eval("!!select.deformer {%s} set" % (deformer.name))
                lx.out("Empty MDD!")
                lx.out("DELETING!!" + deformer.name)
                lx.eval("delete")
                lx.eval("!!select.drop item")
            else:
                lx.out(mddFile)
                driveLoc = mddFile[0]
                if driveLoc == "O" or driveLoc == "X":
                    lx.out("Legal file location")
                else:
                    lx.out("ISSUE FOUND --------- " + mddFile)
                    lx.out("Not legal file location")
                    #lx.out("--------------------This file is in the wrong drive--------------------")
                    lx.out("\n")
                    foundIssue = True
                    localMDDs.append(deformer)
    return foundIssue
    lx.out("----------------- Leaving checLocalkMDDs -----------------")


def checkImages():
    lx.out("----------------- In checkImages -----------------")
    foundIssue = False
    lx.out("Checking for local images......")
    clipNum = lx.eval("query sceneservice clip.N ? fg")
    if clipNum:
        for x in xrange(clipNum):
            clipID = lx.eval("query sceneservice clip.id ? {%s}" % (x))
            sourceDir = lx.eval("query layerservice clip.file ? {%s}" % (x))
            lx.out(clipID)
            lx.out(sourceDir)

            if sourceDir:
                driveLoc = sourceDir[0]
                lx.out("Drive letter: " + driveLoc)
                if "\\optimus\Optimus" in sourceDir:
                    lx.out("Legal file location")
                if driveLoc == "O":
                    lx.out("Legal file location")
                else:
                    lx.out("ISSUE FOUND --------- " + sourceDir)
                    lx.out("Not legal file location")
                    lx.out("\n")
                    foundIssue = True
            lx.out(" ")
    else:
        lx.out("____No Images in Scene____")
    return foundIssue
    lx.out("----------------- Leaving checkImages -----------------")


def checkRenderRegions():
    lx.out("----------------- In checkRenderRegions -----------------")
    try:
        renderID = lx.eval(
            'query sceneservice polyRender.id ? 0'
        )  #this gets the ID of the first polyRender item in the scene
        renderRegionToggle = lx.eval(
            'item.channel name:region value:? item:{%s}' % renderID
        )  #this uses the ID as one of the arguments for the item.channel command
        lx.out(renderRegionToggle)
        if renderRegionToggle == True:
            lx.out("Render Region is On")
            # set up the dialog
            lx.eval('dialog.setup yesNo')
            lx.eval('dialog.title {Turn off render regions?}')
            lx.eval('dialog.msg {Do you want to off your render regions?}')
            lx.eval('dialog.result ok')

            # Open the dialog and see which button was pressed
            lx.eval('dialog.open')
            lx.eval("dialog.result ?")
            lx.out("\n")
            lx.out("-------------Turning off render region--------------")
            lx.out("\n")
            lx.eval("!!renderWindow.renderRegionEnable false")
        else:
            lx.out("Render Region is Off")
    except Exception as e:
        lx.out(e)
        pass
    lx.out("----------------- Leaving checkRenderRegions -----------------")


def checkFileName():
    lx.out("----------------- In checkFileName -----------------")
    foundIssue = False
    fileNameIssue = False
    lx.out(0)
    directory = getDirectory()
    lx.out(1)
    saveDir = directory
    directory = directory[3:]
    fileName = getFileName()
    lx.out(2)
    lx.out(fileName)
    underScores = fileName.count("_")
    lx.out("Number of underscores: " + str(underScores))
    if underScores == 3:
        pass
    else:
        lx.out("FOUND --------- " + "Bad File Name")
        lx.out("\n")
        foundIssue = True
    return foundIssue
    lx.out("----------------- Leaving checkFileName -----------------")


def checkForIssues():
    lx.out("----------------- In checkForIssues -----------------")
    foundIssue = False
    foundLocalImage = checkImages()
    foundLocalMDD = checkLocalMDDs()
    foundFileNameIssue = checkFileName()
    checkRenderRegions()
    if True in {foundLocalImage, foundLocalMDD, foundFileNameIssue}:
        lx.out("!!!!!!! Issues were found !!!!!!!")
        if foundLocalImage:
            lx.eval('dialog.setup warning')
            lx.eval('dialog.title {!!ERRORS FOUND!!}')
            lx.eval('dialog.msg {Check for local images}')
            lx.eval('dialog.result ok')
            lx.eval('dialog.open')
        if foundLocalMDD:
            lx.eval('dialog.setup warning')
            lx.eval('dialog.title {!!ERRORS FOUND!!}')
            lx.eval('dialog.msg {Check for local MDDs}')
            lx.eval('dialog.result ok')
            lx.eval('dialog.open')
        if foundFileNameIssue == True:
            lx.eval('dialog.setup warning')
            lx.eval('dialog.title {!!ERRORS FOUND!!}')
            lx.eval('dialog.msg {Check your File Name}')
            lx.eval('dialog.result ok')
            lx.eval('dialog.open')
        lx.out("----------------- Leaving checkForIssues -----------------")
        foundIssue = True
    lx.out(" No Issues were found ")
    lx.out("----------------- Leaving checkForIssues -----------------")
    return foundIssue


####################################################################################################
# Utilities
#####################################################################################################
def cleanName(name):
    lx.out("----------------- In cleanName -----------------")
    cleanName = name.replace(" ", "")
    cleanName = re.sub('\(.*?\)', '', cleanName)
    cleanName = cleanName.replace("_", "")
    lx.out("----------------- Leaving cleanName -----------------")
    return cleanName


def dialog_getDirectory(msg="Select destination directory"):
    userInput = ""
    try:
        lx.eval('dialog.setup dir')
        lx.eval('dialog.title {%s}' % (msg))
        lx.eval('dialog.open')
        userInput = lx.eval("dialog.result ?")
    except Exception as e:
        lx.out(e)
        lx.out("Canceled!")
        exit()
    return userInput


def dialog_getFile():
    userInput = ""
    try:
        lx.eval('dialog.setup fileOpen')
        lx.eval('dialog.title {Select a scene file}')
        lx.eval('dialog.open')
        userInput = lx.eval("dialog.result ?")
    except Exception as e:
        lx.out(e)
        lx.out("Canceled!")
        exit()
    return userInput


def dialog_getText(userDef, msg="Enter Text"):
    userInput = ""
    try:
        lx.out("Getting user text")
        lx.eval("user.defNew user.%s life:{momentary}" % (userDef))
        lx.eval("user.def user.%s dialogname {%s}" % (userDef, msg))
        lx.eval("user.value user.%s" % (userDef))
        userInput = lx.eval("user.value user.%s ?" % (userDef))
    except Exception as e:
        lx.out(e)
        lx.out("!! Failed at get user input !!")
        exit()
    return userInput


def listMatch(oString, oList):
    newList = [item.lower() for item in oList]
    newString = oString.lower()
    if newString in newList:
        return True
    else:
        return False


def log(message, prefix="Debug", hush=False):
    if not hush:
        print("%s : %s " % (prefix, message))


def printChildren(space, parent):
    if parent.childCount() > 0:
        __space = "   "
        __space += space
        for child in parent.children():
            print __space, child.name
            printChildren(__space, child)


def renameChildren(itemtype, suffix, parent):
    if parent.childCount() > 0:
        for child in parent.children():
            if child.type == itemtype:
                if suffix in child.name:
                    pass
                else:
                    newName = child.name + suffix
                    lx.eval("item.name {%s} item:{%s}" % (newName, child.name))
            renameChildren(itemtype, suffix, child)


def send_mail(send_from,
              send_to,
              subject,
              text,
              files=[],
              server="cybertron02.viscira.local"):
    import smtplib
    import os
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEBase import MIMEBase
    from email.MIMEText import MIMEText
    from email.Utils import COMMASPACE, formatdate
    from email import Encoders
    assert type(send_to) == list
    assert type(files) == list
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    print msg.as_string()
    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment filename="%s"' % os.path.basename(f))
        msg.attach(part)
    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def uniqifyList(seq):
    # not order preserving
    set = {}
    map(set.__setitem__, seq, [])
    return set.keys()


####################################################################################################
# Tests
#####################################################################################################


def error_dialog(errMsg):
    lx.eval("dialog.setup error")
    lx.eval("dialog.title {ERROR}")
    lx.eval("dialog.msg {@_[0]}")
    lx.eval("dialog.open")


def testing(a="a"):
    lx.out("I just ran a")
    lx.out("----------------- In testing --------------------------")
    lx.out(a)
    lx.out("I just ran a")


##Clean zombie renderoutputs
# import modo
# renderOutputs = modo.Scene().items('renderOutput')

# for output in renderOutputs:
# 	print (output.name)
# 	if output.name == "Alpha Output (2)":
# 		print ("Found")
		
		
		
# lx.eval("!!select.deformer {%s} set" % ('renderOutput488'))
# lx.eval("delete")