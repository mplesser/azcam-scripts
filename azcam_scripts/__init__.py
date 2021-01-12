import os
import sys
import importlib

folder = os.path.dirname(__file__)
sys.path.append(folder)

# bring all .py modules with same function name into namespace
_, _, filenames = next(os.walk(folder))
pyfiles = []
for files in filenames:
    if files.endswith(".py"):
        pyfiles.append(files[:-3])
pyfiles.remove("__init__")


__all__ = []
for pfile in pyfiles:
    mod = importlib.import_module(f"azcam_scripts.{pfile}")
    try:
        func = getattr(mod, pfile)
        globals()[pfile] = func
        __all__.append(pfile)
    except Exception:
        pass

# clean namepace
del folder
