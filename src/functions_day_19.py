import copy


def parse_input_file(input_file: str) -> [dict, list[dict]]:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    instructions = {}
    parts = []
    instructions_part = True
    for this_line in lines:
        if this_line.strip() == '':
            instructions_part = False
            continue

        if instructions_part:
            instruction_name, content = this_line.strip().split("{")
            content = content[:-1].split(",")

            instructions[instruction_name] = [x.split(':') for x in content]

        else:
            parts.append({x.split("=")[0]: int(x.split("=")[1]) for x in this_line.strip()[1:-1].split(",")})

    return instructions, parts


def process_part(instructions: dict, part: dict) -> bool:
    instruction_name = 'in'
    x = part['x']
    m = part['m']
    a = part['a']
    s = part['s']

    while True:
        if instruction_name == 'R':
            return False
        elif instruction_name == 'A':
            return True

        instruction_content = instructions[instruction_name]

        for sub_instruction in instruction_content:
            if len(sub_instruction) == 2:
                test_instruction, consequence = sub_instruction
                response = eval(test_instruction)
                if response:
                    instruction_name = consequence
                    break
            elif len(sub_instruction) == 1:
                instruction_name = sub_instruction[0]
            else:
                raise Exception("cannot understand instruction")


def slice_instructions(instructions: dict) -> int:
    accepted = []
    to_do = [('in', {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]})]

    while len(to_do) > 0:
        instruction_name, group = to_do.pop(0)

        if instruction_name == 'R':
            continue
        elif instruction_name == 'A':
            accepted.append(group)
            continue

        instruction_content = instructions[instruction_name]

        for sub_instruction in instruction_content:
            if len(sub_instruction) == 2:
                test_instruction, consequence = sub_instruction

                if ">" in test_instruction:
                    part, break_point = test_instruction.split(">")
                    break_point = int(break_point)
                    if group[part][0] <= break_point < group[part][1]:
                        # true
                        new_group = copy.deepcopy(group)
                        new_group[part][0] = break_point + 1
                        to_do.append((consequence, new_group))

                        # false
                        group[part][1] = break_point

                elif "<" in test_instruction:
                    part, break_point = test_instruction.split("<")
                    break_point = int(break_point)
                    if group[part][0] < break_point <= group[part][1]:
                        # true
                        new_group = copy.deepcopy(group)
                        new_group[part][1] = break_point - 1
                        to_do.append((consequence, new_group))

                        # false
                        group[part][0] = break_point

            elif len(sub_instruction) == 1:

                consequence = sub_instruction[0]
                to_do.append((consequence, group))
            else:

                raise Exception("cannot understand instruction")

    total = 0
    for group in accepted:
        sub_total = 1
        for part, part_range in group.items():
            sub_total *= part_range[1] - part_range[0] + 1
        total += sub_total

    return total
