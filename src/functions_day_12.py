def parse_input_file(input_file: str, expansion: int = 1) -> list[(str, list[int])]:

    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    list_of_records = []

    for this_line in lines:
        record, arrangement = this_line.strip().split(" ")
        list_of_records.append((record * expansion, [int(x) for x in arrangement.split(",")] * expansion))

    return list_of_records


def identify_arrangement(record: str) -> list[int]:
    arrangement = []
    this_count = 0

    for i in range(len(record)):
        if record[i] == '#':
            this_count += 1
        elif record[i] == '.':
            if this_count > 0:
                arrangement.append(this_count)
                this_count = 0
        elif record[i] == '?':
            break

    if this_count > 0:
        arrangement.append(this_count)

    return arrangement


def variate_records(record: str, arrangement: list[int], seed: list[str] = []) -> list[str]:
    # location of the '?'
    idx = [idx for idx, val in enumerate(record) if val == '?']

    if len(idx) > 0:

        test_record_1 = record
        test_record_1 = test_record_1[:idx[0]] + '#' + test_record_1[idx[0] + 1:]
        seed.append(test_record_1)

        test_record_2 = record
        test_record_2 = test_record_2[:idx[0]] + '.' + test_record_2[idx[0] + 1:]
        seed.append(test_record_2)

        idx.pop(0)

        if len(idx) > 0:
            variate_records(test_record_1, arrangement, seed)
            variate_records(test_record_2, arrangement, seed)

    return seed


def solve_row(record: str, arrangement: list[int]) -> list[str]:
    valid_arrangements = []
    candidate_arrangements = variate_records(record, arrangement, [])

    for this_arrangement in candidate_arrangements:

        # location of the '?'
        idx = [idx for idx, val in enumerate(this_arrangement) if val == '?']

        if len(idx) == 0:
            if identify_arrangement(this_arrangement) == arrangement:
                valid_arrangements.append(this_arrangement)

    return valid_arrangements
