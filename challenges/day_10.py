from functions_day_10 import *

# challenge 1
print("challenge 1")
full_map, start = parse_input_file("../input_files/input_day_10.txt")
max_location, nodes = trace_map(full_map, start)

print(max_location)

# challenge 2
print("challenge 2")
full_map, start = parse_input_file("../input_files/input_day_10.txt")
max_location, nodes = trace_map(full_map, start)
n_points_inside = points_inside(nodes, start, max_location)

print(n_points_inside)