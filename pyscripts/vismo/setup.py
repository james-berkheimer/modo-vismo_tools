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
from vismo import renderOutputData
rod = renderOutputData.RenderOutputData()

lx.out("Loading Setup")        
####################################################################################################
# Sets
#####################################################################################################    

def setRenderEnvironment(fileType):
    
    lx.out("_____________________ In setRenderEnvironment _____________________")
    lx.eval ("item.channel outPat {[<pass>_][<LR>_]<FFFF>} item:{%s}" % ("Render")) 
    lx.out("Getting Render Outs")
    renderOutputs = modo.Scene().items('renderOutput')
    lx.out("Got Render Outs")
    if fileType == "PNG08":
        lx.out("Filetype is PNG08")
        for output in renderOutputs:
            currentType = lx.eval("item.channel effect ? item:{%s}" % (output.name)) 
            if currentType == "depth":
                lx.eval ("item.channel clamp false item:{%s}" % (output.name))
                lx.out("Turning off Depth Clamp Colors")
            else:
                lx.eval ("item.channel format PNG item:{%s}" % (output.name))
                lx.eval ("item.channel clamp true item:{%s}" % (output.name))
        
    if fileType == "PNG16":
        lx.out("Filetype is PNG16")
        for output in renderOutputs:
            currentType = lx.eval("item.channel effect ? item:{%s}" % (output.name)) 
            if currentType == "depth":
                lx.eval ("item.channel clamp false item:{%s}" % (output.name))
                lx.out("Turning off Depth Clamp Colors")
            else:
                lx.eval ("item.channel format PNG16 item:{%s}" % (output.name))
                lx.eval ("item.channel clamp true item:{%s}" % (output.name))
                
    if fileType == "EXR16":
        lx.out("Filetype is EXR16")
        for output in renderOutputs:                
            lx.eval ("item.channel format openexr item:{%s}" % (output.name))
            lx.eval ("item.channel clamp false item:{%s}" % (output.name))
            lx.eval ("item.channel unpremul false item:{%s}" % (output.name))
            
    if fileType == "EXR32":
        lx.out("Filetype is EXR32")
        for output in renderOutputs:                
            lx.eval ("item.channel format openexr_32 item:{%s}" % (output.name))
            lx.eval ("item.channel clamp false item:{%s}" % (output.name))
            lx.eval ("item.channel unpremul false item:{%s}" % (output.name))
            
    if fileType == "Layered_EXR":
        lx.out("Filetype is Layered_EXR")
        for output in renderOutputs:                
            lx.eval ("item.channel format openexr item:{%s}" % (output.name))
            lx.eval ("item.channel clamp false item:{%s}" % (output.name))
            lx.eval ("item.channel unpremul false item:{%s}" % (output.name))
    
    #-----------------------------------------------------------------------------
    # set all Alpha outputs to PNGs
    #-----------------------------------------------------------------------------
    print ("set all Alpha outputs to PNGs")
    renderOutputs = modo.Scene().items('renderOutput')
    for output in renderOutputs:
        if lx.eval("item.channel effect ? item:{%s}" % (output.name)) == "shade.alpha":
            lx.eval ("item.channel format PNG item:{%s}" % (output.name))
            
    #-----------------------------------------------------------------------------
    # set all Depth and Motion Vector outputs to EXR 32 and turn off antialias
    #-----------------------------------------------------------------------------
    print ("set defined outputs to EXR 32")
    exr32Outs = ["Depth", "Motion Vector", "UV Coordinates", "Shading Normal"]
    for out in exr32Outs:
        exrRenderOuts(out)
        
    lx.out("_____________________ Leaving setRenderEnvironment _____________________")
    
def exrRenderOuts(name):
    outputs = tools.getDefinedRenderOuts(name)
    lx.out("Number of %s outputs: " % (name) + str(len(outputs)))
    for output in outputs:
        lx.eval ("item.channel format openexr_32 item:{%s}" % (output.name))
        lx.eval ("item.channel antialias false item:{%s}" % (output.name))
        lx.eval ("item.channel clamp false item:{%s}" % (output.name))
        lx.eval ("item.channel saveProcessed false item:{%s}" % (output.name))
    
#----------------------------------------------------------------------------------------------  

