#/usr/bin/env python

##--------------------------------------##
#              DEV VERSION               # 
##--------------------------------------##

import lx
lx.out("Loading RenderOutputData Class")

class RenderOutputData(object):
    def __init__(self):        
############## These are used to generate multiple function instances ###############################
        self.renderOutputAbrv = ["alpha", "depth", "beauty", "motion", "driverA", "driverB", "driverC", "driverD", "dPduVector", "DpdvVector",
                 "geoNorm", "objCoord", "segID", "INC", "norm", "surfID", "uVCoord", "worldCoord", "AO", "ICPos", "ICValues",
                 "illumDirect", "illumIndir", "illumTotal", "illumUnshdw", "reflecOcc", "shadDen", "diffAmt", "diffCoef", "diffClr", "diffEn",
                 "diffRgh", "reflecCoef", "roughness", "specCoef", "subSurfAmt", "subSurfClr", "transAmt", "transClr", "patricleAge",
                 "patricleID", "patricleVel", "diffDirect", "diffIndirect", "diffTotal", "diffUnshdw", "lumShading", "reflec",
                 "shadedAASamples", "spec", "SSS", "transShading", "volDepth", "volOpac", "volScat", "rColorToWhite", "rColorToOutput", "materialMapOutout"]
 
        self.renderOutputLists = ["alphaOuts", "depthOuts", "beautyOuts", "motionOuts", "driverAOuts", "driverBOuts", "driverCOuts", "driverDOuts", "dPduVectorOuts", "DpdvVectorOuts",
                 "geoNormOuts", "objCoordOuts", "segIDOuts", "INCOuts", "normOuts", "surfIDOuts", "uVCoordOuts", "worldCoordOuts", "AOOuts", "ICPosOuts", "ICValuesOuts",
                 "illumDirectOuts", "illumIndirOuts", "iIllumTotalOuts", "illumUnshdwOuts", "reflecOccOuts", "shadDenOuts", "diffAmtOuts", "diffCoefOuts", "diffClrOuts", "diffEnOuts",
                 "diffRghOuts", "reflecCoefOuts", "roughnessOuts", "specCoefOuts", "subSurfAmtOuts", "subSurfClrOuts", "transAmtOuts", "transClrOuts", "patricleAgeOuts",
                 "patricleIDOuts", "patricleVelOuts", "diffDirectOuts", "diffIndirectOuts", "diffTotalOuts", "diffUnshdwOuts", "lumShadingOuts", "reflecOuts",
                 "shadedAASamplesOuts", "specOuts", "SSSOuts", "transShadingOuts", "volDepthOuts", "volOpacOuts", "volScatOuts", "rColorToWhiteOuts", "rColorToOutputOuts", "materialMapOutoutOuts"] 


        self.renderOutputTypes = ["shade.alpha", "depth", "shade.color", "motion", "driver.a", "driver.b", "driver.c", "driver.d", "geo.dpdu", "geo.dpdv",
                "geo.normal", "geo.object", "geo.segment", "shade.incidence", "shade.normal", "geo.surface", "geo.uv", "geo.world", "occl.ambient",
                "ic.position", "ic.value", "shade.illumDir", "shade.illumInd", "shade.illum", "shade.illumUns", "occl.reflect", "shadow",
                "mat.diffAmt", "mat.diffuse", "mat.diffCol", "mat.diffEng", "mat.diffRough", "mat.reflection", "mat.rough", "mat.specular",
                "mat.subsAmt", "mat.subsCol", "mat.tranAmt", "mat.tranCol", "particle.age", "particle.id", "particle.vel", "shade.diffDir", "shade.diffInd",
                "shade.diffuse", "shade.diffUns", "shade.luminosity", "shade.reflection", "shade.samples", "shade.specular", "shade.subsurface",
                "shade.transparency", "volume.depth", "volume.opacity", "volume.scattering", "recolor.toWhite", "recolor.to", "recolor.matMap"]
        
        self.renderOutputNames = ["Alpha", "Depth", "Final Color", "Motion Vector", "Driver A", "Driver B", "Driver C", "Driver D",
                "dPdu Vector", "dPdv Vector", "Geometric Normal", "Object Coordinates", "Segment ID", "Shading Incidence", "Shading Normal",
                "Surface ID", "UV Coordinates", "World Coordinates", "Ambient Occlusion", "IC Positions", "IC Values", "Illumination Direct", "Illumination InDirect",
                "Illumination Total", "Illumination UnShadowed", "Reflection Occlusion", "Shadow Density", "Diffuse Amount", "Diffuse Coeficiant", "Diffuse Color",
                "Diffuse Energy Conservation", "Diffuse Roughness", "Reflection Coefficient", "Roughness", "Specular Coefficient", "Subsurface Amount",
                "Subsurface Color", " Transparent Amount", "Transparent Color", "Particle Age", "Particle ID", "Particle Velocity", "Diffuse Direct",
                "Diffuse InDirect", "Diffuse Shading Total", "Diffuse Shading UnShadowed", "Luminous Shading", "Reflection Shading", "Shaded AA Samples",
                "Specular Shading", "Subsurface Shading", "Transparent Shading", "Volumetric Depth", "Volumetric Opacity", "Volumetric Scattering", "Recolor To White",
                "Recolor To", "Material Map"]
        
