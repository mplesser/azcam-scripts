# from Ian

import sys

import numpy as np
from astropy.io import fits as fits_io

import azcam


def check_bits(filename):
    filename = azcam.utils.make_image_filename(filename)
    fits = fits_io.open(filename)
    print("%5s  " % "", end="")
    for bit in range(8):
        print(" bit%d " % bit, end="")
    print("")
    for ext, hdu in enumerate(fits[1:], start=1):
        print("HDU%2d  " % ext, end="")
        data = hdu.data.astype(np.int32)
        npix = float(data.size)
        for bit in range(8):
            nbit = np.sum((data & (1 << bit)) > 0)
            fbit = nbit / npix
            print("%5.3f " % fbit, end="")
        print("")
    print("")


if __name__ == "__main__":
    args = sys.argv[1:]
    check_bits(*args)
