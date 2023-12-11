import pytest

from functions_day_10 import *


def test_parse_input():
    full_map, start = parse_input_file("../input_files/input_day_10_example.txt")

    assert (start == (1, 1))


def test_parse_map():
    full_map, start = parse_input_file("../input_files/input_day_10_example.txt")
    max_location, nodes = trace_map(full_map, start)

    assert (max_location == 4)


def test_parse_map_2():
    full_map, start = parse_input_file("../input_files/input_day_10_example2.txt")
    max_location, nodes = trace_map(full_map, start)

    assert (max_location == 8)


def test_parse_map_3():
    full_map, start = parse_input_file("../input_files/input_day_10_example.txt")
    max_location, nodes = trace_map(full_map, start)
    n_points_inside = points_inside(full_map, nodes, start, max_location)

    assert (n_points_inside == 1)


def test_parse_map_3a():
    full_map, start = parse_input_file("../input_files/input_day_10_example3.txt")
    max_location, nodes = trace_map(full_map, start)
    n_points_inside = points_inside(full_map, nodes, start, max_location)

    assert (n_points_inside == 4)


def test_parse_map_3b():
    full_map, start = parse_input_file("../input_files/input_day_10_example4.txt")
    max_location, nodes = trace_map(full_map, start)
    n_points_inside = points_inside(full_map, nodes, start, max_location)

    assert (n_points_inside == 4)


def test_parse_map_3c():
    full_map, start = parse_input_file("../input_files/input_day_10_example5.txt")
    max_location, nodes = trace_map(full_map, start)
    n_points_inside = points_inside(full_map, nodes, start, max_location)

    assert (n_points_inside == 8)


def test_parse_map_3d():
    full_map, start = parse_input_file("../input_files/input_day_10_example6.txt")
    max_location, nodes = trace_map(full_map, start)
    n_points_inside = points_inside(full_map, nodes, start, max_location)

    assert (n_points_inside == 10)