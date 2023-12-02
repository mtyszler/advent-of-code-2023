import math

def read_game(game_str: str) -> [int, list]:
    """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Args:
        game_str:

    Returns:

    """

    game_str, content_str = game_str.split(":")

    game_id = int(game_str.split(" ")[1])

    hands = content_str.split(";")
    hands = [h.strip() for h in hands]

    return game_id, hands


def is_hand_possible(red: int, green: int, blue: int, candidate: str) -> bool:

    check = True
    items = candidate.split(",")
    items = [h.strip() for h in items]

    total = red + green + blue

    check_total = 0
    for this_item in items:
        amount, color = this_item.split(" ")
        check_total += int(amount)
        if color.strip() == "red":
            if int(amount) > red:
                check = False
                break
        elif color.strip() == "green":
            if int(amount) > green:
                check = False
                break
        elif color.strip() == "blue":
            if int(amount) > blue:
                check = False
                break

    if check_total > total:
        check = False

    return check


def is_set_of_hands_possible(red: int, green: int, blue: int, hands: list) -> bool:

    check = True
    for hand in hands:
        if not is_hand_possible(red=red, green=green, blue=blue,candidate=hand):
            check = False
            break

    return check


def check_set_of_games(red: int, green: int, blue: int, file_games_input: str) -> list:

    input_file = open(file_games_input, 'r')
    lines = input_file.readlines()

    valid_games = []

    for this_line in lines:
        game_id, hands = read_game(this_line)
        if is_set_of_hands_possible(red=red,green=green,blue=blue, hands=hands):
            valid_games.append(int(game_id))

    return valid_games


def find_min_set_of_cubes(hands: list) -> list:

    red = 0
    blue = 0
    green = 0

    for hand in hands:

        items = hand.split(",")
        items = [h.strip() for h in items]

        for this_item in items:
            amount, color = this_item.split(" ")
            if color.strip() == "red":
                if int(amount) > red:
                    red = int(amount)

            elif color.strip() == "green":
                if int(amount) > green:
                    green = int(amount)

            elif color.strip() == "blue":
                if int(amount) > blue:
                    blue = int(amount)

    return [red, blue, green]


def power_set_of_games(file_games_input: str) -> list:

    input_file = open(file_games_input, 'r')
    lines = input_file.readlines()

    power_games = []

    for this_line in lines:
        game_id, hands = read_game(this_line)
        this_set = find_min_set_of_cubes(hands)
        power_games.append(math.prod(this_set))

    return power_games
