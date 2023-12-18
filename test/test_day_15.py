import pytest

from functions_day_15 import *


def test_parse_input():
    current_value = hash_algorithm('HASH')
    assert (current_value == 52)


def test_parse():
    inputs = parse_input_file('../input_files/input_day_15_example.txt')

    assert (inputs[4] == 'qp-')


def test_input():
    inputs = parse_input_file('../input_files/input_day_15_example.txt')

    total = 0
    for j in inputs:
        total += hash_algorithm(j)

    assert (total == 1320)


def test_input():
    inputs = parse_input_file('../input_files/input_day_15_example.txt')

    boxes = prep_boxes(inputs)

    total = 0
    for i in range(256):
        box_content = boxes[i]
        for idx, content in enumerate(box_content):
            total += (i+1) * (idx + 1) * content[1]

    assert (total == 145)
