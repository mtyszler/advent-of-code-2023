import pytest

from functions_day_14 import *


def test_parse_input():
    grid = parse_input_file("../input_files/input_day_14_example.txt")

    north = to_north_west(grid)
    adjusted_grid = move_to_left(north)

    load = comp_load(adjusted_grid)
    assert (load == 136)


def test_parse_input_cycles():
    grid = parse_input_file("../input_files/input_day_14_example.txt")

    for c in range(1000000000):

        if c % 100 == 0:
            print(c, 1000000000, c/1000000000*100)
        north = to_north_west(grid)
        grid = move_to_left(north)

        west = to_north_west(grid)
        grid = move_to_left(west)

        south = to_north_west(grid)
        grid = move_to_left(south)

        east = to_north_west(grid)
        grid = move_to_left(east)

    load = comp_load(grid)
    assert (load == 64)

