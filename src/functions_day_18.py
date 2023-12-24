def parse_input_file(input_file: str) -> list[(str, int, str)]:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    instructions = []
    for this_line in lines:
        direction, amount, color = this_line.strip().split(" ")
        instructions.append((direction, int(amount), color.split("(")[1].split(")")[0]))

    return instructions


def find_nodes(instructions: list[(str, int, str)]) -> [list[(int, int)], int]:
    edges = [(0, 0)]
    current_node = (0, 0)
    edge_points = 0
    for next_one in instructions:
        direction, amount, color = next_one
        edge_points += amount
        if direction == 'R':
            next_node = (current_node[0] + amount, current_node[1])
        elif direction == 'L':
            next_node = (current_node[0] - amount, current_node[1])
        elif direction == 'D':
            next_node = (current_node[0], current_node[1] + amount)
        elif direction == 'U':
            next_node = (current_node[0], current_node[1] - amount)
        else:
            raise Exception("unknown direction")

        if next_node not in edges:
            edges.append(next_node)
        current_node = next_node

    min_x = min([x[0] for x in edges])
    min_y = min([x[1] for x in edges])

    if min_x < 0 or min_y < 0:
        new_edges = []
        for this_node in edges:
            new_edges.append((this_node[0] - min_x, this_node[1] - min_y))
        edges = new_edges

    return edges, edge_points


def find_nodes_full(instructions: list[(str, int, str)]) -> list[(int, int)]:
    edges = [(0, 0)]
    current_node = (0, 0)
    for next_one in instructions:
        direction, amount, color = next_one
        if direction == 'R':
            for x in range(amount):
                next_node = (current_node[0] + x + 1, current_node[1])
                if next_node not in edges:
                    edges.append(next_node)
        elif direction == 'L':
            for x in range(amount):
                next_node = (current_node[0] - (x + 1), current_node[1])
                if next_node not in edges:
                    edges.append(next_node)
        elif direction == 'D':
            for x in range(amount):
                next_node = (current_node[0], current_node[1] + x + 1)
                if next_node not in edges:
                    edges.append(next_node)
        elif direction == 'U':
            for x in range(amount):
                next_node = (current_node[0], current_node[1] - (x + 1))
                if next_node not in edges:
                    edges.append(next_node)
        else:
            raise Exception("unknown direction")

        current_node = next_node

    min_x = min([x[0] for x in edges])
    min_y = min([x[1] for x in edges])

    if min_x < 0 or min_y < 0:
        new_edges = []
        for this_node in edges:
            new_edges.append((this_node[0] - min_x, this_node[1] - min_y))
        edges = new_edges

    return edges


def find_nodes_hex(instructions: list[(str, int, str)]) -> [list[(int, int)], int]:
    edges = [(0, 0)]
    current_node = (0, 0)
    edge_points = 0
    for next_one in instructions:
        direction_wrong, amount_wrong, color = next_one

        amount = int('0x' + color[1:6], 0)
        direction_coded = color[-1]

        edge_points += amount

        if direction_coded == '0':
            next_node = (current_node[0] + amount, current_node[1])
        elif direction_coded == '2':
            next_node = (current_node[0] - amount, current_node[1])
        elif direction_coded == '1':
            next_node = (current_node[0], current_node[1] + amount)
        elif direction_coded == '3':
            next_node = (current_node[0], current_node[1] - amount)
        else:
            raise Exception("unknown direction")

        if next_node not in edges:
            edges.append(next_node)
        current_node = next_node

    min_x = min([x[0] for x in edges])
    min_y = min([x[1] for x in edges])

    if min_x < 0 or min_y < 0:
        new_edges = []
        for this_node in edges:
            new_edges.append((this_node[0] - min_x, this_node[1] - min_y))
        edges = new_edges

    return edges, edge_points


def compute_lava(nodes: list[(int, int)]) -> float:
    # compute area using shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    A = 0
    for i in range(len(nodes) - 1):
        A += nodes[i][1] * nodes[i + 1][0] - \
             nodes[i + 1][1] * nodes[i][0]
    A += nodes[len(nodes) - 1][1] * nodes[0][0] - \
         nodes[0][1] * nodes[len(nodes) - 1][0]

    A = abs(A / 2)

    # pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    # A = i + b/2 -1
    # i = A - b/2 + 1

    interior_points = A - len(nodes) / 2 + 1

    return interior_points + len(nodes)


def compute_lava_only_edges(nodes: list[(int, int)], edge_points: int) -> float:
    # compute area using shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    A = 0
    for i in range(len(nodes) - 1):
        A += nodes[i][1] * nodes[i + 1][0] - \
             nodes[i + 1][1] * nodes[i][0]
    A += nodes[len(nodes) - 1][1] * nodes[0][0] - \
         nodes[0][1] * nodes[len(nodes) - 1][0]

    A = abs(A / 2)

    # pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    # A = i + b/2 -1
    # i = A - b/2 + 1

    interior_points = A - edge_points / 2 + 1

    return interior_points + edge_points
