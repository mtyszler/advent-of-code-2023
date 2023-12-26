import pytest

from functions_day_21 import *


def test_parse():
    grid, start_location = parse_input('../input_files/input_day_21_example.txt')

    assert (start_location == (5, 5))


def test_steps():
    grid, start_location = parse_input('../input_files/input_day_21_example.txt')
    n_garden = find_possibilities(grid, start_location, n_steps=6)

    assert (n_garden == 16)
