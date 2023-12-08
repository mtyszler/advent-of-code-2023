def parse_input_file(input_file: str) -> [str, dict]:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    nodes = {}
    instructions_read = False
    for this_line in lines:
        if not instructions_read:
            instructions = this_line.strip()
            instructions_read = True
            continue
        if this_line.strip() == "":
            continue

        this_nodes, this_options = this_line.strip().split(" = ")
        left, right = this_options.strip().split(",")
        left = left.strip().split("(")[1].strip()
        right = right.strip().split(")")[0].strip()

        nodes[this_nodes.strip()] = (left, right)

    return instructions, nodes


def follow_path(instructions: str, nodes: dict) -> int:
    found_end = False
    this_node = 'AAA'
    count_steps = 0

    while not found_end:
        this_instruction = instructions[0]
        instructions = instructions[1:] + instructions[0]

        if this_instruction == 'L':
            this_node = nodes[this_node][0]
        else:
            this_node = nodes[this_node][1]

        count_steps += 1

        if this_node == 'ZZZ':
            found_end = True

    return count_steps


def follow_path_ghost(instructions: str, nodes: dict) -> int:
    these_nodes = [x for x in nodes.keys() if x[2] == 'A']

    counts = []
    ends = []

    for this_node in these_nodes:
        this_count, this_end = follow_path_ghost_single_start(this_node, instructions, nodes)
        counts.append(this_count)
        ends.append(this_end)

    count_steps = counts[0]
    for b in counts[1:]:
        count_steps = lcm(count_steps, b)

    return count_steps


def follow_path_ghost_single_start(start: str, instructions: str, nodes: dict) -> [int, str]:
    found_end = False
    this_node = start
    count_steps = 0

    while not found_end:
        this_instruction = instructions[0]
        instructions = instructions[1:] + instructions[0]

        if this_instruction == 'L':
            this_node = nodes[this_node][0]
        else:
            this_node = nodes[this_node][1]

        count_steps += 1

        if this_node[2] == 'Z':
            found_end = True

    return count_steps, this_node


# https://www.scaler.com/topics/lcm-of-two-numbers-in-python/


def gcd(a, b):
    if a == 0:
        return b
    # recursively calculating the gcd.
    return gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b
