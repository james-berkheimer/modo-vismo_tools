#!/usr/bin/env python
import lx
lx.out("Channel Option Labels Class")

class ChannelOptionLabels(object):
    def __init__(self):
        
##################################################################################################
#                       Item List                                                                #
##################################################################################################
        
##--------- Backdrop Item
        self.backdrop = {} #Backdrop Item
        #Deformation Mode
        self.backdrop["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]        
        #Projection Type
        self.backdrop["projection"] = ["Top", "Bottom", "Back", "Front", "Right", "Left", "Camera"]       
        #Render
        self.backdrop["render"] = ["Default", "Yes", "No"]
        #Shape
        self.backdrop["drawShape"] = ["Default", "Custom"]       
        #Visible
        self.backdrop["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Camera
        self.camera = {} #Camera
        #Deformation Mode
        self.camera["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]        
        #Film Fit
        self.camera["filmFit"] = ["Fill", "Horizontal", "Verticle", "Overscan"]
        #Projection Type
        self.camera["projType"] = ["Perspective", "Orthographic", "Cylindrical Map", "Cylindrical VR", "Spherical Map", "Spherical VR"]       
        #Render
        self.camera["render"] = ["Default", "Yes", "No"]
        #Shape
        self.camera["drawShape"] = ["Default", "Custom"]       
        #Stereo Composite
        self.camera["stereoComp"] = ["(none)", "Anaglyph Red-Cyan", "Anaglyph Red-Cyan Half Color", "Anaglyph Red-Cyan Optimized", "Anaglyph Red-Blue Least Squares", "Side-by-Side", "Side-by-Side Full Width", "Side-by-Side Cross-eyed", "Side-by-Side Cross-eyed Full Width"]
        #Stereo Eyes
        self.camera["stereoEye"] = ["Left", "Right", "Both"]
        #Visible
        self.camera["visible"] = ["Default", "Yes", "No", "allOff"]
        

##--------- Locator
        self.groupLocator = {} #Group Locator
        #Deformation Mode
        self.groupLocator["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]        
        #Render
        self.groupLocator["render"] = ["Default", "Yes", "No"]
        #Shape
        self.groupLocator["drawShape"] = ["Default", "Custom"]       
        #Space
        self.groupLocator["space"] = ["(none)", "2D", "3D"]
        #Visible
        self.groupLocator["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.locator = {} #Locator
        #Deformation Mode
        self.locator["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]        
        #Render
        self.locator["render"] = ["Default", "Yes", "No"]
        #Shape
        self.locator["drawShape"] = ["Default", "Custom"]       
        #Space
        self.locator["space"] = ["(none)", "2D", "3D"]
        #Visible
        self.locator["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.txtrlocator = {}  #Texture Locator
        #Deformation Mode
        self.txtrlocator["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]        
        #Falloff Type
        self.txtrlocator["fallType"] = ["Cubic", "Spherical", "Linear X", "Linear Y", "Linear Z"]
        #Horizontal Repeat
        self.txtrlocator["tileU"] = ["Reset", "Repeat", "Mirror", "Edge"]
        #Projection Type
        self.txtrlocator["projType"] = ["Solid", "Planar", "Cylindrical", "Spherical", "Cubic", "Front Projection", "UV Map", "Light Probe", "Implicit UV", "Box"]
        #Random Texture Offsets
        self.txtrlocator["randOffset"] = ["(none)", "Particles and Replicas", "Mesh Parts", "Surfaces"]
        #Render
        self.txtrlocator["render"] = ["Default", "Yes", "No"]
        #Shape
        self.txtrlocator["drawShape"] = ["Default", "Custom"]
        #Tangent Vecotr Type
        self.txtrlocator["tngtType"] = ["dPdu, dPdv", "dPdu, Cross Product"]
        #Vertical Repeat
        self.txtrlocator["tileV"] = ["Reset", "Repeat", "Mirror", "Edge"]
        #Visible
        self.txtrlocator["visible"] = ["Default", "Yes", "No", "allOff"]     

##--------- Mesh
        self.mesh = {} #Mesh
        #Curve Radius Unit
        self.mesh["radUnit"] = ["Meters", "Pixels"]
        #Deformation Mode
        self.mesh["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Fill
        self.mesh["fillOptions"] = ["Default", "User", "Background Light", "Background Dark"]
        #Render
        self.mesh["render"] = ["Default", "Yes", "No"]
        #Shape
        self.mesh["drawShape"] = ["Default", "Wireframe", "Vector Map", "Solid", "Shaded"]
        #Style
        self.mesh["style"] = ["Default", "Custom"]
        #Texture
        self.mesh["texture"] = ["Off", "Texture", "Shaded"]
        #Visible
        self.mesh["visible"] = ["Default", "Yes", "No", "allOff"]
        #Wireframe
        self.mesh["wireOptions"] = ["Default", "User", "Background Light", "Background Dark"]
        
        
        
##--------- Deformers
        self.deform_dot_bend = {} #Bend Effector
        #Deformation Mode
        self.deform_dot_bend["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.deform_dot_bend["render"] = ["Default", "Yes", "No"]
        #Shape
        self.deform_dot_bend["drawShape"] = ["Default", "Custom"]
        #Visible
        self.deform_dot_bend["visible"] = ["Default", "Yes", "No", "allOff"]        
        
        self.deform_dot_crvconst = {} #Curve Constrait Effector
        #Deformation Mode
        self.deform_dot_crvconst["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.deform_dot_crvconst["render"] = ["Default", "Yes", "No"]
        #Shape
        self.deform_dot_crvconst["drawShape"] = ["Default", "Custom"]
        #Visible
        self.deform_dot_crvconst["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.geninfluence = {}  #General Influence
        #Interpolation
        self.geninfluence["interpolation"] = ["Parametric", "Linear"]
        #Type
        self.geninfluence["type"] = ["Entire Mesh", "Weight Map", "Vertex Selection Set", "Material", "Part", "Polygon Selection Set"]
        
        self.iteminfluence = {}  #Item Influence
        #Interpolation
        self.iteminfluence["interpolation"] = ["Parametric", "Linear"]
                
        self.deform_dot_lag = {}  #Lag Effector
        #Deformation Mode
        self.deform_dot_lag["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.deform_dot_lag["render"] = ["Default", "Yes", "No"]
        #Shape
        self.deform_dot_lag["drawShape"] = ["Default", "Custom"]
        #Visible
        self.deform_dot_lag["visible"] = ["Default", "Yes", "No", "allOff"]        
        
        self.deform_dot_lattice = {}  #Lattice Effector
        #Deformation Mode
        self.deform_dot_lattice["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.deform_dot_lattice["render"] = ["Default", "Yes", "No"]
        #Shape
        self.deform_dot_lattice["drawShape"] = ["Default", "Custom"]
        #Visible
        self.deform_dot_lattice["visible"] = ["Default", "Yes", "No", "allOff"]        
        
        self.deform_dot_magnet = {}  #Magnet Effector
        #Deformation Mode
        self.deform_dot_magnet["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.deform_dot_magnet["render"] = ["Default", "Yes", "No"]
        #Shape
        self.deform_dot_magnet["drawShape"] = ["Default", "Custom"]
        #Shape
        self.deform_dot_magnet["magnetShape"] = ["Planar", "Spherical", "Cylindrical"]
        #Visible
        self.deform_dot_magnet["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.deformmdd2 = {}  #MDD Influence
        #End Behavior
        self.deformmdd2["endBehavior"] = ["Stop", "Repeat", "Mirror"]
                
        self.morphdeform = {}  #Morph Influence
        #Deformation Mode
        self.morphdeform["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.morphdeform["render"] = ["Default", "Yes", "No"]
        #Shape
        self.morphdeform["drawShape"] = ["Default", "Custom"]
        #Visible
        self.morphdeform["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.deformgroup = {}  #Normalizing Folder
        #Interpolation
        self.deformgroup["interpolation"] = ["Parametric", "Linear"]
                
        self.softlag = {}  #Soft Lag
        #Deformation Mode
        self.softlag["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.softlag["render"] = ["Default", "Yes", "No"]
        #Shape
        self.softlag["drawShape"] = ["Default", "Custom"]
        #Visible
        self.softlag["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.deform_dot_vortex = {}  #Vortex Effector
        #Deformation Mode
        self.deform_dot_vortex["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.deform_dot_vortex["render"] = ["Default", "Yes", "No"]
        #Shape
        self.deform_dot_vortex["drawShape"] = ["Default", "Custom"]
        #Visible
        self.deform_dot_vortex["visible"] = ["Default", "Yes", "No", "allOff"]
                
        self.weightcontainer = {}  #Weight Container
        #Deformation Mode
        self.weightcontainer["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.weightcontainer["render"] = ["Default", "Yes", "No"]
        #Shape
        self.weightcontainer["drawShape"] = ["Default", "Custom"]
        #Visible
        self.weightcontainer["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Dynamics
        self.collisionemitter = {}  #Collision Emitter
        #Deformation Mode
        self.collisionemitter["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.collisionemitter["render"] = ["Default", "Yes", "No"]
        #reType
        self.collisionemitter["reType"] = ["random", "uniform"]
        #Shape
        self.collisionemitter["drawShape"] = ["Default", "Custom"]        
        #Visible
        self.collisionemitter["visible"] = ["Default", "Yes", "No", "allOff"]        
        
        self.dynamicsconstraintmodifier = {}  #Constraint Modifier
        #Constraint Type
        self.dynamicsconstraintmodifier["constraintType"] = ["consPin", "consPoint"]
        #Deformation Mode
        self.dynamicsconstraintmodifier["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
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
        self.dynamicsconstraintmodifier["drawShape"] = ["Default", "Custom"]
        #Visible
        self.dynamicsconstraintmodifier["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.dynamic_dot_replicatorfilter = {}  #Dynamic Replicator
        #Constraint Type
        self.dynamic_dot_replicatorfilter["constraintType"] = ["consPin", "consPoint"]
        #Deformation Mode
        self.dynamic_dot_replicatorfilter["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #reCollisionShape
        self.dynamic_dot_replicatorfilter["reCollisionShape"] = ["bbox", "sphere", "hull", "multiHull", "mesh", "deformingMesh", "convexDecomposition", "plane"]
        #reMassSource
        self.dynamic_dot_replicatorfilter["reMassSource"] = ["worldDensity", "localDensity", "localMass"]
        #reState
        self.dynamic_dot_replicatorfilter["reState"] = ["dynamic", "kinematic"]
        #Shape
        self.dynamic_dot_replicatorfilter["drawShape"] = ["Default", "Custom"]
        #Visible
        self.dynamic_dot_replicatorfilter["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.conshinge = {}  #Hinge
        #Deformation Mode
        self.conshinge["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.conshinge["render"] = ["Default", "Yes", "No"]
        #Shape
        self.conshinge["drawShape"] = ["Default", "Custom"]
        #Visible
        self.conshinge["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.particlesim = {}  #Particle Simulation
        #Deformation Mode
        self.particlesim["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.particlesim["render"] = ["Default", "Yes", "No"]
        #Shape
        self.particlesim["drawShape"] = ["Default", "Custom"]
        #Visible
        self.particlesim["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.conspin = {}  #Pin
        #Deformation Mode
        self.conspin["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.conspin["render"] = ["Default", "Yes", "No"]
        #Shape
        self.conspin["drawShape"] = ["Default", "Custom"]
        #Visible
        self.conspin["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.conspoint = {}  #Point
        #Deformation Mode
        self.conspoint["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.conspoint["render"] = ["Default", "Yes", "No"]
        #Shape
        self.conspoint["drawShape"] = ["Default", "Custom"]
        #Visible
        self.conspoint["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.proceduralshatteritem = {}  #Procedural Shatter
        #Deformation Mode
        self.proceduralshatteritem["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Pattern
        self.proceduralshatteritem["shatterPatern"] = ["uniform", "impact", "radial"]
        #reImpulseOn
        self.proceduralshatteritem["reImplulseOn"] = ["off", "onWake", "continuous"]
        #Render
        self.proceduralshatteritem["render"] = ["Default", "Yes", "No"]
        #Shape
        self.proceduralshatteritem["drawShape"] = ["Default", "Custom"]
        #Split Islands
        self.proceduralshatteritem["splitIslands"] = ["never", "initial", "afterInitial", "always"]
        #Visible
        self.proceduralshatteritem["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.consslidehinge = {}  #Slide Hinge
        #Deformation Mode
        self.consslidehinge["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.consslidehinge["render"] = ["Default", "Yes", "No"]
        #Shape
        self.consslidehinge["drawShape"] = ["Default", "Custom"]
        #Visible
        self.consslidehinge["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.consspring = {}  #Spring
        #Deformation Mode
        self.consspring["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.consspring["render"] = ["Default", "Yes", "No"]
        #Shape
        self.consspring["drawShape"] = ["Default", "Custom"]
        #Visible
        self.consspring["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.solver = {}  #Solver
        #Deformation Mode
        self.solver["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.solver["render"] = ["Default", "Yes", "No"]
        #Shape
        self.solver["drawShape"] = ["Default", "Custom"]
        #Visible
        self.solver["visible"] = ["Default", "Yes", "No", "allOff"]
        

##--------- Falloffs
        self.falloff_dot_bezier = {}  #Bezier Falloff
        #Axial Shape
        self.falloff_dot_bezier["axialDecayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Deformation Mode
        self.falloff_dot_bezier["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]        
        #Falloff Shape
        self.falloff_dot_bezier["decayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Render
        self.falloff_dot_bezier["render"] = ["Default", "Yes", "No"]
        #Shape
        self.falloff_dot_bezier["drawShape"] = ["Default", "Custom"]
        #Visible
        self.falloff_dot_bezier["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.falloff_dot_capsule = {}  #Capsule Falloff
        #Decay Shape
        self.falloff_dot_capsule["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.falloff_dot_capsule["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.falloff_dot_capsule["render"] = ["Default", "Yes", "No"]
        #Shape
        self.falloff_dot_capsule["drawShape"] = ["Default", "Custom"]
        #Visible
        self.falloff_dot_capsule["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.falloff_dot_linear = {}  #Linear Falloff
        #Decay Shape
        self.falloff_dot_linear["decayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Deformation Mode
        self.falloff_dot_linear["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.falloff_dot_linear["render"] = ["Default", "Yes", "No"]
        #Shape
        self.falloff_dot_linear["drawShape"] = ["Default", "Custom"]
        #Visible
        self.falloff_dot_linear["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.falloff_dot_radial = {}  #Radial Falloff
        #Decay Shape
        self.falloff_dot_radial["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.falloff_dot_radial["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.falloff_dot_radial["render"] = ["Default", "Yes", "No"]
        #Shape
        self.falloff_dot_radial["drawShape"] = ["Default", "Custom"]
        #Visible
        self.falloff_dot_radial["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.falloff_dot_spline = {}  #Spline Falloff
        #Axial Shape
        self.falloff_dot_spline["axialDecayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Deformation Mode
        self.falloff_dot_spline["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Shape
        self.falloff_dot_spline["decayMode"] = ["linear", "easeIn", "easeOut", "smooth"]
        #Render
        self.falloff_dot_spline["render"] = ["Default", "Yes", "No"]
        #Shape
        self.falloff_dot_spline["drawShape"] = ["Default", "Custom"]
        #Visible
        self.falloff_dot_spline["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Forces
        self.force_dot_curve = {}  #Curve Force
        #Decay Shape
        self.force_dot_curve["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.force_dot_curve["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.force_dot_curve["render"] = ["Default", "Yes", "No"]
        #Shape
        self.force_dot_curve["drawShape"] = ["Default", "Custom"]
        #Visible
        self.force_dot_curve["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.force_dot_drag = {}  #Drag Force
        #Decay Shape
        self.force_dot_drag["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.force_dot_drag["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.force_dot_drag["render"] = ["Default", "Yes", "No"]
        #Shape
        self.force_dot_drag["drawShape"] = ["Default", "Custom"]
        #Visible
        self.force_dot_drag["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.force_dot_linear = {}  #Linear Force
        #Decay Shape
        self.force_dot_linear["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.force_dot_linear["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.force_dot_linear["render"] = ["Default", "Yes", "No"]
        #Shape
        self.force_dot_linear["drawShape"] = ["Default", "Custom"]
        #Visible
        self.force_dot_linear["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.force_dot_newton = {}  #Newton Force
        #Decay Shape
        self.force_dot_newton["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.force_dot_newton["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.force_dot_newton["render"] = ["Default", "Yes", "No"]
        #Shape
        self.force_dot_newton["drawShape"] = ["Default", "Custom"]
        #Visible
        self.force_dot_newton["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.particlesim = {}  #Particle Simulation
        #Decay Shape
        self.particlesim["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.particlesim["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.particlesim["render"] = ["Default", "Yes", "No"]
        #Shape
        self.particlesim["drawShape"] = ["Default", "Custom"]
        #Visible
        self.particlesim["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.force_dot_radial = {}  #Radial Force
        #Decay Shape
        self.force_dot_radial["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.force_dot_radial["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.force_dot_radial["render"] = ["Default", "Yes", "No"]
        #Shape
        self.force_dot_radial["drawShape"] = ["Default", "Custom"]
        #Visible
        self.force_dot_radial["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.force_dot_turbulence = {}  #Turbulence Force
        #Decay Shape
        self.force_dot_turbulence["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.force_dot_turbulence["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.force_dot_turbulence["render"] = ["Default", "Yes", "No"]
        #Shape
        self.force_dot_turbulence["drawShape"] = ["Default", "Custom"]
        #Visible
        self.force_dot_turbulence["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.force_dot_vortex = {}  #Vortex Force
        #Decay Shape
        self.force_dot_vortex["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.force_dot_vortex["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.force_dot_vortex["render"] = ["Default", "Yes", "No"]
        #Shape
        self.force_dot_vortex["drawShape"] = ["Default", "Custom"]
        #Visible
        self.force_dot_vortex["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.force_dot_wind = {}  #Wind Force
        #Decay Shape
        self.force_dot_wind["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.force_dot_wind["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.force_dot_wind["render"] = ["Default", "Yes", "No"]
        #Shape
        self.force_dot_wind["drawShape"] = ["Default", "Custom"]
        #Visible
        self.force_dot_wind["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Lights
        self.arealight = {}  #Area Light
        #Decay Shape
        self.arealight["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.arealight["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Type
        self.arealight["fallType"] = ["None", "Inverse Distance", "Inverse Distance Squared"]
        #Mode
        self.arealight["linkMode"] = ["Include", "Exclude"]        
        #Render
        self.arealight["render"] = ["Default", "Yes", "No"]
        #Shadow Type
        self.arealight["shadType"] = ["None", "Ray Trace", "Deep Shadow Map"]
        #Shape
        self.arealight["drawShape"] = ["Default", "Custom"]
        #Shape
        self.arealight["shape"] = ["Rectangle", "Elipse"]
        #Visible
        self.arealight["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.cylinderlight = {}  #Cylinder Light
        #Decay Shape
        self.cylinderlight["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.cylinderlight["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Type
        self.cylinderlight["fallType"] = ["None", "Inverse Distance", "Inverse Distance Squared"]
        #Mode
        self.cylinderlight["linkMode"] = ["Include", "Exclude"]         
        #Render
        self.cylinderlight["render"] = ["Default", "Yes", "No"]
        #Shadow Type
        self.cylinderlight["shadType"] = ["None", "Ray Trace", "Deep Shadow Map"]
        #Shape
        self.cylinderlight["drawShape"] = ["Default", "Custom"]
        #Visible
        self.cylinderlight["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.sunlight = {}  #Directional Light
        #Clamp Intensity
        self.sunlight["clamp"] = ["None", "Clamp", "Replace"]
        #Decay Shape
        self.sunlight["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.sunlight["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Type
        self.sunlight["fallType"] = ["None", "Inverse Distance", "Inverse Distance Squared"]
        #Mode
        self.sunlight["linkMode"] = ["Include", "Exclude"]           
        #Render
        self.sunlight["render"] = ["Default", "Yes", "No"]
        #Shadow Type
        self.sunlight["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Shape
        self.sunlight["drawShape"] = ["Default", "Custom"]
        #Visible
        self.sunlight["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.domelight = {}  #Dome Light
        #Decay Shape
        self.domelight["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.domelight["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Type
        self.domelight["fallType"] = ["None", "Inverse Distance", "Inverse Distance Squared"]
        #Mode
        self.domelight["linkMode"] = ["Include", "Exclude"]         
        #Render
        self.domelight["render"] = ["Default", "Yes", "No"]
        #Shadow Type
        self.domelight["shadType"] = ["None", "Ray Trace", "Deep Shadow Map"]
        #Shape
        self.domelight["drawShape"] = ["Default", "Custom"]
        #Visible
        self.domelight["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.photometrylight = {}  #Photometric Light
        #Decay Shape
        self.photometrylight["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.photometrylight["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Type
        self.photometrylight["fallType"] = ["None", "Inverse Distance", "Inverse Distance Squared"]
        #Mode
        self.photometrylight["linkMode"] = ["Include", "Exclude"]         
        #Render
        self.photometrylight["render"] = ["Default", "Yes", "No"]
        #Shadow Type
        self.photometrylight["shadType"] = ["None", "Ray Trace", "Deep Shadow Map"]
        #Shape
        self.photometrylight["drawShape"] = ["Default", "Custom"]
        #Visible
        self.photometrylight["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pointlight = {}  #Poinr Light
        #Decay Shape
        self.pointlight["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.pointlight["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Type
        self.pointlight["fallType"] = ["None", "Inverse Distance", "Inverse Distance Squared"]
        #Mode
        self.pointlight["linkMode"] = ["Include", "Exclude"]         
        #Render
        self.pointlight["render"] = ["Default", "Yes", "No"]
        #Shadow Type
        self.pointlight["shadType"] = ["None", "Ray Trace", "Deep Shadow Map"]
        #Shape
        self.pointlight["drawShape"] = ["Default", "Custom"]
        #Visible
        self.pointlight["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.portal = {}  #Portal Light
        #Decay Shape
        self.portal["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.portal["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Type
        self.portal["fallType"] = ["None", "Inverse Distance", "Inverse Distance Squared"]
        #Mode
        self.portal["linkMode"] = ["Include", "Exclude"]        
        #Render
        self.portal["render"] = ["Default", "Yes", "No"]
        #Shadow Type
        self.portal["shadType"] = ["None", "Ray Trace", "Deep Shadow Map"]
        #Shape
        self.portal["drawShape"] = ["Default", "Custom"]
        #Shape
        self.portal["shape"] = ["Rectangle", "Elipse"]
        #Visible
        self.portal["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.spotlight = {}  #Spot Light
        #Decay Shape
        self.spotlight["decayMode"] = ["Smooth", "Inverse Power", "Gaussian"]
        #Deformation Mode
        self.spotlight["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Falloff Type
        self.spotlight["fallType"] = ["None", "Inverse Distance", "Inverse Distance Squared"]
        #Mode
        self.spotlight["linkMode"] = ["Include", "Exclude"]         
        #Render
        self.spotlight["render"] = ["Default", "Yes", "No"]
        #Shadow Type
        self.spotlight["shadType"] = ["None", "Ray Trace", "Deep Shadow Map"]
        #Shape
        self.spotlight["drawShape"] = ["Default", "Custom"]
        #Visible
        self.spotlight["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Mootzoid
        self.emPolygonizer5 = {}  #emPolygonizer5
        #Deformation Mode
        self.emPolygonizer5["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
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
        self.emPolygonizer5["render"] = ["Default", "Yes", "No"]
        #Shape
        self.emPolygonizer5["drawShape"] = ["Default", "Custom"]
        #Visible
        self.emPolygonizer5["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.emReader = {}  #emReader
        #Deformation Mode
        self.emReader["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #emRd_flFormat
        self.emReader["emRd_flFormat"] = ["Mootzoid_mzd", "emPolygonizer2_emp2", "Wavefront_obj", "RealFlow_bin"]
        #emRd_flIndexMode
        self.emReader["emRd_flIndexMode"] = ["Use_Idx_Value_Round", "Use_Idx_Value_Floor", "Use_Idx_Value_Cell"]
        #emRd_fxTriangulate
        self.emReader["emRd_fxTriangulate"] = ["off", "Concave_Polygons", "All_Polygons"]
        #emRd_vpDisplay
        self.emReader["emRd_vpDisplay"] = ["None", "Points", "Edges"]
        #Render
        self.emReader["render"] = ["Default", "Yes", "No"]
        #Shape
        self.emReader["drawShape"] = ["Default", "Custom"]
        #Visible
        self.emReader["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Particles
        self.replicator = {}  #Replicator
        #Deformation Mode
        self.replicator["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.replicator["render"] = ["Default", "Yes", "No"]
        #Shape
        self.replicator["drawShape"] = ["Default", "Custom"]
        #Source Mode
        self.replicator["source"] = ["Point Data", "Align to Surface", "Use Polygons", "Use Particles"]
        #Visible
        self.replicator["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Particles - Modifiers
        self.pmod_dot_audio = {}  #Particle Audio Modifier
        #Color Mode
        self.pmod_dot_audio["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_audio["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Dissolve Mode
        self.pmod_dot_audio["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_audio["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_audio["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_audio["render"] = ["Default", "Yes", "No"]
        #Shape
        self.pmod_dot_audio["drawShape"] = ["Default", "Custom"]
        #Visible
        self.pmod_dot_audio["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pmod_dot_expression = {}  #Particle Expression Modifier
        #Color Mode
        self.pmod_dot_expression["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_expression["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Dissolve Mode
        self.pmod_dot_expression["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_expression["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_expression["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_expression["render"] = ["Default", "Yes", "No"]
        #Shape
        self.pmod_dot_expression["drawShape"] = ["Default", "Custom"]
        #Visible
        self.pmod_dot_expression["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pmod_dot_audio = {}  #Particle Audio Modifier
        #Color Mode
        self.replicator["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.replicator["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Dissolve Mode
        self.replicator["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.replicator["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.replicator["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.replicator["render"] = ["Default", "Yes", "No"]
        #Shape
        self.replicator["drawShape"] = ["Default", "Custom"]
        #Visible
        self.replicator["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pmod_dot_lookat = {}  #Particle Look At Modifier
        #Deformation Mode
        self.pmod_dot_lookat["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Mesh Source
        self.pmod_dot_lookat["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_lookat["render"] = ["Default", "Yes", "No"]
        #Shape
        self.pmod_dot_lookat["drawShape"] = ["Default", "Custom"]
        #Target
        self.pmod_dot_lookat["target"] = ["thisLocator", "nextParticle", "previousParticle", "camera"]
        #Visible
        self.pmod_dot_lookat["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pmod_dot_basic = {}  #Particle Modifier
        #Color Mode
        self.pmod_dot_basic["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_basic["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Dissolve Mode
        self.pmod_dot_basic["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_basic["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_basic["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_basic["render"] = ["Default", "Yes", "No"]
        #Shape
        self.pmod_dot_basic["drawShape"] = ["Default", "Custom"]
        #Visible
        self.pmod_dot_basic["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pmod_dot_random = {}  #Particle Random Modifier
        #Color Mode
        self.pmod_dot_random["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_random["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Dissolve Mode
        self.pmod_dot_random["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_random["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_random["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_random["render"] = ["Default", "Yes", "No"]
        #Shape
        self.pmod_dot_random["drawShape"] = ["Default", "Custom"]
        #Visible
        self.pmod_dot_random["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pmod_dot_sieve = {}  #Particle Sieve Modifier
        #Condition
        self.pmod_dot_sieve["condition"] = ["pID", "posX", "posY", "posZ", "velX", "velY", "velZ", "frcX", "frcY", "frcZ", "clrX", "clrY", "clrZ", "lum", "diss", "rate", "age", "mass", "size", "path", "falloff", "particleSource", "slope", "map"]
        #Deformation Mode
        self.pmod_dot_sieve["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #If
        self.pmod_dot_sieve["feature"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_sieve["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_sieve["render"] = ["Default", "Yes", "No"]
        #Shape
        self.pmod_dot_sieve["drawShape"] = ["Default", "Custom"]
        #Visible
        self.pmod_dot_sieve["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pmod_dot_step = {}  #Particle Step Modifier
        #Color Mode
        self.pmod_dot_step["pColorMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Deformation Mode
        self.pmod_dot_step["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Dissolve Mode
        self.pmod_dot_step["pDissMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Luminance Mode
        self.pmod_dot_step["pLumMode"] = ["off", "normal", "add", "subtract", "multiply", "average"]
        #Mesh Source
        self.pmod_dot_step["usePol"] = ["verts", "polys", "detachedVerts"]
        #Render
        self.pmod_dot_step["render"] = ["Default", "Yes", "No"]
        #Shape
        self.pmod_dot_step["drawShape"] = ["Default", "Custom"]
        #Visible
        self.pmod_dot_step["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Particles - Point Clouds
        self.csvcache = {}  #CSV Point Cache
        #Deformation Mode
        self.csvcache["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.csvcache["render"] = ["Default", "Yes", "No"]
        #Shape
        self.csvcache["drawShape"] = ["Default", "Custom"]
        #Type
        self.csvcache["seqType"] = ["Static Points", "Sequence", "Sequence with Range"]
        #Visible
        self.csvcache["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pcloud = {}  #Particle Cloud
        #Deformation Mode
        self.pcloud["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Type
        self.pcloud["seqType"] = ["Static Points", "Sequence", "Sequence with Range"]
        #Density Distribution
        self.pcloud["distrib"] = ["Uniform", "Radial", "Cumulus", "Cumulus Inverted", "Ring"]
        #Shape
        self.pcloud["drawShape"] = ["Default", "Custom"]
        #Visible
        self.pcloud["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.pmod_dot_generator = {}  #Particle Generator
        #Deformation Mode
        self.pmod_dot_generator["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Particle ID's
        self.pmod_dot_generator["pidOrder"] = ["Sequential", "Random"]
        #Render
        self.pmod_dot_generator["render"] = ["Default", "Yes", "No"]
        #Shape
        self.pmod_dot_generator["drawShape"] = ["Default", "Custom"]
        #Type
        self.pmod_dot_generator["type"] = ["array", "radial", "linear"]
        #Visible
        self.pmod_dot_generator["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.realparticle = {}  #Realflow Particles
        #Deformation Mode
        self.realparticle["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.realparticle["render"] = ["Default", "Yes", "No"]
        #Shape
        self.realparticle["drawShape"] = ["Default", "Custom"]
        #Visible
        self.realparticle["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.surfgenloc = {}  #Surface Particle Generator
        #Deformation Mode
        self.surfgenloc["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.surfgenloc["render"] = ["Default", "Yes", "No"]
        #Shape
        self.surfgenloc["drawShape"] = ["Default", "Custom"]
        #Visible
        self.surfgenloc["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Particles - Simulation
        self.collectoremitter = {}  #Collector/Emitter
        #Deformation Mode
        self.collectoremitter["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.collectoremitter["render"] = ["Default", "Yes", "No"]
        #Shape
        self.collectoremitter["drawShape"] = ["Default", "Custom"]
        #Visible
        self.collectoremitter["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.curveemitter = {}  #Curve Emitter
        #Deformation Mode
        self.curveemitter["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.curveemitter["render"] = ["Default", "Yes", "No"]
        #Shape
        self.curveemitter["drawShape"] = ["Default", "Custom"]
        #Visible
        self.curveemitter["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.dynamiccollider = {}  #Dynamic Collider
        #Deformation Mode
        self.dynamiccollider["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.dynamiccollider["render"] = ["Default", "Yes", "No"]
        #Shape
        self.dynamiccollider["drawShape"] = ["Default", "Custom"]
        #Visible
        self.dynamiccollider["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.dynamicfluid = {}  #Dynamic Fluid
        #Deformation Mode
        self.dynamicfluid["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.dynamicfluid["render"] = ["Default", "Yes", "No"]
        #Shape
        self.dynamicfluid["drawShape"] = ["Default", "Custom"]
        #Visible
        self.dynamicfluid["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.flockingop = {}  #Particle Flocking
        #Deformation Mode
        self.flockingop["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.flockingop["render"] = ["Default", "Yes", "No"]
        #Shape
        self.flockingop["drawShape"] = ["Default", "Custom"]
        #Visible
        self.flockingop["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.particleop = {}  #Particle Operator
        #Deformation Mode
        self.particleop["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.particleop["render"] = ["Default", "Yes", "No"]
        #Shape
        self.particleop["drawShape"] = ["Default", "Custom"]
        #Type
        self.particleop["type"] = ["Assign", "Integrate", "New", "Trigger"]
        #Visible
        self.particleop["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.particlesim = {}  #Particle Simulation
        #Deformation Mode
        self.particlesim["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.particlesim["render"] = ["Default", "Yes", "No"]
        #Shape
        self.particlesim["drawShape"] = ["Default", "Custom"]
        #Visible
        self.particlesim["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.radialemitter = {}  #Radial Emitter
        #Deformation Mode
        self.radialemitter["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Emission Type
        self.radialemitter["type"] = ["Random", "Uniform"]
        #Render
        self.radialemitter["render"] = ["Default", "Yes", "No"]
        #Shape
        self.radialemitter["drawShape"] = ["Default", "Custom"]
        #Visible
        self.radialemitter["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.sourceemitter = {}  #Source Emitter
        #Deformation Mode
        self.sourceemitter["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Emit Mode
        self.sourceemitter["mode"] = ["Fixed Total Rate", "Fixed Average Rate", "Per-Particle Rate", "Pulse"]
        #Render
        self.sourceemitter["render"] = ["Default", "Yes", "No"]
        #Shape
        self.sourceemitter["drawShape"] = ["Default", "Custom"]
        #Visible
        self.sourceemitter["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.surfemitter = {}  #Surface Emitter
        #Deformation Mode
        self.surfemitter["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.surfemitter["render"] = ["Default", "Yes", "No"]
        #Shape
        self.surfemitter["drawShape"] = ["Default", "Custom"]
        #Visible
        self.surfemitter["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.particleterminator = {}  #Terminator
        #Deformation Mode
        self.particleterminator["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.particleterminator["render"] = ["Default", "Yes", "No"]
        #Shape
        self.particleterminator["drawShape"] = ["Default", "Custom"]
        #Visible
        self.particleterminator["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Procedurals
        self.deferredmesh = {}  #Deferred Mesh
        #Deformation Mode
        self.deferredmesh["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.deferredmesh["render"] = ["Default", "Yes", "No"]
        #Shape
        self.deferredmesh["drawShape"] = ["Default", "Custom"]
        #Visible
        self.deferredmesh["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.gaskettoy = {}  #Fractel Gasket
        #Deformation Mode
        self.gaskettoy["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Gasket Type
        self.gaskettoy["type"] = ["Square Hole", "Square Flake", "Serpinski", "Tetrahedron"]
        #Render
        self.gaskettoy["render"] = ["Default", "Yes", "No"]
        #Shape
        self.gaskettoy["drawShape"] = ["Default", "Custom"]
        #Visible
        self.gaskettoy["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.gear_dot_item = {}  #Gear
        #Deformation Mode
        self.gear_dot_item["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.gear_dot_item["render"] = ["Default", "Yes", "No"]
        #Shape
        self.gear_dot_item["drawShape"] = ["Default", "Custom"]
        #Teeth Facing
        self.gear_dot_item["teeth_facing"] = ["Outside", "Inside"]
        #Visible
        self.gear_dot_item["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.proxy = {}  #Proxy
        #Deformation Mode
        self.proxy["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Preview Rendering
        self.proxy["previewRender"] = ["None", "Preview Item", "Render Item"]
        #Render
        self.proxy["render"] = ["Default", "Yes", "No"]
        #Shape
        self.proxy["drawShape"] = ["Default", "Custom"]
        #Visible
        self.proxy["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.item_dot_rock = {}  #Rock
        #Deformation Mode
        self.item_dot_rock["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Noise Type lvl1
        self.item_dot_rock["lvl1noisetype"] = ["Noise", "Cellular"]
        #Noise Type lvl2
        self.item_dot_rock["lvl2noisetype"] = ["Noise", "Cellular"]
        #Noise Type lvl3
        self.item_dot_rock["lvl3noisetype"] = ["Noise", "Cellular"]
        #Render
        self.item_dot_rock["render"] = ["Default", "Yes", "No"]
        #Shape
        self.item_dot_rock["drawShape"] = ["Default", "Custom"]
        #Visible
        self.item_dot_rock["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.rpc_dot_mesh = {}  #RPC Mesh
        #Deformation Mode
        self.rpc_dot_mesh["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.rpc_dot_mesh["render"] = ["Default", "Yes", "No"]
        #Shape
        self.rpc_dot_mesh["drawShape"] = ["Default", "Custom"]
        #Visible
        self.rpc_dot_mesh["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.sphere_dot_geometry = {}  #Sphere
        #Deformation Mode
        self.sphere_dot_geometry["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.sphere_dot_geometry["render"] = ["Default", "Yes", "No"]
        #Shape
        self.sphere_dot_geometry["drawShape"] = ["Default", "Custom"]
        #Visible
        self.sphere_dot_geometry["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.sdf_dot_item = {}  #SubDFusion
        #Deformation Mode
        self.sdf_dot_item["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Mesh Mode
        self.sphere_dot_geometry["OutputMeshMode"] = ["Draft", "Airtight Draft", "Airtight Final", "Airtight Final w/Parts"]
        #Render
        self.sdf_dot_item["render"] = ["Default", "Yes", "No"]
        #Shape
        self.sdf_dot_item["drawShape"] = ["Default", "Custom"]
        #Visible
        self.sdf_dot_item["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.sdfstrip_dot_item = {}  #SubDFusion Strip
        #Deformation Mode
        self.sdfstrip_dot_item["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.sdfstrip_dot_item["render"] = ["Default", "Yes", "No"]
        #Shape
        self.sdfstrip_dot_item["drawShape"] = ["Default", "Custom"]
        #Visible
        self.sdfstrip_dot_item["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Volumes
        self.blob = {}  #Blob
        #Deformation Mode
        self.blob["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.blob["render"] = ["Default", "Yes", "No"]
        #Render Quality
        self.blob["renderQuality"] = ["low", "med", "high", "veryHigh", "best"]
        #Shape
        self.blob["drawShape"] = ["Default", "Custom"]
        #Visible
        self.blob["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.gplane = {}  #Ground Plane
        #Deformation Mode
        self.gplane["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.gplane["render"] = ["Default", "Yes", "No"]
        #Shape
        self.gplane["drawShape"] = ["Default", "Custom"]
        #Visible
        self.gplane["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.renderbool = {}  #Render Boolean
        #Deformation Mode
        self.renderbool["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Particle Geometry
        self.renderbool["geoType"] = ["Sphere", "Cube", "Cylinder", "Cumulus"]
        #Render
        self.renderbool["render"] = ["Default", "Yes", "No"]
        #Shape
        self.renderbool["drawShape"] = ["Default", "Custom"]
        #Visible
        self.renderbool["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.sprite = {}  #Sprite
        #Deformation Mode
        self.sprite["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.sprite["render"] = ["Default", "Yes", "No"]
        #Shape
        self.sprite["drawShape"] = ["Default", "Custom"]
        #Texture Effect
        self.sprite["textureFX"] = ["None", "Velocity Translate", "Expand", "Expand & Dissolve", "Pyroclastic"]
        #Visible
        self.sprite["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.vdbvoxel = {}  #VDBVoxel
        #Deformation Mode
        self.vdbvoxel["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #filtMode
        self.vdbvoxel["filtMode"] = ["null", "mean", "gaussian", "median"]
        #Render
        self.vdbvoxel["render"] = ["Default", "Yes", "No"]
        #Shape
        self.vdbvoxel["drawShape"] = ["Default", "Custom"]
        #Visible
        self.vdbvoxel["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.volume = {}  #Volume
        #Deformation Mode
        self.volume["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Hypertexture Mode
        self.volume["htexMode"] = ["additive", "multiply"]
        #Particle Geometry
        self.volume["geoType"] = ["Sphere", "Cube", "Cylinder", "Cumulus"]
        #Render
        self.volume["render"] = ["Default", "Yes", "No"]
        #Render Quality
        self.volume["renderQuality"] = ["low", "med", "high", "veryHigh", "best"]
        #Shadow Quality
        self.volume["shadowQuality"] = ["low", "med", "high", "veryHigh", "best"]
        #Shape
        self.volume["drawShape"] = ["Default", "Custom"]
        #Texture Effect
        self.volume["textureFX"] = ["None", "Velocity Translate", "Expand", "Expand & Dissolve", "Pyroclastic"]
        #Visible
        self.volume["visible"] = ["Default", "Yes", "No", "allOff"]
        
        
##--------- Other
        self.beziernode = {}  #Bezier Node
        #Deformation Mode
        self.beziernode["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.beziernode["render"] = ["Default", "Yes", "No"]
        #Shape
        self.beziernode["drawShape"] = ["Default", "Custom"]
        #Visible
        self.beziernode["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.canvaspi = {}  #CanvasPI
        #Deformation Mode
        self.canvaspi["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.canvaspi["render"] = ["Default", "Yes", "No"]
        #Shape
        self.canvaspi["drawShape"] = ["Default", "Custom"]
        #Visible
        self.canvaspi["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.widget = {}  #ChannelHandle
        #Deformation Mode
        self.widget["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Handle Type
        self.widget["whType"] = ["Disc", "Square", "Rectangle", "Triangle", "Arrow", "Curved Arrow", "Spin"]
        #Handle Draw Axis
        self.widget["whAxisDraw"] = ["Local X", "Local Y", "Local Z", "View Horizontal", "View Vertical"]
        #Handle Nove Axis
        self.widget["whAxisMove"] = ["X", "Y", "Z"]
        #Render
        self.widget["render"] = ["Default", "Yes", "No"]
        #Shape
        self.widget["drawShape"] = ["Default", "Custom"]
        #Visible
        self.widget["visible"] = ["Default", "Yes", "No", "allOff"]
        
        self.surf_dot_sample = {}  #surf.sample
        #Deformation Mode
        self.surf_dot_sample["deformMode"] = ["World", "Local", "Local YZ Rotation", "Local XZ Rotation", "Local XY Rotation"]
        #Render
        self.surf_dot_sample["render"] = ["Default", "Yes", "No"]
        #Shape
        self.surf_dot_sample["drawShape"] = ["Default", "Custom"]
        #Visible
        self.surf_dot_sample["visible"] = ["Default", "Yes", "No", "allOff"]
        
        


##################################################################################################
#                       Shader Tree                                                              #
##################################################################################################
        
##---------  Advanced Material
        self.advancedmaterial = {}
        #Blend Mode
        self.advancedmaterial["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Shading Model
        self.advancedmaterial["brdfType"] = ["Traditional", "Energy Conserving", "Physically Based"]
        #Reflection Type
        self.advancedmaterial["reflType"] = ["Full Scene", "Environment Only"]
        
        
##---------  Environment Material
        self.Envmaterial = {}
        #Blend Mode
        self.Envmaterial["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Environment Type
        self.Envmaterial["type"] = ["Constant", "2 Color Gradient", "4 Color Gradient", "CIE Overcast Sky", "Physically-based Daylight"]
        #Fog Type
        self.Envmaterial["fogType"] = ["None", "Linear", "Exponential", "Underwater", "Layered"]
        
        
##---------  Light Material
        self.Lightmaterial = {}
        #Blend Mode
        self.Lightmaterial["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        


##---------  Custom Material
        self.material_dot_celedges = {} #Cel Edges Material
        #Blend Mode
        self.material_dot_celedges["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.material_dot_celshader = {}#Cel Material
        #Blend Mode
        self.material_dot_celshader["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
       
        self.material_dot_hairmaterial = {}# Hair Material
        #Blend Mode
        self.material_dot_hairmaterial["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Global Illumination
        self.material_dot_hairmaterial["gi"] = ["None", "Recieve Indirect Lighting", "Cast Indirect Lighting", "Both"]
       
        self.material_dot_halftone = {} #Halftone Material
        #Blend Mode
        self.material_dot_halftone["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Environment Type
        self.material_dot_halftone["cellPattern"] = ["Dots", "Lines", "Crosshatch", "Addaptive Hatching", "Circle", "Square", "Diamond", "Plus", "Checkerboard", "Diamond Check"]
        #Fog Type
        self.material_dot_halftone["specPattern"] = ["Dots", "Lines", "Crosshatch", "Addaptive Hatching", "Circle", "Square", "Diamond", "Plus", "Checkerboard", "Diamond Check"]
        
        self.material_dot_iridescence = {} #Iridescence Material
        #Blend Mode
        self.material_dot_iridescence["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Iridescence Mode
        self.material_dot_iridescence["iridescenceMode"] = ["interference", "diffraction"]
        
        self.material_dot_skinmaterial = {} #Skin Material
        #Blend Mode
        self.material_dot_skinmaterial["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.material_dot_thinfilm = {} # ThinFilm Material
        #Blend Mode
        self.material_dot_thinfilm["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        
##---------  Enhance: Modo Textures - Display
        self.val_dot_display_counter1_dot_rjj = {} #Counter 1
        #Blend Mode
        self.val_dot_display_counter1_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Base Type
        self.val_dot_display_counter1_dot_rjj["BaseType"] = ["Decimal", "Hexadecimal", "Octal", "Binary"]
        #Format Type
        self.val_dot_display_counter1_dot_rjj["FormatType"] = ["Counter", "Realtime Clock", "SMPTE 24", "SMPTE 25", "SMPTE 30"]
        
        self.val_dot_display_counter2_dot_rjj = {} #Counter2
        #Blend Mode
        self.val_dot_display_counter2_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Base Type
        self.val_dot_display_counter2_dot_rjj["BaseType"] = ["Decimal", "Hexadecimal", "Octal", "Binary"]
        #Format Type
        self.val_dot_display_counter2_dot_rjj["FormatType"] = ["Counter", "Realtime Clock", "SMPTE 24", "SMPTE 25", "SMPTE 30"]
        
        self.val_dot_display_uvleds_dot_rjj = {} #UV LEDs
        #Blend Mode
        self.val_dot_display_uvleds_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Shape Type
        self.val_dot_display_uvleds_dot_rjj["shapeType"] = ["Round", "Square"]
        

##---------  Enhance: Modo Textures - Geometric        
        self.val_dot_geometric_uvleds_dot_rjj = {} #Box
        #Blend Mode
        self.val_dot_geometric_uvleds_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_uvleds_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_circular_dot_rjj = {} #Circular
        #Blend Mode
        self.val_dot_geometric_circular_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_circular_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_corners_dot_rjj = {} #Corners
        #Blend Mode
        self.val_dot_geometric_corners_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_corners_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_cubic_dot_rjj = {} #Cubic
        #Blend Mode
        self.val_dot_geometric_cubic_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_cubic_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_dimples_dot_rjj = {} #Dimples
        #Blend Mode
        self.val_dot_geometric_dimples_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_dimples_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_grid_dot_rjj = {} #Grid
        #Blend Mode
        self.val_dot_geometric_grid_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_grid_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_iris_dot_rjj = {} #Iris
        #Blend Mode
        self.val_dot_geometric_iris_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_iris_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_linear_dot_rjj = {} #Linear
        #Blend Mode
        self.val_dot_geometric_linear_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_linear_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_polygon_dot_rjj = {} #Polygon
        #Blend Mode
        self.val_dot_geometric_polygon_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_polygon_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_radial_dot_rjj = {} #Radial
        #Blend Mode
        self.val_dot_geometric_radial_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_radial_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_rndlinear_dot_rjj = {} #Random Linear
        #Blend Mode
        self.val_dot_geometric_rndlinear_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_rndlinear_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        #Random Noise Type
        self.val_dot_geometric_rndlinear_dot_rjj["RandomType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_ring_dot_rjj = {} #Ring
        #Blend Mode
        self.val_dot_geometric_ring_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_ring_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_spiral_dot_rjj = {} #Spiral
        #Blend Mode
        self.val_dot_geometric_spiral_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_spiral_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_geometric_star_dot_rjj = {} #Star
        #Blend Mode
        self.val_dot_geometric_star_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_geometric_star_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        

##---------  Enhance: Modo Textures - Noise        
        self.val_dot_noise_agate_dot_rjj = {} #Agate
        #Blend Mode
        self.val_dot_noise_agate_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Disturb Noise Type
        self.val_dot_noise_agate_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Implulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_bozo_dot_rjj = {} #Bozo
        #Blend Mode
        self.val_dot_noise_bozo_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_bozo_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_cruddy_dot_rjj = {} #Cruddy
        #Blend Mode
        self.val_dot_noise_cruddy_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_cruddy_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_dented_dot_rjj = {} #dented
        #Blend Mode
        self.val_dot_noise_dented_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_dented_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_etched_dot_rjj = {} #etched
        #Blend Mode
        self.val_dot_noise_etched_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_etched_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_fBm_dot_rjj = {} #fBm
        #Blend Mode
        self.val_dot_noise_fBm_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_fBm_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_flowbozo_dot_rjj = {} #Flow Bozo
        #Blend Mode
        self.val_dot_noise_flowbozo_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_flowbozo_dot_rjj["FlowType"] = ["Flat", "Square", "Inverse"]
        
        self.val_dot_noise_granite_dot_rjj = {} #Granite
        #Blend Mode
        self.val_dot_noise_granite_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_granite_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_hybrid_dot_rjj = {} #Hybrid
        #Blend Mode
        self.val_dot_noise_hybrid_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_hybrid_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_lump_dot_rjj = {} #Lump
        #Blend Mode
        self.val_dot_noise_lump_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_lump_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_marblenoise_dot_rjj = {} #Marble Noise
        #Blend Mode
        self.val_dot_noise_marblenoise_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_marblenoise_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_marblevein_dot_rjj = {} #Marble NVeinoise
        #Blend Mode
        self.val_dot_noise_marblevein_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_marblevein_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_multifractal_dot_rjj = {} #Multi Fractal
        #Blend Mode
        self.val_dot_noise_multifractal_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_multifractal_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_pebbles_dot_rjj = {} #Pebbles
        #Blend Mode
        self.val_dot_noise_pebbles_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_pebbles_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_puffyclouds_dot_rjj = {} #Puffy Clouds
        #Blend Mode
        self.val_dot_noise_puffyclouds_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_puffyclouds_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_ridged_dot_rjj = {} #Ridged
        #Blend Mode
        self.val_dot_noise_ridged_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_ridged_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_scar_dot_rjj = {} #Scar
        #Blend Mode
        self.val_dot_noise_scar_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_scar_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_scruffed_dot_rjj = {} #Scruffed
        #Blend Mode
        self.val_dot_noise_scruffed_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_scruffed_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_strata_dot_rjj = {} #Strata
        #Blend Mode
        self.val_dot_noise_strata_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_strata_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_stucco_dot_rjj = {} #Stucco
        #Blend Mode
        self.val_dot_noise_stucco_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_stucco_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_vectorbozo_dot_rjj = {} #Vector Bozo
        #Blend Mode
        self.val_dot_noise_vectorbozo_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_vectorbozo_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_noise_wrappedfbm_dot_rjj = {} #Wrapped fBm
        #Blend Mode
        self.val_dot_noise_wrappedfbm_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_noise_wrappedfbm_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        


##---------  Enhance: Modo Textures - Organic
        self.val_dot_organic_artdeco_dot_rjj = {} #Art Deco
        #Blend Mode
        self.val_dot_organic_artdeco_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_organic_blister_dot_rjj = {} #Blister
        #Blend Mode
        self.val_dot_organic_blister_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_organic_branches_dot_rjj = {} #Branches
        #Blend Mode
        self.val_dot_organic_branches_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_branches_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.cellular = {} #Cellular
        #Blend Mode
        self.cellular["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.cellular["type"] = ["Angular", "Round"]
        
        self.val_dot_organic_caustic_dot_rjj = {} #Caustic
        #Blend Mode
        self.val_dot_organic_caustic_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_caustic_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_cheesy_dot_rjj = {} #Cheesy
        #Blend Mode
        self.val_dot_organic_cheesy_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_cheesy_dot_rjj["CellOrder"] = ["First", "Second", "Third", "Forth"]
        
        self.val_dot_organic_concrete_dot_rjj = {} #concrete
        #Blend Mode
        self.val_dot_organic_concrete_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_concrete_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_crackle_dot_rjj = {} #Crackle
        #Blend Mode
        self.val_dot_organic_crackle_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_organic_dirt_dot_rjj = {} #dirt
        #Blend Mode
        self.val_dot_organic_dirt_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_dirt_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_disturbed_dot_rjj = {} #Disturbed
        #Blend Mode
        self.val_dot_organic_disturbed_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_disturbed_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_easywood_dot_rjj = {} #Easy Wood
        #Blend Mode
        self.val_dot_organic_easywood_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_easywood_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_electric_dot_rjj = {} #Electric
        #Blend Mode
        self.val_dot_organic_electric_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_electric_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_fire_dot_rjj = {} #Fire
        #Blend Mode
        self.val_dot_organic_fire_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_fire_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_hardwood_dot_rjj = {} #Hardwood
        #Blend Mode
        self.val_dot_organic_hardwood_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_hardwood_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_membrane_dot_rjj = {} #Membrane
        #Blend Mode
        self.val_dot_organic_membrane_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_organic_minky_dot_rjj = {} #Minky
        #Blend Mode
        self.val_dot_organic_minky_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_minky_dot_rjj["CellOrder"] = ["First", "Second", "Third", "Forth"]
        
        self.val_dot_organic_scatter_dot_rjj = {} #Scatter
        #Blend Mode
        self.val_dot_organic_scatter_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_scatter_dot_rjj["Shape"] = ["Spheres", "Cubes", "Diamonds"]
        
        self.val_dot_organic_sinblob_dot_rjj = {} #Sin Blog
        #Blend Mode
        self.val_dot_organic_sinblob_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_organic_veins_dot_rjj = {} #Veins
        #Blend Mode
        self.val_dot_organic_veins_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_veins_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_organic_wires_dot_rjj = {} #Wires
        #Blend Mode
        self.val_dot_organic_wires_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
       
        self.val_dot_organic_wormvein_dot_rjj = {} #Worm Vein
        #Blend Mode
        self.val_dot_organic_wormvein_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_organic_wormvein_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
              
##---------  Enhance: Modo Textures - Panels
        self.val_dot_panels_peel_dot_rjj = {} #Peel
        #Blend Mode
        self.val_dot_panels_peel_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_panels_peel_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_plates_dot_rjj = {} #Plates
        #Blend Mode
        self.val_dot_panels_plates_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_panels_plates_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_rivetrust_dot_rjj = {} #Rivet Rust
        #Blend Mode
        self.val_dot_panels_rivetrust_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_panels_rivetrust_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_rivets_dot_rjj = {} #Rivets
        #Blend Mode
        self.val_dot_panels_rivets_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_panels_rivets_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_rust_dot_rjj = {} #Rust
        #Blend Mode
        self.val_dot_panels_rust_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_panels_rust_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_panels_smear_dot_rjj = {} #Smear
        #Blend Mode
        self.val_dot_panels_smear_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_panels_smear_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        

##---------  Enhance: Modo Textures - Process
        self.val_dot_process_easygrad_dot_rjj = {} #Easy Gradient
        #Blend Mode
        self.val_dot_process_easygrad_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_process_regionalhsv_dot_rjj = {} #Regional HSV
        #Blend Mode
        self.val_dot_process_regionalhsv_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        

##---------  Enhance: Modo Textures - Skins
        self.val_dot_skins_camo_dot_rjj = {} #Camo
        #Blend Mode
        self.val_dot_skins_camo_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_camo_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_crumpled_dot_rjj = {} #Crunmpled
        #Blend Mode
        self.val_dot_skins_crumpled_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_crumpled_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_dinoskin_dot_rjj = {} #Dino Skin
        #Blend Mode
        self.val_dot_skins_dinoskin_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_dinoskin_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_disease_dot_rjj = {} #Disease
        #Blend Mode
        self.val_dot_skins_disease_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_disease_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_frogskin_dot_rjj = {} #Frog Skin
        #Blend Mode
        self.val_dot_skins_frogskin_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_frogskin_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_grainywood_dot_rjj = {} #Grainy Wood
        #Blend Mode
        self.val_dot_skins_grainywood_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_grainywood_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_leather_dot_rjj = {} #Leather
        #Blend Mode
        self.val_dot_skins_leather_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_leather_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_monster_dot_rjj = {} #Monster
        #Blend Mode
        self.val_dot_skins_monster_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_monster_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_pastella_dot_rjj = {} #Pastella
        #Blend Mode
        self.val_dot_skins_pastella_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_pastella_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_Peened_dot_rjj = {} #Peened
        #Blend Mode
        self.val_dot_skins_Peened_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_Peened_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_skins_scratches_dot_rjj = {} #Scratches
        #Blend Mode
        self.val_dot_skins_scratches_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_skins_scratches_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        
##---------  Enhance: Modo Textures- Space
        self.val_dot_space_blast_dot_rjj = {} #Blast
        #Blend Mode
        self.val_dot_space_blast_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_blast_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_coriolis_dot_rjj = {} #Coriolis
        #Blend Mode
        self.val_dot_space_coriolis_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_coriolis_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_flare_dot_rjj = {} #Flare
        #Blend Mode
        self.val_dot_space_flare_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_flare_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_gasgiant_dot_rjj = {} #Gas Giant
        #Blend Mode
        self.val_dot_space_gasgiant_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_gasgiant_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_glint_dot_rjj = {} #Glint
        #Blend Mode
        self.val_dot_space_glint_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_glint_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_hurricane_dot_rjj = {} #Hurricane
        #Blend Mode
        self.val_dot_space_hurricane_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_hurricane_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_nurnies_dot_rjj = {} #Nurnies
        #Blend Mode
        self.val_dot_space_nurnies_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_nurnies_dot_rjj["CellOrder"] = ["First", "Second", "Third", "Forth"]
        
        self.val_dot_space_planet_dot_rjj = {} #Planet
        #Blend Mode
        self.val_dot_space_planet_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_planet_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_planetclouds_dot_rjj = {} #Planet Clouds
        #Blend Mode
        self.val_dot_space_planetclouds_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_planetclouds_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_rings_dot_rjj = {} #Rings
        #Blend Mode
        self.val_dot_space_rings_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_rings_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_starfield_dot_rjj = {} #Star Field
        #Blend Mode
        self.val_dot_space_starfield_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_starfield_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_swirl_dot_rjj = {} #Swirl
        #Blend Mode
        self.val_dot_space_swirl_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_swirl_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_terra_dot_rjj = {} #Terra
        #Blend Mode
        self.val_dot_space_terra_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_space_terra_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_space_windows_dot_rjj = {} #Windows
        #Blend Mode
        self.val_dot_space_windows_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        

##---------  Enhance: Modo Textures - Tiles
        self.val_dot_tiles_basket_dot_rjj = {} #Basket
        #Blend Mode
        self.val_dot_tiles_basket_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_basket_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        #Weave Pattern Type
        self.val_dot_tiles_basket_dot_rjj["PatternType"] = ["Plain", "End Satin", "Basket", "Back and Forth", "Blips", "Plaid 1", "Steps", "Spots", "Plaid 2", "Lockstep", "Rows", "Herringbone", "Half Basket", "Quad 1", "Quad 2", "Stripes", "Zigzag 1", "Zigzag 2", "Zigzag 3", "Alternate 1", "Alternate 2", "Circles", "Crosses", "Speckles", "Stripes"]
        
        self.val_dot_tiles_bathtile_dot_rjj = {} #Bath Tile
        #Blend Mode
        self.val_dot_tiles_bathtile_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_bathtile_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_bricks_dot_rjj = {} #Bricks
        #Blend Mode
        self.val_dot_tiles_bricks_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_bricks_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_checks_dot_rjj = {} #Checks
        #Blend Mode
        self.val_dot_tiles_checks_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_checks_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_cornerless_dot_rjj = {} #Cornerless
        #Blend Mode
        self.val_dot_tiles_cornerless_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_cornerless_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_cubes_dot_rjj = {} #Cubes
        #Blend Mode
        self.val_dot_tiles_cubes_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_cubes_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_dashline_dot_rjj = {} #Dash Line
        #Blend Mode
        self.val_dot_tiles_dashline_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_dashline_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_diamonddeck_dot_rjj = {} #Diamond Deck
        #Blend Mode
        self.val_dot_tiles_diamonddeck_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_diamonddeck_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_fishscales_dot_rjj = {} #Fish Scales
        #Blend Mode
        self.val_dot_tiles_fishscales_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_fishscales_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_hextile_dot_rjj = {} #Hex Tile
        #Blend Mode
        self.val_dot_tiles_hextile_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_hextile_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_lattice1_dot_rjj = {} #Lattice 1
        #Blend Mode
        self.val_dot_tiles_lattice1_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_lattice1_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_lattice2_dot_rjj = {} #Lattice 2
        #Blend Mode
        self.val_dot_tiles_lattice2_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_lattice2_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_lattice3_dot_rjj = {} #Lattice 3
        #Blend Mode
        self.val_dot_tiles_lattice3_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_lattice3_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_mosaic_dot_rjj = {} #Mosaic
        #Blend Mode
        self.val_dot_tiles_mosaic_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_mosaic_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_octtile_dot_rjj = {} #Oct Tile
        #Blend Mode
        self.val_dot_tiles_octtile_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_octtile_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_parquet_dot_rjj = {} #Parquet
        #Blend Mode
        self.val_dot_tiles_parquet_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_parquet_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_paving_dot_rjj = {} #Paving
        #Blend Mode
        self.val_dot_tiles_paving_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_paving_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        #Paving Shape
        self.val_dot_tiles_paving_dot_rjj["PavingShape"] = ["Square", "Hexagon", "Octagon", "Triangle", "Wedges"]
        #Paving Style
        self.val_dot_tiles_paving_dot_rjj["PavingStyle"] = ["Straight", "Crazy", "Ornate", "Uneven"]        
        
        self.val_dot_tiles_plaid_dot_rjj = {} #Plaid
        #Blend Mode
        self.val_dot_tiles_plaid_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_plaid_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_planks_dot_rjj = {} #Planks
        #Blend Mode
        self.val_dot_tiles_planks_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_planks_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_ribs_dot_rjj = {} #Ribs
        #Blend Mode
        self.val_dot_tiles_ribs_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_ribs_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_roundedtile_dot_rjj = {} #Rounded Tile
        #Blend Mode
        self.val_dot_tiles_roundedtile_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_roundedtile_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_shingles_dot_rjj = {} #Shingles
        #Blend Mode
        self.val_dot_tiles_shingles_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_shingles_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_spots_dot_rjj = {} #Spots
        #Blend Mode
        self.val_dot_tiles_spots_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_spots_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_tacos_dot_rjj = {} #Tacos
        #Blend Mode
        self.val_dot_tiles_tacos_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_tacos_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_tartan_dot_rjj = {} #Tartan
        #Blend Mode
        self.val_dot_tiles_tartan_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_tartan_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_tiler_dot_rjj = {} #Tiler
        #Blend Mode
        self.val_dot_tiles_tiler_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_tiler_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_trichecks_dot_rjj = {} #Tri Checks
        #Blend Mode
        self.val_dot_tiles_trichecks_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_trichecks_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_tritile_dot_rjj = {} #Tri Tile
        #Blend Mode
        self.val_dot_tiles_tritile_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_tritile_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        
        self.val_dot_tiles_wall_dot_rjj = {} #Wall
        #Blend Mode
        self.val_dot_tiles_wall_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.val_dot_tiles_wall_dot_rjj["NoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        

##---------  Enhance: Modo Textures - Water
        self.val_dot_water_dripdrop_dot_rjj = {} #Drip Drop
        #Blend Mode
        self.val_dot_water_dripdrop_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_water_rain_dot_rjj = {} #rain
        #Blend Mode
        self.val_dot_water_rain_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_water_ripples_dot_rjj = {} #Ripples
        #Blend Mode
        self.val_dot_water_ripples_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_water_surf_dot_rjj = {} #Surf
        #Blend Mode
        self.val_dot_water_surf_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_water_waves_dot_rjj = {} #Waves
        #Blend Mode
        self.val_dot_water_waves_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_water_windywaves_dot_rjj = {} #Windy Waves
        #Blend Mode
        self.val_dot_water_windywaves_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Wave Noise Type
        self.val_dot_water_windywaves_dot_rjj["WaveNoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        #Wind Noise Type
        self.val_dot_water_windywaves_dot_rjj["WindNoiseType"] = ["Perlin", "Enhanced Perlin", "Gradient", "Value", "Gradient Value", "Impulse", "Lattice", "Bubble"]
        

##---------  Enhance: Modo Textures - Waveforms
        self.val_dot_waveforms_biasgain_dot_rjj = {} #Bias Gain
        #Blend Mode
        self.val_dot_waveforms_biasgain_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_fresnel_dot_rjj = {} #Fresnel
        #Blend Mode
        self.val_dot_waveforms_fresnel_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_gamma_dot_rjj = {} #Gamma
        #Blend Mode
        self.val_dot_waveforms_gamma_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_gaussian_dot_rjj = {} #Gaussian
        #Blend Mode
        self.val_dot_waveforms_gaussian_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_impulse_dot_rjj = {} #Impulse
        #Blend Mode
        self.val_dot_waveforms_impulse_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_Noise_dot_rjj = {} #Noise
        #Blend Mode
        self.val_dot_Noise_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_ramp_dot_rjj = {} #Ramp
        #Blend Mode
        self.val_dot_waveforms_ramp_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_rounded_dot_rjj = {} #Rounded
        #Blend Mode
        self.val_dot_waveforms_rounded_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_scurve_dot_rjj = {} #S-Curve
        #Blend Mode
        self.val_dot_waveforms_scurve_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_sawtooth_dot_rjj = {} #Sawtooth
        #Blend Mode
        self.val_dot_waveforms_sawtooth_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_scallop_dot_rjj = {} #Scallop
        #Blend Mode
        self.val_dot_waveforms_scallop_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_sine_dot_rjj = {} #Sine
        #Blend Mode
        self.val_dot_waveforms_sine_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_smooth_dot_rjj = {} #Smooth
        #Blend Mode
        self.val_dot_waveforms_smooth_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_smoothimpulse_dot_rjj = {} #Smooth Impulse
        #Blend Mode
        self.val_dot_waveforms_smoothimpulse_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_smoothsteps_dot_rjj = {} #Smooth Step
        #Blend Mode
        self.val_dot_waveforms_smoothsteps_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_waveforms_staircase_dot_rjj = {} #Staircase
        #Blend Mode
        self.val_dot_waveforms_staircase_dot_rjj["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
                

##---------  Image Map
        self.image_dot_gradfill = {} #Gradient Fill
        #Blend Mode
        self.image_dot_gradfill["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Shape
        self.image_dot_gradfill["shape"] = ["linear", "radial", "angular", "diamond"]
        
        self.imagemap = {} #Image Map
        #Alpha Channel
        self.imagemap["alpha"] = ["Ignore", "Use", "Alpha Only"]
        #Blend Mode
        self.imagemap["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Channel
        self.imagemap["rgba"] = ["RGB", "RGBA", "Alpha", "Red", "Green", "Blue"]
        #Texture Filtering
        self.imagemap["pixblend"] = ["Nearest", "Bilinear", "Bicubic"]
        
        self.videosequence = {} #Video Sequence
        #Blend Mode
        self.videosequence["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #End Behavior
        self.videosequence["endBehavior"] = ["Hold", "Repeat", "Mirror"]
        
        self.videostill = {} #Video Still
        #Blend Mode
        self.videostill["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
       

##---------  Mask
        self.mask = {}
        #Blend Mode
        self.mask["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Noise Type
        self.mask["surfType"] = ["(all)", "Surface", "Fur"]
        

##---------  NPR Materials
        self.material_dot_dab = {} #Dab Material
        #Blend Mode
        self.material_dot_dab["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.material_dot_edgeink = {} #Edge Ink Material
        #Blend Mode
        self.material_dot_dab["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_noise_dot_gabor = {} #Gabor Noise
        #Blend Mode
        self.val_dot_noise_dot_gabor["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.material_dot_gooch = {} #Gooch Material
        #Blend Mode
        self.material_dot_gooch["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.material_dot_halftone2 = {} #Halftone2 Material
        #Blend Mode
        self.material_dot_halftone2["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Pattern
        self.material_dot_halftone2["cellPattern"] = ["Dots", "Lines", "Crosshatch", "Adaptive Hatching", "Circle", "Square", "Diamond", "Plus", "Checkerboard", "Diamond Check"]
        #Specular Pattern
        self.material_dot_halftone2["specPattern"] = ["Dots", "Lines", "Crosshatch", "Adaptive Hatching", "Circle", "Square", "Diamond", "Plus", "Checkerboard", "Diamond Check"]
        
        self.material_dot_sketchtone = {} #SketchTone Material
        #Blend Mode
        self.material_dot_sketchtone["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.material_dot_stipple = {} #Stipple Material
        #Blend Mode
        self.material_dot_stipple["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.material_dot_toon = {} #Toon Material
        #Blend Mode
        self.material_dot_dab["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        


##---------  Processing
        self.constant = {} #Constant
        #Blend Mode
        self.constant["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.gradient = {}#Gradient
        #Blend Mode
        self.gradient["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.occlusion = {}#Occlusion
        #Blend Mode
        self.occlusion["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Type
        self.occlusion["type"] = ["Uniform", "Up", "Down Slope", "Reflection", "Concavity", "Convexity", "Concavity & Convexity"]
        
        self.process = {}#Process
        #Blend Mode
        self.process["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.tensiontexture = {}#Tension Texture
        #Blend Mode
        self.tensiontexture["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Method
        self.tensiontexture["type"] = ["Area", "Angle"]
        
        self.variationtexture = {}#Variation Texture
        #Blend Mode
        self.variationtexture["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Type
        self.variationtexture["type"] = ["Particle", "Texture Particle", "Mesh Part", "Item"]
        
        self.wmaptexture = {}#Weight Map Texture
        #Blend Mode
        self.wmaptexture["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
                

##--------- Render
        self.polyRender = {}        
        #indirectSSS
        self.polyRender["globSubs"] = ["Direct Only", "Indirect Affects SSS", "SSS Affects indirect", "Both"]
        #indirectCaustics
        self.polyRender["globCaus"] = ["None", "Reflection Only", "Refraction Only", "Both"]
        #irradianceUsage
        self.polyRender["irrUsage"] = ["First Bounce Only", "Second Bounce Only", "First and Second Bounces"]
        #irradianceGradients
        self.polyRender["irrGrads"] = ["None", "Rotation Only", "Translation Only", "Both"]
        #irradianceSamplingMethod
        self.polyRender["irrSample"] = ["Jittered Grid", "Poisson Disk"]
        #irradianceDataStructure
        self.polyRender["irrData"] = ["Smaller", "Faster"]
        #firstPrePassSpacing
        self.polyRender["irrStart"] = ["2 Pixels", "4 Pixels", "8 Pixels", "16 Pixels", "32 Pixels", "64 Pixels"]
        #lastPrePassSpacing
        self.polyRender["irrEnd"] = ["2 Pixels", "4 Pixels", "8 Pixels", "16 Pixels", "32 Pixels", "64 Pixels"]        
        #environmentMIS  
        self.polyRender["envMIS"] = ["None", "Indirect Diffuse Only", "Blurry Reflection Only", "Both"]
        #directLightMIS
        self.polyRender["directMIS"] = ["None", "Diffuse Only", "Specular Only", "Both"]
        #resolutionUnit
        self.polyRender["resUnit"] = ["Pixels", "Inches", "Centimeters"]
        #renderType
        self.polyRender["rendType"] = ["Automatic", "Scanline", "Ray Trace"]
        #antialiasing
        self.polyRender["aa"] = ["1 Sample/Pixel", "2 Sample/Pixel", "4 Sample/Pixel", "8 Sample/Pixel", "16 Sample/Pixel", "32 Sample/Pixel", "64 Sample/Pixel", "128 Sample/Pixel", "256 Sample/Pixel", "512 Sample/Pixel", "1024 Sample/Pixel"]
        #antialiasingFilter
        self.polyRender["aaFilter"] = ["Box", "Triangle", "Gaussian", "Catmull-Rom", "Mitchell-Netravali"]
        #fieldRendering
        self.polyRender["field"] = ["Off", "Upper Field First", "Lower Field First"]
        #bucketOrder
        self.polyRender["bktOrder"] = ["Rows", "Columns", "Spiral", "Hilbert", "Random"]        

##--------- Render Outputs
        self.renderOutput = {}
        #Blend Mode
        self.renderOutput["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Contours
        self.renderOutput["contour"] = ["None", "Surface Boundaries", "Segment Boundaries"]
        #Exposure Control
        self.renderOutput["expType"] = ["White Level", "Photographic"]
        #Tone Map Type
        self.renderOutput["toneMap"] = ["Reinhard Luminance", "Reinhard RGB"]
        
        
##---------  Shader Folder
        self.shaderfolder = {}
        #Blend Mode
        self.shaderfolder["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        
##---------  Special
        self.furmaterial = {} #Fur Material
        #Bend Direction
        self.furmaterial["bendDirection"] = ["Down", "Normal"]
        #Billboard
        self.furmaterial["billboard"] = ["Off", "Trees", "Leaves", "Feathers"]
        #Blend Mode
        self.furmaterial["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Curl Type
        self.furmaterial["curlMode"] = ["Curls", "Waves"]
        #Guides
        self.furmaterial["guides"] = ["None", "Clump", "Direction", "Direction + Length", "Shape", "Range"]
        #Type
        self.furmaterial["type"] = ["Strips", "Cylinders"]
        
        self.matcapshader = {} #Matcap Shader
        #Blend Mode
        self.matcapshader["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.projectshader = {} #Projection Shader
        #Blend Mode
        self.projectshader["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.projecttexture = {} #Projection Texture
        #Blend Mode
        self.projecttexture["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.defaultshader = {} #Shader
        #Alpha Type
        self.defaultshader["alphaType"] = ["Opacity", "Constant", "Shadow Catcher"]
        #Blend Mode
        self.defaultshader["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Indirect Illum Type
        self.defaultshader["indType"] = ["None", "Monte Carlo", "Irradiance Caching"]
        #Fog Type
        self.defaultshader["fogType"] = ["None", "Linear", "Exponential", "Underwater", "Layered"]
        #Light Linking Mode
        self.defaultshader["lightLink"] = ["Include", "Exclude"]
        
        self.surfgen = {} #Surface Generator
        #Blend Mode
        self.surfgen["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_wireframe = {} #Wireframe Texture
        #Blend Mode
        self.val_dot_wireframe["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        

##---------  Textures
        self.checker = {} #Checker
        #Blend Mode
        self.checker["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Type
        self.checker["type"] = ["Square", "Cube"]
        
        self.dots = {} #Dots
        #Blend Mode
        self.dots["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Type
        self.dots["type"] = ["Square", "Cube"]
        
        self.grid = {} #Grid
        #Blend Mode
        self.grid["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Type
        self.grid["type"] = ["Line", "Triangle", "Square", "Hexagon", "Cube"]
        
        self.Noise = {} #Noise
        #Blend Mode
        self.Noise["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Type
        self.Noise["type"] = ["Simple", "Fractal", "Turbulence"]
        
        self.val_dot_noise_poisson = {} #Poisson Cells
        #Blend Mode
        self.val_dot_noise_poisson["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Type
        self.val_dot_noise_poisson["type"] = ["Square", "Cube"]
        
        self.ripples = {} #Ripples
        #Blend Mode
        self.ripples["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.val_dot_rpctexture = {} #RPC Texture
        #Blend Mode
        self.val_dot_rpctexture["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Type
        self.val_dot_rpctexture["type"] = ["Square", "Cube"]
        
        self.val_dot_rtcurvature = {} #TR Curvature
        #Blend Mode
        self.val_dot_rtcurvature["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        #Grid Size
        self.val_dot_rtcurvature["gridSize"] = ["very low", "low", "high", "very high", "best"]
        
        self.weave = {} #Weave
        #Blend Mode
        self.weave["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
        self.wood = {} #Wood
        #Blend Mode
        self.wood["blend"] = ["Normal", "Add", "Subtract", "Difference", "Normal Multiply", "Divide", "Multiply", "Screen", "Overlay", "Soft Light", "Hard Light", "Darken", "Lighten", "Color Dodge", "Color Burn"]
        
####################################################################################################
# Utilities
#####################################################################################################
    def swap_dot(self, var, flip=0):
        if flip == 0:
            return var.replace("_dot_", ".")
        else:
            return var.replace(".", "_dot_")
        
        
        
        
        
        
        
        
        
        