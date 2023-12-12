from functions_day_11 import *

# challenge 1
print("challenge 1")
stars = parse_input_file("../input_files/input_day_11.txt")
stars_expanded = expand_galaxy(stars)

total = all_distances(stars_expanded)

print(total)

# challenge 2
print("challenge 2")
stars = parse_input_file("../input_files/input_day_11.txt")
stars_expanded = expand_galaxy(stars, 1000000-1)

total = all_distances(stars_expanded)

print(total)