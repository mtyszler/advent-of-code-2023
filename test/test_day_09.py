import pytest

from functions_day_09 import *


@pytest.mark.parametrize("this_list, response",
                         [([0, 3, 6, 9, 12, 15], 18),
                          ([1, 3, 6, 10, 15, 21], 28),
                          ([10, 13, 16, 21, 30, 45], 68)
                          ])
def test_find_next(this_list, response):
    new_lists = process_seq(this_list)

    next_value = find_next_number(new_lists)

    assert (next_value == response)


def test_from_input():
    all_values = find_all_next_numbers("../input_files/input_day_09_example.txt")
    total = sum(all_values)

    assert (total == 114)


def test_from_input_left():
    all_values = find_all_next_numbers_left("../input_files/input_day_09_example.txt")
    total = sum(all_values)

    assert (total == 2)
