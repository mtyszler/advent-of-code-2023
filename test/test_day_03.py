import pytest
import math

from functions_day_03 import *


def test_parse_input():
    df = parse_input_file('../input_files/input_day_03_example.txt')


def test_find_numbers():
    df = parse_input_file('../input_files/input_day_03_example.txt')
    part_numbers = find_part_numbers(df)

    assert (sum(part_numbers) == 4361)


def test_find_gear_ratios():
    df = parse_input_file('../input_files/input_day_03_example.txt')
    part_numbers = find_gear_ratios(df)

    assert (sum(part_numbers) == 467835)