"""
Save a sequence of FITS images as png files.
"""

import os
import sys
import winsound

import azcam
from azcam.image import Image


def plot_images(folder="."):

    FreqYES = 2000  # Set Frequency
    DurYES = 500  # Set Duration

    print("")
    print("Plotting all files in the current folder")
    print("")

    # get gain for scaling - TODO: fix me
    if not azcam.api.gain.valid:
        azcam.api.gain.read_datafile("../gain/gain.txt")

    # loop through files
    QUIT = 0
    count = 0
    for root, topfolders, filenames in os.walk("."):

        if QUIT:
            break

        images = {}
        for filename in filenames:
            if not filename.endswith(".fits"):
                continue
            winsound.Beep(FreqYES, DurYES)
            f = os.path.join(root, filename)

            azcam.api.display.display(f)
            azcam.api.display.zoom(0)

            print(f"Filename: {filename}")
            key = azcam.utils.check_keyboard(0)
            if key.lower() == "q":
                QUIT = 1
                break

            images[filename] = Image(f)
            images[filename].set_scaling(
                azcam.api.gain.system_gain,
                azcam.api.gain.zero_mean,
            )
            images[filename].assemble(1)
            # m = images[filename].buffer.mean()
            images[filename].scale_type = "sdev"
            # images[filename].scale_factor = m / 5.0
            implot = azcam.plot.plt.imshow(images[filename].buffer)
            implot.set_cmap("gray")
            azcam.plot.update()
            # newfilename = filename.replace(".fits", ".png")
            # azcam.plot.save_figure(1, newfilename)
            count += 1

            # debug
            if count == -1:
                break

    return images


# returned images is dictionary of images by filename key
if __name__ == "__main__":
    args = sys.argv[1:]
    images = plot_images(*args)