from functions_day_25 import *
import time

# challenge 1

print("challenge 1")
from_to = parse_input_file('../input_files/input_day_25.txt')
check = find_intersections(from_to)

print (len(check[0]) * len(check[1]))

print("challenge 2")