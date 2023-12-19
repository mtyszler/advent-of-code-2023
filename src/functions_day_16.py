def parse_input_file(input_file: str) -> list[list[str]]:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    grid = []
    for this_line in lines:
        grid.append([x for x in this_line.strip()])

    return grid


def move_light(grid: list[list[str]], test=False) -> list[list[str]]:
    # initialize:
    energized_row = ['.'] * len(grid[0])
    energized = []
    for r in range(len(grid)):
        energized.append(energized_row.copy())

    total = 0
    old_total = -99
    repeat = 0
    if test:
        rays = [((0, 0), 'r')]
    else:
        rays = [((0, 0), 'd')]
    visited = []
    energized[0][0] = '#'
    while len(rays) > 0:
        left_the_building = False
        this_ray = rays.pop(0)
        pos = this_ray[0]
        direction = this_ray[1]

        while not left_the_building:

            energized[pos[0]][pos[1]] = '#'
            visited.append((pos, direction))

            if direction == 'r':
                next_pos = (pos[0], pos[1] + 1)
            elif direction == 'l':
                next_pos = (pos[0], pos[1] - 1)
            elif direction == 'u':
                next_pos = (pos[0] - 1, pos[1])
            elif direction == 'd':
                next_pos = (pos[0] + 1, pos[1])

            if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(grid) or next_pos[1] >= len(grid[0]):
                left_the_building = True
            else:
                next_char = grid[next_pos[0]][next_pos[1]]
                if next_char == '.':
                    next_direction = direction
                elif next_char == '/':
                    if direction == 'r':
                        next_direction = 'u'
                    elif direction == 'l':
                        next_direction = 'd'
                    elif direction == 'd':
                        next_direction = 'l'
                    elif direction == 'u':
                        next_direction = 'r'
                elif next_char == '\\':
                    if direction == 'r':
                        next_direction = 'd'
                    elif direction == 'l':
                        next_direction = 'u'
                    elif direction == 'd':
                        next_direction = 'r'
                    elif direction == 'u':
                        next_direction = 'l'
                elif next_char == '-':
                    if direction == 'r' or direction == 'l':
                        next_direction = direction
                    elif direction == 'd' or direction == 'u':
                        next_direction = 'r'
                        if (next_pos, 'l') not in visited:
                            rays.append((next_pos, 'l'))
                elif next_char == '|':
                    if direction == 'r' or direction == 'l':
                        next_direction = 'u'
                        if (next_pos, 'd') not in visited:
                            rays.append((next_pos, 'd'))
                    elif direction == 'd' or direction == 'u':
                        next_direction = direction

            pos = next_pos
            direction = next_direction
            if (pos, direction) in visited:
                left_the_building = True

            total = 0
            for r in energized:
                total += sum([x == '#' for x in r])

    return energized, total
