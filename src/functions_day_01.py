import regex as re

num2words = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)


def code_from_string(input_str: str) -> float:
    first_digit = -999
    last_digit = -999

    for this_string in input_str:
        if this_string.isdigit():
            if first_digit == -999:
                first_digit = this_string
            else:
                last_digit = this_string

    if last_digit == -999:
        last_digit = first_digit

    combined = float(first_digit + last_digit)

    return combined


def parse_input(filename: str) -> float:
    input_file = open(filename, 'r')
    lines = input_file.readlines()

    total = 0

    for this_line in lines:
        total += code_from_string(this_line)

    return total


def code_from_string_also_text(input_str: str) -> float:
    """
    inspired by:
    https://stackoverflow.com/questions/50145945/python-extract-quantifiable-text-numbers

    https://stackoverflow.com/questions/11430863/how-to-find-overlapping-matches-with-a-regexp
    """

    numbers = re.findall(r'[1-9]|one|two|three|four|five|six|seven|eight|nine', input_str,
                         overlapped=True)

    first_digit = numbers[0] if numbers[0].isdigit() else num2words[numbers[0]]
    last_digit = numbers[-1] if numbers[-1].isdigit() else num2words[numbers[-1]]

    combined = float(str(first_digit) + str(last_digit))

    return combined


def parse_input_also_text(filename: str) -> float:
    input_file = open(filename, 'r')
    lines = input_file.readlines()

    total = 0

    for this_line in lines:
        total += code_from_string_also_text(this_line)

    return total
