from functions_day_18 import *
import time

# challenge 1
print("challenge 1")

instructions = parse_input_file('../input_files/input_day_18.txt')
edges = find_nodes_full(instructions)
area = compute_lava(edges)
print(area)

print("challenge 2")
instructions = parse_input_file('../input_files/input_day_18.txt')
edges, edge_points = find_nodes_hex(instructions)
area = compute_lava_only_edges(edges, edge_points)
print(area)
