import operator

import pytest

from functions_day_08 import *


def test_instructions_1():
    instructions, nodes = parse_input_file("../input_files/input_day_08_example_1.txt")
    n_steps = follow_path(instructions, nodes)

    assert (n_steps == 2)


def test_instructions_2():
    instructions, nodes = parse_input_file("../input_files/input_day_08_example_2.txt")
    n_steps = follow_path(instructions, nodes)

    assert (n_steps == 6)


def test_instructions_3():
    instructions, nodes = parse_input_file("../input_files/input_day_08_example_3.txt")
    n_steps = follow_path_ghost(instructions, nodes)

    assert (n_steps == 6)

