"""
Continuously read detector temperatures until 'q' is pressed.
Prints date/time, relative seconds, and temperatures in Celsius.
Optionally plots data.
"""

import datetime
import sys
import time

import azcam


def get_temps(delay=10.0, logfile="get_temps.log", plottemps=1):

    plot_range = [-200, 30]

    # inputs
    delay = azcam.db.config.get_script_par(
        "get_temps", "delay", "prompt", "Enter delay time in seconds", delay
    )

    logfile = azcam.db.config.get_script_par(
        "get_temps",
        "logfile",
        "prompt",
        "Enter log file name or N to skip logging",
        logfile,
    )
    if logfile == ".":
        reply = azcam.utils.file_browser(logfile, [("all files", ("*.*"))])
        logfile = reply[0]

    plottemps = azcam.db.config.get_script_par(
        "get_temps", "plottemps", "prompt", "Enter 1 to plot data", plottemps
    )

    delay = float(delay)
    plottemps = int(plottemps)

    # display header and open log file
    s = "#Date and Time         Secs   CamTemp  DewTemp  Temp3   Temp4"
    print(s)
    if logfile.lower() != "n":
        lfile = open(logfile, "w")
        lfile.write(s + "\n")

    timestart = datetime.datetime.now()

    if plottemps:
        # setup plot
        fig = azcam.plot.plt.figure()
        fignum = fig.number
        azcam.plot.move_window(fignum)
        sub = azcam.plot.plt.subplot(111)
        sub.grid(1)
        azcam.plot.plt.title("System Temperatures")
        azcam.plot.plt.ylabel("Temperature [C]")
        azcam.plot.plt.xlabel("Time [secs]")
        sub.set_ylim(plot_range[0], plot_range[1])
        azcam.plot.update()

    # loop
    times = []
    temps1 = []
    temps2 = []
    temps3 = []
    temps4 = []
    reply = "OK"

    while 1:

        key = azcam.utils.check_keyboard()
        if key == "q":
            break

        # on an error, just keep going
        temps = azcam.db.tempcon.get_temperatures()

        for _ in range(max(0, 4 - len(temps))):
            temps.append(0.0)
        for i, temp in enumerate(temps):  # put in a decent plot range
            temps[i] = max(temp, plot_range[0])
        timenow = datetime.datetime.now()
        secs = timenow - timestart
        timenow = str(timenow)[:-5]
        secslist = str(secs).split(":")
        secs1 = float(secslist[0]) * 3600 + float(secslist[1]) * 60 + float(secslist[2])
        t0 = float(temps[0])
        t1 = float(temps[1])
        t2 = float(temps[2])
        t3 = float(temps[3])
        temps1.append(t0)
        temps2.append(t1)
        temps3.append(t2)
        temps4.append(t3)
        times.append(secs1)
        s = "%s  %.1f    %-6.1f   %-6.1f   %-6.1f  %-6.1f" % (
            timenow,
            secs1,
            t0,
            t1,
            t2,
            t3,
        )
        print(s)

        if logfile.lower() != "n":
            lfile.write(s + "\n")
            lfile.flush()

        # plot data
        if plottemps:
            if len(azcam.plot.plt.gca().lines) > 3:
                del azcam.plot.plt.gca().lines[-4:]  # erase old lines
            azcam.plot.plt.plot(times, temps1, azcam.plot.style_lines[0])
            azcam.plot.plt.plot(times, temps2, azcam.plot.style_lines[1])
            azcam.plot.plt.plot(times, temps3, azcam.plot.style_lines[2])
            azcam.plot.plt.plot(times, temps4, azcam.plot.style_lines[3])
            # update in real time
            azcam.plot.update()

        # delay
        time.sleep(delay)

        if plottemps:
            azcam.plot.plt.plot(times, temps1, azcam.plot.style_lines[0])
            azcam.plot.plt.plot(times, temps2, azcam.plot.style_lines[1])
            # azcam.plot.plt.plot(times,temps3,azcam.plot.style_lines[2])
            # azcam.plot.plt.plot(times,temps4,azcam.plot.style_lines[3])
            sub.set_ylim(plot_range[0], plot_range[1])

            azcam.plot.save_figure(fignum, "gettemps.png")

    # close
    if logfile.lower() != "n":
        lfile.close()

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    get_temps(*args)
