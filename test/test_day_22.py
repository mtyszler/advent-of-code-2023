import pytest

from functions_day_22 import *


def test_parse():
    positions, grid = parse_input('../input_files/input_day_22_example.txt')

    assert (grid[1, 1, 1] == 'idx_1')
    assert (grid[8, 1, 1] == 'idx_7')


def test_fall():
    positions, grid = parse_input('../input_files/input_day_22_example.txt')

    new_positions, new_grid = drop_blocks(positions, grid)

    can_desintegrate = desintegrate(new_positions, new_grid)

    assert (len(can_desintegrate) == 5)


def test_fall_full():
    positions, grid = parse_input('../input_files/input_day_22_example.txt')

    new_positions, new_grid = drop_blocks(positions, grid)

    cannot_desintegrate = desintegrate_full(new_positions, new_grid)

    assert (cannot_desintegrate['idx_1'] == 6)
    assert (len(cannot_desintegrate) == 2)

    x = sum(cannot_desintegrate.values())

    assert (x == 7)
