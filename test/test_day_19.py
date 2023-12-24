import pytest

from functions_day_19 import *


def test_parse():
    instructions, parts = parse_input_file('../input_files/input_day_19_example.txt')

    assert (parts[2] == {'x': 2036, 'm': 264, 'a': 79, 's': 2244})
    assert (instructions['in'] == [['s<1351', 'px'], ['qqz']])


def test_check():
    instructions, parts = parse_input_file('../input_files/input_day_19_example.txt')

    test_case_1 = process_part(instructions, parts[0])
    test_case_2 = process_part(instructions, parts[3])

    assert (test_case_1 == True)
    assert (test_case_2 == False)


def test_all_parts():
    instructions, parts = parse_input_file('../input_files/input_day_19_example.txt')

    total = 0
    for part in parts:
        if process_part(instructions, part):
            total += sum(part.values())

    assert (total == 19114)


def test_all_enumerate_parts():
    instructions, parts = parse_input_file('../input_files/input_day_19_example.txt')

    total = slice_instructions(instructions)

    assert (total == 167409079868000)
