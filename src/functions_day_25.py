def parse_input_file(input_file: str) -> set[frozenset]:
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    pairs = set()
    for this_line in lines:
        a, b = this_line.strip().split(": ")
        bb = b.split(" ")
        for x in bb:
            pairs.add(frozenset([a,x]))

    return pairs


def find_intersections(pairs: set[frozenset]):
    print()
    original_pairs = pairs.copy()
    all_pairs = original_pairs.copy()

    list_all_pairs = list(all_pairs)
    for i in range(len(list_all_pairs)):
        for j in range(i+1, len(list_all_pairs)):
            for l in range(j+1, len(list_all_pairs)):

                print(i,j,l, len(original_pairs))
                all_connected = []

                all_pairs = original_pairs.copy()
                all_pairs.remove(list_all_pairs[i])
                all_pairs.remove(list_all_pairs[j])
                all_pairs.remove(list_all_pairs[l])

                while len(all_pairs) > 0:

                    this_connected = set()

                    remaining_pairs = all_pairs.copy()
                    old_remaining_pairs = set()

                    while len(all_pairs)>0 and len(remaining_pairs) != len(old_remaining_pairs):
                        old_remaining_pairs = remaining_pairs.copy()
                        remaining_pairs = all_pairs.copy()
                        for x in all_pairs:
                            if len(this_connected) == 0:
                                this_connected.update([xx for xx in x])
                                remaining_pairs.remove(x)
                            else:
                                xx = list(x)
                                if xx[0] in this_connected or xx[1] in this_connected:
                                    this_connected.update(xx)
                                    remaining_pairs.remove(x)

                        all_pairs = remaining_pairs.copy()

                    all_connected.append(this_connected)
                    all_pairs = original_pairs.copy()
                    new_pairs = all_pairs.copy()
                    for xx in all_connected:
                        for x in xx:
                            for y in all_pairs:
                                if x in y and y in new_pairs:
                                    new_pairs.remove(y)
                    all_pairs = new_pairs.copy()

                if len(all_connected) == 2:
                    return all_connected

    return -99

