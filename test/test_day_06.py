import pytest

from functions_day_06 import *


@pytest.mark.parametrize("charge, race, response",
                         [(0, 7, 0),
                          (1, 7, 6),
                          (2, 7, 10),
                          (3, 7, 12),
                          (4, 7, 12),
                          (5, 7, 10),
                          (6, 7, 6),
                          (7, 7, 0),
                          ])
def test_distances(charge, race, response):
    this_distance = distance(charge, race)
    assert (this_distance == response)


@pytest.mark.parametrize("race, record, response",
                         [(7, 9,  4),
                          (15, 40,  8),
                          (30, 200,  9),
                          (71530, 940200,  71503)
                          ])
def test_possible_wins(race, record, response):
    this_options = cross_points(race, record)
    assert (this_options == response)
