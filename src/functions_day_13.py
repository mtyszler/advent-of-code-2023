import functools
import math

from itertools import product


def parse_input_file(input_file: str) -> list:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    patterns = []
    this_pattern = []
    for this_line in lines:
        if this_line.strip() != '':
            this_pattern.append([x for x in this_line.strip()])
        else:
            patterns.append(this_pattern)
            this_pattern = []

    patterns.append(this_pattern)

    return patterns


def _confirm_reflection_r(found_r_idx, pattern, part2=False) -> bool:
    confirmed_r = True
    total_diff = 0
    for rr in range(found_r_idx):
        onder_r = rr
        boven_r = 2 * found_r_idx - rr - 1
        if boven_r > len(pattern) - 1:
            continue
        if pattern[onder_r] != pattern[boven_r]:
            if part2:
                total_diff += sum([x != y for x, y in zip(pattern[onder_r], pattern[boven_r])])
                if total_diff > 1:
                    break
            else:
                confirmed_r = False
                break

    if part2:
        if total_diff != 1:
            confirmed_r = False

    return confirmed_r


def _confirm_reflection_c(found_c_idx, vertical, part2=False) -> bool:
    confirmed_c = True
    total_diff = 0
    for cc in range(found_c_idx):
        onder_c = cc
        boven_c = 2 * found_c_idx - cc - 1
        if boven_c > len(vertical) - 1:
            continue
        if vertical[onder_c] != vertical[boven_c]:
            if part2:
                total_diff += sum([x != y for x, y in zip(vertical[onder_c], vertical[boven_c])])
                if total_diff > 1:
                    break
            else:
                confirmed_c = False
                break

    if part2:
        if total_diff != 1:
            confirmed_c = False

    return confirmed_c


def find_reflection(pattern: list[list[str]], part2=False) -> [int, str]:
    # find horizontal reflection
    found_r = False
    found_r_idx = 0
    confirmed_r = False
    for r in range(len(pattern) - 1):
        if pattern[r] == pattern[r + 1]:
            new_found_r_idx = r
            confirmed_r = _confirm_reflection_r(new_found_r_idx + 1, pattern, part2)
            if confirmed_r:
                found_r = True
                found_r_idx = new_found_r_idx

        elif part2 and (sum(x != y for x, y in zip(pattern[r], pattern[r + 1])) == 1):
            new_found_r_idx = r
            confirmed_r = _confirm_reflection_r(new_found_r_idx + 1, pattern, part2)
            if confirmed_r:
                found_r = True
                found_r_idx = new_found_r_idx

    found_r_idx += 1

    if not found_r:
        found_r_idx = 0

    # find vertical reflection:
    found_c = False
    found_c_idx = 0
    confirmed_c = False
    vertical = list(map(list, zip(*pattern)))
    for c in range(len(vertical) - 1):
        if vertical[c] == vertical[c + 1]:
            new_found_c_idx = c
            confirmed_c = _confirm_reflection_c(new_found_c_idx + 1, vertical, part2)
            if confirmed_c:
                found_c = True
                found_c_idx = new_found_c_idx

        elif part2 and (sum(x != y for x, y in zip(vertical[c], vertical[c + 1])) == 1):
            new_found_c_idx = c
            confirmed_c = _confirm_reflection_c(new_found_c_idx + 1, vertical, part2)
            if confirmed_c:
                found_c = True
                found_c_idx = new_found_c_idx

    found_c_idx += 1

    if not found_c:
        found_c_idx = 0

    if found_c_idx >= found_r_idx:
        return found_c_idx, 'vertical'
    else:
        return found_r_idx, 'horizontal'
