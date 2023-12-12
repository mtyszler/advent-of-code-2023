import pytest

from functions_day_12 import *


def test_parse_input():
    list_of_records = parse_input_file("../input_files/input_day_12_example.txt")

    assert (list_of_records[1] == (".#...#....###.", [1, 1, 3]))


@pytest.mark.parametrize("record, known_arrangement",
                         [('#.#.###', [1, 1, 3]),
                          ('.#...#....###.', [1, 1, 3]),
                          ('.#.###.#.######', [1, 3, 1, 6]),
                          ('####.#...#...', [4, 1, 1]),
                          ('#....######..#####.', [1, 6, 5]),
                          ('.###.##....#', [3, 2, 1])
                          ])
def test_arrangement(record, known_arrangement):
    arrangement = identify_arrangement(record)

    assert (arrangement == known_arrangement)


@pytest.mark.parametrize("record, known_arrangement, possibilities",
                         [('???.###', [1, 1, 3], 1),
                          ('.??..??...?##.', [1, 1, 3], 4),
                          ('?#?#?#?#?#?#?#?', [1, 3, 1, 6], 1),
                          ('????.#...#...', [4, 1, 1], 1),
                          ('????.######..#####.', [1, 6, 5],  4),
                          ('?###????????', [3, 2, 1], 10),
                          ('???????##?????#?#?',[9,6], 5)
                          ])
def test_possibilities(record, known_arrangement, possibilities):

    valid_arrangements = solve_row(record, known_arrangement)

    assert (len(valid_arrangements) == possibilities)


def test_possibilities_from_file():

    list_of_records = parse_input_file("../input_files/input_day_12_example2.txt")
    total = 0
    for this_entry in list_of_records:
        total += len(solve_row(this_entry[0], this_entry[1]))

    assert (total == 21)


def test_possibilities_from_file_expansion():

    list_of_records = parse_input_file("../input_files/input_day_12_example2.txt", expansion=5)
    total = 0
    for this_entry in list_of_records:
        total += len(solve_row(this_entry[0], this_entry[1]))

    assert (total == 525152)
