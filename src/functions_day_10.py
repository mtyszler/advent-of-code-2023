def parse_input_file(input_file: str) -> [list[list[str]], (int, int)]:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    full_map = []
    count_rows = 0
    for this_line in lines:
        this_line_as_list = [x for x in this_line.strip()]
        full_map.append(this_line_as_list)
        if 'S' in this_line_as_list:
            s_row = count_rows
            s_col = this_line_as_list.index('S')
        count_rows += 1

    return full_map, (s_row, s_col)


def trace_map(full_map: list[list[str]], start: (int, int)) -> [int, dict]:
    # find direction of S:
    """
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    """

    reached_nodes = {start: 0}
    nodes_to_treat = [[start, 'S', 0]]
    max_count = 0

    keep_on_going = True
    while keep_on_going:
        yet_to_treat = []
        for this_position, this_pipe, this_count in nodes_to_treat:
            candidates = find_continuation_candidates(full_map, this_position, this_pipe)
            keep_on_going = False
            for this_candidate in candidates:
                if this_candidate[0] not in reached_nodes.keys():
                    keep_on_going = True
                    this_candidate.extend([this_count + 1])
                    yet_to_treat.extend([this_candidate])
                    reached_nodes[this_candidate[0]] = this_count + 1

                    if this_count + 1 > max_count:
                        max_count = this_count + 1

        nodes_to_treat = yet_to_treat.copy()

    return max_count, reached_nodes


def find_continuation_candidates(full_map: list[list[str]], position: (int, int), pipe: str) -> list[[(int, int), str]]:
    """
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    """

    n_rows = len(full_map) - 1
    n_cols = len(full_map[0]) - 1

    left = (position[0], position[1] - 1)  # left
    right = (position[0], position[1] + 1)  # right
    top = (position[0] - 1, position[1])  # top
    bottom = (position[0] + 1, position[1])  # bottom

    connections = []

    if 0 <= left[1] <= n_cols:
        left_pipe = full_map[left[0]][left[1]]
        if pipe in ['S', '-', 'J', '7']:
            if left_pipe == '-' or \
                    left_pipe == 'L' or \
                    left_pipe == 'F':
                connections.append([left, left_pipe])

    if 0 <= right[1] <= n_cols:
        right_pipe = full_map[right[0]][right[1]]
        if pipe in ['S', '-', 'L', 'F']:
            if right_pipe == '-' or \
                    right_pipe == 'J' or \
                    right_pipe == '7':
                connections.append([right, right_pipe])

    if 0 <= top[0] <= n_rows:
        top_pipe = full_map[top[0]][top[1]]
        if pipe in ['S', '|', 'L', 'J']:
            if top_pipe == '|' or \
                    top_pipe == '7' or \
                    top_pipe == 'F':
                connections.append([top, top_pipe])

    if 0 <= bottom[0] <= n_rows:
        bottom_pipe = full_map[bottom[0]][bottom[1]]
        if pipe in ['S', '|', '7', 'F']:
            if bottom_pipe == '|' or \
                    bottom_pipe == 'L' or \
                    bottom_pipe == 'J':
                connections.append([bottom, bottom_pipe])

    if len(connections) > 2:
        raise Exception("more than 2 directions found")

    return connections


def points_inside(all_nodes: dict, start: (int, int), max_count: int) -> int:
    # order nodes:
    unchecked_nodes = list(set([x for x in all_nodes.keys()]))
    count = 0
    direction = 'plus'

    unchecked_nodes.remove(start)
    ordered_nodes = [start]

    # find counter-clock from start:
    candidates = [x for x in all_nodes.keys() if all_nodes[x] == count + 1]

    for this_node in candidates:
        if this_node[1] == start[1] - 1 or this_node[0] == start[0] + 1:
            unchecked_nodes.remove(this_node)
            current_node = this_node
            ordered_nodes.append(current_node)
            count += 1

            break

    while len(unchecked_nodes) > 0:
        if direction == 'plus':
            candidates = [x for x in all_nodes.keys() if all_nodes[x] == count + 1]
        else:
            candidates = [x for x in all_nodes.keys() if all_nodes[x] == count - 1]

        for this_node in candidates:
            if (this_node in unchecked_nodes) and \
                    (
                            (this_node[0] == current_node[0] - 1 and this_node[1] == current_node[1]) or
                            (this_node[0] == current_node[0] + 1 and this_node[1] == current_node[1]) or
                            (this_node[1] == current_node[1] - 1 and this_node[0] == current_node[0]) or
                            (this_node[1] == current_node[1] + 1 and this_node[0] == current_node[0])
                    ):
                unchecked_nodes.remove(this_node)
                current_node = this_node
                ordered_nodes.append(current_node)
                if direction == 'plus':
                    count += 1
                else:
                    count -= 1

                if count == max_count:
                    direction = 'min'
                break

    # compute area using shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    A = 0
    for i in range(len(ordered_nodes) - 1):
        A += ordered_nodes[i][1] * ordered_nodes[i + 1][0] - \
             ordered_nodes[i + 1][1] * ordered_nodes[i][0]
    A += ordered_nodes[len(ordered_nodes)-1][1] * ordered_nodes[0][0] - \
             ordered_nodes[0][1] * ordered_nodes[len(ordered_nodes)-1][0]

    A = abs(A / 2)

    # pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    # A = i + b/2 -1
    # i = A - b/2 + 1

    interior_points = A - len(ordered_nodes) / 2 + 1

    return int(interior_points)
