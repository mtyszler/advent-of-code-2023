import numpy as np


def parse_heat_map(input_file: str) -> np.ndarray:
    """

    Args:
        input_file:

    Returns:
       list of dict of monkey attributes
    """

    with open(input_file, 'r') as f:
        lines = f.readlines()

    grid_raw = []

    for this_line in lines:
        grid_raw.append([x for x in this_line.strip()])

    return np.array(grid_raw)


def find_exit(grid: np.ndarray, start_location: (int, int),
              target_location: (int, int), ignore_slip: bool = False) -> int:
    tentative_distances = {}  # ((rol,col)): distance
    best_path = {}

    # initialize:
    to_check = []
    to_check.append(start_location)
    tentative_distances[start_location] = 0
    best_path[start_location] = [start_location]

    best_value = np.inf
    while True:
        if len(to_check) == 0:
            return best_value
        node = to_check.pop(0)
        if node == target_location:
            if tentative_distances[node] < best_value:
                best_value = tentative_distances[node]
        node_row, node_col = node
        this_dist = tentative_distances[node]
        this_path = best_path[node].copy()

        if ignore_slip:
            candidates = [
                (node_row, node_col + 1),
                (node_row, node_col - 1),
                (node_row - 1, node_col),
                (node_row + 1, node_col)
            ]
        else:
            if grid[node] == '>':
                candidates = [(node_row, node_col + 1)]
            elif grid[node] == '<':
                candidates = [(node_row, node_col - 1)]
            elif grid[node] == '^':
                candidates = [(node_row - 1, node_col)]
            elif grid[node] == 'v':
                candidates = [(node_row + 1, node_col)]
            else:
                candidates = [
                    (node_row, node_col + 1),
                    (node_row, node_col - 1),
                    (node_row - 1, node_col),
                    (node_row + 1, node_col)
                ]

        for candidate_coord in candidates:
            if candidate_coord[0] < 0 or candidate_coord[1] < 0 or \
                    candidate_coord[0] >= grid.shape[0] or candidate_coord[1] >= grid.shape[1]:
                continue

            candidate_char = grid[candidate_coord]
            if candidate_char == '#':
                continue

            if candidate_coord in this_path:
                continue

            potential_dist = this_dist - 1

            if candidate_coord in tentative_distances.keys():
                if potential_dist < tentative_distances[candidate_coord]:
                    tentative_distances[candidate_coord] = potential_dist
                    to_check.append(candidate_coord)
                    new_path = this_path.copy()
                    new_path.append(candidate_coord)
                    best_path[candidate_coord] = new_path
            else:
                tentative_distances[candidate_coord] = potential_dist
                to_check.append(candidate_coord)
                new_path = this_path.copy()
                new_path.append(candidate_coord)
                best_path[candidate_coord] = new_path


def find_exit_v2(grid_heat: np.ndarray, start_location: [(int, int), list[str]],
              target_location: (int, int)) -> [int, list]:

    tentative_distances = {}  # ((rol,col), direction, repeat): distance
    best_path = {}

    # initialize:
    to_check = []
    for direction in start_location[1]:
        to_check.append((start_location[0], direction))
        tentative_distances[(start_location[0], direction)] = 0
        best_path[(start_location[0], direction)] = [start_location[0]]

    best_value = np.inf
    while True:
        if len(to_check) == 0:
            return best_value
        this_node = to_check.pop(0)
        node, direction = this_node
        if node == target_location:
            if tentative_distances[this_node] < best_value:
                best_value = tentative_distances[this_node]
        node_row, node_col = node
        this_heat = tentative_distances[this_node]
        this_path = best_path[this_node].copy()

        candidates = []
        if direction in ['r', 'd', 'u']:
            candidates.append(((node_row, node_col + 1), 'r'))
        if direction in ['l', 'd', 'u']:
            candidates.append(((node_row, node_col - 1), 'l'))
        if direction in ['r', 'l', 'u']:
            candidates.append(((node_row - 1, node_col), 'u'))
        if direction in ['r', 'l', 'd']:
            candidates.append(((node_row + 1, node_col), 'd'))

        for candidate_coord, candidate_direction in candidates:
            if candidate_coord[0] < 0 or candidate_coord[1] < 0 or \
                    candidate_coord[0] >= grid_heat.shape[0] or candidate_coord[1] >= grid_heat.shape[1]:
                continue

            if grid_heat[candidate_coord] == '#':
                continue

            if candidate_coord in this_path:
                continue

            candidate_heat = -1
            potential_total_heat = candidate_heat + this_heat

            if (candidate_coord, candidate_direction) in tentative_distances.keys():
                if potential_total_heat < tentative_distances[(candidate_coord, candidate_direction)]:
                    tentative_distances[
                        (candidate_coord, candidate_direction)] = potential_total_heat
                    new_path = this_path.copy()
                    new_path.append(candidate_coord)
                    best_path[(candidate_coord, candidate_direction)] = new_path
                    to_check.append((candidate_coord, candidate_direction))
            else:
                tentative_distances[(candidate_coord, candidate_direction)] = potential_total_heat
                new_path = this_path.copy()
                new_path.append(candidate_coord)
                best_path[(candidate_coord, candidate_direction)] = new_path
                to_check.append((candidate_coord, candidate_direction))


def find_exit_dfs(grid: np.ndarray, start_location: (int, int),
              target_location: (int, int)) -> int:

    print()
    paths_to_target = []

    # initialize:
    to_check = []
    to_check.append([start_location])

    best_value = 0
    paths_being_checked = 0
    while True:
        if len(to_check) == 0:
            return best_value - 1
        if len(to_check) != paths_being_checked:
            paths_being_checked = len(to_check)
            print("path being checked:", paths_being_checked)
        path_to_check = to_check.pop()
        node = path_to_check[-1]
        if node == target_location:
            paths_to_target.append(path_to_check)
            if len(path_to_check) > best_value:
                best_value = len(path_to_check)
                print("path being checked:", paths_being_checked)
                print("new best value:", best_value)
        node_row, node_col = node
        this_path = path_to_check.copy()

        candidates = [
            (node_row, node_col + 1),
            (node_row, node_col - 1),
            (node_row - 1, node_col),
            (node_row + 1, node_col)
        ]

        for candidate_coord in candidates:
            if candidate_coord[0] < 0 or candidate_coord[1] < 0 or \
                    candidate_coord[0] >= grid.shape[0] or candidate_coord[1] >= grid.shape[1]:
                continue

            candidate_char = grid[candidate_coord]
            if candidate_char == '#':
                continue

            if candidate_coord in this_path:
                continue

            new_path = this_path.copy()
            new_path.append(candidate_coord)
            to_check.append(new_path)
