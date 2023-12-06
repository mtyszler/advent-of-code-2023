import pytest

from functions_day_05 import *


def test_parse_input():
    lowest_location = parse_input_file('../input_files/input_day_05_example.txt')
    assert (lowest_location == 35)


def test_parse_input_v2():
    lowest_location = parse_input_file_v2('../input_files/input_day_05_example.txt')
    assert (lowest_location == 35)


def test_parse_input_v3():
    lowest_location = parse_input_file_v3('../input_files/input_day_05_example.txt')
    assert (lowest_location == 46)