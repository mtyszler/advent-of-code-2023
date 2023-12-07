import operator

import pytest
from functools import reduce

from functions_day_07 import *


@pytest.mark.parametrize("hand,  response",
                         [("AAAAA", 6),
                          ("AA8AA", 5),
                          ("23332", 4),
                          ("TTT98", 3),
                          ("23432", 2),
                          ("A23A4", 1),
                          ("23456", 0),
                          ])
def test_type_of_hand(hand, response):
    this_type_of_hand = type_of_hand(hand)

    assert (this_type_of_hand == response)


@pytest.mark.parametrize("hand_1, hand_2,  response",
                         [("33332", "2AAAA", "33332"),
                          ("77888", "77788", "77888")
                          ])
def test_highest_hand(hand_1, hand_2, response):
    highest_hand = winning_hand(hand_1, hand_2)
    assert (highest_hand == response)


def test_value_of_hands():
    list_of_hands = parse_input_file("../input_files/input_day_07_example.txt")
    ordered_hands = order_hands(list_of_hands)

    values = [x * y for x, y in zip([w[1] for w in ordered_hands], range(1, len(ordered_hands) + 1))]
    assert (6440 == sum(values))


def test_value_of_hands_joker():
    list_of_hands = parse_input_file("../input_files/input_day_07_example.txt")
    ordered_hands = order_hands_joker(list_of_hands)

    values = [x * y for x, y in zip([w[1] for w in ordered_hands], range(1, len(ordered_hands) + 1))]
    assert (5905 == sum(values))