import pytest

from functions_day_23 import *


def test_parse_height_map():
    grid = parse_heat_map('../input_files/input_day_23_example.txt')


def test_find_top():
    grid = parse_heat_map('../input_files/input_day_23_example.txt')
    best_distance = find_exit(grid,
                              start_location=(0, 1),
                              target_location=(22, 21))

    assert (best_distance == -94)


def test_find_top_2():
    grid = parse_heat_map('../input_files/input_day_23_example.txt')
    best_distance = find_exit_dfs(grid,
                              start_location=(0, 1),
                              target_location=(22, 21))

    assert (best_distance == 154)
