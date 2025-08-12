import pifoam
from pifoam.system.controlDict import write_controlDict_transient
from pifoam.system.blockMeshDict import write_blockMeshDict, run_blockMeshDict
from pifoam.constant.transportProperties import write_Newtonian
from pifoam.system.schemes.icoFoam import write_fvSchemes_icoFoam, write_fvSolution_icoFoam
from pifoam.initial.U import set_uniformVelocity
from pifoam.system.snappyHexMeshDict import write_snappyHexMeshDict, run_snappyHexMeshDict
from pifoam.system.meshQualityDict import write_meshQualityDict


case_dir = "./sample"
x_range = [-10., 40.]
y_range = [-10., 10.]
z_range = [5, 6.]
x_num = 250
y_num = 100
z_num = 1
boundary_types = {"north":"wall", "top": "wall", "bottom": "wall", "east": "patch", "west": "patch", "south": "wall"}

pifoam.utils.create_casedir(case_dir, exist_ok=True)
write_controlDict_transient(case_dir, startTime=0, endTime=1, deltaT=0.1, writeInterval=1, application="pisoFoam")
write_fvSchemes_icoFoam(case_dir)
write_fvSolution_icoFoam(case_dir)
pifoam.utils.move_STL(case_dir, "./Unnamed-cyl.stl")
run_blockMeshDict(
    case_dir,
    scale=1,
    x_range=x_range,
    y_range=y_range,
    z_range=z_range,
    x_num=x_num,
    y_num=y_num,
    z_num=z_num,
    boundary_types=boundary_types
)
write_meshQualityDict(case_dir)
write_snappyHexMeshDict(case_dir, "Unnamed-cyl.stl", (29.9, 0.1, 5.51))
run_snappyHexMeshDict(case_dir)
set_uniformVelocity(case_dir, boundaryNames=["north", "south", "east", "west", "top", "bottom"], boundaryConditions=[{"type":"noSlip"} for i in range(6)])
# pifoam.utils.delete_casedir(case_dir)