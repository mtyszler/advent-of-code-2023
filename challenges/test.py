def solve(s, seed_interpreter):
    groups = s.split('\n\n')

    seed_ranges = seed_interpreter(list(map(int, groups[0].split()[1:])))

    for g in groups[1:]:
        step_mapping = [tuple(map(int, l.split()))
                        for l in g.splitlines()[1:]]

        new_ranges = []

        for start, r_len in seed_ranges:
            while r_len != 0:
                found_match = False
                best_dist = r_len

                for dst, src, length in step_mapping:
                    if src <= start < src+length:
                        # Found a match
                        off = start - src
                        rem_length = min(length - off, r_len)
                        new_ranges.append((dst+off, rem_length))
                        start += rem_length
                        r_len -= rem_length
                        found_match = True
                        break
                    else:
                        if start < src:
                            best_dist = min(src - start, best_dist)

                if not found_match:
                    handling_len = min(best_dist, r_len)
                    new_ranges.append((start, handling_len))
                    start += handling_len
                    r_len -= handling_len

        seed_ranges = new_ranges

    return min(start for start, length in seed_ranges)


def part2(ss):
    input_file = open(ss, 'r')
    s = input_file.read().rstrip('\n')
    def seed_interpreter(nums):
        return list(zip(nums[::2], nums[1::2]))


    answer = solve(s, seed_interpreter)

    print(answer)
part2('../input_files/input_day_05_example.txt')