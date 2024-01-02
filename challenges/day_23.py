from functions_day_23 import *
import time

# challenge 1
print("challenge 1")
grid = parse_heat_map('../input_files/input_day_23.txt')
best_distance = find_exit(grid,
                          start_location=(0, 1),
                          target_location=(140, 139))

print(-best_distance)

# challenge 2
print("challenge 2")
grid = parse_heat_map('../input_files/input_day_23.txt')
best_distance = find_exit_dfs(grid,
                          start_location=(0, 1),
                          target_location=(140, 139)
                              )

print(best_distance)