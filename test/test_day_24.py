import pytest

from functions_day_24 import *


def test_crossings():
    stones = parse_input_file('../input_files/input_day_24_example.txt')
    equations = make_equations_lines(stones)
    n_crossings = find_crossings(equations, 7, 27)

    assert (n_crossings == 2)


def test_magic():
    stones = parse_input_file('../input_files/input_day_24_example.txt')
    equations, len_stones = make_equations_system(stones)
    magic = find_magic(equations, len_stones)

    assert (sum(magic[0][0:3]) == 47)
