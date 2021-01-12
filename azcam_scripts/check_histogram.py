"""
Histogram check for ADC
"""

import sys

import numpy

import azcam
from azcam.image import Image


def check_histogram(filename):

    im1 = Image(filename)
    im1.assemble(1)
    data = im1.buffer

    # make histogram
    HistY, HistX = numpy.histogram(data, bins="auto")  # bins,edges -> Y[N],X[N+1]
    centers = (HistX[:-1] + HistX[1:]) / 2  # centers of bins

    # plot
    fig, ax = azcam.plot.plt.subplots(constrained_layout=True)
    azcam.plot.plt.semilogy([int(x) for x in centers], HistY)
    xlabel = "Value"
    ylabel = "Events"
    title = "Image Histogram"
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    azcam.plot.plt.ylim(1)
    ax.grid(True)
    azcam.plot.plt.show()

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    check_histogram(*args)
