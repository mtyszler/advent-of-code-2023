import pytest

from functions_day_17 import *


def test_parse_height_map():
    grid_height = parse_heat_map('../input_files/input_day_17_example.txt')


def test_find_top():
    grid_heat = parse_heat_map('../input_files/input_day_17_example.txt')
    best_distance = find_exit(grid_heat,
                                         start_location=[(0,0),['r','d']],
                                         target_location=(12,12))

    assert (best_distance == 102)


def test_find_top2():
    grid_heat = parse_heat_map('../input_files/input_day_17_example.txt')
    best_distance = find_exit_2(grid_heat,
                                         start_location=[(0,0),['r','d']],
                                         target_location=(12,12))

    assert (best_distance == 94)