import copy

import numpy as np


def parse_input(input_file: str) -> [dict, np.ndarray]:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    positions = {}

    idx = 1
    max_x = 0
    max_y = 0
    max_z = 0
    for this_line in lines:
        st, ed = this_line.strip().split("~")
        st_lst = [int(x) for x in st.split(',')]
        ed_lst = [int(x) for x in ed.split(',')]
        x, y, z = ed_lst
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z
        positions['idx_' + str(idx)] = [st_lst, ed_lst]
        idx += 1

    grid = np.empty([max_z + 1, max_x + 1, max_y + 1], dtype=object)
    for k, v in positions.items():
        s_x, s_y, s_z = v[0]
        e_x, e_y, e_z = v[1]

        for z in range(s_z, e_z + 1):
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    grid[z, x, y] = k

    return positions, grid


def drop_blocks(original_positions: dict, filled_grid: np.ndarray,
                stability_check: bool = False) -> [dict, np.ndarray]:
    grid = filled_grid.copy()
    positions = copy.deepcopy(original_positions)

    changes = True
    while changes:
        changes = False
        for k, v in positions.items():
            s_x, s_y, s_z = v[0]
            e_x, e_y, e_z = v[1]

            # can fall?
            new_z = s_z
            z = s_z
            found_block = False
            for z in range(s_z - 1, 0, -1):
                if found_block:
                    break
                for x in range(s_x, e_x + 1):
                    if found_block:
                        break
                    for y in range(s_y, e_y + 1):
                        if grid[z, x, y] is not None:
                            new_z = z + 1
                            found_block = True
                            break
            if not found_block:
                new_z = z
            if new_z != s_z:
                changes = True
                for oz in range(s_z, e_z + 1):
                    for ox in range(s_x, e_x + 1):
                        for oy in range(s_y, e_y + 1):
                            grid[oz, ox, oy] = None

                for nz in range(s_z - (s_z - new_z), e_z - (s_z - new_z) + 1):
                    for nx in range(s_x, e_x + 1):
                        for ny in range(s_y, e_y + 1):
                            grid[nz, nx, ny] = k

                positions[k] = [[s_x, s_y, s_z - (s_z - new_z)],
                                [e_x, e_y, e_z - (s_z - new_z)]]

                if stability_check:
                    return positions, grid

    return positions, grid


def desintegrate(original_positions: dict, filled_grid: np.ndarray) -> list[str]:
    can_desintegrate = []
    for k, v in original_positions.items():
        grid = filled_grid.copy()
        positions = copy.deepcopy(original_positions)

        s_x, s_y, s_z = v[0]
        e_x, e_y, e_z = v[1]

        for z in range(s_z, e_z + 1):
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    grid[z, x, y] = None

        positions.pop(k)
        new_positions, new_grid = drop_blocks(positions, grid, stability_check=True)

        if new_positions == positions:
            can_desintegrate.append(k)

    return can_desintegrate


def desintegrate_full(original_positions: dict, filled_grid: np.ndarray) -> dict:
    cannot_desintegrate = {}
    for k, v in original_positions.items():
        grid = filled_grid.copy()
        positions = copy.deepcopy(original_positions)

        s_x, s_y, s_z = v[0]
        e_x, e_y, e_z = v[1]

        for z in range(s_z, e_z + 1):
            for x in range(s_x, e_x + 1):
                for y in range(s_y, e_y + 1):
                    grid[z, x, y] = None

        positions.pop(k)
        new_positions, new_grid = drop_blocks(positions, grid)

        if new_positions != positions:
            changes = 0
            for nk in new_positions.keys():
                if new_positions[nk] != positions[nk]:
                    changes += 1

            cannot_desintegrate[k] = changes

    return cannot_desintegrate
