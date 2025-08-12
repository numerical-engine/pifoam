from pifoam import utils

def set_uniformVelocity(
        case_dir:str,
        boundaryNames:list[str],
        boundaryConditions:list[dict[str, str]],
        U_init:list[float] = [0., 0., 0.],
        )->None:
    """Set uniform velocity boundary conditions.

    Args:
        case_dir (str): The case directory.
        boundaryNames (list[str]): The names of the boundaries.
        boundaryConditions (list[dict[str, str]]): The boundary conditions.
        U_init (list[float], optional): The initial velocity. Defaults to [0., 0., 0.].
    """
    
    with open(f"{case_dir}/0/U", "w") as file:
        utils.write_format(file, {
            "version": 2.0,
            "format": "ascii",
            "class": "volVectorField",
            "object": "U"
        })
        file.write("dimensions\t[0 1 -1 0 0 0 0];\n")
        file.write("internalField\tuniform " + utils.tupleToDict(U_init) + ";\n")
        file.write("boundaryField\n{\n")
        
        for boundaryCondition, boundaryName in zip(boundaryConditions, boundaryNames):
            utils.write_format(file, boundaryCondition, boundaryName)
        file.write("}\n")