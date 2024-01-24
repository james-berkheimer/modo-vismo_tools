#!/usr/bin/env python
import lx
lx.out("Channel Option Commands Class")

class ChannelOptionCmds(object):
    def __init__(self):
        
##################################################################################################
#                       Item List                                                                #
##################################################################################################
        
##--------- Backdrop Item
        self.backdrop = {} #Backdrop Item
        #Deformation Mode
        self.backdrop["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]        
        #Projection Type
        self.backdrop["projection"] = ["top", "bottom", "back", "front", "right", "left", "camera"]       
        #Render
        self.backdrop["render"] = ["default", "on", "off"]
        #Shape
        self.backdrop["drawShape"] = ["default", "custom"]       
        #Visible
        self.backdrop["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Camera
        self.camera = {} #Camera
        #Deformation Mode
        self.camera["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]        
        #Film Fit
        self.camera["filmFit"] = ["fill", "horizontal", "verticle", "overscan"]
        #Projection Type
        self.camera["projType"] = ["persp", "ortho", "cylindrical", "cylindricalvr", "spherical", "sphericalvr"]       
        #Render
        self.camera["render"] = ["default", "on", "off"]
        #Shape
        self.camera["drawShape"] = ["default", "custom"]      
        #Stereo Composite
        self.camera["stereoComp"] = ["stereoNone", "anaRedCyan", "anaGrayscale", "anaRedCyanHalf", "anaRedCyanOpt", "anaRedBlueLS", "sideBySide", "sideBySideFull", "sideBySideCross", "sideBySideCrossFull"]
        #Stereo Eyes
        self.camera["stereoEye"] = ["left", "right", "both"]
        #Visible
        self.camera["visible"] = ["default", "on", "off", "allOff"]
        

##--------- Locator
        self.groupLocator = {} #Group Locator
        #Deformation Mode
        self.groupLocator["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]        
        #Render
        self.groupLocator["render"] = ["default", "on", "off"]
        #Shape
        self.groupLocator["drawShape"] = ["default", "custom"]      
        #Space
        self.groupLocator["space"] = ["none", "space2d", "space3d"]
        #Visible
        self.groupLocator["visible"] = ["default", "on", "off", "allOff"]
        
        self.locator = {} #Locator
        #Deformation Mode
        self.locator["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]        
        #Render
        self.locator["render"] = ["default", "on", "off"]
        #Shape
        self.locator["drawShape"] = ["default", "custom"]      
        #Visible
        self.locator["visible"] = ["default", "on", "off", "allOff"]
        
        self.txtrlocator = {}  #Texture Locator
        #Deformation Mode
        self.txtrlocator["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]        
        #Falloff Type
        self.txtrlocator["fallType"] = ["cubic", "spherical", "linearX", "linearY", "linearZ"]
        #Horizontal Repeat
        self.txtrlocator["tileU"] = ["reset", "repeat", "mirror", "edge"]
        #Projection Type
        self.txtrlocator["projType"] = ["solid", "planar", "cylindrical", "spherical", "cubic", "front", "uv", "lightprobe", "implicitUV", "box"]
        #Random Texture Offsets
        self.txtrlocator["randOffset"] = ["none", "particle", "meshPart", "item"]
        #Render
        self.txtrlocator["render"] = ["default", "on", "off"]
        #Shape
        self.txtrlocator["drawShape"] = ["default", "custom"]
        #Tangent Vecotr Type
        self.txtrlocator["tngtType"] = ["dpdudpdv", "dpducross"]
        #Vertical Repeat
        self.txtrlocator["tileV"] = ["reset", "repeat", "mirror", "edge"]
        #Visible
        self.txtrlocator["visible"] = ["default", "on", "off", "allOff"]     

##--------- Mesh
        self.mesh = {} #Mesh
        #Curve Radius Unit
        self.mesh["radUnit"] = ["meters", "pixels"]
        #Deformation Mode
        self.mesh["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Fill
        self.mesh["fillOptions"] = ["default", "user", "bgplus", "bgminus"]
        #Render
        self.mesh["render"] = ["default", "on", "off"]
        #Shape
        self.mesh["drawShape"] = ["default", "custom"]
        #Style
        self.mesh["style"] = ["default", "wire", "vmap", "solid", "shaded"]
        #Texture
        self.mesh["texture"] = ["off", "decal", "shade"]
        #Visible
        self.mesh["visible"] = ["default", "on", "off", "allOff"]
        #Wireframe
        self.mesh["wireOptions"] = ["default", "user", "bgplus", "bgminus"]
        
        
##--------- Deformers
        self.deform_dot_bend = {} #Bend Effector
        #Deformation Mode
        self.deform_dot_bend["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.deform_dot_bend["render"] = ["default", "on", "off"]
        #Shape
        self.deform_dot_bend["drawShape"] = ["default", "custom"]
        #Visible
        self.deform_dot_bend["visible"] = ["default", "on", "off", "allOff"]        
        
        self.deform_dot_crvconst = {} #Curve Constrait Effector
        #Deformation Mode
        self.deform_dot_crvconst["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.deform_dot_crvconst["render"] = ["default", "on", "off"]
        #Shape
        self.deform_dot_crvconst["drawShape"] = ["default", "custom"]
        #Visible
        self.deform_dot_crvconst["visible"] = ["default", "on", "off", "allOff"]
        
        self.geninfluence = {}  #General Influence
        #Interpolation
        self.geninfluence["interpolation"] = ["local", "linear"]
        #Type
        self.geninfluence["type"] = ["all", "mapWeight", "mapPick", "ptagMaterial", "ptagPart", "ptagPick"]
        
        self.iteminfluence = {}  #Item Influence
        #Interpolation
        self.iteminfluence["interpolation"] = ["local", "linear"]
                
        self.deform_dot_lag = {}  #Lag Effector
        #Deformation Mode
        self.deform_dot_lag["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.deform_dot_lag["render"] = ["default", "on", "off"]
        #Shape
        self.deform_dot_lag["drawShape"] = ["default", "custom"]
        #Visible
        self.deform_dot_lag["visible"] = ["default", "on", "off", "allOff"]        
        
        self.deform_dot_lattice = {}  #Lattice Effector
        #Deformation Mode
        self.deform_dot_lattice["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.deform_dot_lattice["render"] = ["default", "on", "off"]
        #Shape
        self.deform_dot_lattice["drawShape"] = ["default", "custom"]
        #Visible
        self.deform_dot_lattice["visible"] = ["default", "on", "off", "allOff"]        
        
        self.deform_dot_magnet = {}  #Magnet Effector
        #Deformation Mode
        self.deform_dot_magnet["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.deform_dot_magnet["render"] = ["default", "on", "off"]
        #Shape
        self.deform_dot_magnet["drawShape"] = ["default", "custom"]
        #Shape
        self.deform_dot_magnet["magnetShape"] = ["plane", "sphere", "cylinder"]
        #Visible
        self.deform_dot_magnet["visible"] = ["default", "on", "off", "allOff"]
        
        self.deformmdd2 = {}  #MDD Influence
        #End Behavior
        self.deformmdd2["endBehavior"] = ["Stop", "Repeat", "Mirror"]
                
        self.morphdeform = {}  #Morph Influence
        #Deformation Mode
        self.morphdeform["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.morphdeform["render"] = ["default", "on", "off"]
        #Shape
        self.morphdeform["drawShape"] = ["default", "custom"]
        #Visible
        self.morphdeform["visible"] = ["default", "on", "off", "allOff"]
        
        self.deformgroup = {}  #Normalizing Folder
        #Interpolation
        self.deformgroup["interpolation"] = ["local", "linear"]
                
        self.softlag = {}  #Soft Lag
        #Deformation Mode
        self.softlag["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.softlag["render"] = ["default", "on", "off"]
        #Shape
        self.softlag["drawShape"] = ["default", "custom"]
        #Visible
        self.softlag["visible"] = ["default", "on", "off", "allOff"]
        
        self.deform_dot_vortex = {}  #Vortex Effector
        #Deformation Mode
        self.deform_dot_vortex["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.deform_dot_vortex["render"] = ["default", "on", "off"]
        #Shape
        self.deform_dot_vortex["drawShape"] = ["default", "custom"]
        #Visible
        self.deform_dot_vortex["visible"] = ["default", "on", "off", "allOff"]
                
        self.weightcontainer = {}  #Weight Container
        #Deformation Mode
        self.weightcontainer["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.weightcontainer["render"] = ["default", "on", "off"]
        #Shape
        self.weightcontainer["drawShape"] = ["default", "custom"]
        #Visible
        self.weightcontainer["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Dynamics
        self.collisionemitter = {}  #Collision Emitter
        #Deformation Mode
        self.collisionemitter["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.collisionemitter["render"] = ["default", "on", "off"]
        #reType
        self.collisionemitter["reType"] = ["random", "uniform"]
        #Shape
        self.collisionemitter["drawShape"] = ["default", "custom"]       
        #Visible
        self.collisionemitter["visible"] = ["default", "on", "off", "allOff"]        
        
        self.dynamicsconstraintmodifier = {}  #Constraint Modifier
        #Constraint Type
        self.dynamicsconstraintmodifier["constraintType"] = ["consPin", "consPoint"]
        #Deformation Mode
        self.dynamicsconstraintmodifier["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Limit
        self.dynamicsconstraintmodifier["limit"] = ["limitByNone", "limitByVolumeLessThan", "limitByVolumeGreaterThan"]
        #Method
        self.dynamicsconstraintmodifier["method"] = ["makeByOverlap", "makeByContact", "makeByProximity", "break", "decay", "strengthen"]
        #Mode
        self.dynamicsconstraintmodifier["mode"] = ["all", "boundary"]
        #reType
        self.dynamicsconstraintmodifier["reType"] = ["random", "uniform", "area"]
        #Phase
        self.dynamicsconstraintmodifier["phase"] = ["start", "tick", "birth"]
        #Shape
        self.dynamicsconstraintmodifier["drawShape"] = ["default", "custom"]
        #Visible
        self.dynamicsconstraintmodifier["visible"] = ["default", "on", "off", "allOff"]
        
        self.dynamic_dot_replicatorfilter = {}  #Dynamic Replicator
        #Constraint Type
        self.dynamic_dot_replicatorfilter["constraintType"] = ["consPin", "consPoint"]
        #Deformation Mode
        self.dynamic_dot_replicatorfilter["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #reCollisionShape
        self.dynamic_dot_replicatorfilter["reCollisionShape"] = ["bbox", "sphere", "hull", "multiHull", "mesh", "deformingMesh", "convexDecomposition", "plane"]
        #reMassSource
        self.dynamic_dot_replicatorfilter["reMassSource"] = ["worldDensity", "localDensity", "localMass"]
        #reState
        self.dynamic_dot_replicatorfilter["reState"] = ["dynamic", "kinematic"]
        #Shape
        self.dynamic_dot_replicatorfilter["drawShape"] = ["default", "custom"]
        #Visible
        self.dynamic_dot_replicatorfilter["visible"] = ["default", "on", "off", "allOff"]
        
        self.conshinge = {}  #Hinge
        #Deformation Mode
        self.conshinge["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.conshinge["render"] = ["default", "on", "off"]
        #Shape
        self.conshinge["drawShape"] = ["default", "custom"]
        #Visible
        self.conshinge["visible"] = ["default", "on", "off", "allOff"]
        
        self.particlesim = {}  #Particle Simulation
        #Deformation Mode
        self.particlesim["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.particlesim["render"] = ["default", "on", "off"]
        #Shape
        self.particlesim["drawShape"] = ["default", "custom"]
        #Visible
        self.particlesim["visible"] = ["default", "on", "off", "allOff"]
        
        self.conspin = {}  #Pin
        #Deformation Mode
        self.conspin["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.conspin["render"] = ["default", "on", "off"]
        #Shape
        self.conspin["drawShape"] = ["default", "custom"]
        #Visible
        self.conspin["visible"] = ["default", "on", "off", "allOff"]
        
        self.conspoint = {}  #Point
        #Deformation Mode
        self.conspoint["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.conspoint["render"] = ["default", "on", "off"]
        #Shape
        self.conspoint["drawShape"] = ["default", "custom"]
        #Visible
        self.conspoint["visible"] = ["default", "on", "off", "allOff"]
        
        self.proceduralshatteritem = {}  #Procedural Shatter
        #Deformation Mode
        self.proceduralshatteritem["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Pattern
        self.proceduralshatteritem["shatterPatern"] = ["uniform", "impact", "radial"]
        #reImpulseOn
        self.proceduralshatteritem["reImplulseOn"] = ["off", "onWake", "continuous"]
        #Render
        self.proceduralshatteritem["render"] = ["default", "on", "off"]
        #Shape
        self.proceduralshatteritem["drawShape"] = ["default", "custom"]
        #Split Islands
        self.proceduralshatteritem["splitIslands"] = ["never", "initial", "afterInitial", "always"]
        #Visible
        self.proceduralshatteritem["visible"] = ["default", "on", "off", "allOff"]
        
        self.consslidehinge = {}  #Slide Hinge
        #Deformation Mode
        self.consslidehinge["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.consslidehinge["render"] = ["default", "on", "off"]
        #Shape
        self.consslidehinge["drawShape"] = ["default", "custom"]
        #Visible
        self.consslidehinge["visible"] = ["default", "on", "off", "allOff"]
        
        self.consspring = {}  #Spring
        #Deformation Mode
        self.consspring["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.consspring["render"] = ["default", "on", "off"]
        #Shape
        self.consspring["drawShape"] = ["default", "custom"]
        #Visible
        self.consspring["visible"] = ["default", "on", "off", "allOff"]
        
        self.solver = {}  #Solver
        #Deformation Mode
        self.solver["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.solver["render"] = ["default", "on", "off"]
        #Shape
        self.solver["drawShape"] = ["default", "custom"]
        #Visible
        self.solver["visible"] = ["default", "on", "off", "allOff"]
        

##--------- Falloffs
        self.falloff_dot_bezier = {}  #Bezier Falloff
        #Axial Shape
        self.falloff_dot_bezier["axialDecayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Deformation Mode
        self.falloff_dot_bezier["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]        
        #Falloff Shape
        self.falloff_dot_bezier["decayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Render
        self.falloff_dot_bezier["render"] = ["default", "on", "off"]
        #Shape
        self.falloff_dot_bezier["drawShape"] = ["default", "custom"]
        #Visible
        self.falloff_dot_bezier["visible"] = ["default", "on", "off", "allOff"]
        
        self.falloff_dot_capsule = {}  #Capsule Falloff
        #Decay Shape
        self.falloff_dot_capsule["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.falloff_dot_capsule["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.falloff_dot_capsule["render"] = ["default", "on", "off"]
        #Shape
        self.falloff_dot_capsule["drawShape"] = ["default", "custom"]
        #Visible
        self.falloff_dot_capsule["visible"] = ["default", "on", "off", "allOff"]
        
        self.falloff_dot_linear = {}  #Linear Falloff
        #Decay Shape
        self.falloff_dot_linear["decayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Deformation Mode
        self.falloff_dot_linear["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.falloff_dot_linear["render"] = ["default", "on", "off"]
        #Shape
        self.falloff_dot_linear["drawShape"] = ["default", "custom"]
        #Visible
        self.falloff_dot_linear["visible"] = ["default", "on", "off", "allOff"]
        
        self.falloff_dot_radial = {}  #Radial Falloff
        #Decay Shape
        self.falloff_dot_radial["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.falloff_dot_radial["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.falloff_dot_radial["render"] = ["default", "on", "off"]
        #Shape
        self.falloff_dot_radial["drawShape"] = ["default", "custom"]
        #Visible
        self.falloff_dot_radial["visible"] = ["default", "on", "off", "allOff"]
        
        self.falloff_dot_spline = {}  #Spline Falloff
        #Axial Shape
        self.falloff_dot_spline["axialDecayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Deformation Mode
        self.falloff_dot_spline["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Shape
        self.falloff_dot_spline["decayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Render
        self.falloff_dot_spline["render"] = ["default", "on", "off"]
        #Shape
        self.falloff_dot_spline["drawShape"] = ["default", "custom"]
        #Visible
        self.falloff_dot_spline["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Forces
        self.force_dot_curve = {}  #Curve Force
        #Decay Shape
        self.force_dot_curve["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.force_dot_curve["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.force_dot_curve["render"] = ["default", "on", "off"]
        #Shape
        self.force_dot_curve["drawShape"] = ["default", "custom"]
        #Visible
        self.force_dot_curve["visible"] = ["default", "on", "off", "allOff"]
        
        self.force_dot_drag = {}  #Drag Force
        #Decay Shape
        self.force_dot_drag["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.force_dot_drag["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.force_dot_drag["render"] = ["default", "on", "off"]
        #Shape
        self.force_dot_drag["drawShape"] = ["default", "custom"]
        #Visible
        self.force_dot_drag["visible"] = ["default", "on", "off", "allOff"]
        
        self.force_dot_linear = {}  #Linear Force
        #Decay Shape
        self.force_dot_linear["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.force_dot_linear["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.force_dot_linear["render"] = ["default", "on", "off"]
        #Shape
        self.force_dot_linear["drawShape"] = ["default", "custom"]
        #Visible
        self.force_dot_linear["visible"] = ["default", "on", "off", "allOff"]
        
        self.force_dot_newton = {}  #Newton Force
        #Decay Shape
        self.force_dot_newton["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.force_dot_newton["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.force_dot_newton["render"] = ["default", "on", "off"]
        #Shape
        self.force_dot_newton["drawShape"] = ["default", "custom"]
        #Visible
        self.force_dot_newton["visible"] = ["default", "on", "off", "allOff"]
        
        self.particlesim = {}  #Particle Simulation
        #Decay Shape
        self.particlesim["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.particlesim["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.particlesim["render"] = ["default", "on", "off"]
        #Shape
        self.particlesim["drawShape"] = ["default", "custom"]
        #Visible
        self.particlesim["visible"] = ["default", "on", "off", "allOff"]
        
        self.force_dot_radial = {}  #Radial Force
        #Decay Shape
        self.force_dot_radial["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.force_dot_radial["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.force_dot_radial["render"] = ["default", "on", "off"]
        #Shape
        self.force_dot_radial["drawShape"] = ["default", "custom"]
        #Visible
        self.force_dot_radial["visible"] = ["default", "on", "off", "allOff"]
        
        self.force_dot_turbulence = {}  #Turbulence Force
        #Decay Shape
        self.force_dot_turbulence["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.force_dot_turbulence["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.force_dot_turbulence["render"] = ["default", "on", "off"]
        #Shape
        self.force_dot_turbulence["drawShape"] = ["default", "custom"]
        #Visible
        self.force_dot_turbulence["visible"] = ["default", "on", "off", "allOff"]
        
        self.force_dot_vortex = {}  #Vortex Force
        #Decay Shape
        self.force_dot_vortex["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.force_dot_vortex["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.force_dot_vortex["render"] = ["default", "on", "off"]
        #Shape
        self.force_dot_vortex["drawShape"] = ["default", "custom"]
        #Visible
        self.force_dot_vortex["visible"] = ["default", "on", "off", "allOff"]
        
        self.force_dot_wind = {}  #Wind Force
        #Decay Shape
        self.force_dot_wind["decayMode"] = ["smooth", "power", "gaussian"]
        #Deformation Mode
        self.force_dot_wind["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.force_dot_wind["render"] = ["default", "on", "off"]
        #Shape
        self.force_dot_wind["drawShape"] = ["default", "custom"]
        #Visible
        self.force_dot_wind["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Lights
        self.arealight = {}  #Area Light
        #Deformation Mode
        self.arealight["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Type
        self.arealight["fallType"] = ["none", "invdist", "invdist2"]
        #Mode
        self.arealight["linkMode"] = ["include", "exclude"]        
        #Render
        self.arealight["render"] = ["default", "on", "off"]
        #Shadow Type
        self.arealight["shadType"] = ["none", "raytrace", "shadowmap"]
        #Shape
        self.arealight["drawShape"] = ["default", "custom"]
        #Shape
        self.arealight["shape"] = ["rectangle", "elipse"]
        #Visible
        self.arealight["visible"] = ["default", "on", "off", "allOff"]
        
        self.cylinderlight = {}  #Cylinder Light
        #Deformation Mode
        self.cylinderlight["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Type
        self.cylinderlight["fallType"] = ["none", "invdist", "invdist2"]
        #Mode
        self.cylinderlight["linkMode"] = ["include", "exclude"]        
        #Render
        self.cylinderlight["render"] = ["default", "on", "off"]
        #Shadow Type
        self.cylinderlight["shadType"] = ["none", "raytrace", "shadowmap"]
        #Shape
        self.cylinderlight["drawShape"] = ["default", "custom"]
        #Visible
        self.cylinderlight["visible"] = ["default", "on", "off", "allOff"]
        
        self.sunlight = {}  #Directional Light
        #Clamp Intensity
        self.sunlight["clamp"] = ["none", "clamp", "replace"]
        #Deformation Mode
        self.sunlight["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Type
        self.sunlight["fallType"] = ["none", "invdist", "invdist2"]
        #Mode
        self.sunlight["linkMode"] = ["include", "exclude"]           
        #Render
        self.sunlight["render"] = ["default", "on", "off"]
        #Shadow Type
        self.sunlight["decayMode"] = ["smooth", "power", "gaussian"]
        #Shape
        self.sunlight["drawShape"] = ["default", "custom"]
        #Visible
        self.sunlight["visible"] = ["default", "on", "off", "allOff"]
        
        self.domelight = {}  #Dome Light
        #Deformation Mode
        self.domelight["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Type
        self.domelight["fallType"] = ["none", "invdist", "invdist2"]
        #Mode
        self.domelight["linkMode"] = ["include", "exclude"]         
        #Render
        self.domelight["render"] = ["default", "on", "off"]
        #Shadow Type
        self.domelight["shadType"] = ["none", "raytrace", "shadowmap"]
        #Shape
        self.domelight["drawShape"] = ["default", "custom"]
        #Visible
        self.domelight["visible"] = ["default", "on", "off", "allOff"]
        
        self.photometrylight = {}  #Photometric Light
        #Deformation Mode
        self.photometrylight["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Type
        self.photometrylight["fallType"] = ["none", "invdist", "invdist2"]
        #Mode
        self.photometrylight["linkMode"] = ["include", "exclude"]         
        #Render
        self.photometrylight["render"] = ["default", "on", "off"]
        #Shadow Type
        self.photometrylight["shadType"] = ["none", "raytrace", "shadowmap"]
        #Shape
        self.photometrylight["drawShape"] = ["default", "custom"]
        #Visible
        self.photometrylight["visible"] = ["default", "on", "off", "allOff"]
        
        self.pointlight = {}  #Poinr Light
        #Deformation Mode
        self.pointlight["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Type
        self.pointlight["fallType"] = ["none", "invdist", "invdist2"]
        #Mode
        self.pointlight["linkMode"] = ["include", "exclude"]         
        #Render
        self.pointlight["render"] = ["default", "on", "off"]
        #Shadow Type
        self.pointlight["shadType"] = ["none", "raytrace", "shadowmap"]
        #Shape
        self.pointlight["drawShape"] = ["default", "custom"]
        #Visible
        self.pointlight["visible"] = ["default", "on", "off", "allOff"]
        
        self.portal = {}  #Portal Light
        #Deformation Mode
        self.portal["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Type
        self.portal["fallType"] = ["none", "invdist", "invdist2"]
        #Mode
        self.portal["linkMode"] = ["Include", "Exclude"]        
        #Render
        self.portal["render"] = ["default", "on", "off"]
        #Shadow Type
        self.portal["shadType"] = ["none", "raytrace", "shadowmap"]
        #Shape
        self.portal["drawShape"] = ["default", "custom"]
        #Shape
        self.portal["shape"] = ["rectangle", "elipse"]
        #Visible
        self.portal["visible"] = ["default", "on", "off", "allOff"]
        
        self.spotlight = {}  #Spot Light
        #Deformation Mode
        self.spotlight["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Falloff Type
        self.spotlight["fallType"] = ["none", "invdist", "invdist2"]
        #Mode
        self.spotlight["linkMode"] = ["include", "exclude"]         
        #Render
        self.spotlight["render"] = ["default", "on", "off"]
        #Shadow Type
        self.spotlight["shadType"] = ["none", "raytrace", "shadowmap"]
        #Shape
        self.spotlight["drawShape"] = ["default", "custom"]
        #Visible
        self.spotlight["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Mootzoid
        self.emPolygonizer5 = {}  #emPolygonizer5
        #Deformation Mode
        self.emPolygonizer5["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #emP5_mnAlgorithm
        self.emPolygonizer5["emP5_mnAlgorithm"] = ["Polygonizer_(Marching_Cubes)", "Polygonizer_(Marching_Tetrahedrons)"]
        #emP5_inMode
        self.emPolygonizer5["emP5_inMode"] = ["Use_Particle_Cache_File", "Use_connected_Scene_Item"]
        #emP5_lsMeanMode
        self.emPolygonizer5["emP5_lsMeanMode"] = ["Automatic_Mean", "Use_Point_Position_as_Mean"]
        #emP5_dtNormalPnMode
        self.emPolygonizer5["emP5_dtNormalPnMode"] = ["Disabled", "One_Pass", "Two_Passes", "Three_Passes"]
        #emP5_fcMode
        self.emPolygonizer5["emP5_fcMode"] = ["No_File_Caching", "Simulate_and_Write", "Read"]
        #emP5_fcFileFormat
        self.emPolygonizer5["emP5_fcFileFormat"] = ["Proprietary,_binary___(.mzd)", "Proprietary,_binary___(.emp2)", "Proprietary,_ascii___(.emp2)", "Wavefront___(.obj)", "RealFlow___(.bin)"]
        #emP5_dtDataTransferMode
        self.emPolygonizer5["emP5_dtDataTransferMode"] = ["Automatic", "Ignore", "Tolerant", "Strict", "Ultra_Strict"]
        #emP5_exDgDebugGeo
        self.emPolygonizer5["emP5_exDgDebugGeo"] = ["off", "Leaves_only_(Replace)", "Leaves_and_Borders_(Replace)", "Leaves_only_(Merge)", "Leaves_and_Borders_(Merge)", "Position_as_Boxes"]
        #emP5_exPrOnError
        self.emPolygonizer5["emP5_exPrOnError"] = ["do_nothing", "create_an_empty_mesh", "create_an_error_message_mesh"]
        #emP5_vpDisplay
        self.emPolygonizer5["emP5_vpDisplay"] = ["None", "Points", "Edges"]
        #Render
        self.emPolygonizer5["render"] = ["default", "on", "off"]
        #Shape
        self.emPolygonizer5["drawShape"] = ["default", "custom"]
        #Visible
        self.emPolygonizer5["visible"] = ["default", "on", "off", "allOff"]
        
        self.emReader = {}  #emReader
        #Deformation Mode
        self.emReader["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #emRd_flFormat
        self.emReader["emRd_flFormat"] = ["Mootzoid_mzd", "emPolygonizer2_emp2", "Wavefront_obj", "RealFlow_bin"]
        #emRd_flIndexMode
        self.emReader["emRd_flIndexMode"] = ["Use_Idx_Value_Round", "Use_Idx_Value_Floor", "Use_Idx_Value_Cell"]
        #emRd_fxTriangulate
        self.emReader["emRd_fxTriangulate"] = ["off", "Concave_Polygons", "All_Polygons"]
        #emRd_vpDisplay
        self.emReader["emRd_vpDisplay"] = ["None", "Points", "Edges"]
        #Render
        self.emReader["render"] = ["default", "on", "off"]
        #Shape
        self.emReader["drawShape"] = ["default", "custom"]
        #Visible
        self.emReader["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Particles
        self.replicator = {}  #Replicator
        #Deformation Mode
        self.replicator["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.replicator["render"] = ["default", "on", "off"]
        #Shape
        self.replicator["drawShape"] = ["default", "custom"]
        #Source Mode
        self.replicator["source"] = ["particle", "surface", "polygon", "singleVertex"]
        #Visible
        self.replicator["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Particles - Modifiers
        self.pmod_dot_audio = {}  #Particle Audio Modifier
        #Color Mode
        self.pmod_dot_audio["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_audio["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Dissolve Mode
        self.pmod_dot_audio["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_audio["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_audio["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_audio["render"] = ["default", "on", "off"]
        #Shape
        self.pmod_dot_audio["drawShape"] = ["default", "custom"]
        #Visible
        self.pmod_dot_audio["visible"] = ["default", "on", "off", "allOff"]
        
        self.pmod_dot_expression = {}  #Particle Expression Modifier
        #Color Mode
        self.pmod_dot_expression["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_expression["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Dissolve Mode
        self.pmod_dot_expression["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_expression["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_expression["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_expression["render"] = ["default", "on", "off"]
        #Shape
        self.pmod_dot_expression["drawShape"] = ["default", "custom"]
        #Visible
        self.pmod_dot_expression["visible"] = ["default", "on", "off", "allOff"]
        
        self.pmod_dot_audio = {}  #Particle Audio Modifier
        #Color Mode
        self.replicator["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.replicator["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Dissolve Mode
        self.replicator["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.replicator["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.replicator["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.replicator["render"] = ["default", "on", "off"]
        #Shape
        self.replicator["drawShape"] = ["default", "custom"]
        #Visible
        self.replicator["visible"] = ["default", "on", "off", "allOff"]
        
        self.pmod_dot_lookat = {}  #Particle Look At Modifier
        #Deformation Mode
        self.pmod_dot_lookat["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Mesh Source
        self.pmod_dot_lookat["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_lookat["render"] = ["default", "on", "off"]
        #Shape
        self.pmod_dot_lookat["drawShape"] = ["default", "custom"]
        #Target
        self.pmod_dot_lookat["target"] = ["thisLocator", "nextParticle", "previousParticle", "camera"]
        #Visible
        self.pmod_dot_lookat["visible"] = ["default", "on", "off", "allOff"]
        
        self.pmod_dot_basic = {}  #Particle Modifier
        #Color Mode
        self.pmod_dot_basic["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_basic["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Dissolve Mode
        self.pmod_dot_basic["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_basic["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_basic["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_basic["render"] = ["default", "on", "off"]
        #Shape
        self.pmod_dot_basic["drawShape"] = ["default", "custom"]
        #Visible
        self.pmod_dot_basic["visible"] = ["default", "on", "off", "allOff"]
        
        self.pmod_dot_random = {}  #Particle Random Modifier
        #Color Mode
        self.pmod_dot_random["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_random["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Dissolve Mode
        self.pmod_dot_random["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_random["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_random["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_random["render"] = ["default", "on", "off"]
        #Shape
        self.pmod_dot_random["drawShape"] = ["default", "custom"]
        #Visible
        self.pmod_dot_random["visible"] = ["default", "on", "off", "allOff"]
        
        self.pmod_dot_sieve = {}  #Particle Sieve Modifier
        #Condition
        self.pmod_dot_sieve["condition"] = ["pID", "posX", "posY", "posZ", "velX", "velY", "velZ", "frcX", "frcY", "frcZ", "clrX", "clrY", "clrZ", "lum", "diss", "rate", "age", "mass", "size", "path", "falloff", "particleSource", "slope", "map"]
        #Deformation Mode
        self.pmod_dot_sieve["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #If
        self.pmod_dot_sieve["feature"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_sieve["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_sieve["render"] = ["default", "on", "off"]
        #Shape
        self.pmod_dot_sieve["drawShape"] = ["default", "custom"]
        #Visible
        self.pmod_dot_sieve["visible"] = ["default", "on", "off", "allOff"]
        
        self.pmod_dot_step = {}  #Particle Step Modifier
        #Color Mode
        self.pmod_dot_step["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_step["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Dissolve Mode
        self.pmod_dot_step["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_step["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_step["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_step["render"] = ["default", "on", "off"]
        #Shape
        self.pmod_dot_step["drawShape"] = ["default", "custom"]
        #Visible
        self.pmod_dot_step["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Particles - Point Clouds
        self.csvcache = {}  #CSV Point Cache
        #Deformation Mode
        self.csvcache["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.csvcache["render"] = ["default", "on", "off"]
        #Shape
        self.csvcache["drawShape"] = ["default", "custom"]
        #Type
        self.csvcache["seqType"] = ["still", "seq", "seqRange"]
        #Visible
        self.csvcache["visible"] = ["default", "on", "off", "allOff"]
        
        self.pcloud = {}  #Particle Cloud
        #Deformation Mode
        self.pcloud["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Type
        self.pcloud["seqType"] = ["still", "seq", "seqRange"]
        #Density Distribution
        self.pcloud["distrib"] = ["none", "radial", "cumulus1", "cumulus2", "ring"]
        #Shape
        self.pcloud["drawShape"] = ["default", "custom"]
        #Visible
        self.pcloud["visible"] = ["default", "on", "off", "allOff"]
        
        self.pmod_dot_generator = {}  #Particle Generator
        #Deformation Mode
        self.pmod_dot_generator["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Particle ID's
        self.pmod_dot_generator["pidOrder"] = ["sequential", "random"]
        #Render
        self.pmod_dot_generator["render"] = ["default", "on", "off"]
        #Shape
        self.pmod_dot_generator["drawShape"] = ["default", "custom"]
        #Type
        self.pmod_dot_generator["type"] = ["array", "radial", "linear"]
        #Visible
        self.pmod_dot_generator["visible"] = ["default", "on", "off", "allOff"]
        
        self.realparticle = {}  #Realflow Particles
        #Deformation Mode
        self.realparticle["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.realparticle["render"] = ["default", "on", "off"]
        #Shape
        self.realparticle["drawShape"] = ["default", "custom"]
        #Visible
        self.realparticle["visible"] = ["default", "on", "off", "allOff"]
        
        self.surfgenloc = {}  #Surface Particle Generator
        #Deformation Mode
        self.surfgenloc["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.surfgenloc["render"] = ["default", "on", "off"]
        #Shape
        self.surfgenloc["drawShape"] = ["default", "custom"]
        #Visible
        self.surfgenloc["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Particles - Simulation
        self.collectoremitter = {}  #Collector/Emitter
        #Deformation Mode
        self.collectoremitter["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.collectoremitter["render"] = ["default", "on", "off"]
        #Shape
        self.collectoremitter["drawShape"] = ["default", "custom"]
        #Visible
        self.collectoremitter["visible"] = ["default", "on", "off", "allOff"]
        
        self.curveemitter = {}  #Curve Emitter
        #Deformation Mode
        self.curveemitter["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.curveemitter["render"] = ["default", "on", "off"]
        #Shape
        self.curveemitter["drawShape"] = ["default", "custom"]
        #Visible
        self.curveemitter["visible"] = ["default", "on", "off", "allOff"]
        
        self.dynamiccollider = {}  #Dynamic Collider
        #Deformation Mode
        self.dynamiccollider["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.dynamiccollider["render"] = ["default", "on", "off"]
        #Shape
        self.dynamiccollider["drawShape"] = ["default", "custom"]
        #Visible
        self.dynamiccollider["visible"] = ["default", "on", "off", "allOff"]
        
        self.dynamicfluid = {}  #Dynamic Fluid
        #Deformation Mode
        self.dynamicfluid["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.dynamicfluid["render"] = ["default", "on", "off"]
        #Shape
        self.dynamicfluid["drawShape"] = ["default", "custom"]
        #Visible
        self.dynamicfluid["visible"] = ["default", "on", "off", "allOff"]
        
        self.flockingop = {}  #Particle Flocking
        #Deformation Mode
        self.flockingop["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.flockingop["render"] = ["default", "on", "off"]
        #Shape
        self.flockingop["drawShape"] = ["default", "custom"]
        #Visible
        self.flockingop["visible"] = ["default", "on", "off", "allOff"]
        
        self.particleop = {}  #Particle Operator
        #Deformation Mode
        self.particleop["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.particleop["render"] = ["default", "on", "off"]
        #Shape
        self.particleop["drawShape"] = ["default", "custom"]
        #Type
        self.particleop["type"] = ["assign", "integrate", "new", "trigger"]
        #Visible
        self.particleop["visible"] = ["default", "on", "off", "allOff"]
        
        self.particlesim = {}  #Particle Simulation
        #Deformation Mode
        self.particlesim["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.particlesim["render"] = ["default", "on", "off"]
        #Shape
        self.particlesim["drawShape"] = ["default", "custom"]
        #Visible
        self.particlesim["visible"] = ["default", "on", "off", "allOff"]
        
        self.radialemitter = {}  #Radial Emitter
        #Deformation Mode
        self.radialemitter["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Emission Type
        self.radialemitter["type"] = ["Random", "Uniform"]
        #Render
        self.radialemitter["render"] = ["default", "on", "off"]
        #Shape
        self.radialemitter["drawShape"] = ["default", "custom"]
        #Visible
        self.radialemitter["visible"] = ["default", "on", "off", "allOff"]
        
        self.sourceemitter = {}  #Source Emitter
        #Deformation Mode
        self.sourceemitter["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Emit Mode
        self.sourceemitter["mode"] = ["fixed", "average", "particle", "pulse"]
        #Render
        self.sourceemitter["render"] = ["default", "on", "off"]
        #Shape
        self.sourceemitter["drawShape"] = ["default", "custom"]
        #Visible
        self.sourceemitter["visible"] = ["default", "on", "off", "allOff"]
        
        self.surfemitter = {}  #Surface Emitter
        #Deformation Mode
        self.surfemitter["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.surfemitter["render"] = ["default", "on", "off"]
        #Shape
        self.surfemitter["drawShape"] = ["default", "custom"]
        #Visible
        self.surfemitter["visible"] = ["default", "on", "off", "allOff"]
        
        self.particleterminator = {}  #Terminator
        #Deformation Mode
        self.particleterminator["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.particleterminator["render"] = ["default", "on", "off"]
        #Shape
        self.particleterminator["drawShape"] = ["default", "custom"]
        #Visible
        self.particleterminator["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Procedurals
        self.deferredmesh = {}  #Deferred Mesh
        #Deformation Mode
        self.deferredmesh["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.deferredmesh["render"] = ["default", "on", "off"]
        #Shape
        self.deferredmesh["drawShape"] = ["default", "custom"]
        #Visible
        self.deferredmesh["visible"] = ["default", "on", "off", "allOff"]
        
        self.gaskettoy = {}  #Fractel Gasket
        #Deformation Mode
        self.gaskettoy["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Gasket Type
        self.gaskettoy["type"] = ["squareHole", "squareFlake", "serpinski", "tetrahedron"]
        #Render
        self.gaskettoy["render"] = ["default", "on", "off"]
        #Shape
        self.gaskettoy["drawShape"] = ["default", "custom"]
        #Visible
        self.gaskettoy["visible"] = ["default", "on", "off", "allOff"]
        
        self.gear_dot_item = {}  #Gear
        #Deformation Mode
        self.gear_dot_item["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.gear_dot_item["render"] = ["default", "on", "off"]
        #Shape
        self.gear_dot_item["drawShape"] = ["default", "custom"]
        #Teeth Facing
        self.gear_dot_item["teeth_facing"] = ["FacingOutside", "FacingInside"]
        #Visible
        self.gear_dot_item["visible"] = ["default", "on", "off", "allOff"]
        
        self.proxy = {}  #Proxy
        #Deformation Mode
        self.proxy["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Preview Rendering
        self.proxy["previewRender"] = ["none", "preview", "render"]
        #Render
        self.proxy["render"] = ["default", "on", "off"]
        #Shape
        self.proxy["drawShape"] = ["default", "custom"]
        #Visible
        self.proxy["visible"] = ["default", "on", "off", "allOff"]
        
        self.item_dot_rock = {}  #Rock
        #Deformation Mode
        self.item_dot_rock["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Noise Type lvl1
        self.item_dot_rock["lvl1noisetype"] = ["Noise", "Cellular"]
        #Noise Type lvl2
        self.item_dot_rock["lvl2noisetype"] = ["Noise", "Cellular"]
        #Noise Type lvl3
        self.item_dot_rock["lvl3noisetype"] = ["Noise", "Cellular"]
        #Render
        self.item_dot_rock["render"] = ["default", "on", "off"]
        #Shape
        self.item_dot_rock["drawShape"] = ["default", "custom"]
        #Visible
        self.item_dot_rock["visible"] = ["default", "on", "off", "allOff"]
        
        self.rpc_dot_mesh = {}  #RPC Mesh
        #Deformation Mode
        self.rpc_dot_mesh["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.rpc_dot_mesh["render"] = ["default", "on", "off"]
        #Shape
        self.rpc_dot_mesh["drawShape"] = ["default", "custom"]
        #Visible
        self.rpc_dot_mesh["visible"] = ["default", "on", "off", "allOff"]
        
        self.sphere_dot_geometry = {}  #Sphere
        #Deformation Mode
        self.sphere_dot_geometry["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.sphere_dot_geometry["render"] = ["default", "on", "off"]
        #Shape
        self.sphere_dot_geometry["drawShape"] = ["default", "custom"]
        #Visible
        self.sphere_dot_geometry["visible"] = ["default", "on", "off", "allOff"]
        
        self.sdf_dot_item = {}  #SubDFusion
        #Deformation Mode
        self.sdf_dot_item["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Mesh Mode
        self.sphere_dot_geometry["OutputMeshMode"] = ["outModeWorking", "outModeAirtight", "outModeFinal", "outModeFinalParts"]
        #Render
        self.sdf_dot_item["render"] = ["default", "on", "off"]
        #Shape
        self.sdf_dot_item["drawShape"] = ["default", "custom"]
        #Visible
        self.sdf_dot_item["visible"] = ["default", "on", "off", "allOff"]
        
        self.sdfstrip_dot_item = {}  #SubDFusion Strip
        #Deformation Mode
        self.sdfstrip_dot_item["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.sdfstrip_dot_item["render"] = ["default", "on", "off"]
        #Shape
        self.sdfstrip_dot_item["drawShape"] = ["default", "custom"]
        #Visible
        self.sdfstrip_dot_item["visible"] = ["default", "on", "off", "allOff"]
        
       
##--------- Volumes
        self.blob = {}  #Blob
        #Deformation Mode
        self.blob["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.blob["render"] = ["default", "on", "off"]
        #Render Quality
        self.blob["renderQuality"] = ["low", "med", "high", "veryHigh", "best"]
        #Shape
        self.blob["drawShape"] = ["default", "custom"]
        #Visible
        self.blob["visible"] = ["default", "on", "off", "allOff"]
        
        self.gplane = {}  #Ground Plane
        #Deformation Mode
        self.gplane["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.gplane["render"] = ["default", "on", "off"]
        #Shape
        self.gplane["drawShape"] = ["default", "custom"]
        #Visible
        self.gplane["visible"] = ["default", "on", "off", "allOff"]
        
        self.renderbool = {}  #Render Boolean
        #Deformation Mode
        self.renderbool["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Particle Geometry
        self.renderbool["geoType"] = ["sphere", "cube", "cylinder", "cumulus"]
        #Render
        self.renderbool["render"] = ["default", "on", "off"]
        #Shape
        self.renderbool["drawShape"] = ["default", "custom"]
        #Visible
        self.renderbool["visible"] = ["default", "on", "off", "allOff"]
        
        self.sprite = {}  #Sprite
        #Deformation Mode
        self.sprite["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.sprite["render"] = ["default", "on", "off"]
        #Shape
        self.sprite["drawShape"] = ["default", "custom"]
        #Texture Effect
        self.sprite["textureFX"] = ["none", "vtrans", "expand", "expdis", "pyro"]
        #Visible
        self.sprite["visible"] = ["default", "on", "off", "allOff"]
        
        self.vdbvoxel = {}  #VDBVoxel
        #Deformation Mode
        self.vdbvoxel["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #filtMode
        self.vdbvoxel["filtMode"] = ["null", "mean", "gaussian", "median"]
        #Render
        self.vdbvoxel["render"] = ["default", "on", "off"]
        #Shape
        self.vdbvoxel["drawShape"] = ["default", "custom"]
        #Visible
        self.vdbvoxel["visible"] = ["default", "on", "off", "allOff"]
        
        self.volume = {}  #Volume
        #Deformation Mode
        self.volume["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Hypertexture Mode
        self.volume["htexMode"] = ["additive", "multiply"]
        #Particle Geometry
        self.volume["geoType"] = ["sphere", "cube", "cylinder", "cumulus"]
        #Render
        self.volume["render"] = ["default", "on", "off"]
        #Render Quality
        self.volume["renderQuality"] = ["low", "med", "high", "veryHigh", "best"]
        #Shadow Quality
        self.volume["shadowQuality"] = ["low", "med", "high", "veryHigh", "best"]
        #Shape
        self.volume["drawShape"] = ["default", "custom"]
        #Texture Effect
        self.volume["textureFX"] = ["none", "vtrans", "expand", "expdis", "pyro"]
        #Visible
        self.volume["visible"] = ["default", "on", "off", "allOff"]
        
        
##--------- Other
        self.beziernode = {}  #Bezier Node
        #Deformation Mode
        self.beziernode["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.beziernode["render"] = ["default", "on", "off"]
        #Shape
        self.beziernode["drawShape"] = ["default", "custom"]
        #Visible
        self.beziernode["visible"] = ["default", "on", "off", "allOff"]
        
        self.canvaspi = {}  #CanvasPI
        #Deformation Mode
        self.canvaspi["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.canvaspi["render"] = ["default", "on", "off"]
        #Shape
        self.canvaspi["drawShape"] = ["default", "custom"]
        #Visible
        self.canvaspi["visible"] = ["default", "on", "off", "allOff"]
        
        self.widget = {}  #ChannelHandle
        #Deformation Mode
        self.widget["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Handle Type
        self.widget["whType"] = ["disc", "square", "rectangle", "triangle", "arrow", "arrowCurve", "arrowSpin"]
        #Handle Draw Axis
        self.widget["whAxisDraw"] = ["x", "y", "z", "scrLR", "scrUD"]
        #Handle Nove Axis
        self.widget["whAxisMove"] = ["x", "y", "z"]
        #Render
        self.widget["render"] = ["default", "on", "off"]
        #Shape
        self.widget["drawShape"] = ["default", "custom"]
        #Visible
        self.widget["visible"] = ["default", "on", "off", "allOff"]
        
        self.surf_dot_sample = {}  #surf.sample
        #Deformation Mode
        self.surf_dot_sample["deformMode"] = ["world", "local", "rotYZ", "rotXZ", "rotXY"]
        #Render
        self.surf_dot_sample["render"] = ["default", "on", "off"]
        #Shape
        self.surf_dot_sample["drawShape"] = ["default", "custom"]
        #Visible
        self.surf_dot_sample["visible"] = ["default", "on", "off", "allOff"]
        
        


##################################################################################################
#                       Shader Tree                                                              #
##################################################################################################
        
##---------  Advanced Material
        self.advancedmaterial = {}
        #Blend Mode
        self.advancedmaterial["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Shading Model
        self.advancedmaterial["brdfType"] = ["blinn", "ashikhmin", "gtr"]
        #Reflection Type
        self.advancedmaterial["reflType"] = ["full", "environ"]
        
        
##---------  Environment Material
        self.Envmaterial = {}
        #Blend Mode
        self.Envmaterial["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Environment Type
        self.Envmaterial["type"] = ["constant", "grad2", "grad4", "overcast", "physical"]
        #Fog Type
        self.Envmaterial["fogType"] = ["none", "linear", "exp", "water", "layer"]
        
        
##---------  Light Material
        self.Lightmaterial = {}
        #Blend Mode
        self.Lightmaterial["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        


##---------  Custom Material
        self.material_dot_celedges = {} #Cel Edges Material
        #Blend Mode
        self.material_dot_celedges["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.material_dot_celshader = {}#Cel Material
        #Blend Mode
        self.material_dot_celshader["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
       
        self.material_dot_hairmaterial = {}# Hair Material
        #Blend Mode
        self.material_dot_hairmaterial["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Global Illumination
        self.material_dot_hairmaterial["gi"] = ["none", "recv", "cast", "both"]
       
        self.material_dot_halftone = {} #Halftone Material
        #Blend Mode
        self.material_dot_halftone["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Environment Type
        self.material_dot_halftone["cellPattern"] = ["dots", "lines", "crosshatch", "addaptive", "circle", "square", "diamond", "cross", "checker", "diamCheck"]
        #Fog Type
        self.material_dot_halftone["specPattern"] = ["dots", "lines", "crosshatch", "addaptive", "circle", "square", "diamond", "cross", "checker", "diamCheck"]
        
        self.material_dot_iridescence = {} #Iridescence Material
        #Blend Mode
        self.material_dot_iridescence["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Iridescence Mode
        self.material_dot_iridescence["iridescenceMode"] = ["interference", "diffraction"]
        
        self.material_dot_skinmaterial = {} #Skin Material
        #Blend Mode
        self.material_dot_skinmaterial["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.material_dot_thinfilm = {} # ThinFilm Material
        #Blend Mode
        self.material_dot_thinfilm["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        
##---------  Enhance: Modo Textures - Display
        self.val_dot_display_counter1_dot_rjj = {} #Counter 1
        #Blend Mode
        self.val_dot_display_counter1_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Base Type
        self.val_dot_display_counter1_dot_rjj["BaseType"] = ["Decimal", "Hexadecimal", "Octal", "Binary"]
        #Format Type
        self.val_dot_display_counter1_dot_rjj["FormatType"] = ["Counter", "Realtime Clock", "SMPTE 24", "SMPTE 25", "SMPTE 30"]
        
        self.val_dot_display_counter2_dot_rjj = {} #Counter2
        #Blend Mode
        self.val_dot_display_counter2_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Base Type
        self.val_dot_display_counter2_dot_rjj["BaseType"] = ["Decimal", "Hexadecimal", "Octal", "Binary"]
        #Format Type
        self.val_dot_display_counter2_dot_rjj["FormatType"] = ["Counter", "Realtime Clock", "SMPTE 24", "SMPTE 25", "SMPTE 30"]
        
        self.val_dot_display_uvleds_dot_rjj = {} #UV LEDs
        #Blend Mode
        self.val_dot_display_uvleds_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Shape Type
        self.val_dot_display_uvleds_dot_rjj["shapeType"] = ["Round", "Square"]
        

##---------  Enhance: Modo Textures - Geometric        
        self.val_dot_geometric_uvleds_dot_rjj = {} #Box
        #Blend Mode
        self.val_dot_geometric_uvleds_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_uvleds_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_circular_dot_rjj = {} #Circular
        #Blend Mode
        self.val_dot_geometric_circular_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_circular_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_corners_dot_rjj = {} #Corners
        #Blend Mode
        self.val_dot_geometric_corners_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_corners_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_cubic_dot_rjj = {} #Cubic
        #Blend Mode
        self.val_dot_geometric_cubic_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_cubic_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_dimples_dot_rjj = {} #Dimples
        #Blend Mode
        self.val_dot_geometric_dimples_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_dimples_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_grid_dot_rjj = {} #Grid
        #Blend Mode
        self.val_dot_geometric_grid_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_grid_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_iris_dot_rjj = {} #Iris
        #Blend Mode
        self.val_dot_geometric_iris_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_iris_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_linear_dot_rjj = {} #Linear
        #Blend Mode
        self.val_dot_geometric_linear_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_linear_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_polygon_dot_rjj = {} #Polygon
        #Blend Mode
        self.val_dot_geometric_polygon_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_polygon_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_radial_dot_rjj = {} #Radial
        #Blend Mode
        self.val_dot_geometric_radial_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_radial_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_rndlinear_dot_rjj = {} #Random Linear
        #Blend Mode
        self.val_dot_geometric_rndlinear_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_rndlinear_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        #Random Noise Type
        self.val_dot_geometric_rndlinear_dot_rjj["RandomType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_ring_dot_rjj = {} #Ring
        #Blend Mode
        self.val_dot_geometric_ring_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_ring_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_spiral_dot_rjj = {} #Spiral
        #Blend Mode
        self.val_dot_geometric_spiral_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_spiral_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_star_dot_rjj = {} #Star
        #Blend Mode
        self.val_dot_geometric_star_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_geometric_star_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        

##---------  Enhance: Modo Textures - Noise        
        self.val_dot_noise_agate_dot_rjj = {} #Agate
        #Blend Mode
        self.val_dot_noise_agate_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Disturb Noise Type
        self.val_dot_noise_agate_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_bozo_dot_rjj = {} #Bozo
        #Blend Mode
        self.val_dot_noise_bozo_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_bozo_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_cruddy_dot_rjj = {} #Cruddy
        #Blend Mode
        self.val_dot_noise_cruddy_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_cruddy_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_dented_dot_rjj = {} #dented
        #Blend Mode
        self.val_dot_noise_dented_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_dented_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_etched_dot_rjj = {} #etched
        #Blend Mode
        self.val_dot_noise_etched_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_etched_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_fBm_dot_rjj = {} #fBm
        #Blend Mode
        self.val_dot_noise_fBm_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_fBm_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_flowbozo_dot_rjj = {} #Flow Bozo
        #Blend Mode
        self.val_dot_noise_flowbozo_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_flowbozo_dot_rjj["FlowType"] = ["Flat", "Square", "Inverse"]
        
        self.val_dot_noise_granite_dot_rjj = {} #Granite
        #Blend Mode
        self.val_dot_noise_granite_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_granite_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_hybrid_dot_rjj = {} #Hybrid
        #Blend Mode
        self.val_dot_noise_hybrid_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_hybrid_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_lump_dot_rjj = {} #Lump
        #Blend Mode
        self.val_dot_noise_lump_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_lump_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_marblenoise_dot_rjj = {} #Marble Noise
        #Blend Mode
        self.val_dot_noise_marblenoise_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_marblenoise_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_marblevein_dot_rjj = {} #Marble NVeinoise
        #Blend Mode
        self.val_dot_noise_marblevein_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_marblevein_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_multifractal_dot_rjj = {} #Multi Fractal
        #Blend Mode
        self.val_dot_noise_multifractal_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_multifractal_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_pebbles_dot_rjj = {} #Pebbles
        #Blend Mode
        self.val_dot_noise_pebbles_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_pebbles_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_puffyclouds_dot_rjj = {} #Puffy Clouds
        #Blend Mode
        self.val_dot_noise_puffyclouds_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_puffyclouds_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_ridged_dot_rjj = {} #Ridged
        #Blend Mode
        self.val_dot_noise_ridged_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_ridged_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_scar_dot_rjj = {} #Scar
        #Blend Mode
        self.val_dot_noise_scar_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_scar_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_scruffed_dot_rjj = {} #Scruffed
        #Blend Mode
        self.val_dot_noise_scruffed_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_scruffed_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_strata_dot_rjj = {} #Strata
        #Blend Mode
        self.val_dot_noise_strata_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_strata_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_stucco_dot_rjj = {} #Stucco
        #Blend Mode
        self.val_dot_noise_stucco_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_stucco_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_vectorbozo_dot_rjj = {} #Vector Bozo
        #Blend Mode
        self.val_dot_noise_vectorbozo_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_vectorbozo_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_wrappedfbm_dot_rjj = {} #Wrapped fBm
        #Blend Mode
        self.val_dot_noise_wrappedfbm_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_noise_wrappedfbm_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        


##---------  Enhance: Modo Textures - Organic
        self.val_dot_organic_artdeco_dot_rjj = {} #Art Deco
        #Blend Mode
        self.val_dot_organic_artdeco_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_organic_blister_dot_rjj = {} #Blister
        #Blend Mode
        self.val_dot_organic_blister_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_organic_branches_dot_rjj = {} #Branches
        #Blend Mode
        self.val_dot_organic_branches_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_branches_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_caustic_dot_rjj = {} #Caustic
        #Blend Mode
        self.val_dot_organic_caustic_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_caustic_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.cellular = {} #Cellular
        #Blend Mode
        self.cellular["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.cellular["CellOrder"] = ["F1", "F2", "F3", "F4"]      
        
        self.val_dot_organic_cheesy_dot_rjj = {} #Cheesy
        #Blend Mode
        self.val_dot_organic_cheesy_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_cheesy_dot_rjj["CellOrder"] = ["F1", "F2", "F3", "F4"] 
        
        self.val_dot_organic_concrete_dot_rjj = {} #concrete
        #Blend Mode
        self.val_dot_organic_concrete_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_concrete_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_crackle_dot_rjj = {} #Crackle
        #Blend Mode
        self.val_dot_organic_crackle_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_organic_dirt_dot_rjj = {} #dirt
        #Blend Mode
        self.val_dot_organic_dirt_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_dirt_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_disturbed_dot_rjj = {} #Disturbed
        #Blend Mode
        self.val_dot_organic_disturbed_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_disturbed_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_easywood_dot_rjj = {} #Easy Wood
        #Blend Mode
        self.val_dot_organic_easywood_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_easywood_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_electric_dot_rjj = {} #Electric
        #Blend Mode
        self.val_dot_organic_electric_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_electric_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_fire_dot_rjj = {} #Fire
        #Blend Mode
        self.val_dot_organic_fire_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_fire_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_hardwood_dot_rjj = {} #Hardwood
        #Blend Mode
        self.val_dot_organic_hardwood_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_hardwood_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_membrane_dot_rjj = {} #Membrane
        #Blend Mode
        self.val_dot_organic_membrane_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_organic_minky_dot_rjj = {} #Minky
        #Blend Mode
        self.val_dot_organic_minky_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_minky_dot_rjj["CellOrder"] = ["F1", "F2", "F3", "F4"] 
        
        self.val_dot_organic_scatter_dot_rjj = {} #Scatter
        #Blend Mode
        self.val_dot_organic_scatter_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_scatter_dot_rjj["Shape"] = ["Spheres", "Cubes", "Diamonds"]
        
        self.val_dot_organic_sinblob_dot_rjj = {} #Sin Blog
        #Blend Mode
        self.val_dot_organic_sinblob_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_organic_veins_dot_rjj = {} #Veins
        #Blend Mode
        self.val_dot_organic_veins_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_veins_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_wires_dot_rjj = {} #Wires
        #Blend Mode
        self.val_dot_organic_wires_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
       
        self.val_dot_organic_wormvein_dot_rjj = {} #Worm Vein
        #Blend Mode
        self.val_dot_organic_wormvein_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_organic_wormvein_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
              
##---------  Enhance: Modo Textures - Panels
        self.val_dot_panels_peel_dot_rjj = {} #Peel
        #Blend Mode
        self.val_dot_panels_peel_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_panels_peel_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_plates_dot_rjj = {} #Plates
        #Blend Mode
        self.val_dot_panels_plates_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_panels_plates_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_rivetrust_dot_rjj = {} #Rivet Rust
        #Blend Mode
        self.val_dot_panels_rivetrust_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_panels_rivetrust_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_rivets_dot_rjj = {} #Rivets
        #Blend Mode
        self.val_dot_panels_rivets_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_panels_rivets_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_rust_dot_rjj = {} #Rust
        #Blend Mode
        self.val_dot_panels_rust_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_panels_rust_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_smear_dot_rjj = {} #Smear
        #Blend Mode
        self.val_dot_panels_smear_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_panels_smear_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        

##---------  Enhance: Modo Textures - Process
        self.val_dot_process_easygrad_dot_rjj = {} #Easy Gradient
        #Blend Mode
        self.val_dot_process_easygrad_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_process_regionalhsv_dot_rjj = {} #Regional HSV
        #Blend Mode
        self.val_dot_process_regionalhsv_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        

##---------  Enhance: Modo Textures - Skins
        self.val_dot_skins_camo_dot_rjj = {} #Camo
        #Blend Mode
        self.val_dot_skins_camo_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_camo_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_crumpled_dot_rjj = {} #Crunmpled
        #Blend Mode
        self.val_dot_skins_crumpled_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_crumpled_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_dinoskin_dot_rjj = {} #Dino Skin
        #Blend Mode
        self.val_dot_skins_dinoskin_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_dinoskin_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_disease_dot_rjj = {} #Disease
        #Blend Mode
        self.val_dot_skins_disease_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_disease_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_frogskin_dot_rjj = {} #Frog Skin
        #Blend Mode
        self.val_dot_skins_frogskin_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_frogskin_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_grainywood_dot_rjj = {} #Grainy Wood
        #Blend Mode
        self.val_dot_skins_grainywood_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_grainywood_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_leather_dot_rjj = {} #Leather
        #Blend Mode
        self.val_dot_skins_leather_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_leather_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_monster_dot_rjj = {} #Monster
        #Blend Mode
        self.val_dot_skins_monster_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_monster_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_pastella_dot_rjj = {} #Pastella
        #Blend Mode
        self.val_dot_skins_pastella_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_pastella_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_Peened_dot_rjj = {} #Peened
        #Blend Mode
        self.val_dot_skins_Peened_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_Peened_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_scratches_dot_rjj = {} #Scratches
        #Blend Mode
        self.val_dot_skins_scratches_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_skins_scratches_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        
##---------  Enhance: Modo Textures- Space
        self.val_dot_space_blast_dot_rjj = {} #Blast
        #Blend Mode
        self.val_dot_space_blast_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_blast_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_coriolis_dot_rjj = {} #Coriolis
        #Blend Mode
        self.val_dot_space_coriolis_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_coriolis_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_flare_dot_rjj = {} #Flare
        #Blend Mode
        self.val_dot_space_flare_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_flare_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_gasgiant_dot_rjj = {} #Gas Giant
        #Blend Mode
        self.val_dot_space_gasgiant_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_gasgiant_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_glint_dot_rjj = {} #Glint
        #Blend Mode
        self.val_dot_space_glint_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_glint_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_hurricane_dot_rjj = {} #Hurricane
        #Blend Mode
        self.val_dot_space_hurricane_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_hurricane_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_nurnies_dot_rjj = {} #Nurnies
        #Blend Mode
        self.val_dot_space_nurnies_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_nurnies_dot_rjj["CellOrder"] = ["F1", "F2", "F3", "F4"] 
        
        self.val_dot_space_planet_dot_rjj = {} #Planet
        #Blend Mode
        self.val_dot_space_planet_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_planet_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_planetclouds_dot_rjj = {} #Planet Clouds
        #Blend Mode
        self.val_dot_space_planetclouds_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_planetclouds_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_rings_dot_rjj = {} #Rings
        #Blend Mode
        self.val_dot_space_rings_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_rings_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_starfield_dot_rjj = {} #Star Field
        #Blend Mode
        self.val_dot_space_starfield_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_starfield_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_swirl_dot_rjj = {} #Swirl
        #Blend Mode
        self.val_dot_space_swirl_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_swirl_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_terra_dot_rjj = {} #Terra
        #Blend Mode
        self.val_dot_space_terra_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_space_terra_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_windows_dot_rjj = {} #Windows
        #Blend Mode
        self.val_dot_space_windows_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        

##---------  Enhance: Modo Textures - Tiles
        self.val_dot_tiles_basket_dot_rjj = {} #Basket
        #Blend Mode
        self.val_dot_tiles_basket_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_basket_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        #Weave Pattern Type
        self.val_dot_tiles_basket_dot_rjj["PatternType"] = ["Plain", "EndSatin", "Basket", "BackForth", "Blips", "Plaid1", "Steps", "Spots", "Plaid2", "Lockstep", "Rows", "Herringbone", "HalfBasket", "Quad", "Quad2", "Stripes", "Zigzag", "Zigzag2", "Zigzag3", "ZigStep", "Alternate", "Alternate2", "Circles", "Crosses", "Speckles", "Stripes"]
        
        self.val_dot_tiles_bathtile_dot_rjj = {} #Bath Tile
        #Blend Mode
        self.val_dot_tiles_bathtile_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_bathtile_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_bricks_dot_rjj = {} #Bricks
        #Blend Mode
        self.val_dot_tiles_bricks_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_bricks_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_checks_dot_rjj = {} #Checks
        #Blend Mode
        self.val_dot_tiles_checks_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_checks_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_cornerless_dot_rjj = {} #Cornerless
        #Blend Mode
        self.val_dot_tiles_cornerless_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_cornerless_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_cubes_dot_rjj = {} #Cubes
        #Blend Mode
        self.val_dot_tiles_cubes_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_cubes_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_dashline_dot_rjj = {} #Dash Line
        #Blend Mode
        self.val_dot_tiles_dashline_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_dashline_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_diamonddeck_dot_rjj = {} #Diamond Deck
        #Blend Mode
        self.val_dot_tiles_diamonddeck_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_diamonddeck_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_fishscales_dot_rjj = {} #Fish Scales
        #Blend Mode
        self.val_dot_tiles_fishscales_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_fishscales_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_hextile_dot_rjj = {} #Hex Tile
        #Blend Mode
        self.val_dot_tiles_hextile_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_hextile_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_lattice1_dot_rjj = {} #Lattice 1
        #Blend Mode
        self.val_dot_tiles_lattice1_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_lattice1_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_lattice2_dot_rjj = {} #Lattice 2
        #Blend Mode
        self.val_dot_tiles_lattice2_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_lattice2_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_lattice3_dot_rjj = {} #Lattice 3
        #Blend Mode
        self.val_dot_tiles_lattice3_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_lattice3_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_mosaic_dot_rjj = {} #Mosaic
        #Blend Mode
        self.val_dot_tiles_mosaic_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_mosaic_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_octtile_dot_rjj = {} #Oct Tile
        #Blend Mode
        self.val_dot_tiles_octtile_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_octtile_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_parquet_dot_rjj = {} #Parquet
        #Blend Mode
        self.val_dot_tiles_parquet_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_parquet_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_paving_dot_rjj = {} #Paving
        #Blend Mode
        self.val_dot_tiles_paving_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_paving_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        #Paving Shape
        self.val_dot_tiles_paving_dot_rjj["PavingShape"] = ["Square", "Hexagon", "Octagon", "Triangle", "Wedges"]
        #Paving Style
        self.val_dot_tiles_paving_dot_rjj["PavingStyle"] = ["Straight", "Crazy", "Ornate", "Uneven"]        
        
        self.val_dot_tiles_plaid_dot_rjj = {} #Plaid
        #Blend Mode
        self.val_dot_tiles_plaid_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_plaid_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_planks_dot_rjj = {} #Planks
        #Blend Mode
        self.val_dot_tiles_planks_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_planks_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_ribs_dot_rjj = {} #Ribs
        #Blend Mode
        self.val_dot_tiles_ribs_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_ribs_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_roundedtile_dot_rjj = {} #Rounded Tile
        #Blend Mode
        self.val_dot_tiles_roundedtile_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_roundedtile_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_shingles_dot_rjj = {} #Shingles
        #Blend Mode
        self.val_dot_tiles_shingles_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_shingles_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_spots_dot_rjj = {} #Spots
        #Blend Mode
        self.val_dot_tiles_spots_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_spots_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_tacos_dot_rjj = {} #Tacos
        #Blend Mode
        self.val_dot_tiles_tacos_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_tacos_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_tartan_dot_rjj = {} #Tartan
        #Blend Mode
        self.val_dot_tiles_tartan_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_tartan_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_tiler_dot_rjj = {} #Tiler
        #Blend Mode
        self.val_dot_tiles_tiler_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_tiler_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_trichecks_dot_rjj = {} #Tri Checks
        #Blend Mode
        self.val_dot_tiles_trichecks_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_trichecks_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_tritile_dot_rjj = {} #Tri Tile
        #Blend Mode
        self.val_dot_tiles_tritile_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_tritile_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_wall_dot_rjj = {} #Wall
        #Blend Mode
        self.val_dot_tiles_wall_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.val_dot_tiles_wall_dot_rjj["NoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        

##---------  Enhance: Modo Textures - Water
        self.val_dot_water_dripdrop_dot_rjj = {} #Drip Drop
        #Blend Mode
        self.val_dot_water_dripdrop_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_water_rain_dot_rjj = {} #rain
        #Blend Mode
        self.val_dot_water_rain_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_water_ripples_dot_rjj = {} #Ripples
        #Blend Mode
        self.val_dot_water_ripples_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_water_surf_dot_rjj = {} #Surf
        #Blend Mode
        self.val_dot_water_surf_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_water_waves_dot_rjj = {} #Waves
        #Blend Mode
        self.val_dot_water_waves_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_water_windywaves_dot_rjj = {} #Windy Waves
        #Blend Mode
        self.val_dot_water_windywaves_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Wave Noise Type
        self.val_dot_water_windywaves_dot_rjj["WaveNoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        #Wind Noise Type
        self.val_dot_water_windywaves_dot_rjj["WindNoiseType"] = ["Perlin", "EnhancedPerlin", "Gradient", "Value", "GradientValue", "Impulse", "Lattice", "Bubble"]
        

##---------  Enhance: Modo Textures - Waveforms
        self.val_dot_waveforms_biasgain_dot_rjj = {} #Bias Gain
        #Blend Mode
        self.val_dot_waveforms_biasgain_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_fresnel_dot_rjj = {} #Fresnel
        #Blend Mode
        self.val_dot_waveforms_fresnel_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_gamma_dot_rjj = {} #Gamma
        #Blend Mode
        self.val_dot_waveforms_gamma_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_gaussian_dot_rjj = {} #Gaussian
        #Blend Mode
        self.val_dot_waveforms_gaussian_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_impulse_dot_rjj = {} #Impulse
        #Blend Mode
        self.val_dot_waveforms_impulse_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_Noise_dot_rjj = {} #Noise
        #Blend Mode
        self.val_dot_Noise_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
                
        self.val_dot_waveforms_ramp_dot_rjj = {} #Ramp
        #Blend Mode
        self.val_dot_waveforms_ramp_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_rounded_dot_rjj = {} #Rounded
        #Blend Mode
        self.val_dot_waveforms_rounded_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_scurve_dot_rjj = {} #S-Curve
        #Blend Mode
        self.val_dot_waveforms_scurve_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_sawtooth_dot_rjj = {} #Sawtooth
        #Blend Mode
        self.val_dot_waveforms_sawtooth_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_scallop_dot_rjj = {} #Scallop
        #Blend Mode
        self.val_dot_waveforms_scallop_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_sine_dot_rjj = {} #Sine
        #Blend Mode
        self.val_dot_waveforms_sine_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_smooth_dot_rjj = {} #Smooth
        #Blend Mode
        self.val_dot_waveforms_smooth_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_smoothimpulse_dot_rjj = {} #Smooth Impulse
        #Blend Mode
        self.val_dot_waveforms_smoothimpulse_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_smoothsteps_dot_rjj = {} #Smooth Step
        #Blend Mode
        self.val_dot_waveforms_smoothsteps_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_waveforms_staircase_dot_rjj = {} #Staircase
        #Blend Mode
        self.val_dot_waveforms_staircase_dot_rjj["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
                

##---------  Image Map
        self.image_dot_gradfill = {} #Gradient Fill
        #Blend Mode
        self.image_dot_gradfill["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Shape
        self.image_dot_gradfill["shape"] = ["linear", "radial", "angular", "diamond"]
        
        self.imagemap = {} #Image Map
        #Alpha Channel
        self.imagemap["alpha"] = ["ignore", "use", "only"]
        #Blend Mode
        self.imagemap["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Channel
        self.imagemap["rgba"] = ["ignore", "use", "only", "red", "green", "blue"]
        #Texture Filtering
        self.imagemap["pixblend"] = ["nearest", "bilinear", "bicubic"]
        
        self.videosequence = {} #Video Sequence
        #Blend Mode
        self.videosequence["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #End Behavior
        self.videosequence["endBehavior"] = ["hold", "repeat", "pingpong"]
        
        self.videostill = {} #Video Still
        #Blend Mode
        self.videostill["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
       

##---------  Mask
        self.mask = {}
        #Blend Mode
        self.mask["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Noise Type
        self.mask["surfType"] = ["all", "surface", "fur"]
        

##---------  NPR Materials
        self.material_dot_dab = {} #Dab Material
        #Blend Mode
        self.material_dot_dab["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.material_dot_edgeink = {} #Edge Ink Material
        #Blend Mode
        self.material_dot_dab["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_noise_dot_gabor = {} #Gabor Noise
        #Blend Mode
        self.val_dot_noise_dot_gabor["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.material_dot_gooch = {} #Gooch Material
        #Blend Mode
        self.material_dot_gooch["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.material_dot_halftone2 = {} #Halftone2 Material
        #Blend Mode
        self.material_dot_halftone2["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Pattern
        self.material_dot_halftone2["cellPattern"] = ["dots", "lines", "crosshatch", "adaptive", "circle", "square", "diamond", "cross", "checker", "diamCheck"]
        #Specular Pattern
        self.material_dot_halftone2["specPattern"] = ["dots", "lines", "crosshatch", "adaptive", "circle", "square", "diamond", "cross", "checker", "diamCheck"]
        
        self.material_dot_sketchtone = {} #SketchTone Material
        #Blend Mode
        self.material_dot_sketchtone["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.material_dot_stipple = {} #Stipple Material
        #Blend Mode
        self.material_dot_stipple["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.material_dot_toon = {} #Toon Material
        #Blend Mode
        self.material_dot_dab["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        


##---------  Processing
        self.constant = {} #Constant
        #Blend Mode
        self.constant["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.gradient = {}#Gradient
        #Blend Mode
        self.gradient["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.occlusion = {}#Occlusion
        #Blend Mode
        self.occlusion["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Type
        self.occlusion["type"] = ["hemisphere", "up", "downSlope", "reflection", "concavity", "convexity", "both"]
        
        self.process = {}#Process
        #Blend Mode
        self.process["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.tensiontexture = {}#Tension Texture
        #Blend Mode
        self.tensiontexture["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Method
        self.tensiontexture["type"] = ["area", "angle"]
        
        self.variationtexture = {}#Variation Texture
        #Blend Mode
        self.variationtexture["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Type
        self.variationtexture["type"] = ["particle", "txtrParticle", "meshPart", "item"]
        
        self.wmaptexture = {}#Weight Map Texture
        #Blend Mode
        self.wmaptexture["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
                

##--------- Render
        self.polyRender = {}        
        #indirectSSS
        self.polyRender["globSubs"] = ["none", "giaffectsss", "sssaffectgi", "both"]
        #indirectCaustics
        self.polyRender["globCaus"] = ["none", "reflection", "refraction", "both"]
        #irradianceUsage
        self.polyRender["irrUsage"] = ["first", "second", "both"]
        #irradianceGradients
        self.polyRender["irrGrads"] = ["none", "rotation", "translation", "both"]
        #irradianceSamplingMethod
        self.polyRender["irrSample"] = ["jitter", "poisson"]
        #irradianceDataStructure
        self.polyRender["irrData"] = ["small", "fast"]
        #firstPrePassSpacing
        self.polyRender["irrStart"] = ["s2", "s4", "s8", "s16", "s32", "s64"]
        #lastPrePassSpacing
        self.polyRender["irrEnd"] = ["s2", "s4", "s8", "s16", "s32", "s64"]       
        #environmentMIS  
        self.polyRender["envMIS"] = ["none", "diffuse", "reflection", "both"]
        #directLightMIS
        self.polyRender["directMIS"] = ["none", "diffuse", "specular", "both"]
        #resolutionUnit
        self.polyRender["resUnit"] = ["pixels", "inches", "cm"]
        #renderType
        self.polyRender["rendType"] = ["auto", "scanline", "raytrace"]
        #antialiasing
        self.polyRender["aa"] = ["s2", "s4", "s8", "s16", "s32", "s64", "s128", "s256", "s512", "s1024"]
        #antialiasingFilter
        self.polyRender["aaFilter"] = ["box", "triangle", "gaussian", "catmull", "mitchell"]
        #fieldRendering
        self.polyRender["field"] = ["off", "upper", "lower"]
        #bucketOrder
        self.polyRender["bktOrder"] = ["rows", "columns", "spiral", "hilbert", "random"]        

##--------- Render Outputs
        self.renderOutput = {}
        #Blend Mode
        self.renderOutput["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Contours
        self.renderOutput["contour"] = ["none", "surface", "segment"]
        #Exposure Control
        self.renderOutput["expType"] = ["white", "photo"]
        #Tone Map Type
        self.renderOutput["toneMap"] = ["lum", "rgb"]
        
        
##---------  Shader Folder
        self.shaderfolder = {}
        #Blend Mode
        self.shaderfolder["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        
##---------  Special
        self.furmaterial = {} #Fur Material
        #Bend Direction
        self.furmaterial["bendDirection"] = ["down", "normal"]
        #Billboard
        self.furmaterial["billboard"] = ["off", "tree", "leaf", "feather"]
        #Blend Mode
        self.furmaterial["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Curl Type
        self.furmaterial["curlMode"] = ["curls", "waves"]
        #Guides
        self.furmaterial["guides"] = ["none", "clump", "normal", "dirlen", "shape", "range"]
        #Type
        self.furmaterial["type"] = ["strips", "cylinders"]
        
        self.matcapshader = {} #Matcap Shader
        #Blend Mode
        self.matcapshader["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.projectshader = {} #Projection Shader
        #Blend Mode
        self.projectshader["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.projecttexture = {} #Projection Texture
        #Blend Mode
        self.projecttexture["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.defaultshader = {} #Shader
        #Alpha Type
        self.defaultshader["alphaType"] = ["opacity", "constant", "shadow"]
        #Blend Mode
        self.defaultshader["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Indirect Illum Type
        self.defaultshader["indType"] = ["none", "mc", "ic"]
        #Fog Type
        self.defaultshader["fogType"] = ["none", "linear", "exp", "water", "layer"]
        #Light Linking Mode
        self.defaultshader["lightLink"] = ["include", "exclude"]
        
        self.surfgen = {} #Surface Generator
        #Blend Mode
        self.surfgen["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_wireframe = {} #Wireframe Texture
        #Blend Mode
        self.val_dot_wireframe["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        

##---------  Textures
        self.checker = {} #Checker
        #Blend Mode
        self.checker["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Type
        self.checker["type"] = ["square", "cube"]
        
        self.dots = {} #Dots
        #Blend Mode
        self.dots["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Type
        self.dots["type"] = ["square", "cube"]
        
        self.grid = {} #Grid
        #Blend Mode
        self.grid["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Type
        self.grid["type"] = ["line", "triangle", "square", "hexagon", "cube"]
        
        self.Noise = {} #Noise
        #Blend Mode
        self.Noise["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Type
        self.Noise["type"] = ["simple", "fractal", "turbulence"]
        
        self.val_dot_noise_poisson = {} #Poisson Cells
        #Blend Mode
        self.val_dot_noise_poisson["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Type
        self.val_dot_noise_poisson["type"] = ["square", "cube"]
        
        self.ripples = {} #Ripples
        #Blend Mode
        self.ripples["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.val_dot_rpctexture = {} #RPC Texture
        #Blend Mode
        self.val_dot_rpctexture["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Type
        self.val_dot_rpctexture["type"] = ["square", "cube"]
        
        self.val_dot_rtcurvature = {} #RT Curvature
        #Blend Mode
        self.val_dot_rtcurvature["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        #Grid Size
        self.val_dot_rtcurvature["gridSize"] = ["three", "five", "seven", "nine", "eleven"]
        
        self.weave = {} #Weave
        #Blend Mode
        self.weave["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
        self.wood = {} #Wood
        #Blend Mode
        self.wood["blend"] = ["normal", "add", "subtract", "difference", "normalmult", "divide", "multiply", "screen", "overlay", "softlight", "hardlight", "darken", "lighten", "colordodge", "colorburn"]
        
####################################################################################################
# Utilities
#####################################################################################################
    def swap_dot(self, var, flip=0):
        if flip == 0:
            return var.replace("_dot_", ".")
        else:
            return var.replace(".", "_dot_")
        
        
        
        
        
        
        
        
        
        