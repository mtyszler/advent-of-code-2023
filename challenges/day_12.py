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
list_of_records_1 = parse_input_file("../input_files/input_day_12.txt", expansion=1)
list_of_records_2 = parse_input_file("../input_files/input_day_12.txt", expansion=2)
total = 0
count = 0
for original_entry, this_entry in zip(list_of_records_1, list_of_records_2):
    if count % 1 == 0:
        print(count, len(list_of_records))

    len_1 = len(solve_row(original_entry[0], original_entry[1]))
    len_2 = len(solve_row(this_entry[0], this_entry[1]))

    factor = len_2/len_1
    check = len_1*factor*factor*factor*factor
    total += check
    count += 1

print(total)