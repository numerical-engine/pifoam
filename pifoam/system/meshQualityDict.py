from pifoam import utils

def write_meshQualityDict(case_dir:str, minFaceWeight:float = 0.02) -> None:
    with open(f"{case_dir}/system/meshQualityDict", "w") as file:
        utils.write_format(file, {"version": 2.0, "format": "ascii", "class": "dictionary", "location": "system", "object": "meshQualityDict"}, "FoamFile")
        file.write("#includeEtc \"caseDicts/meshQualityDict\"\n")
        file.write(f"minFaceWeight\t{minFaceWeight};\n")