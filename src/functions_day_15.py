def hash_algorithm(input_str: str) -> int:
    current_value = 0

    for i in range(len(input_str)):
        this_ascii = ord(input_str[i])
        current_value += this_ascii
        current_value = current_value * 17
        current_value = current_value % 256

    return current_value


def parse_input_file(input_file: str) -> list:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    patterns = []
    for this_line in lines:
        patterns.extend([x for x in this_line.strip().split(",")])

    return patterns


def prep_boxes(patterns: list[str]) -> dict:
    boxes = {x: [] for x in range(256)}

    # {1 : ('cm',1)

    for this_pattern in patterns:
        if '=' in this_pattern:
            label, focal_length = this_pattern.split("=")
            focal_length = int(focal_length)
        else:
            label = this_pattern[:-1]

        box = hash_algorithm(label)
        box_content = boxes[box]

        if '=' in this_pattern:
            found_len = False
            for content in box_content:
                if content[0] == label:
                    found_len = True
                    box_content[box_content.index(content)] = (label, focal_length)

            if not found_len:
                box_content.append((label, focal_length))

        else:

            for content in box_content:
                if content[0] == label:
                    box_content.remove(content)

    return boxes