def saveRenderReadyVersion(versionUp = True):
    
    lx.out("_____________________ In saveRenderReadyVersion _____________________")
    directory = tools.getDirectory()
    if versionUp == False:
        renderFileName = tools.getRenderFileName(False)
    else:
        renderFileName = tools.getRenderFileName()
    fileExtension = ".lxo"
    renderReady = renderFileName + fileExtension
    saveFile = directory + "\\" + renderReady
            
    lx.out("Saving Render Ready file: " + saveFile)
    lx.eval("scene.saveAs {%s}" % (saveFile))        
    lx.eval('dialog.setup info')
    
    lx.out("_____________________ Leaving saveRenderReadyVersion _____________________")
    
#----------------------------------------------------------------------------------------------          
    
def setAlphaOutName():        
    lx.out("_____________________ In setAlphaOutName _____________________")
    # alphaOuts = tools.getAlphaOuts()
    alphaOuts = tools.getDefinedRenderOuts("Alpha")
    for alpha in alphaOuts:
        alphaName = alpha.name
        mask = alpha.parent
        maskName = mask.name
        print ("Alpha parent:  " + maskName)
        print "--------------------------+++++++++++++++++++++++++++++++++++++++++++-----------------------"
        if maskName != "Render":
            print "----------------------------------------------------------------------------------------"
            cleanMaskName = tools.cleanName(maskName)
            newAlphaName = cleanMaskName + "_Alpha"
            lx.eval ("item.name {%s} item:{%s}" % (newAlphaName, alpha.name))
    lx.out("_____________________ Leaving setAlphaOutName _____________________")
    
#----------------------------------------------------------------------------------------------  
    
def setMaterialName():        
    lx.out("_____________________ In setMaterialName _____________________")
    masks = modo.Scene().items('mask')
    for mask in masks:            
        cleanMaskName = tools.cleanName(mask.name)
        for child in mask.children():
            if child.type == "advancedMaterial":                    
                newMaterialName = cleanMaskName + "_mtrl"
                print newMaterialName
                lx.eval ("item.name {%s} item:{%s}" % (newMaterialName, child.name))               
    lx.out("_____________________ Leaving setMaterialName _____________________")
           
#----------------------------------------------------------------------------------------------

def setShaderName():        
    lx.out("_____________________ In setShaderName _____________________")
    masks = modo.Scene().items('mask')
    for mask in masks:
        cleanMaskName = tools.cleanName(mask.name)
        for child in mask.children():
            if child.type == "defaultShader":
                newShaderName = cleanMaskName + "_shdr"
                lx.eval ("item.name {%s} item:{%s}" % (newShaderName, child.name))   
    lx.out("_____________________ Leaving setShaderName _____________________")
           
#----------------------------------------------------------------------------------------------

def setTextureName():        
    lx.out("_____________________ In setTextureName _____________________")
    masks = modo.Scene().items('mask')
    processList = ["constant", "gradient", "occlusion", "process", "tensionTexture", "variationTexture", "vmapTexture"]
    for mask in masks:
        cleanMaskName = tools.cleanName(mask.name)
        for child in mask.children():
            if any(x in child.type for x in processList):
                if child.type == "vmapTexture":
                    cleanTextureName = tools.cleanName("weightMapTexture")
                else:
                    cleanTextureName = tools.cleanName(child.type)
                newTextureName = cleanMaskName + "-" + cleanTextureName + "_prcs"
                print newTextureName
                lx.eval ("item.name {%s} item:{%s}" % (newTextureName, child.name))
            if any(x in child.type for x in [".val", ".RJJ"]):
                cleanTextureName = tools.cleanName(child.name)
                newTextureName = cleanMaskName + "-" + cleanTextureName + "_txtr"
                print newTextureName
                if cleanMaskName not in child.name:
                    lx.eval ("item.name {%s} item:{%s}" % (newTextureName, child.name))
            if "imageMap" in child.type:
                cleanTextureName = tools.cleanName(child.name)
                newTextureName = cleanMaskName + "-" + cleanTextureName + "_img"
                print newTextureName
                if cleanMaskName not in child.name:
                    lx.eval ("item.name {%s} item:{%s}" % (newTextureName, child.name))
    lx.out("_____________________ Leaving setTextureName _____________________")
           
#---------------------------------------------------------------------------------------------- 
    
def dirMaker(par, num):
    test = par
    dirCheck = os.path.exists(test) 
    lx.out("Dir Check %s" % (num))
    lx.out(dirCheck)
    if not dirCheck:
        lx.out("Creating: " + test)            
        os.makedirs(test)

