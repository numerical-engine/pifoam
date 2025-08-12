from pifoam import utils

def write_fvSchemes_icoFoam(
        case_dir:str,
        *,
        gradSchemes:dict[str, str] = {"default":"Gauss linear"},
        divSchemes:dict[str, str] = {"default":"none", "div(phi,U)":"Gauss limitedLinearV 1"},
        laplacianSchemes:dict[str, str] = {"default":"Gauss linear corrected"},
        interpolationSchemes:dict[str, str] = {"default":"linear"},
        snGradSchemes:dict[str, str] = {"default":"corrected"},
        )->None:
    """Write the fvSchemes file for the icoFoam solver.

    Args:
        case_dir (str): The case directory.
        gradSchemes (dict[str, str], optional): The gradient schemes. Defaults to {"default":"Gauss linear"}.
        divSchemes (dict[str, str], optional): The divergence schemes. Defaults to {"default":"none", "div(phi,U)":"Gauss limitedLinearV 1"}.
        laplacianSchemes (dict[str, str], optional): The Laplacian schemes. Defaults to {"default":"Gauss linear corrected"}.
        interpolationSchemes (dict[str, str], optional): The interpolation schemes. Defaults to {"default":"linear"}.
        snGradSchemes (dict[str, str], optional): The second normal gradient schemes. Defaults to {"default":"corrected"}.
    """
    with open(f"{case_dir}/system/fvSchemes", "w") as file:
        utils.write_format(file, {
            "version": 2.0,
            "format": "ascii",
            "class": "dictionary",
            "object": "fvSchemes"
        })
        utils.write_format(file, gradSchemes, "gradSchemes")
        utils.write_format(file, divSchemes, "divSchemes")
        utils.write_format(file, laplacianSchemes, "laplacianSchemes")
        utils.write_format(file, interpolationSchemes, "interpolationSchemes")
        utils.write_format(file, snGradSchemes, "snGradSchemes")

def write_fvSolution_icoFoam(
        case_dir:str,
        *,
        p:dict[str, any] = {"solver":"PCG", "preconditioner":"DIC", "tolerance":1e-06, "relTol":0.05},
        pFinal:dict[str, any] = {"$p":"", "relTol":0.0},
        U:dict[str, any] = {"solver":"smoothSolver", "smoother":"symGaussSeidel", "tolerance":1e-05, "relTol":0},
        PISO:dict[str, int] = {"nCorrectors":2, "nNonOrthogonalCorrectors":0},
        )->None:
    with open(f"{case_dir}/system/fvSolution", "w") as file:
        utils.write_format(file, {
            "version": 2.0,
            "format": "ascii",
            "class": "dictionary",
            "object": "fvSolution"
        })

        file.write("solvers\n{\n")
        utils.write_format(file, p, "p")
        utils.write_format(file, pFinal, "pFinal")
        utils.write_format(file, U, "U")
        file.write("}\n")

        utils.write_format(file, PISO, "PISO")