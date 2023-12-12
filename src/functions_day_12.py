def parse_input_file(input_file: str) -> list[(int, int)]:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    points_in_map = []

    count_rows = 0
    for this_line in lines:
        this_line_as_list = [x for x in this_line.strip()]
        if '#' in this_line_as_list:
            this_row = count_rows
            these_col = [idx for idx, val in enumerate(this_line_as_list) if val == '#']
            for this_col in these_col:
                points_in_map.append((this_row, this_col))
        count_rows += 1

    return points_in_map


def expand_galaxy(points_in_map: list[(int, int)], expansion_factor: int = 1) -> list[(int, int)]:
    # expand rows:
    existing_rows = list(set([x[0] for x in points_in_map]))
    existing_rows.sort()
    # min_row = min(existing_rows)
    max_row = max(existing_rows)

    r = 0
    while r < max_row:
        if r not in existing_rows:
            points_in_map = [(x[0] + expansion_factor, x[1]) if x[0] > r else (x[0], x[1]) for x in points_in_map]
            existing_rows = list(set([x[0] for x in points_in_map]))
            existing_rows.sort()
            max_row = max(existing_rows)
            r += expansion_factor
        r += 1

    # expand cols:
    existing_cols = list(set([x[1] for x in points_in_map]))
    existing_cols.sort()
    # min_col = min(existing_cols)
    max_col = max(existing_cols)

    c = 0
    while c < max_col:
        if c not in existing_cols:
            points_in_map = [(x[0], x[1] + expansion_factor) if x[1] > c else (x[0], x[1]) for x in points_in_map]
            existing_cols = list(set([x[1] for x in points_in_map]))
            existing_cols.sort()
            max_col = max(existing_cols)
            c += expansion_factor
        c += 1

    return points_in_map


def manhattan_adj(a, b):

    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def all_distances(points_in_map: list[(int, int)]) -> int:

    total = 0
    for i in range(len(points_in_map)):
        for j in range(i, len(points_in_map)):
            total += manhattan_adj(points_in_map[i], points_in_map[j])

    return total
