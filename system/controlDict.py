from pifoam import utils

def write_controlDict_steady(
        case_dir: str,
        *,
        writeInterval: int,
        application:str,
        startFrom:str = "startTime",
        startTime:int = 0,
        stopAt:str = "endTime",
        endTime:int = None,
        purgeWrite:int = 1,
        ) -> None:
    """Write a steady-state controlDict file for OpenFOAM.

    Args:
        case_dir (str): The case directory.
        writeInterval (int): The write interval.
        application (str): The application name.
        startFrom (str, optional): The start time specification. Defaults to "startTime".
        startTime (int, optional): The start time value. Defaults to 0.
        stopAt (str, optional): The stop time specification. Defaults to "endTime".
        endTime (int, optional): The end time value. Defaults to None.
        purgeWrite (int, optional): The purge write setting. Defaults to 1.
    """
    with open(f"{case_dir}/system/controlDict", "w") as file:
        utils.write_format(file, {
            "version" : 2.0,
            "format" : "ascii",
            "class" : "dictionary",
            "location" : "system",
            "object" : "controlDict"
        })

        utils.write_value(file, "application", application)

        assert startFrom in ["startTime", "latestTime", "firstTime"], "startFrom must be 'startTime', 'latestTime', or 'firstTime'"
        utils.write_value(file, "startFrom", startFrom)

        if startFrom == "startTime":
            utils.write_value(file, "startTime", startTime)

        assert stopAt in ["endTime", "noWriteNow", "writeNow", "nextWrite"], "stopAt must be 'endTime', 'noWriteNow', 'writeNow', or 'nextWrite'"
        utils.write_value(file, "stopAt", stopAt)

        if stopAt == "endTime":
            assert endTime is not None, "endTime must be specified when stopAt is 'endTime'"
            utils.write_value(file, "endTime", endTime)
        
        utils.write_value(file, "deltaT", 1)

        utils.write_value(file, "writeControl", "timeStep")
        utils.write_value(file, "writeInterval", writeInterval)
        utils.write_value(file, "purgeWrite", purgeWrite)
        utils.write_value(file, "writeFormat", "ascii")
        utils.write_value(file, "writePrecision", 6)
        utils.write_value(file, "writeCompression", "off")
        utils.write_value(file, "timeFormat", "general")
        utils.write_value(file, "timePrecision", 6)
        utils.write_value(file, "runTimeModifiable", "true")


def write_controlDict_transient(
        case_dir: str,
        *,
        writeInterval: int | float,
        deltaT:float,
        application:str,
        startFrom:str = "startTime",
        startTime:int = 0,
        stopAt:str = "endTime",
        endTime:int = None,
        purgeWrite:int = 1,
        writeControl:str = "timeStep",
        )->None:
    """Write a transient controlDict file for OpenFOAM.

    Args:
        case_dir (str): The case directory.
        writeInterval (int | float): The write interval.
        deltaT (float): The time step size.
        application (str): The application name.
        startFrom (str, optional): The start time specification. Defaults to "startTime".
        startTime (int, optional): The start time value. Defaults to 0.
        stopAt (str, optional): The stop time specification. Defaults to "endTime".
        endTime (int, optional): The end time value. Defaults to None.
        purgeWrite (int, optional): The purge write setting. Defaults to 1.
        writeControl (str, optional): The write control setting. Defaults to "timeStep".
    """

    with open(f"{case_dir}/system/controlDict", "w") as file:
        utils.write_format(file, {
            "version" : 2.0,
            "format" : "ascii",
            "class" : "dictionary",
            "location" : "system",
            "object" : "controlDict"
        })

        utils.write_value(file, "application", application)

        assert startFrom in ["startTime", "latestTime", "firstTime"], "startFrom must be 'startTime', 'latestTime', or 'firstTime'"
        utils.write_value(file, "startFrom", startFrom)

        if startFrom == "startTime":
            utils.write_value(file, "startTime", startTime)

        assert stopAt in ["endTime", "noWriteNow", "writeNow", "nextWrite"], "stopAt must be 'endTime', 'noWriteNow', 'writeNow', or 'nextWrite'"
        utils.write_value(file, "stopAt", stopAt)

        if stopAt == "endTime":
            assert endTime is not None, "endTime must be specified when stopAt is 'endTime'"
            utils.write_value(file, "endTime", endTime)
        
        utils.write_value(file, "deltaT", deltaT)

        assert writeControl in ["timeStep", "runTime"], "writeControl must be 'timeStep' or 'runTime'"
        utils.write_value(file, "writeControl", writeControl)

        utils.write_value(file, "writeInterval", writeInterval)
        utils.write_value(file, "purgeWrite", purgeWrite)
        utils.write_value(file, "writeFormat", "ascii")
        utils.write_value(file, "writePrecision", 6)
        utils.write_value(file, "writeCompression", "off")
        utils.write_value(file, "timeFormat", "general")
        utils.write_value(file, "timePrecision", 6)
        utils.write_value(file, "runTimeModifiable", "true")