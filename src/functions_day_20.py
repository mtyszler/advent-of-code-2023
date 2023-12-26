import copy


def parse_input_file(input_file: str) -> [dict, dict, dict]:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    outputs = {}
    types = {}
    inputs = {}
    for this_line in lines:
        source, destinations = this_line.strip().split(" -> ")
        if source == "broadcaster":
            source_name = source
            types[source_name] = source
        elif source[0] == '%':
            source_name = source[1:]
            types[source_name] = 'flip-flop'
        elif source[0] == '&':
            source_name = source[1:]
            types[source_name] = 'conjunction'
        else:
            raise Exception("Can't parse")

        outputs[source_name] = [x.strip() for x in destinations.split(',')]
        for o in outputs[source_name]:
            if o in inputs.keys():
                inputs[o].append(source_name)
            else:
                inputs[o] = [source_name]

    return outputs, inputs, types


def flipflop(status: str, destinations: list[str], pulse: str) -> [str, dict]:
    if pulse == 'high':
        return status, {}
    else:
        if status == 'on':
            status_response = 'off'
            pulse_response = 'low'
        else:
            status_response = 'on'
            pulse_response = 'high'

        return status_response, {x: pulse_response for x in destinations}


def conjunction(memory: dict, sender: str, destinations: list[str], pulse: str) -> [dict, dict]:
    new_memory = copy.deepcopy(memory)
    new_memory[sender] = pulse

    if all([x == 'high' for x in new_memory.values()]):
        return new_memory, {x: 'low' for x in destinations}
    else:
        return new_memory, {x: 'high' for x in destinations}


def run_pulses(outputs: dict, inputs: dict, types: dict, n_pulses: int) -> dict:
    statuses = {x: 'off' for x in types.keys() if types[x] == 'flip-flop'}
    memories = {}
    for x, this_type in types.items():
        if this_type == 'conjunction':
            memories[x] = {x: 'low' for x in inputs[x]}

    pulses = {'high': 0, 'low': 0}
    for i in range(n_pulses):
        statuses, memories, pulses = press_button(outputs, inputs, types, statuses, memories, pulses)

    return pulses


def press_button(outputs: dict, inputs: dict, types: dict, statuses: dict, memories: dict, pulses: dict) -> [dict, dict,
                                                                                                             dict]:
    to_do = [('broadcaster', 'low', 'button')]

    while len(to_do) > 0:
        this_module, current_pulse, current_sender = to_do.pop(0)
        pulses[current_pulse] += 1
        if this_module not in types.keys():
            continue
        if types[this_module] == 'broadcaster':
            to_do.extend([(x, current_pulse, this_module) for x in outputs[this_module]])
        elif types[this_module] == 'flip-flop':
            new_status, passes = flipflop(status=statuses[this_module],
                                          destinations=outputs[this_module],
                                          pulse=current_pulse)
            statuses[this_module] = new_status
            to_do.extend([(k, v, this_module) for k, v in passes.items()])
        elif types[this_module] == 'conjunction':
            new_memory, passes = conjunction(memory=memories[this_module],
                                             destinations=outputs[this_module],
                                             pulse=current_pulse,
                                             sender=current_sender)
            memories[this_module] = new_memory
            to_do.extend([(k, v, this_module) for k, v in passes.items()])

    return statuses, memories, pulses


def retrace_steps(outputs: dict, inputs: dict, types: dict, target: str) -> int:

    inputs_of_target = inputs[target]
    while len(inputs_of_target) == 1:
        inputs_of_target = inputs[inputs_of_target[0]]

    return 1
