from pifoam import utils
import subprocess







def write_snappyHexMeshDict(
        case_dir:str,
        stl_name:str,
        locationInMesh:tuple,
        *,
        castellatedMesh:str = "true",
        snap:str = "true",
        addLayers:str = "true",
        maxLocalCells:int = 100000,
        maxGlobalCells:int = 2000000,
        minRefinementCells:int = 10,
        nCellsBetweenLevels:int = 2,
        layers:dict[str, str] = {},
        expansionRatio:float = 1.0,
        finalLayerThickness:float = 0.3,
        minThickness:float = 0.1,
    )->None:

    with open(f"{case_dir}/system/snappyHexMeshDict", "w") as file:
        utils.write_format(file, 
                        {"version": 2.0,
                        "format": "ascii",
                        "class": "dictionary",
                        "object": "snappyHexMeshDict",
                        })
        utils.write_value(file, "castellatedMesh", castellatedMesh)
        utils.write_value(file, "snap", snap)
        utils.write_value(file, "addLayers", addLayers)

        file.write("geometry\n{\n")
        utils.write_format(file, {"type":"triSurfaceMesh", "name":stl_name[:-4]},stl_name)
        file.write("}\n")

        file.write("castellatedMeshControls\n{\n")
        utils.write_value(file, "maxLocalCells", maxLocalCells)
        utils.write_value(file, "maxGlobalCells", maxGlobalCells)
        utils.write_value(file, "minRefinementCells", minRefinementCells)
        utils.write_value(file, "maxLoadUnbalance", 0.1)
        utils.write_value(file, "nCellsBetweenLevels", nCellsBetweenLevels)
        file.write("features\n();\n")
        file.write("refinementSurfaces{\n}\n")
        utils.write_value(file, "resolveFeatureAngle", 30)
        file.write("refinementRegions{\n}\n")
        utils.write_value(file, "locationInMesh", utils.tupleToDict(locationInMesh))
        utils.write_value(file, "allowFreeStandingZoneFaces", "true")
        file.write("}\n")

        file.write("snapControls\n{\n")
        utils.write_value(file, "nSmoothPatch", 3)
        utils.write_value(file, "tolerance", 2.0)
        utils.write_value(file, "nSolveIter", 30)
        utils.write_value(file, "nRelaxIter", 5)
        file.write("}\n")

        file.write("addLayersControls\n{\n")
        utils.write_value(file, "relativeSizes", "true")
        file.write("layers\n{\n")
        for key, n in layers.items():
            utils.write_value(file, {"nSurfaceLayers":n}, key)
        file.write("}\n")
        utils.write_value(file, "expansionRatio", expansionRatio)
        utils.write_value(file, "finalLayerThickness", finalLayerThickness)
        utils.write_value(file, "minThickness", minThickness)
        utils.write_value(file, "nGrow", 0)
        utils.write_value(file, "featureAngle", 60)
        utils.write_value(file, "slipFeatureAngle", 30)
        utils.write_value(file, "nRelaxIter", 3)
        utils.write_value(file, "nSmoothSurfaceNormals", 1)
        utils.write_value(file, "nSmoothNormals", 3)
        utils.write_value(file, "nSmoothThickness", 10)
        utils.write_value(file, "maxFaceThicknessRatio", 0.5)
        utils.write_value(file, "maxThicknessToMedialRatio", 0.3)
        utils.write_value(file, "minMedianAxisAngle", 90)
        utils.write_value(file, "nBufferCellsNoExtrude", 0)
        utils.write_value(file, "nLayerIter", 50)
        file.write("}\n")

        file.write("meshQualityControls\n{\n")
        file.write("#include \"meshQualityDict\"\n")
        utils.write_value(file, "nSmoothScale", 4)
        utils.write_value(file, "errorReduction", 0.75)
        file.write("}\n")

        utils.write_value(file, "mergeTolerance", 1e-6)

def run_snappyHexMeshDict(case_dir:str)->None:
    subprocess.run(["snappyHexMesh", "-case", case_dir, "-overwrite"], stdout=subprocess.DEVNULL)