############### Basic ###############################
    #Alpha Outs 
        self.alpha = "alp"
        self.alphaOuts = []
    #Depth Pass 
        self.depth = "dep"
        self.depthOuts = []
    #Final Color  
        self.beauty = "col"
        self.beautyOuts = []
    #Motion Vector 
        self.motion = "mot"
        self.motionOuts = []
        
############### Driver ##############################
    #Driver A
        self.driverA = "drvrA"
        self.driverAOuts = []
    #Driver B
        self.driverB = "drvrB"
        self.driverBOuts = []
    #Driver C
        self.driverC = "drvrC"
        self.driverCOuts = []
    #Driver D
        self.driverD = "drvrD"
        self.driverDOuts = []

############### Geometry ############################
    #dPdu Vector  
        self.dPduVector = "dpdu"
        self.dPduVectorOuts = []
    #Dpdv Vector  
        self.DpdvVector = "dpdv"
        self.DpdvVectorOuts = []
    #Geometry  
        self.geoNorm = "gnr"
        self.geoNormOuts = []
    #Object Coordinates 
        self.objCoord = "objc"
        self.objCoordOuts = []
    #Segment ID 
        self.segID = "gid"
        self.segIDOuts = []
    #Shading Incidence 
        self.INC = "inc"
        self.INCOuts = []
    #Shading Normal 
        self.norm = "nrm"
        self.normOuts = []
    #Surface ID 
        self.surfID = "sid" 
        self.surfIDOuts = []
    #UV Coordinates 
        self.uVCoord = "uvc" 
        self.uVCoordOuts = []
    #World Coordinates 
        self.worldCoord = "wcd" 
        self.worldCoordOuts = [] 

############### Lighting ############################
    #Ambient Occlusion 
        self.AO = "aoc"
        self.AOOuts = []
    #IC Positions  
        self.ICPos = "icp"
        self.ICPosOuts = []
    #IC Values  
        self.ICValues = "icv"
        self.ICValuesOuts = []
    #Illumination (Direct) 
        self.illumDirect = "ild"
        self.illumDirectOuts = []
    #Illumination (Indirect) 
        self.illumIndir = "ili"
        self.illumIndirOuts = []
    #Illumination (Total) 
        self.illumTotal = "ilt"
        self.iIllumTotalOuts = []
    #Illumination (Unshadowed) 
        self.illumUnshdw = "ilu"
        self.illumUnshdwOuts = []
    #Reflection Occlusion 
        self.reflecOcc = "rfo"
        self.reflecOccOuts = []
    #Shadow Density 
        self.shadDen = "shd"
        self.shadDenOuts = []
        

############### Material ############################
    #Diffuse Amount 
        self.diffAmt = "dfAm"
        self.diffAmtOuts = []
    #Diffuse Coeficient 
        self.diffCoef = "dfc"
        self.diffCoefOuts = []
    #Diffuse Color 
        self.diffClr = "dfClr"
        self.diffClrOuts = []
    #Diffuse Energy Conservation 
        self.diffEn = "dfEn"
        self.diffEnOuts = []
    #Diffuse Roughness 
        self.diffRgh = "dfRgh"
        self.diffRghOuts = []
    #Reflection Coefficient 
        self.reflecCoef = "rfc"
        self.reflecCoefOuts = []
    #Roughness  
        self.roughness = "rgh"
        self.roughnessOuts = []
    #Specular Coefficient 
        self.specCoef = "spcoef"
        self.specCoefOuts = []
    #Subsurface Amount 
        self.subSurfAmt = "ssAmt"
        self.subSurfAmtOuts = []
    #Subsurface Color 
        self.subSurfClr = "ssClr"
        self.subSurfClrOuts = []
    #Transparent Amount 
        self.transAmt = "trAmt"
        self.transAmtOuts = []
    #Transparent Color
        self.transClr = "trClr"
        self.transClrOuts = []

