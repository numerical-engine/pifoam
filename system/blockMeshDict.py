from pifoam import utils
import subprocess

def write_blockMeshDict(
        case_dir:str,
        *,
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
            "object" : "blockMeshDict"
        })
        utils.write_value(file, "scale", scale)

        file.write("vertices\n(\n")
        x_min, x_max = x_range
        y_min, y_max = y_range
        z_min, z_max = z_range
        file.write(f"({x_min} {y_min} {z_min})\n")
        file.write(f"({x_max} {y_min} {z_min})\n")
        file.write(f"({x_max} {y_max} {z_min})\n")
        file.write(f"({x_min} {y_max} {z_min})\n")
        file.write(f"({x_min} {y_min} {z_max})\n")
        file.write(f"({x_max} {y_min} {z_max})\n")
        file.write(f"({x_max} {y_max} {z_max})\n")
        file.write(f"({x_min} {y_max} {z_max})\n")
        file.write(");\n")

        file.write("blocks\n(\n")
        file.write(f"hex (0 1 2 3 4 5 6 7) ({x_num} {y_num} {z_num}) simpleGrading (1 1 1)\n")
        file.write(");\n")

        file.write("edges\n(\n")
        file.write(");\n")

        faces = {"top": (4,5,6,7), "bottom": (0,3,2,1), "north": (3,7,6,2), "south": (0,4,7,3), "east": (3,7,6,2), "west": (1,5,4,0)}
        assert set(faces.keys()).issubset(boundary_types.keys())
        file.write("boundary\n(\n")

        for key in boundary_types.keys():
            file.write(f"{key}\n{{\n")
            file.write(f"type\t{boundary_types[key]};\n")
            file.write("faces\n(\n")
            file.write(f"{utils.tupleToDict(faces[key])}\n")
            file.write(");\n")
            file.write("}\n")

        file.write(");\n")
        file.write("mergePatchPairs\n(\n);\n")


def run_blockMeshDict(case_dir:str,
        *,
        scale:float,
        x_range:list[float],
        y_range:list[float],
        z_range:list[float],
        x_num:int,
        y_num:int,
        z_num:int,
        boundary_types:dict[str, str],
    ) -> None:
    """Run blockMesh for the OpenFOAM case.

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

    write_blockMeshDict(
        case_dir,
        scale=scale,
        x_range=x_range,
        y_range=y_range,
        z_range=z_range,
        x_num=x_num,
        y_num=y_num,
        z_num=z_num,
        boundary_types=boundary_types
    )

    subprocess.run(["blockMesh", "-case", case_dir], stdout=subprocess.DEVNULL)