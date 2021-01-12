"""
Usage: Run scan_wavelengths
"""

import sys

import azcam


def scan_wavelengths():

    et = 15 * 60.0

    azcam.api.config.set_par("imagetest", 0)

    for wave in range(800, 1110, 10):

        print("")
        print("Moving to wavelength is %.0f" % float(wave))
        azcam.api.instrument.set_wavelength(wave)
        print("Current wavelength is %.0f" % azcam.api.instrument.get_wavelength())

        print("Exposing...")
        azcam.api.exposure.expose(et, "flat", "wavelength scan: %d" % wave)
        print("Finished")

    # reset
    azcam.api.config.set_par("imagetest", 1)

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    scan_wavelengths(*args)
