from functions_day_12 import *

# challenge 1
print("challenge 1")
list_of_records = parse_input_file("../input_files/input_day_12.txt")
total = 0
count = 0
for this_entry in list_of_records:
    if count % 100 == 0:
        print(count, len(list_of_records))
    count += 1
    total += len(solve_row(this_entry[0], this_entry[1]))

print(total)

# challenge 2
print("challenge 2")
