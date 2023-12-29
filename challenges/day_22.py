from functions_day_22 import *
import time

# challenge 1
print("challenge 1")
positions, grid = parse_input('../input_files/input_day_22.txt')
print('original done')

new_positions, new_grid = drop_blocks(positions, grid)
print('falling done')

can_desintegrate = desintegrate(new_positions, new_grid)
print('desintegration done')

print(len(can_desintegrate))

print("challenge 2")
positions, grid = parse_input('../input_files/input_day_22.txt')
print('original done')

new_positions, new_grid = drop_blocks(positions, grid)
print('falling done')

cannot_desintegrate = desintegrate_full(new_positions, new_grid)
print('desintegration done')

x = sum(cannot_desintegrate.values())

print(x)