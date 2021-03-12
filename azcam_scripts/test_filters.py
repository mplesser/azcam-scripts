"""
test filter changing
"""

import sys

import azcam


def test_filters(cycles: int = 2, filter_id: int = 0):

    cycles = int(cycles)
    server = azcam.get_tools("server")

    filters = server.command(f"instrument.get_filters {filter_id}")
    print(f"Checking filters for ID {filter_id}: {filters}")

    for filter_name in filters:
        for i in range(cycles):
            print(f"Test cycle {(i+1)}/{cycles} at {filter_name}")
            azcam.db.instrument.set_filter(filter_name, filter_id)
            print(f"Filter postion: {azcam.db.instrument.get_filter(filter_id)}")

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    test_filters(*args)
