import pytest
import math

from functions_day_02 import *


def test_read_game():
    game_id, hands = read_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")

    assert (game_id == 1)
    assert (hands[0] == "3 blue, 4 red")
    assert (hands[1] == "1 red, 2 green, 6 blue")
    assert (hands[2] == "2 green")


def test_is_hand_possible():
    check = is_hand_possible(red=12, green=13, blue=14, candidate="1 red, 2 green, 6 blue")
    check_2 = is_hand_possible(red=12, green=13, blue=14, candidate="8 green, 6 blue, 20 red")

    assert (check == True)
    assert (check_2 == False)


def test_is_set_of_hands_possible():
    game_id, hands = read_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    check = is_set_of_hands_possible(red=12, green=13, blue=14, hands=hands)

    game_id, hands = read_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    check_2 = is_set_of_hands_possible(red=12, green=13, blue=14, hands=hands)

    assert (check == True)
    assert (check_2 == False)


def test_all_games():
    valid_games = check_set_of_games(red=12, green=13, blue=14,
                                     file_games_input='../input_files/input_day_02_example.txt')

    assert (valid_games == [1, 2, 5])
    assert (sum(valid_games) == 8)


def test_find_min_set_of_cubes():
    game_id, hands = read_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    set_1 = find_min_set_of_cubes(hands)

    game_id, hands = read_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    set_2 = find_min_set_of_cubes(hands)

    assert (math.prod(set_1) == 12)
    assert (math.prod(set_2) == 630)


def test_all_games_power():
    power_games = power_set_of_games(file_games_input='../input_files/input_day_02_example.txt')

    assert (sum(power_games) == 2286)

