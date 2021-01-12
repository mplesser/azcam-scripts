"""
exposure timing - server-side
"""

import sys
from timeit import default_timer as timer

import azcam


def exposure_timer():

    azcam.api.exposure.begin()
    azcam.api.exposure.integrate()

    start = timer()
    azcam.api.exposure.readout()
    azcam.api.controller.flush()
    end = timer()
    print(end - start)

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    exposure_timer(*args)
