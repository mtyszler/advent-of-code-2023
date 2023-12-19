import pytest
import time

from functions_day_16 import *


def test_parse():
    grid = parse_input_file('../input_files/input_day_16_example.txt')

    start_time = time.time()
    energized, total = move_light(grid, start_pos=(0, 0), start_dir='r')
    print("--- %s seconds ---" % (time.time() - start_time))

    assert (total == 46)


def test_parse_all():
    grid = parse_input_file('../input_files/input_day_16_example.txt')

    all_energies = []
    for r in [0, len(grid)-1]:
        for c in range(len(grid[0])):
            start_time = time.time()
            start_dir = 'd' if r == 0 else 'u'
            energized, total = move_light(grid, start_pos=(r, c), start_dir=start_dir)
            all_energies.append(total)
            print("--- %s seconds ---" % (time.time() - start_time))

    for c in [0, len(grid[0])-1]:
        for r in range(len(grid)):
            start_time = time.time()
            start_dir = 'r' if c == 0 else 'l'
            energized, total = move_light(grid, start_pos=(r, c), start_dir=start_dir)
            all_energies.append(total)
            print("--- %s seconds ---" % (time.time() - start_time))

    best = max(all_energies)
    assert (best == 51)