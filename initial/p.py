from pifoam import utils

def set_uniformPressure(
        case_dir:str,
        boundaryNames:list[str],
        boundaryConditions:list[dict[str, str]],
        p_init:float = 0.,
        )->None:
    """Set uniform pressure boundary conditions.

    Args:
        case_dir (str): The case directory.
        boundaryNames (list[str]): The names of the boundaries.
        boundaryConditions (list[dict[str, str]]): The boundary conditions.
        p_init (float, optional): The initial pressure. Defaults to 0..
    """
    with open(f"{case_dir}/0/p", "w") as file:
        utils.write_format(file, {
            "version": 2.0,
            "format": "ascii",
            "class": "volScalarField",
            "object": "p"
        })
        file.write("dimensions\t[0 2 -2 0 0 0 0];\n")
        file.write(f"internalField\tuniform {p_init};\n")
        file.write("boundaryField\n{\n")

        for boundaryCondition, boundaryName in zip(boundaryConditions, boundaryNames):
            utils.write_format(file, boundaryCondition, boundaryName)
        file.write("}\n")