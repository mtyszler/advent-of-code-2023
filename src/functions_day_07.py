type_of_hands = {
    "five_of_a_kind": 6,
    "four_of_a_kind": 5,
    "full_house": 4,
    "three_of_a_kind": 3,
    "two_pair": 2,
    "one_pair": 1,
    "high_card": 0
}


def type_of_hand(hand_str: str) -> int:
    # check unique
    list_hand = [x for x in hand_str]
    set_hand = set(list_hand)
    if len(set_hand) == 1:
        return 6

    elif len(set_hand) == 2:
        # four of a kind or
        # full house
        for test_card in set_hand:
            if list_hand.count(test_card) == 4:
                return 5
        return 4

    elif len(set_hand) == 3:
        # three of a kind or
        # two pair:

        for test_card in set_hand:
            if list_hand.count(test_card) == 3:
                return 3
        return 2
    elif len(set_hand) == 4:
        return 1
    elif len(set_hand) == 5:
        return 0


def type_of_hand_joker(hand_str: str) -> int:
    # check unique
    list_hand = [x for x in hand_str]
    set_hand = set(list_hand)
    if len(set_hand) == 1:  # [AAAAA]
        return 6

    elif len(set_hand) == 2:
        # four of a kind  [AAAA, B]
        # full house [AAA, BB]
        for test_card_joker in set_hand:
            if test_card_joker == "J":  # [AAAAA]
                return 6

        for test_card in set_hand:
            if list_hand.count(test_card) == 4:
                return 5
        return 4

    elif len(set_hand) == 3:
        # three of a kind [AAA, B, C]
        # two pair: [AA, BB, C]

        for test_card in set_hand:
            if list_hand.count(test_card) == 3:  # [AAA, B, Y]
                for test_card_joker in set_hand:
                    if test_card_joker == "J":  # [AAAA, Y]
                        return 5
                return 3
        # [AA, XX, Y]
        for test_card_joker in set_hand:
            if test_card_joker == "J":
                if list_hand.count(test_card_joker) == 1:  # [AAA, XX] or [AA, XXX]
                    return 4
                elif list_hand.count(test_card_joker) == 2:  # [AAAA, Y] or [AA, YYY]
                    return 5
        return 2
    elif len(set_hand) == 4:  # [AA, B, C, D]
        # [AA, B, C, X] or [XX, B, C, D]
        for test_card_joker in set_hand:
            if test_card_joker == "J":
                # [AAA, B, C] or [BBB, C, D]
                return 3
        return 1
    elif len(set_hand) == 5:  # [A, B, C, D, E]
        # [A, B, C, D, X]
        for test_card_joker in set_hand:
            if test_card_joker == "J":  # [AA, B, C, D]
                return 1
        return 0


def winning_hand(hand_1: str, hand_2: str) -> str:
    type_hand_1 = type_of_hand(hand_1)
    type_hand_2 = type_of_hand(hand_2)

    if type_hand_1 > type_hand_2:
        return hand_1
    elif type_hand_1 < type_hand_2:
        return hand_2
    else:
        # tie:
        h1 = [x for x in hand_1]
        h2 = [x for x in hand_2]
        for c1, c2 in zip(h1, h2):

            if value_of_card(c1) > value_of_card(c2):
                return hand_1
            elif value_of_card(c1) < value_of_card(c2):
                return hand_2

        raise Exception("Could not find highest hand")


def winning_hand_joker(hand_1: str, hand_2: str) -> str:
    type_hand_1 = type_of_hand_joker(hand_1)
    type_hand_2 = type_of_hand_joker(hand_2)

    if type_hand_1 > type_hand_2:
        return hand_1
    elif type_hand_1 < type_hand_2:
        return hand_2
    else:
        # tie:
        h1 = [x for x in hand_1]
        h2 = [x for x in hand_2]
        for c1, c2 in zip(h1, h2):

            if value_of_card_joker(c1) > value_of_card_joker(c2):
                return hand_1
            elif value_of_card_joker(c1) < value_of_card_joker(c2):
                return hand_2

        raise Exception("Could not find highest hand")


def value_of_card(card: str) -> int:
    if card.isdigit():
        return int(card)
    else:
        if card == "T":
            return 10
        elif card == "J":
            return 11
        elif card == "Q":
            return 12
        elif card == "K":
            return 13
        elif card == "A":
            return 14
        else:
            raise Exception("unknown card")


def value_of_card_joker(card: str) -> int:
    if card.isdigit():
        return int(card)
    else:
        if card == "T":
            return 10
        elif card == "J":
            return 1
        elif card == "Q":
            return 12
        elif card == "K":
            return 13
        elif card == "A":
            return 14
        else:
            raise Exception("unknown card")


def parse_input_file(input_file: str) -> list[(str, float)]:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    list_of_hands = []
    for this_line in lines:
        hand, bid = this_line.strip().split(" ")
        list_of_hands.append([hand, float(bid)])

    return list_of_hands


def order_hands(list_of_hands: list[(str, float)]) -> list[(str, float)]:
    ordered_list = []

    while len(list_of_hands) > 0:
        this_hand = list_of_hands.pop()
        if len(ordered_list) == 0:
            ordered_list.append(this_hand)
        else:
            found = False
            for i in range(len(ordered_list)):

                highest_hand = winning_hand(this_hand[0], ordered_list[i][0])
                if highest_hand == ordered_list[i][0]:
                    found = True
                    ordered_list.insert(i, this_hand)
                    break

            if not found:
                ordered_list.append(this_hand)

    return ordered_list


def order_hands_joker(list_of_hands: list[(str, float)]) -> list[(str, float)]:
    ordered_list = []

    while len(list_of_hands) > 0:
        this_hand = list_of_hands.pop()
        if len(ordered_list) == 0:
            ordered_list.append(this_hand)
        else:
            found = False
            for i in range(len(ordered_list)):

                highest_hand = winning_hand_joker(this_hand[0], ordered_list[i][0])
                if highest_hand == ordered_list[i][0]:
                    found = True
                    ordered_list.insert(i, this_hand)
                    break

            if not found:
                ordered_list.append(this_hand)

    return ordered_list
