import numpy as np


def parse_heat_map(input_file: str) -> np.ndarray:
    """

    Args:
        input_file:

    Returns:
       list of dict of monkey attributes
    """

    with open(input_file, 'r') as f:
        first_line = f.readline().strip('\n')

    n = len(first_line)

    grid_heat = np.genfromtxt(input_file,
                              delimiter=np.ones(n, dtype='i'))

    return grid_heat


def find_exit(grid_heat: np.ndarray, start_location: [(int, int), list[str]],
              target_location: [(int, int), list[str]]) -> [int, list]:
    tentative_distances = {}  # ((rol,col), direction, repeat): distance

    # initialize:
    to_check = []
    for direction in start_location[1]:
        to_check.append((start_location[0], direction, 0))
        tentative_distances[(start_location[0], direction, 0)] = 0

    best_value = np.inf
    while True:
        if len(to_check) == 0:
            return best_value
        this_node = to_check.pop(0)
        node, direction, repeat = this_node
        if node == target_location:
            if tentative_distances[this_node] < best_value:
                best_value = tentative_distances[this_node]
        node_row, node_col = node
        this_heat = tentative_distances[this_node]

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
            if candidate_direction == direction:
                candidate_repeat = repeat + 1
                if candidate_repeat > 3:
                    continue
            else:
                candidate_repeat = 1

            if candidate_coord[0] < 0 or candidate_coord[1] < 0 or \
                    candidate_coord[0] >= grid_heat.shape[0] or candidate_coord[1] >= grid_heat.shape[1]:
                continue

            candidate_heat = grid_heat[candidate_coord[0], candidate_coord[1]]
            potential_total_heat = candidate_heat + this_heat

            if (candidate_coord, candidate_direction, candidate_repeat) in tentative_distances.keys():
                if potential_total_heat < tentative_distances[(candidate_coord, candidate_direction, candidate_repeat)]:
                    tentative_distances[
                        (candidate_coord, candidate_direction, candidate_repeat)] = potential_total_heat
                    to_check.append((candidate_coord, candidate_direction, candidate_repeat))
            else:
                tentative_distances[(candidate_coord, candidate_direction, candidate_repeat)] = potential_total_heat
                to_check.append((candidate_coord, candidate_direction, candidate_repeat))


def find_exit_2(grid_heat: np.ndarray, start_location: [(int, int), list[str]],
                target_location: [(int, int), list[str]]) -> [int, list]:
    tentative_distances = {}  # ((rol,col), direction, repeat): distance

    # initialize:
    to_check = []
    for direction in start_location[1]:
        to_check.append((start_location[0], direction, 0))
        tentative_distances[(start_location[0], direction, 0)] = 0

    best_value = np.inf
    while True:
        if len(to_check) == 0:
            return best_value
        this_node = to_check.pop(0)
        node, direction, repeat = this_node
        if node == target_location:
            if tentative_distances[this_node] < best_value:
                best_value = tentative_distances[this_node]
        node_row, node_col = node
        this_heat = tentative_distances[this_node]

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
            if candidate_direction == direction:
                candidate_repeat = repeat + 1
                if candidate_repeat > 10:
                    continue
            elif repeat <= 3:
                continue
            else:
                candidate_repeat = 1

            if candidate_coord[0] < 0 or candidate_coord[1] < 0 or \
                    candidate_coord[0] >= grid_heat.shape[0] or candidate_coord[1] >= grid_heat.shape[1]:
                continue

            candidate_heat = grid_heat[candidate_coord[0], candidate_coord[1]]
            potential_total_heat = candidate_heat + this_heat

            if (candidate_coord, candidate_direction, candidate_repeat) in tentative_distances.keys():
                if potential_total_heat < tentative_distances[(candidate_coord, candidate_direction, candidate_repeat)]:
                    tentative_distances[
                        (candidate_coord, candidate_direction, candidate_repeat)] = potential_total_heat
                    to_check.append((candidate_coord, candidate_direction, candidate_repeat))
            else:
                tentative_distances[(candidate_coord, candidate_direction, candidate_repeat)] = potential_total_heat
                to_check.append((candidate_coord, candidate_direction, candidate_repeat))
