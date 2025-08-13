from pifoam import utils
import subprocess
import sys

def write_blockMeshDict(
        case_dir:str,
        scale:float,
        x_range:list[float],
        y_range:list[float],
        z_range:list[float],
        x_num:int,
        y_num:int,
        z_num:int,
        boundary_types:dict[str, str],
        )->None:
    """Write the blockMeshDict file for the OpenFOAM case.

    Args:
        case_dir (str): The directory of the OpenFOAM case.
        scale (float): Conversion factor to meters.
        x_range (list[float]): The range of x coordinates.
        y_range (list[float]): The range of y coordinates.
        z_range (list[float]): The range of z coordinates.
        x_num (int): The number of cells in the x direction.
        y_num (int): The number of cells in the y direction.
        z_num (int): The number of cells in the z direction.
        boundary_types (dict[str, str]): The boundary types for each face.
    """
    with open(f"{case_dir}/system/blockMeshDict", "w") as file:
        utils.write_format(file, {
            "version" : 2.0,
            "format" : "ascii",
            "class" : "dictionary",
            "location" : "system",
            "object" : "blockMeshDict"}, 
            "FoamFile")
        file.write(f"scale\t{scale};\n")
        vertices = [
            utils.tupleToDict((x_range[0], y_range[0], z_range[0])),
            utils.tupleToDict((x_range[1], y_range[0], z_range[0])),
            utils.tupleToDict((x_range[1], y_range[1], z_range[0])),
            utils.tupleToDict((x_range[0], y_range[1], z_range[0])),
            utils.tupleToDict((x_range[0], y_range[0], z_range[1])),
            utils.tupleToDict((x_range[1], y_range[0], z_range[1])),
            utils.tupleToDict((x_range[1], y_range[1], z_range[1])),
            utils.tupleToDict((x_range[0], y_range[1], z_range[1])),
        ]
        utils.write_list(file, vertices, "vertices")
        utils.write_list(file, ["hex", "(0 1 2 3 4 5 6 7)", f"({x_num} {y_num} {z_num}) simpleGrading (1 1 1)"], "blocks")
        utils.write_list(file, [""], "edges")

        faces = {"top": (4,5,6,7), "bottom": (0,3,2,1), "north": (3,7,6,2), "south": (1,5,4,0), "east": (0,4,7,3), "west": (2,6,5,1)}
        assert set(faces.keys()).issubset(boundary_types.keys())
        file.write("boundary (\n")
        for key in boundary_types.keys():
            file.write(f"{key}{{")
            file.write(f"type\t{boundary_types[key]};")
            file.write("faces ( ")
            file.write(f"{utils.tupleToDict(faces[key])}")
            file.write(" );")
            file.write("}\n")
        file.write(" );\n")
        utils.write_list(file, [""], "mergePatchPairs")

def run_blockMesh(case_dir:str,)->None:
    subprocess.run(["blockMesh", "-case", case_dir], stdout=subprocess.DEVNULL)