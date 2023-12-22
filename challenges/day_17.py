from functions_day_17 import *

# challenge 1
print("challenge 1")

grid_heat = parse_heat_map('../input_files/input_day_17.txt')
best_distance = find_exit(grid_heat,
                           start_location=[(0, 0), ['r', 'd']],
                           target_location=(140, 140))

print(best_distance)

print("challenge 2")
grid_heat = parse_heat_map('../input_files/input_day_17.txt')
best_distance = find_exit_2(grid_heat,
                           start_location=[(0, 0), ['r', 'd']],
                           target_location=(140, 140))

print(best_distance)