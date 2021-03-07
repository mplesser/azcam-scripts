import imp
import importlib
import sys
import os

import azcam


def load(scripts="all") -> None:
    """
    Load all scripts from folder into azcam.db.cli_tools
    If package is True then folder is an installed package name.
    """

    folder = "azcam_scripts"
    rootpackage = folder
    _, folder, _ = imp.find_module(folder)
    if folder not in sys.path:
        sys.path.append(folder)

    # bring all .py modules with same function name into namespace
    _, _, filenames = next(os.walk(folder))
    pyfiles = []
    for files in filenames:
        if files.endswith(".py"):
            pyfiles.append(files[:-3])
    if "__init__" in pyfiles:
        pyfiles.remove("__init__")
    if "scripts" in pyfiles:
        pyfiles.remove("scripts")

    for pfile in pyfiles:
        try:
            mod = importlib.import_module(f"{rootpackage}.{pfile}")
            func = getattr(mod, pfile)
            azcam.db.cli_tools[pfile] = func
        except Exception as e:
            print(e)
            azcam.AzcamWarning(f"Could not import script {pfile}")

    return
