import pytest

from functions_day_18 import *


def test_parse():
    instructions = parse_input_file('../input_files/input_day_18_example.txt')

    assert (instructions[2][0] == "L")


def test_edges():
    instructions = parse_input_file('../input_files/input_day_18_example.txt')
    edges = find_nodes(instructions)
    assert (edges[0][3] == (0 + 6 - 2, 0 + 5))


def test_area():
    instructions = parse_input_file('../input_files/input_day_18_example.txt')
    edges = find_nodes_full(instructions)
    area = compute_lava(edges)
    assert (area == 62)


def test_area_just_edges():
    instructions = parse_input_file('../input_files/input_day_18_example.txt')
    edges, edge_points = find_nodes(instructions)
    area = compute_lava_only_edges(edges, edge_points)
    assert (area == 62)


def test_area_hex():
    instructions = parse_input_file('../input_files/input_day_18_example.txt')
    edges, edge_points = find_nodes_hex(instructions)
    area = compute_lava_only_edges(edges, edge_points)
    assert (area == 952408144115)
