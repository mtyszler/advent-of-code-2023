def parse_input_file_v2(input_file: str) -> float:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    seeds = []
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}

    target_dict = {}

    for this_line in lines:
        if 'seeds' in this_line:
            _, seed_str = this_line.split(":")
            seeds = [int(x) for x in seed_str.strip().split(" ")]

        elif "seed-to-soil" in this_line:
            target_dict = seed_to_soil
        elif "soil-to-fertilizer" in this_line:
            target_dict = soil_to_fertilizer
        elif "fertilizer-to-water" in this_line:
            target_dict = fertilizer_to_water
        elif "water-to-light" in this_line:
            target_dict = water_to_light
        elif "light-to-temperature" in this_line:
            target_dict = light_to_temperature
        elif "temperature-to-humidity" in this_line:
            target_dict = temperature_to_humidity
        elif "humidity-to-location" in this_line:
            target_dict = humidity_to_location

        elif this_line.strip() == "":
            continue

        else:
            dest_range_start, source_range_start, range_len = this_line.strip().split(" ")

            target_dict[(int(source_range_start), int(source_range_start) + int(range_len))] = \
                (int(dest_range_start), int(dest_range_start) + int(range_len))

    # find the lowest location:
    location = 1000000000000000000
    for this_seed in seeds:

        next_key = this_seed
        for search_mapper in [seed_to_soil,
                              soil_to_fertilizer,
                              fertilizer_to_water,
                              water_to_light,
                              light_to_temperature,
                              temperature_to_humidity,
                              humidity_to_location]:
            next_key = find_key(next_key, search_mapper)

        if next_key < location:
            location = next_key

    return location


def find_key(key: int, mapping: dict) -> int:
    found_key = -999
    for this_key in mapping.keys():

        if this_key[0] <= key < this_key[1]:
            found_key = mapping[this_key][0] + (key - this_key[0])
            break

    if found_key == -999:
        found_key = key

    return found_key


def parse_input_file_v3(input_file: str) -> float:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    seeds = []
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}

    target_dict = {}

    for this_line in lines:
        if 'seeds' in this_line:
            _, seed_str = this_line.split(":")
            seeds_base = [int(x) for x in seed_str.strip().split(" ")]
            for i in range(0, len(seeds_base), 2):
                seeds.append((seeds_base[i], seeds_base[i] + seeds_base[i + 1]))

        elif "seed-to-soil" in this_line:
            target_dict = seed_to_soil
        elif "soil-to-fertilizer" in this_line:
            target_dict = soil_to_fertilizer
        elif "fertilizer-to-water" in this_line:
            target_dict = fertilizer_to_water
        elif "water-to-light" in this_line:
            target_dict = water_to_light
        elif "light-to-temperature" in this_line:
            target_dict = light_to_temperature
        elif "temperature-to-humidity" in this_line:
            target_dict = temperature_to_humidity
        elif "humidity-to-location" in this_line:
            target_dict = humidity_to_location

        elif this_line.strip() == "":
            continue

        else:
            dest_range_start, source_range_start, range_len = this_line.strip().split(" ")

            target_dict[(int(source_range_start), int(source_range_start) + int(range_len))] = \
                (int(dest_range_start), int(dest_range_start) + int(range_len))

    # find the lowest location:
    location_ranges = []
    for this_seed_range in seeds:
        next_range = [this_seed_range]
        for search_mapper in [seed_to_soil,
                              soil_to_fertilizer,
                              fertilizer_to_water,
                              water_to_light,
                              light_to_temperature,
                              temperature_to_humidity,
                              humidity_to_location]:
            next_range = find_ranges(next_range, search_mapper)
        location_ranges.extend(next_range)

    # find the lowest location:
    location = min([x[0] for x in location_ranges])

    return location


def find_location(key: int, list_of_mappers: list[dict]) -> int:
    next_key = key
    for search_mapper in list_of_mappers:
        next_key = find_key(next_key, search_mapper)

    return next_key


def find_ranges(key: (int, int), mapping: dict) -> list[(int, int)]:
    translated_ranges = []
    still_unprocessed_ranges = key.copy()

    for this_key in mapping.keys():
        unprocessed_ranges = list(still_unprocessed_ranges.copy())
        still_unprocessed_ranges = set()

        while len(unprocessed_ranges) > 0:
            this_unprocessed_range = unprocessed_ranges.pop()
            lower = this_unprocessed_range[0]
            upper = this_unprocessed_range[1]

            # case 1 range does not overlap mapping range:
            if lower >= this_key[1] or upper < this_key[0]:
                still_unprocessed_ranges.add((lower, upper))
                continue

            # lower number
            if this_key[0] <= lower < this_key[1]:
                # lower within range:
                mapped_lower = mapping[this_key][0] + (lower - this_key[0])
            else:
                # lower not within range, split:
                still_unprocessed_ranges.add((lower, this_key[0]))
                mapped_lower = mapping[this_key][0]

            #  higher number:
            if this_key[0] <= upper < this_key[1]:
                # upper within range:
                mapped_upper = mapping[this_key][0] + (upper - this_key[0])
                translated_ranges.append((mapped_lower, mapped_upper))
            else:
                # upper not within range, split:
                translated_ranges.append((mapped_lower, mapping[this_key][1]))
                still_unprocessed_ranges.add((this_key[1], upper))

    translated_ranges.extend(list(still_unprocessed_ranges))

    return translated_ranges
