from functions_day_24 import *
import time

# challenge 1

print("challenge 1")
stones = parse_input_file('../input_files/input_day_24.txt')
equations = make_equations_lines(stones)
n_crossings = find_crossings(equations, 200000000000000, 400000000000000)
print(n_crossings)

print("challenge 2")
stones = parse_input_file('../input_files/input_day_24.txt')
equations, len_stones = make_equations_system(stones)
magic = find_magic(equations, len_stones)

print (sum(magic[0][0:3]))
