import pifoam


boundary_types = {
    "top" : "empty",
    "bottom" : "empty",
    "north" : "wall",
    "south" : "wall",
    "east" : "patch",
    "west" : "patch",
    "cyl1" : "wall",
    "cyl2" : "wall",
}

case_dir = "./sample"

blockmesh_props = {"scale":1.0, "x_range":(-10, 40), "y_range":(-10, 10), "z_range":(5, 6), "x_num":250, "y_num":100, "z_num":1}
mesher = pifoam.mesh.snappyHexMesh(boundary_types, stlFile = "./cylinder.stl", blockmesh_props=blockmesh_props, locationInMesh=(39, 0, 5.5))

ico_foam = pifoam.application.icoFoam(case_dir, mesher)
ico_foam.setup()
ico_foam.create_mesh()