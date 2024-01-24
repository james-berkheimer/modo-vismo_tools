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
import lx
import lxu.select
import modo

# Local application imports
import vismo.tools as tools

lx.out("Loading Render")

alphaOuts = []
userName = ""
userInitials = ""
foundIssue = False
localMDDs = []
localImages = []
        
####################################################################################################
# Run Renders
#####################################################################################################

def launchDeadline(outPath = "", fileName = "", fileFormat = "Layered OpenEXR 16-bit"):
    lx.out("********************************** In launchDeadline **********************************")
    lx.out("***************************************************************************************")
    lx.out("***************************************************************************************")
    sceneFileFull = lx.eval ("query sceneservice scene.file ? all")
    lx.out( "scene: " + sceneFileFull )
    if sceneFileFull == "":
            
            # If scene filename is empty, tell user that they must save the scene file.
            errmsg = "Scene must be saved once before it can be submitted to Deadline"
            error_dialog(errMsg)
            sys.extit()
            
    deadlinebin = os.environ['DEADLINE_PATH'].split(os.pathsep)
    deadlinebin = deadlinebin[0]
    deadlinecommand = deadlinebin +  "\\" + "deadlinecommand.exe"
    deadlinecommandbg = deadlinebin +  "\\" + "deadlinecommandbg.exe"
    
    lx.out(deadlinebin)
    lx.out(deadlinecommand)
    lx.out(deadlinecommandbg)
    
    # Change directory to avoid dependency issues.
    os.chdir(deadlinebin)
    
    # Call DeadlineCommand to launch the monitor script file.
    deadlinecmd = [deadlinecommand, '-getrepositoryroot']
    p = subprocess.Popen(deadlinecmd, stdout=subprocess.PIPE)
    root = p.stdout.read()
    root = root.rstrip()
    lx.out("Root: " + root)
    script = root + "\custom\scripts\Submission\Modo\VISMO_ModoSubmission_D10.py"  
    lx.out("Script: " + script)
    
    fileTypeBox = tools.getFileType()
    frameRange = tools.getFrameRange()
    modoVersion = tools.getModoVersion()
    if modoVersion == '902':
        modoVersion = "9xx"
    sceneVersion = tools.getRenderVersion()
    
    projectPath = sceneFileFull.split("Animation")[0] + "Animation"
    
    projectCode = tools.getProjectCode()
    projectPhase = tools.getProjectPhase()
    frameSize = tools.getFrameSize()
    
    #########################################################
    lx.out("------------ Dealing With PassGroups ---------------")
    passGroupNames = []
    passNames = []
    try:
        for pg in modo.Scene().renderPassGroups:
            if pg.type == "render":
                lx.out("Pass Group: %s" % pg.name)
                passGroupNames.append(pg.name)
                for p in pg.passes:
                    lx.out("Pass: %s" % p.name)
                    passNames.append(p.name)
    except:
        lx.out("Failed to get groups, using backup method")
        lx.eval("select.itemType group set")
        passGroups = lx.eval("query sceneservice selection ? group")
        lx.out ("passGroups: %s" % passGroups)
        lx.out ("passGroups Type: %s" % type(passGroups))
        if passGroups is not None:     
            lx.out("1")       
            if type(passGroups) == str:    
                lx.out("Checking for existing passGroups")
                lx.eval("select.type item")
                lx.eval("select.drop item")
                lx.eval("select.item {%s} set" %(passGroups))
                name = lx.eval("item.name ?")
                passGroupNames.append(name)
                lx.out(passGroups.name)
                for p in passGroups.passes:
                    lx.out(p.name)
                    passNames.append(p.name)
                            
            else:
                lx.out("2")
                for pg in passGroups:
                    lx.eval("select.type item")
                    lx.eval("select.drop item")
                    lx.eval("select.item {%s} set" %(pg))
                    name = lx.eval("item.name ?")
                    passGroupNames.append(name)
                    lx.out(pg.name)
                    for p in pg.passes:
                        lx.out(p.name)
                        passNames.append(p.name)
    #########################################################
    passGroupNames.insert(0,"")
    if passNames is None:
        passNames.insert(0,"")
    
    print "PassGroupNames: "
    print passGroupNames
    
    # This turns a list of strings into a single string, separating items with commas        
    passGroupString = ",".join(passGroupNames) 
    print ("PassGroupString: %s" % passGroupString)

    
    passNameString = ",".join(passNames)
    print ("passNameString: %s" % passNameString)
    
    outputArguments = []
    outputArgumentsString = ""
    if fileFormat == "Layered OpenEXR 16-bit":
        print "Layered EXR"
        outputPath = outPath
    else:
        outputPath = tools.getFinalColorPath()
        outputFormat = tools.getFileType()
        print "This is the output path for Deadline: " + outputPath
        outputArguments.append(outputPath)
        outputArguments.append(outputFormat)
        outputArgumentsString = ",".join(outputArguments)
    
   
    if outPath != "":
        fileTypeBox = "Layered EXR"
    else:
        fileTypeBox = tools.getFileType()
        
    fileTypeBox = fileTypeBox.upper()
    
    #print "---------------------------------------------------------------------------------------------------------------------------------"
    #print passGroupString
    #print outputArgumentsString 
    #print "---------------------------------------------------------------------------------------------------------------------------------"
    
    print "================ TESTING ================"
    print "Script: " + script
    print "sceneFileFull: " + sceneFileFull
    print "frameRange: " + frameRange
    print "modoVersion: " + str(modoVersion)
    print "projectCode: " + projectCode
    print "projectPhase: " + projectPhase
    print "frameSize: " + frameSize
    print "fileTypeBox: " + fileTypeBox
    print "passGroupString: " + passGroupString
    print "outputArgumentsString: " + outputArgumentsString
    print "sceneVersion: " + sceneVersion
    print "projectPath:  "  + projectPath
    
    print "============== RUNNING ================="
    if script:
        if outPath != "":
            lx.out("Rendering Layered EXR")
            fileName = fileName + "_"
            # launchDeadline = [deadlinecommandbg, '-executescript', script, sceneFileFull, frameRange, outPath, fileName, fileFormat, modoVersion, projectCode, projectPhase, frameSize, fileTypeBox, passGroupString, sceneVersion, projectPath]
        else:
            lx.out("Not rendering Layered EXR")
            launchDeadline = [deadlinecommandbg, '-executescript', 
                              script, sceneFileFull, frameRange, modoVersion, 
                              projectCode, projectPhase, frameSize, fileTypeBox, 
                              passGroupString, outputArgumentsString, sceneVersion, 
                              passNameString, projectPath]
            # launchDeadline = [deadlinecommandbg, '-executescript', script, sceneFileFull, frameRange, modoVersion, projectCode, projectPhase, frameSize, fileTypeBox, passGroupString, outputArgumentsString, sceneVersion, projectPath, passNameString]

            
        print launchDeadline
        process = subprocess.Popen(launchDeadline, stdout=subprocess.PIPE)
    
    else:
        scripterrmsg = "The ModoSubmission.py script could not be found in the Deadline Repository. Please make sure that the Deadline Client has been installed on this machine,\nthat the Deadline Client bin folder is set in the DEADLINE_PATH environment variable, and that the Deadline Client has been configured to point to a valid Repository."
        error_dialog( scripterrmsg )
        
    lx.out("********************************** Leaving launchDeadline **********************************")


def error_dialog(errMsg):
        lx.eval("dialog.setup error")
        lx.eval("dialog.title {ERROR}")
        lx.eval("dialog.msg {@_[0]}")
        lx.eval("dialog.open")