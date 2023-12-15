from functions_day_13 import *

# challenge 1
print("challenge 1")
total = 0
list_of_records = parse_input_file("../input_files/input_day_13.txt")
track =[0]
for p in list_of_records:

    score, direction = find_reflection(p)
    if direction == 'vertical':
        total += score
        track.append(score)
    elif direction == 'horizontal':
        total += 100 * score
        track.append(100*score)

print(total)

# challenge 2
print("challenge 2")
total = 0
list_of_records = parse_input_file("../input_files/input_day_13.txt")
track =[0]
for p in list_of_records:

    score, direction = find_reflection(p, part2=True)
    if direction == 'vertical':
        total += score
        track.append(score)
    elif direction == 'horizontal':
        total += 100 * score
        track.append(100*score)

print(total)
