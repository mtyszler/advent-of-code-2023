import pytest

from functions_day_25 import *


def test_crossings():
    from_to = parse_input_file('../input_files/input_day_25_example.txt')

    assert (from_to['pzl'] == {'lsr', 'hfx', 'nvd', 'rsh'})


def test_connections():
    from_to = parse_input_file('../input_files/input_day_25_example.txt')
    check = find_intersections(from_to)

    assert(len(check[0])*len(check[1]) == 54)
