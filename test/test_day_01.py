import pytest

from functions_day_01 import *


@pytest.mark.parametrize("input_string, response",
                         [("1abc2", 12),
                          ("pqr3stu8vwx", 38),
                          ("a1b2c3d4e5f", 15),
                          ("treb7uchet", 77)])
def test_code_from_string(input_string, response):
    this_response = code_from_string(input_string)
    assert (this_response == response)


def test_full_code_from_string():
    all_codes = parse_input('../input_files/input_day_01_example.txt')
    assert (all_codes == 142)


@pytest.mark.parametrize("input_string, response",
                         [("two1nine", 29),
                          ("abcone2threexyz", 13),
                          ("4nineeightseven2", 42),
                          ("7pqrstsixteen", 76),
                          ("2sevenjqlpprggjlkddqv9oneightpj", 28),
                          ('eighthree', 83),
                          ('sevenine', 79)])
def test_code_from_string_also_text(input_string, response):
    this_response = code_from_string_also_text(input_string)
    assert (this_response == response)


def test_full_code_from_string_also_text():
    all_codes = parse_input_also_text('../input_files/input_day_01a_example.txt')
    assert (all_codes == 281)
