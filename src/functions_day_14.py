import functools
import math

from itertools import product


def parse_input_file(input_file: str) -> list:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    patterns = []
    for this_line in lines:
        patterns.append([x for x in this_line.strip()])

    return patterns


def to_north_west(patterns: list[list[str]]) -> list[list[str]]:
    spinned = list(map(list, zip(*patterns)))

    return spinned


def to_south(patterns: list[list[str]]) -> list[list[str]]:
    spinned = list(map(list, zip(*patterns)))

    flipped = []
    for x in spinned:
        x.reverse()
        flipped.append(x)

    return flipped


def to_east(patterns: list[list[str]]) -> list[list[str]]:
    spinned = list(map(list, zip(*patterns)))

    r_spinned = []
    for x in spinned:
        x.reverse()
        r_spinned.append(x)

    new_r_spinned = []
    for r in range(len(r_spinned) - 1, -1, -1):
        new_r_spinned.append(r_spinned[r])

    return new_r_spinned


def move_to_left(grid: list[list[str]]) -> list[list[str]]:
    new_grid = []
    for r in grid:
        new_r = r.copy()
        for p in range(1, len(r)):
            if new_r[p] == 'O':
                got_to_end = True
                for pp in range(p - 1, -1, -1):
                    if new_r[pp] != '.':
                        got_to_end = False
                        break
                new_r[p] = '.'
                if got_to_end:
                    pp = -1
                new_r[pp + 1] = 'O'

        new_grid.append(new_r)

    return new_grid


def comp_load(grid: list[list[str]]) -> int:
    load = 0
    for r in grid:
        r.reverse()
        for idx in range(len(r)):
            if r[idx] == 'O':
                load += idx + 1

    return load
