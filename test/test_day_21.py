import pytest

from functions_day_21 import *


def test_parse():
    grid, start_location = parse_input('../input_files/input_day_21_example.txt')

    assert (start_location == [5, 5])


def test_steps():
    grid, start_location = parse_input('../input_files/input_day_21_example.txt')
    n_garden = find_possibilities(grid, start_location, n_steps=6)

    assert (n_garden == 16)

def test_steps_v3():
    grid, start_location = parse_input('../input_files/input_day_21_example.txt')
    n_garden = find_possibilities(grid, start_location, n_steps=10)

    assert (n_garden == 50)
'''
def test_steps_v4():
    grid, start_location = parse_input('../input_files/input_day_21_example.txt')
    n_garden = find_possibilities(grid, start_location, n_steps=50)

    assert (n_garden == 1594)

@pytest.mark.parametrize("steps,  response",
                         [(6, 16),
                          (10, 50),
                          (50, 1594),
                          (100, 6536),
                          (500, 167004),
                          (1000, 558697),
                          (5000, 16733044),
                          ])
def test_steps_v2(steps, response):
    grid, start_location = parse_input('../input_files/input_day_21_example.txt')
    n_garden = find_possibilities(grid, start_location, n_steps=steps)

    assert (n_garden == response)
'''