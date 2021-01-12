"""
test camera controller.
"""

import sys
import time

import azcam


def test_controller(cycles=10):

    cycles = azcam.api.config.get_script_par(
        "test_controller", "cycles", "prompt", "Enter number of test cycles", cycles
    )
    cycles = int(cycles)

    # test board communication
    print("Testing low-level datalink board level communication...")
    reply = azcam.api.server.rcommand("controller.test_datalink")
    print("--> Board communication is communication OK")

    # reset
    print("Testing communication and reset...")
    for loop in range(cycles):
        if loop > 0:
            time.sleep(1)  # delay for Mag DSP file lock
        azcam.api.exposure.reset()
        print(f"Controller reset OK {loop + 1}/{cycles}")
        time.sleep(1)
    print("--> Controller communications and reset OK")

    # temperature
    if int(azcam.api.config.get_par("utilityboardinstalled")):
        print("Testing controller temperature readback...")
        for loop in range(cycles):
            reply = azcam.api.tempcon.get_temperaturess()
            print(
                "Temperatures: %.1f %.1f %.1f: %d/%d"
                % (reply[1], reply[2], reply[3], loop + 1, cycles)
            )
        print("--> Temperature communication OK")

    print("Controller tests finished.")

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    test_controller(*args)
