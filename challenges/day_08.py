from functions_day_08 import *

# challenge 1
print("challenge 1")
instructions, nodes = parse_input_file("../input_files/input_day_08.txt")
n_steps = follow_path(instructions, nodes)

print(n_steps)

# challenge 2
print("challenge 2")
instructions, nodes = parse_input_file("../input_files/input_day_08.txt")
n_steps = follow_path_ghost(instructions, nodes)

print(n_steps)



