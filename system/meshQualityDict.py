from pifoam import utils

def write_meshQualityDict(
        case_dir:str,
        minFaceWeight:float = 0.02,
        )->None:
    """Write the meshQualityDict file for the OpenFOAM case.

    Args:
        case_dir (str): The directory of the OpenFOAM case.
        minFaceWeight (float, optional): The minimum face weight. Defaults to 0.02.
    """
    with open(f"{case_dir}/system/meshQualityDict", "w") as file:
        utils.write_format(file, {
            "version": 2.0,
            "format": "ascii",
            "class": "dictionary",
            "object": "meshQualityDict"
        })
        file.write("#includeEtc \"caseDicts/meshQualityDict\"\n")
        utils.write_value(file, "minFaceWeight", minFaceWeight)