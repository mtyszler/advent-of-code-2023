import pytest

from functions_day_13 import *


def test_parse_input():
    list_of_records = parse_input_file("../input_files/input_day_13_example.txt")

    pass


def test_reflections():
    list_of_records = parse_input_file("../input_files/input_day_13_example.txt")
    p1 = find_reflection(list_of_records[0])
    p2 = find_reflection(list_of_records[1])

    assert (p1[0] == 5)
    assert (p2[0] == 4)


def test_total():

    total = 0
    list_of_records = parse_input_file("../input_files/input_day_13_example.txt")
    for p in list_of_records:
        score, direction = find_reflection(p)
        if direction == 'vertical':
            total +=score
        elif direction == 'horizontal':
            total += 100*score

    assert (total == 405)


def test_total_p2():

    total = 0
    list_of_records = parse_input_file("../input_files/input_day_13_example.txt")
    for p in list_of_records:
        score, direction = find_reflection(p, part2=True)
        if direction == 'vertical':
            total +=score
        elif direction == 'horizontal':
            total += 100*score

    assert (total == 400)