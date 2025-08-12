from pifoam import utils

def write_gravity(case_dir:str, g:list[float])->None:
    """Write the gravity vector.

    Args:
        case_dir (str): The directory of the OpenFOAM case.
        g (list[float]): The gravity vector [gx, gy, gz].
    """
    assert len(g) == 3, "Gravity vector must have three components (gx, gy, gz)"
    with open(f"{case_dir}/constant/g", "w") as file:
        utils.write_format(file, {
            "version" : 2.0,
            "format" : "ascii",
            "class" : "dictionary",
            "location" : "constant",
            "object" : "g"
        })
        utils.write_value(file, "dimensions", "[0 1 -2 0 0 0 0]")
        utils.write_value(file, "g", g)