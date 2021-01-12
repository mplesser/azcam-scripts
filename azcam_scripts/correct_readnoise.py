"""
correct for system readnoise
"""

import math
import sys

import azcam


def correct_readnoise():
    """
    Correct measured noise for camera system noise.
    measured_noise and gain are lists.
    """

    system_noise = 2.2  # camera system noise in DN

    gain = azcam.api.gain
    measured_noise = gain.noise
    # measured_gain = gain.system_gain

    sensor_noise = []
    for chan, mn in enumerate(measured_noise):
        # mg = measured_gain[chan]
        sn = math.sqrt(mn ** 2 - system_noise ** 2)

        print(
            "Chan: %2d\tGain: %3.12f\tNoise_(DN): %4.1f\tNoise_(e): %4.1f"
            % (chan, mn, sn)
        )

        sensor_noise.append(sn)

    return sensor_noise


if __name__ == "__main__":
    args = sys.argv[1:]
    sensor_noise = correct_readnoise(*args)
