from functions_day_21 import *
import time

# challenge 1
print("challenge 1")

grid, start_location = parse_input('../input_files/input_day_21.txt')
n_garden = find_possibilities(grid, start_location, n_steps=64)

print(n_garden)

print("challenge 2")



