import pytest

from functions_day_05 import *


def test_parse_input_v2():
    lowest_location = parse_input_file_v2('../input_files/input_day_05_example.txt')
    assert (lowest_location == 35)


def test_parse_input_v3():
    lowest_location = parse_input_file_v3('../input_files/input_day_05_example.txt')
    assert (lowest_location == 46)


def test_find_ranges():
    new_ranges = find_ranges((79,79+14), {(98, 100): (50, 52), (50, 98): (52, 100)})
    assert (new_ranges == [(81,81+14)])