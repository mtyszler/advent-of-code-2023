import pytest

from functions_day_04 import *


def test_parse_input():
    total = parse_input_file('../input_files/input_day_04_example.txt')
    assert (total == 13)


def test_parse_input_v2():
    total = parse_input_file_v2('../input_files/input_day_04_example.txt')
    assert (total == 30)