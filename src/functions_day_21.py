import numpy as np


def parse_input(input_file: str) -> [np.ndarray, (int, int)]:
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

    return np.array(grid_raw), (s_row, s_col)


def find_possibilities(grid: np.ndarray, start_location: (int, int), n_steps: int) -> int:
    # assuming even steps
    if n_steps % 2 != 0:
        raise Exception('function works with even n_steps')

    to_check = [[start_location, 0]]
    garden_plots = set([start_location])

    while len(to_check) > 0:

        this_location, this_steps = to_check.pop(0)
        if this_steps == n_steps:
            continue

        this_r, this_c = this_location
        candidates = [(this_r, this_c + 1),
                      (this_r, this_c - 1),
                      (this_r - 1, this_c),
                      (this_r + 1, this_c)]

        for this_candidate in candidates:
            if this_candidate[0] < 0 or this_candidate[1] < 0 or \
                    this_candidate[0] >= grid.shape[0] or this_candidate[1] >= grid.shape[1]:
                continue

            if grid[this_candidate] == '.' or grid[this_candidate] == 'S':
                if (this_steps + 1) % 2 == 0:
                    if this_candidate not in garden_plots:
                        garden_plots.add(this_candidate)
                        to_check.append([this_candidate, this_steps + 1])
                else:
                    to_check.append([this_candidate, this_steps + 1])

    return len(garden_plots)
