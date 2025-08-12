import os
import _io
import shutil

def create_casedir(case_dir:str, exist_ok:bool = True)->None:
    """Create a case directory with the necessary subdirectories.

    Args:
        case_dir (str): The name of the case directory to create.
        exist_ok (bool, optional): If True, will not raise an error if the directory already exists. Defaults to True.
    """
    os.makedirs(f"{case_dir}/constant", exist_ok=exist_ok)
    os.makedirs(f"{case_dir}/system", exist_ok=exist_ok)
    os.makedirs(f"{case_dir}/0", exist_ok=exist_ok)
    os.makedirs(f"{case_dir}/constant/triSurface", exist_ok=exist_ok)


def delete_casedir(case_dir:str)->None:
    """Delete a case directory and all its contents.

    Args:
        case_dir (str): The name of the case directory to delete.
    """
    import shutil
    shutil.rmtree(case_dir, ignore_errors=True)

def write_value(file:_io.TextIOWrapper, name:str, value:any)->None:
    """Write a key-value pair to a file.

    Args:
        file (_io.TextIOWrapper): The file to write to.
        name (str): The name of the key.
        value (any): The value to write.
    """
    file.write(f"{name}\t{value};\n")

def tupleToDict(tup:tuple[int|float])->str:
    """Convert a tuple of integers or floats to a dictionary representation.

    Args:
        tup (tuple[int | float]): A tuple of integers or floats.
    Returns:
        str: A string representation of the dictionary.
    """
    s = "("
    for t in tup:
        s += f"{t} "
    s = s[:-1]+")"
    return s

def write_format(file:_io.TextIOWrapper, form:dict, name:str = "FoamFile")->None:
    """Write a formatted dictionary to a file.

    Args:
        file (_io.TextIOWrapper): The file to write to.
        form (dict): The dictionary to write.
        name (str, optional): The name to use for the FoamFile header. Defaults to "FoamFile".
    """
    file.write(f"{name}\n{{\n")
    for key, value in form.items():
        write_value(file, key, value)
    file.write("}\n")

def move_STL(case_dir: str, filename: str, copied: bool = True) -> None:
    """Move or copy an STL file to the case directory.

    Args:
        case_dir (str): The OpenFOAM case directory.
        filename (str): The path of the STL file to move/copy.
        copied (bool, optional): If True, copy the file; if False, move it. Defaults to True.
    """
    if copied:
        shutil.copy2(filename, f"{case_dir}/constant/triSurface")
    else:
        shutil.move(filename, f"{case_dir}/constant/triSurface")
