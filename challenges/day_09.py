from functions_day_09 import *

# challenge 1
print("challenge 1")
all_values = find_all_next_numbers("../input_files/input_day_09.txt")
total = sum(all_values)

print(total)

# challenge 2
print("challenge 2")
all_values = find_all_next_numbers_left("../input_files/input_day_09.txt")
total = sum(all_values)

print(total)
