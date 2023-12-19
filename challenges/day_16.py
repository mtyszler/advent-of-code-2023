from functions_day_16 import *

# challenge 1
print("challenge 1")
grid = parse_input_file('../input_files/input_day_16.txt')

energized, total = move_light(grid)
print(total)

print("challenge 2")
