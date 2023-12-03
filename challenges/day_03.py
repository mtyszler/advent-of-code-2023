from functions_day_03 import *

# challenge 1
df = parse_input_file('../input_files/input_day_03.txt')
part_numbers = find_part_numbers(df)

print("challenge 1")
print(sum(part_numbers))

# challenge 2
df = parse_input_file('../input_files/input_day_03.txt')
gear_ratios = find_gear_ratios(df)

print("challenge 2")
print(sum(gear_ratios))