def setBaseRenderDir(exr = True, versionUp = True, testRun = False):        
    #---------------------------------------------------------------------------------------------
    # This sets the base render directory.  Another method will set each Render Output Directory.
    #---------------------------------------------------------------------------------------------        
    lx.out("_____________________ In setBaseRenderDir _____________________")
    if versionUp == False:
        if exr == True:
            renderDir = tools.getRenderOutputDir(True, False)
        else:
            renderDir = tools.getRenderOutputDir(False, False)
    else:
        if exr == True:
            renderDir = tools.getRenderOutputDir(True, True)
        else:
            renderDir = tools.getRenderOutputDir(False, True)
    
    dirList = []
    dirList.append(renderDir)
    par1 = os.path.dirname(renderDir)
    dirList.append(os.path.dirname(par1))
    lx.out("par1 " + par1)
    par2 = os.path.dirname(par1)
    dirList.append(os.path.dirname(par2))
    lx.out("par2 " + par2)
    par3 = os.path.dirname(par2)
    dirList.append(os.path.dirname(par3))
    lx.out("par3 " + par3)
    par4 = os.path.dirname(par3)
    dirList.append(os.path.dirname(par4))
    lx.out("par4 " + par4)
    par5 = os.path.dirname(par4)
    dirList.append(os.path.dirname(par5))
    lx.out("par5 " + par5)
    par6 = os.path.dirname(par5)
    dirList.append(os.path.dirname(par6))
    lx.out("par6 " + par6)
    par7 = os.path.dirname(par6)
    dirList.append(os.path.dirname(par7))
    lx.out("par7 " + par7)
    par8 = os.path.dirname(par7)
    dirList.append(os.path.dirname(par8))
    lx.out("par8 " + par8)
    
    for d in range(len(dirList)):
        dirMaker(dirList[d], d)              
    lx.out("_____________________ Leaving setBaseRenderDir _____________________")                
            
#----------------------------------------------------------------------------------------------

