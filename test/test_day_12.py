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

    assert (arrangement[0] == known_arrangement)


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
    list_of_records_1 = parse_input_file("../input_files/input_day_12_example2.txt", expansion=1)
    list_of_records_2 = parse_input_file("../input_files/input_day_12_example2.txt", expansion=2)
    total = 0
    for original_entry, this_entry in zip(list_of_records_1, list_of_records_2):
        print(this_entry)
        len_1 = len(solve_row(original_entry[0], original_entry[1]))
        len_2 = len(solve_row(this_entry[0], this_entry[1]))

        factor = len_2/len_1
        check = len_1*factor*factor*factor*factor
        total += check

    assert (total == 525152)


def test_1():
    a =solve_row_v2('???.###', [1,1,3])
    assert (len(a)==1)

def test_2():
    a = solve_row('?????#???????????#?#??????#???????????#?#', [1,4,1,2,1,1,1,4,1,2,1,1])
    assert (len(a)==1)
