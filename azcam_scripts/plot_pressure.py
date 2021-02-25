"""
plot pressure
"""

import datetime
import sys
import time

import azcam


def plot_pressure(delay=1.0):

    # setup plot
    sub = azcam.plot.plt.subplot(111)
    sub.grid(1)
    azcam.plot.plt.title("Dewar Pressure")
    azcam.plot.plt.ylabel("Pressure[C]")
    azcam.plot.plt.xlabel("Time [secs]")
    # sub.set_ylim(1.e-7, 1.e-2)

    times = []
    pressures = []

    timestart = datetime.datetime.now()

    loop = 1
    print("Secs\t\tPressure")
    while loop:

        timenow = datetime.datetime.now()
        s = str(timenow)
        secs = timenow - timestart
        secs1 = secs.total_seconds()
        #timenow = str(timenow)[:-5]
        #secslist = str(secs).split(":")
        #secs1 = float(secslist[0]) * 3600 + float(secslist[1]) * 60 + float(secslist[2])
        times.append(secs1)

        p = azcam.db.instrument.get_pressures()[0]
        pressures.append(p)

        print(f"{secs1:.0f}\t\t{p:.2e}\t\t{s}")

        azcam.plot.plt.semilogy(times, pressures, azcam.plot.style_lines[0])
        azcam.plot.plt.plot(times, pressures, azcam.plot.style_lines[0])

        azcam.plot.update()

        if azcam.utils.check_keyboard() == "q":
            break

        time.sleep(delay)

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    plot_pressure(*args)
