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
    checked = [grid]
    counter = 0
    repeated = False
    for c in range(1000000000):

        north = to_north_west(grid)
        grid = move_to_left(north)

        west = to_north_west(grid)
        grid = move_to_left(west)

        south = to_south(grid)
        grid = move_to_left(south)

        east = to_east(grid)
        grid = move_to_left(east)
        flipped = []
        for x in grid:
            x.reverse()
            flipped.append(x)
        grid = flipped
        counter += 1
        if grid in checked:
            print("repeat", checked.index(grid))
            key = checked.index(grid)
            f_key = (1000000000 - (key + 1)) % (counter - key) + key + 1
            repeated = True

        else:
            checked.append(grid)
            #        print(counter, comp_load(to_north_west(grid)))

        if repeated:
            break

    load = comp_load(to_north_west(checked[f_key]))
    assert (load == 64)

