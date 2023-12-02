from functions_day_02 import *

# challenge 1
valid_games = check_set_of_games(red=12, green=13, blue=14,
                                 file_games_input='../input_files/input_day_02.txt')

print("Sum of valid games IDs")
print(sum(valid_games))

# challenge 2
power_games = power_set_of_games(file_games_input='../input_files/input_day_02.txt')

print("Sum of power of games")
print(sum(power_games))
