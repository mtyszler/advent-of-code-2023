def parse_input_file(input_file: str) -> float:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    total = 0

    for this_line in lines:
        card_str, content_str = this_line.split(":")
        winning_str, candidates_str = content_str.split("|")

        winning = [int(x) for x in winning_str.strip().split(" ") if x.isdigit()]
        candidates = [int(x) for x in candidates_str.strip().split(" ") if x.isdigit()]

        winning_numbers_have = [x for x in candidates if x in winning]

        if len(winning_numbers_have) > 0:
            total += 2 ** (len(winning_numbers_have) - 1)

    return total


def parse_input_file_v2(input_file: str) -> list[int]:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    winning_list = []
    card_nbr = 0
    for this_line in lines:
        card_nbr +=1
        card_str, content_str = this_line.split(":")
        winning_str, candidates_str = content_str.split("|")

        winning = [int(x) for x in winning_str.strip().split(" ") if x.isdigit()]
        candidates = [int(x) for x in candidates_str.strip().split(" ") if x.isdigit()]

        winning_numbers_have = [x for x in candidates if x in winning]

        winning_list.append(len(winning_numbers_have))

    # count cards
    total_cards = len(winning_list)

    each_card = [1] * total_cards

    for this_card in range(total_cards-1):
        wins = winning_list[this_card]
        for this_win in range(this_card+1, min(this_card + wins + 1, total_cards)):
            multiplier = each_card[this_card]
            each_card[this_win] += 1 * multiplier

    return sum(each_card)