############### Particle Effects ####################
    #Particle Age
        self.patricleAge = "ptAge";
        self.patricleAgeOuts = []
    #Particle ID
        self.patricleID = "ptID";
        self.patricleIDOuts = []
    #Particle Velocity
        self.patricleVel = "ptVel";
        self.patricleVelOuts = []

############### Shading #############################
    #Diffuse Shading (Direct) 
        self.diffDirect = "dfd";
        self.diffDirectOuts = []
    #Diffuse Shading (Indirect) 
        self.diffIndirect = "dfi"
        self.diffIndirectOuts = []
    #Diffuse Shading (Total) 
        self.diffTotal = "dft"
        self.diffTotalOuts = []
    #Diffuse Shading (Unshadowed) 
        self.diffUnshdw = "dfu"
        self.diffUnshdwOuts = []
    #Luminous Shading 
        self.lumShading = "lum"
        self.lumShadingOuts = []
    #Reflection Shading 
        self.reflec = "rfl"
        self.reflecOuts = []
    #Shaded AA Samples 
        self.shadedAASamples = "aas"
        self.shadedAASamplesOuts = []
    #Specular Shading
        self.spec = "spc" 
        self.specOuts = []
    #Subsurface Shading
        self.SSS = "sss"
        self.SSSOuts = []
    #Transparent Shading 
        self.transShading = "tran" 
        self.transShadingOuts = []

############### Volume ##############################
    #Volumetric Depth 
        self.volDepth = "voldp" 
        self.volDepthOuts = []
    #Volumetric Opacity 
        self.volOpac = "volop" 
        self.volOpacOuts = []
    #Volumetric Scattering 
        self.volScat = "volsc" 
        self.volScatOuts = []
        
############### Recolor ##############################
    #Recolor To White Output 
        self.rColorToWhite = "rCtW" 
        self.rColorToWhiteOuts = []
    #Recolor To Output
        self.rColorToOutput = "rCtO" 
        self.rColorToOutputOuts = []
    #Material Map Output
        self.materialMapOutout = "mmO" 
        self.materialMapOutoutOuts = []
        
    def clearData(self):
        lx.out("<<<<<<<<<<<<<<< In clearData >>>>>>>>>>>>>>>")
        self.alphaOuts = []
        self.depthOuts = []
        self.beautyOuts = []
        self.motionOuts = []
        self.driverAOuts = []
        self.driverBOuts = []
        self.driverCOuts = []
        self.driverDOuts = []
        self.dPduVectorOuts = []
        self.DpdvVectorOuts = []
        self.geoNormOuts = []
        self.objCoordOuts = []
        self.segIDOuts = []
        self.INCOuts = []
        self.normOuts = [] 
        self.surfIDOuts = []
        self.uVCoordOuts = [] 
        self.worldCoordOuts = [] 
        self.AOOuts = []
        self.ICPosOuts = []
        self.ICValuesOuts = []
        self.illumDirectOuts = []
        self.illumIndirOuts = []
        self.iIllumTotalOuts = []
        self.illumUnshdwOuts = []
        self.reflecOccOuts = []
        self.shadDenOuts = []
        self.diffAmtOuts = []
        self.diffCoefOuts = []
        self.diffClrOuts = []
        self.diffEnOuts = []
        self.diffRghOuts = []
        self.reflecCoefOuts = []
        self.roughnessOuts = []
        self.specCoefOuts = []
        self.subSurfAmtOuts = []
        self.subSurfClrOuts = []
        self.transAmtOuts = []
        self.transClrOuts = []
        self.patricleAgeOuts = []
        self.patricleIDOuts = []
        self.patricleVelOuts = []
        self.diffDirectOuts = []
        self.diffIndirectOuts = []
        self.diffTotalOuts = []
        self.diffUnshdwOuts = []
        self.lumShadingOuts = []
        self.reflecOuts = []
        self.shadedAASamplesOuts = []
        self.specOuts = []
        self.SSSOuts = []
        self.transShadingOuts = []
        self.volDepthOuts = []
        self.volOpacOuts = []
        self.volScatOuts = []
        self.rColorToWhiteOuts = []
        self.rColorToOutputOuts = [] 
        self.materialMapOutoutOuts = []
        
        lx.out("<<<<<<<<<<<<<<< Out clearData >>>>>>>>>>>>>>>")
        