import os
import sys
import importlib

import azcam

folder = os.path.dirname(__file__)
sys.path.append(folder)

# bring all .py modules with same function name into namespace
_, _, filenames = next(os.walk(folder))
pyfiles = []
for files in filenames:
    if files.endswith(".py"):
        pyfiles.append(files[:-3])
pyfiles.remove("__init__")
pyfiles.remove("load_scripts")
pyfiles.remove("all_scripts")

__all__ = []
for pfile in pyfiles:
    try:
        mod = importlib.import_module(f"azcam_scripts.{pfile}")
        func = getattr(mod, pfile)
        globals()[pfile] = func
        __all__.append(pfile)
    except Exception:
        azcam.AzcamWarning(f"Could not import script {pfile}")
