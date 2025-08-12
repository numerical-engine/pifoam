from pifoam import utils

def write_Newtonian(case_dir:str, nu:float)->None:
    """Write the Newtonian transport model properties.

    Args:
        case_dir (str): The directory of the OpenFOAM case.
        nu (float): The kinematic viscosity [m2/s].
    """
    with open(f"{case_dir}/constant/transportProperties", "w") as file:
        utils.write_format(file, {
            "version" : 2.0,
            "format" : "ascii",
            "class" : "dictionary",
            "location" : "constant",
            "object" : "transportProperties"
        })
        utils.write_value(file, "transportModel", "Newtonian")
        utils.write_value(file, "nu", nu)