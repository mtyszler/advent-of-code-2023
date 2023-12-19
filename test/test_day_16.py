import pytest

from functions_day_16 import *


def test_parse():
    grid = parse_input_file('../input_files/input_day_16_example.txt')

    energized, total = move_light(grid, test=True)

    assert (total == 46)