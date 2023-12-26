from functions_day_21 import *
import time

# challenge 1
print("challenge 1")

grid, start_location = parse_input('../input_files/input_day_21.txt')
n_garden, _ = find_possibilities(grid, start_location, n_steps=64)

print(n_garden)

print("challenge 2")
grid, start_location = parse_input('../input_files/input_day_21.txt')

for s, start_location in [
    [65, (65, 65)],
    [64, (65, 65)],
    [64, (0, 0)],
    [63, (0, 0)],
    [64, (0, 130)],
    [63, (0, 130)],
    [64, (130, 0)],
    [63, (130, 0)],
    [64, (130, 130)],
    [63, (130, 130)]

]:
    n_garden, garden_plots = find_possibilities(grid, start_location, n_steps=s)
    print(s, start_location, n_garden)
