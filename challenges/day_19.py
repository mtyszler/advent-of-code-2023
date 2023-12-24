from functions_day_19 import *
import time

# challenge 1
print("challenge 1")

instructions, parts = parse_input_file('../input_files/input_day_19.txt')

total = 0
for part in parts:
    if process_part(instructions, part):
        total += sum(part.values())

print(total)

print("challenge 2")

instructions, parts = parse_input_file('../input_files/input_day_19.txt')

total = slice_instructions(instructions)

print(total)
