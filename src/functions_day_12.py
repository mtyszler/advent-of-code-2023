import functools
import math

from itertools import product


def parse_input_file(input_file: str, expansion: int = 1) -> list[(str, list[int])]:

    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    list_of_records = []

    for this_line in lines:
        record, arrangement = this_line.strip().split(" ")
        if expansion == 1:
            exp_record = record
        else:
            exp_record = record
            for i in range(1, expansion):
                exp_record += '?' + record

        list_of_records.append((exp_record, [int(x) for x in arrangement.split(",")] * expansion))

    return list_of_records


def identify_arrangement(record: str) -> list[int]:
    arrangement = []
    this_count = 0
    complete_block = False
    for i in range(len(record)):
        if record[i] == '#':
            this_count += 1
            complete_block = False
        elif record[i] == '.':
            if this_count > 0:
                arrangement.append(this_count)
                this_count = 0
                complete_block = True
        elif record[i] == '?':
            break

    if this_count > 0:
        arrangement.append(this_count)
        if record[i] == '?':
            complete_block = False
        else:
            complete_block = True

    return arrangement, complete_block


def variate_records(record: str, arrangement: list[int], seed: list[str] = []) -> list[str]:

    # location of the '?'
    idx = [idx for idx, val in enumerate(record) if val == '?']

    if len(idx) > 0:

        test_record_1 = record
        test_record_1 = test_record_1[:idx[0]] + '#' + test_record_1[idx[0] + 1:]
        if test_record_1 not in seed:
            if possible_arrangement(test_record_1, arrangement):
                seed.append(test_record_1)

        test_record_2 = record
        test_record_2 = test_record_2[:idx[0]] + '.' + test_record_2[idx[0] + 1:]
        if test_record_2 not in seed:
            if possible_arrangement(test_record_2, arrangement):
                seed.append(test_record_2)

        idx.pop(0)

        if len(idx) > 0:
            if test_record_1 in seed:
                variate_records(test_record_1, arrangement, seed)
            if test_record_2 in seed:
                variate_records(test_record_2, arrangement, seed)

    return seed


def possible_arrangement(record: str, arrangement: list[int]) -> bool:
    n_int = len([idx for idx, val in enumerate(record) if val == '?'])
    n_hash = len([idx for idx, val in enumerate(record) if val == '#'])
    n_point = len([idx for idx, val in enumerate(record) if val == '.'])

    if n_hash + n_int == sum(arrangement):
        new_record = ''
        for i in range(len(record)):
            if record[i]=='?':
                new_record +='#'
            else:
                new_record += record[i]

        if identify_arrangement(new_record)[0] != arrangement:
            return False
        else:
            return True


    if n_hash > sum(arrangement):
        return False

    if n_hash + n_int < sum(arrangement):
        return False

    '''

    new_record = ''
    for i in range(len(record)):
        if record[i]==


    blocks = record.split('.')
    # check number of groups:
    b_groups = 0
    for b in blocks:
        if b == '':
            continue
        elif '?' in b:
#            n_int = len([idx for idx, val in enumerate(b) if val == '?'])
            b_groups += math.ceil(len(b)/2)
        else:
            b_groups += 1

    if b_groups < len(arrangement):
        return False
    '''
    this_arrangement, last_block_complete = identify_arrangement(record)
    if this_arrangement:
        i = -999
        for i in range(min(len(arrangement), len(this_arrangement))-1):
            if this_arrangement[i] != arrangement[i]:
                return False
        if i == -999:
            i = -1
        if last_block_complete:
            if this_arrangement[i + 1] != arrangement[i + 1]:
                return False
        else:
            if this_arrangement[i+1] > arrangement[i+1]:
                return False


    return True


def solve_row(record: str, arrangement: list[int]) -> list[str]:

    valid_arrangements = []
    candidate_arrangements = variate_records(record, arrangement, [])

    for this_arrangement in candidate_arrangements:

        # location of the '?'
        idx = [idx for idx, val in enumerate(this_arrangement) if val == '?']

        if len(idx) == 0:
            if identify_arrangement(this_arrangement)[0] == arrangement:
                valid_arrangements.append(this_arrangement)

    return valid_arrangements


def variate_block(block: str) -> list[str]:

    seeds = []

    # location of the '?'
    idx = [idx for idx, val in enumerate(block) if val == '?']
    for i in range(len(block)):
        if i in idx:
            seeds.append(['#','.'])
        else:
            seeds.append([block[i]])

    return [''.join(x) for x in product(*seeds)]


def identify_blocks(record:str) -> list[str]:

    blocks = []
    this_block = ''
    for i in range(len(record)):
        if record[i] == '.' and ('?' in this_block or '#' in this_block):
            blocks.append(this_block)
            this_block = ''
        else:
            this_block += record[i]

    if this_block != '':
        blocks.append(this_block)

    return blocks


def solve_row_v2(record: str, arrangement: list[int]) -> list[str]:

    blocks = identify_blocks(record)

    v_blocks = [variate_block(b) for b in blocks]

    candidates = [''.join(x) for x in product(*v_blocks)]

    return candidates