def renderDirSetup(versionUp):        
    lx.out("_____________________ In renderDirSetup _____________________")
    renderOutputs = modo.Scene().items('renderOutput')
    lx.out("Outs: ")
    lx.out(renderOutputs)
    currentDir = ""
    currentType = ""
    lx.out(" ")
    directory = tools.getRenderOutputDir(False, versionUp)
    lx.out("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    lx.out("Directory: " + directory)
    #### Make the root directories ####
    lx.out(" ")
    lx.out("###################################")
    lx.out("#### Make the root directories ####")
    lx.out("###################################")
    lx.out(" ")
    for output in renderOutputs:
        lx.out(" ")
        lx.out("|||||||||||||||||||||||||||||||||||||||| IN OUTPUTS LOOP ||||||||||||||||||||||||||||||||||||||||")
        lx.out(" ")
        currentType = lx.eval("item.channel effect ? item:{%s}" % (output.name)) 
        lx.out("Renderout name: " + output.name)
        lx.out("Renderout type: " + currentType)              
        currentDir = makeRenderOutPath(output, currentType, directory)   
        lx.out("CurrentDir: " + currentDir)
        dirTest = currentDir
        dirCheck = os.path.exists(dirTest)
        lx.out("Dir Check: " + str(dirCheck))
        if not dirCheck:
            lx.out("Making Directory: " + currentDir)
            os.makedirs(currentDir)
        # lx.eval ("item.channel filename {%s} item:{%s}" % (currentDir, output.name))
    lx.out("<<<<<<<< On to makeRenderOutputDir >>>>>>>>")        
    #### Make the Render Output Directories ####
    lx.out(" ")
    lx.out("############################################")
    lx.out("#### Make the Render Output Directories ####")
    lx.out("############################################")
    lx.out(" ")
    size = len(rod.renderOutputTypes)                
    for i in range(size):
        lx.out("Index #: " + str(i))
        lx.out("mkDir - " + rod.renderOutputNames[i] + " Outs")
        lx.out("DEBUG: Abrv - " + getattr(rod,rod.renderOutputAbrv[i]))
        lx.out("DEBUG: Types - " + rod.renderOutputTypes[i])
        lx.out("DEBUG: Lists - " + rod.renderOutputLists[i])            
        lx.out("DEBUG: List contents - ")
        lx.out(getattr(rod,rod.renderOutputLists[i]))
        makeRenderOutputDir(getattr(rod,rod.renderOutputAbrv[i]), getattr(rod,rod.renderOutputLists[i]), directory, versionUp)
    
    lx.out(" ")
    lx.out("Clear output arrays")
    rod.clearData()
    lx.out("_____________________ Leaving renderDirSetup _____________________")
    
#----------------------------------------------------------------------------------------------  
    
def makeRenderOutPath(output, currentType, directory):        
    #-------------------------------------------------------------------------------
    # This will set the output path in the Render Output in Modo.
    #-------------------------------------------------------------------------------                
    lx.out("_____________________ In makeRenderOutPath _____________________")    
    currentDir = ""
    lx.out(" ")        
    ## Loop through Output types
    size = len(rod.renderOutputTypes)
    for i in range(size):
        if currentType == rod.renderOutputTypes[i]:
            lx.out("Output type:")
            lx.out("             " + rod.renderOutputNames[i])
            getattr(rod,rod.renderOutputLists[i]).append(output)
            currentDir = directory + "\\" + getattr(rod,rod.renderOutputAbrv[i]).upper()
            ## Let's set the file path for each render output in Modo
            # lx.eval( "item.channel filename value:{%s}" % (currentDir))          
    lx.out(" ")    
    lx.out("_____________________ Leaving makeRenderOutPath _____________________")            
    return currentDir

#----------------------------------------------------------------------------------------------

def makeRenderOutputDir(renderOutABRV, renderOutArray, directory, versionUp):        
    lx.out(" ")
    lx.out("_____________________ In makeRenderOutputDir _____________________")
    lx.out(" ")        
    currentDir = ""
    currentName = ""
    matMask = ""
    maskName = ""
    renderOutName = "Global"
    bSlash = "\\"
    renderOutArray = tools.uniqifyList(renderOutArray)
    renderOutNum = len(renderOutArray)
    lx.out("renderOutArray:   ")
    lx.out(renderOutArray)
    lx.out("Number of " + renderOutABRV.upper() + " outputs: " + str(renderOutNum))        
    if renderOutNum >= 1:
        for renderOut in renderOutArray:
            lx.out(" ")
            lx.out(" ")
            lx.out("On render output: " + renderOut.name)
            lx.out("------------------ IN FOR LOOP -------------------------")  
            lx.out("**********************************************************")
            lx.out("**********************************************************")
            lx.out("**********************************************************")
            lx.out("**********************************************************")  
            currentDir = directory + bSlash + renderOutABRV.upper() + bSlash        
            lx.out("currentDir #1: " + currentDir)     
            renderOutParent = renderOut.parent
            lx.out( renderOutParent.name )
            if renderOutParent.name != "Render":
                maskName = renderOutParent.name
                lx.out("maskName: " + maskName)
                maskName = re.sub(r'Material', r'', maskName)
                maskName = maskName.replace(" ", "") # removes all whitespaces
                maskName = re.sub('[()]', '', maskName) #Removes all () 
                lx.out("maskName new: " + maskName)
                renderOutName = maskName
            currentDir = currentDir + renderOutName + "_" + renderOutABRV;                
            currentDir = currentDir.replace(" ", "") # removes all whitespaces
            currentDir = re.sub('[()]', '', currentDir) #Removes all ()
            lx.out("currentDir #2: " + currentDir)                   
            lx.out(" ")
            projShotVers = tools.getRenderFileName(versionUp)
            lx.out(" ")                
            lx.out("ProjShotVers: " + projShotVers)
            
            # popping off the initials at the end of the string
            tmp = projShotVers.split('_')
            projShotVers = tmp[0] + "_" + tmp[1] + "_" + tmp[2]
            
            fileName = currentDir + "\\" + projShotVers + "_" + renderOutName + "_" + renderOutABRV + "_"
            lx.out("File name: " + fileName)
            lx.out("Renderout name: " + renderOutName)
            lx.eval ("item.channel filename {%s} item:{%s}" % (fileName, renderOut.name))
            newFolder = currentDir + bSlash                
            dirTest = newFolder
            dirCheck = os.path.exists(dirTest)                
            if not dirCheck:      
                lx.out("Making new folder: " + newFolder)
                os.makedirs(newFolder)                    
            renderOutName = "Global"
            lx.out(" ")
            lx.out(" ")
            
    lx.out(" ")
    lx.out("##########################################################")
    lx.out(" ")
    
    lx.out("_____________________ Leaving makeRenderOutputDir _____________________")
    

