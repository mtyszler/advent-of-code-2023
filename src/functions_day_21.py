import numpy as np


def parse_input(input_file: str) -> [np.ndarray, list[int, int]]:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    grid_raw = []

    r = 0
    for this_line in lines:
        if 'S' in this_line:
            s_row = r
            s_col = max([idx for idx, val in enumerate([x for x in this_line.strip()]) if val == 'S'])
        grid_raw.append([x for x in this_line.strip()])
        r += 1

    return np.array(grid_raw), [s_row, s_col]


def find_possibilities(grid: np.ndarray, start_location: list[int, int], n_steps: int) -> int:
    if n_steps % 2 == 0:
        mod_check = 0
    else:
        mod_check = 1

    to_check = [[start_location, 0, [0, 0]]]
    garden_plots = set()
    garden_plots.add((start_location[0], start_location[1], 0, 0))

    while len(to_check) > 0:

        this_location, this_steps, this_realm = to_check.pop(0)
        if this_steps == n_steps:
            continue

        this_r, this_c = this_location
        candidates = [[this_r, this_c + 1],
                      [this_r, this_c - 1],
                      [this_r - 1, this_c],
                      [this_r + 1, this_c]]

        for this_candidate in candidates:
            new_realm = this_realm.copy()
            if this_candidate[0] < 0:
                # print(this_candidate)
                # continue
                this_candidate[0] = grid.shape[0] + this_candidate[0]
                new_realm[0] -= 1

            if this_candidate[1] < 0:
                # continue
                # print(this_candidate)
                this_candidate[1] = grid.shape[1] + this_candidate[1]
                new_realm[1] -= 1

            if this_candidate[0] >= grid.shape[0]:
                # print(this_candidate)
                # continue
                this_candidate[0] = this_candidate[0] - grid.shape[0]
                new_realm[0] += 1

            if this_candidate[1] >= grid.shape[1]:
                # print(this_candidate)
                # continue
                this_candidate[1] = this_candidate[1] - grid.shape[1]
                new_realm[1] += 1

            if grid[*this_candidate] == '.' or grid[*this_candidate] == 'S':
                if (this_steps + 1) % 2 == mod_check:
                    if (this_candidate[0], this_candidate[1], this_realm[0], new_realm[1]) not in garden_plots:
                        garden_plots.add((this_candidate[0], this_candidate[1], new_realm[0], new_realm[1]))
                        to_check.append([this_candidate, this_steps + 1, new_realm])
                else:
                    to_check.append([this_candidate, this_steps + 1, new_realm])

    return len(garden_plots), garden_plots


def find_target(grid: np.ndarray,
                start_location: list[int, int],
                target_location: list[int, int],
                tentative_distances: dict) -> dict:
    # initialize:
    to_check = []
    to_check.append((start_location, 0))
    tentative_distances[tuple(start_location)] = 0

    while len(to_check) > 0:
        this_node = to_check.pop(0)
        node, steps = this_node
        if node == target_location:
            return tentative_distances

        this_r = node[0]
        this_c = node[1]
        candidates = [[this_r, this_c + 1],
                      [this_r, this_c - 1],
                      [this_r - 1, this_c],
                      [this_r + 1, this_c]]
        for this_candidate in candidates:
            if this_candidate[0] < 0:
                continue

            if this_candidate[1] < 0:
                continue

            if this_candidate[0] >= grid.shape[0]:
                continue

            if this_candidate[1] >= grid.shape[1]:
                continue

            if grid[*this_candidate] == '#':
                continue

            potential_steps = steps + 1
            if tuple(this_candidate) in tentative_distances.keys():
                if potential_steps < tentative_distances[tuple(this_candidate)]:
                    tentative_distances[tuple(this_candidate)] = potential_steps
                    to_check.append([this_candidate, potential_steps])
            else:
                tentative_distances[tuple(this_candidate)] = potential_steps
                to_check.append([this_candidate, potential_steps])

    return tentative_distances
