from functions_day_16 import *
import time

# challenge 1
print("challenge 1")

grid = parse_input_file('../input_files/input_day_16.txt')

start_time = time.time()
energized, total = move_light(grid, start_pos=(0, 0), start_dir='d')
print("--- %s seconds ---" % (time.time() - start_time))

print(total)

print("challenge 2")

grid = parse_input_file('../input_files/input_day_16.txt')

all_energies = []
start_time = time.time()
for r in [0, len(grid) - 1]:
    for c in range(len(grid[0])):
        start_dir = 'd' if r == 0 else 'u'
        energized, total = move_light(grid, start_pos=(r, c), start_dir=start_dir)
        all_energies.append(total)
        print((r, c))

for c in [0, len(grid[0]) - 1]:
    for r in range(len(grid)):
        start_dir = 'r' if c == 0 else 'l'
        energized, total = move_light(grid, start_pos=(r, c), start_dir=start_dir)
        all_energies.append(total)
        print((r, c))

print("--- %s seconds ---" % (time.time() - start_time))
best = max(all_energies)
print(best)
