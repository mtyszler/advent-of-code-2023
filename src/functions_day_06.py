import math


def distance(x_ms: int, max_ms: int) -> int:

    distance_calc = (max_ms-x_ms)*x_ms

    return distance_calc


def cross_points(max_ms: int, record_ms: int) -> int:
    """
    distance_calc = (max_ms-x_ms)*x_ms
    distance_calc = max_ms*x_ms-x_ms**2

    solve:
    max_ms*x_ms-x_ms**2 = record_ms
    x_ms**2 - max_ms*x_ms + record_ms = 0

    x_ms = (max_ms +- sqr(max_ms**2 - 4*record_ms))/2
    """

    x_ms_1 = (max_ms + math.sqrt(max_ms ** 2 - 4 * record_ms)) / 2
    x_ms_2 = (max_ms - math.sqrt(max_ms ** 2 - 4 * record_ms)) / 2

    highest = math.floor(max(x_ms_2, x_ms_1))
    if highest == max(x_ms_2, x_ms_1):
        highest -= 1
    lowest = math.ceil(min(x_ms_2, x_ms_1))
    if lowest == min(x_ms_2, x_ms_1):
        lowest += 1

    int_n_possible_wins = highest-lowest+1
    return int_n_possible_wins
