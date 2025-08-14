import pifoam


boundary_types = {
    "top" : "empty",
    "bottom" : "empty",
    "north" : "wall",
    "south" : "wall",
    "east" : "patch",
    "west" : "patch",
    "cylinder" : "wall",
}

case_dir = "./sample"

blockmesh_props = {"scale":1.0, "x_range":(-10, 40), "y_range":(-10, 10), "z_range":(5, 6), "x_num":250, "y_num":100, "z_num":1}
mesher = pifoam.mesh.snappyHexMesh(boundary_types, stlFile = "./cylinder.stl", blockmesh_props=blockmesh_props, locationInMesh=(39, 0, 5.5))

ico_foam = pifoam.application.icoFoam(case_dir, mesher, {"p": 0, "U": (0, 0, 0)}, nu=0.001)
ico_foam.set_controlDict("endTime", 100.0)
ico_foam.set_controlDict("purgeWrite", 1)
ico_foam.set_controlDict("writeInterval", 20)
ico_foam.set_controlDict("deltaT", 0.1)

ico_foam.set_boundaryCondition("U", "north", "slip")
ico_foam.set_boundaryCondition("U", "south", "slip")
ico_foam.set_boundaryCondition("U", "top", "empty")
ico_foam.set_boundaryCondition("U", "bottom", "empty")
ico_foam.set_boundaryCondition("U", "east", "fixedValue", "uniform (1 0 0)")
ico_foam.set_boundaryCondition("U", "west", "zeroGradient")
ico_foam.set_boundaryCondition("U", "cylinder", "noSlip")

ico_foam.set_boundaryCondition("p", "north", "zeroGradient")
ico_foam.set_boundaryCondition("p", "south", "zeroGradient")
ico_foam.set_boundaryCondition("p", "top", "empty")
ico_foam.set_boundaryCondition("p", "bottom", "empty")
ico_foam.set_boundaryCondition("p", "east", "zeroGradient")
ico_foam.set_boundaryCondition("p", "west", "fixedValue", "uniform 0")
ico_foam.set_boundaryCondition("p", "cylinder", "zeroGradient")

ico_foam.setup()
ico_foam.create_mesh()
ico_foam.run(show_log=True)