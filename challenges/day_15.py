from functions_day_15 import *

# challenge 1
print("challenge 1")
inputs = parse_input_file('../input_files/input_day_15.txt')

total = 0
for j in inputs:
    total += hash_algorithm(j)
print(total)

print("challenge 2")
inputs = parse_input_file('../input_files/input_day_15.txt')

boxes = prep_boxes(inputs)

total = 0
for i in range(256):
    box_content = boxes[i]
    for idx, content in enumerate(box_content):
        total += (i + 1) * (idx + 1) * content[1]

print(total)