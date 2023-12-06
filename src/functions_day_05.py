def parse_input_file(input_file: str) -> float:
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
    max_counter = 0

    for this_line in lines:
        if 'seeds' in this_line:
            print("seeds")
            _, seed_str = this_line.split(":")
            seeds = [int(x) for x in seed_str.strip().split(" ")]
            max_counter = max(seeds)

        elif "seed-to-soil" in this_line:
            print("seed-to-soil")
            target_dict = seed_to_soil
        elif "soil-to-fertilizer" in this_line:
            print("soil-to-fertilizer")
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

            for i in range(int(range_len)):
                target_dict[int(source_range_start) + i] = int(dest_range_start) + i
                if int(dest_range_start) + i > max_counter:
                    max_counter = int(dest_range_start) + i

    # complete dicts:

    for this_dict in [seed_to_soil,
                      soil_to_fertilizer,
                      fertilizer_to_water,
                      water_to_light,
                      light_to_temperature,
                      temperature_to_humidity,
                      humidity_to_location]:
        print("complete dict")
        for i in range(max_counter + 1):
            if i not in this_dict.keys():
                this_dict[i] = i

    # find the lowest location:
    location = 10000000
    this_location = 10000000
    for this_seed in seeds:

        this_location = humidity_to_location[temperature_to_humidity[
            light_to_temperature[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[this_seed]]]]]]]
        if this_location < location:
            location = this_location

    return this_location


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

        if this_key[0] <= key <= this_key[1]:
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

    seeds = {}
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
                seeds[seeds_base[i]] = seeds_base[i + 1]

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
    for this_seed_start in seeds.keys():
        print('--------------------------')
        next_key = map(lambda x: find_location(key=x, list_of_mappers=[seed_to_soil,
                                                                       soil_to_fertilizer,
                                                                       fertilizer_to_water,
                                                                       water_to_light,
                                                                       light_to_temperature,
                                                                       temperature_to_humidity,
                                                                       humidity_to_location]),
                       range(this_seed_start, this_seed_start + seeds[this_seed_start]))
        next_key = min(list(next_key))
        if next_key < location:
            print(next_key)
            location = next_key

    return location


def find_location(key: int, list_of_mappers: list[dict]) -> int:
    next_key = key
    for search_mapper in list_of_mappers:
        next_key = find_key(next_key, search_mapper)

    return next_key
