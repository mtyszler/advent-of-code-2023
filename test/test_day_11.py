import pytest

from functions_day_11 import *


def test_parse_input():
    stars = parse_input_file("../input_files/input_day_11_example.txt")

    assert (stars[1] == (1, 7))


def test_parse_input_v2():
    stars = parse_input_file("../input_files/input_day_11_example.txt")

    assert (stars[3] == (4, 6))

    stars_expanded = expand_galaxy(stars)

    assert (stars_expanded[3] == (5, 8))


@pytest.mark.parametrize("pair, response",
                         [([5, 9], 9),
                          ([1, 7], 15),
                          ([3, 6], 17),
                          ([8, 9], 5)
                          ])
def test_some_distances(pair, response):
    stars = parse_input_file("../input_files/input_day_11_example.txt")
    stars_expanded = expand_galaxy(stars)
    dist = manhattan_adj(stars_expanded[pair[0]-1], stars_expanded[pair[1]-1])

    assert (dist == response)


def test_dist():
    stars = parse_input_file("../input_files/input_day_11_example.txt")
    stars_expanded = expand_galaxy(stars)

    total = all_distances(stars_expanded)

    assert (total == 374)


def test_dist_bigger_expansion():
    stars = parse_input_file("../input_files/input_day_11_example.txt")
    stars_expanded = expand_galaxy(stars, 10-1)

    total = all_distances(stars_expanded)

    assert (total == 1030)


def test_dist_even_bigger_expansion():
    stars = parse_input_file("../input_files/input_day_11_example.txt")
    stars_expanded = expand_galaxy(stars, 100-1)

    total = all_distances(stars_expanded)

    assert (total == 8410)
