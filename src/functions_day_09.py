def parse_input_file(input_file: str) -> list[list[int]]:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    all_lists = []
    for this_line in lines:
        all_lists.append([int(x) for x in this_line.strip().split(" ")])

    return all_lists


def first_dif(input_lst: list[int]) -> list[int]:
    new_list = []
    for i in range(1, len(input_lst)):
        new_list.append((input_lst[i] - input_lst[i - 1]))

    return new_list


def process_seq(input_lst: list[int]) -> list[list[int]]:
    latest_list = input_lst
    new_list = [input_lst.copy()]
    while not all([x == 0 for x in latest_list]):
        latest_list = first_dif(latest_list)
        new_list.append(latest_list)

    return new_list


def find_next_number(input_lst: list[list[int]]) -> int:
    current_value = 0
    for i in range(len(input_lst) - 2, -1, -1):
        current_value += input_lst[i][-1]

    return current_value


def find_next_number_left(input_lst: list[list[int]]) -> int:
    current_value = 0
    for i in range(len(input_lst) - 2, -1, -1):
        current_value = input_lst[i][0] - current_value

    return current_value


def find_all_next_numbers(input_str: str) -> list[int]:
    all_lists = parse_input_file(input_str)
    all_next_values = []
    for this_list in all_lists:
        new_lists = process_seq(this_list)
        all_next_values.append(find_next_number(new_lists))

    return all_next_values


def find_all_next_numbers_left(input_str: str) -> list[int]:
    all_lists = parse_input_file(input_str)
    all_next_values = []
    for this_list in all_lists:
        new_lists = process_seq(this_list)
        all_next_values.append(find_next_number_left(new_lists))

    return all_next_values


