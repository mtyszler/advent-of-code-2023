from functions_day_07 import *

# challenge 1
print("challenge 1")
list_of_hands = parse_input_file("../input_files/input_day_07.txt")
ordered_hands = order_hands(list_of_hands)

values = [x * y for x, y in zip([w[1] for w in ordered_hands], range(1, len(ordered_hands) + 1))]
print(sum(values))

# challenge 2
print("challenge 2")
list_of_hands = parse_input_file("../input_files/input_day_07.txt")
ordered_hands = order_hands_joker(list_of_hands)

values = [x * y for x, y in zip([w[1] for w in ordered_hands], range(1, len(ordered_hands) + 1))]
print(sum(values))


