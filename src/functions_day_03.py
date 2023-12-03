import pandas as pd


def parse_input_file(input_file: str) -> pd.DataFrame:
    """

    Args:
        input_file:

    Returns:

    """
    df = pd.read_fwf(input_file)
    df = df.iloc[:, 0].apply(lambda x: pd.Series(list(x)))
    return df


def find_part_numbers(df: pd.DataFrame) -> list:
    part_numbers = []

    nrows, ncols = df.shape
    nrows -= 1
    ncols -= 1

    for row_id, this_row in df.iterrows():
        candidate = ""
        left = -999
        right = -999
        for col in range(len(this_row)):
            if this_row[col].isdigit():
                if left == -999:
                    left = col
                right = col
                candidate += str(this_row[col])

            elif candidate == "":
                continue
            else:

                # check for symbol
                found_symbol = False
                for check_row in range(max(int(row_id) - 1, 0),
                                       min(int(row_id) + 1, nrows) + 1):
                    if found_symbol:
                        break

                    for check_col in range(max(left - 1, 0),
                                           min(right + 1, ncols) + 1):

                        check_symbol = df.iloc[check_row, check_col]
                        if (not check_symbol.isdigit()) & (check_symbol != '.'):
                            part_numbers.append(int(candidate))
                            found_symbol = True
                            break

                candidate = ""
                left = -999
                right = -999

    return part_numbers


def find_gear_ratios(df: pd.DataFrame) -> list:
    gear_ratios = []
    part_gears = []

    nrows, ncols = df.shape
    nrows -= 1
    ncols -= 1

    for row_id, this_row in df.iterrows():
        candidate = ""
        left = -999
        right = -999
        for col in range(len(this_row)):
            if this_row[col].isdigit():
                if left == -999:
                    left = col
                right = col
                candidate += str(this_row[col])

            elif candidate == "":
                continue
            else:

                # check for symbol
                found_symbol = False
                for check_row in range(max(int(row_id) - 1, 0),
                                       min(int(row_id) + 1, nrows) + 1):
                    if found_symbol:
                        break

                    for check_col in range(max(left - 1, 0),
                                           min(right + 1, ncols) + 1):

                        check_symbol = df.iloc[check_row, check_col]
                        if check_symbol == "*":
                            part_gears.append([int(candidate), (check_row, check_col)])
                            found_symbol = True
                            break

                candidate = ""
                left = -999
                right = -999

    gear_elements = {}
    for part_number, location in part_gears:
        if location not in gear_elements.keys():
            gear_elements[location] = [part_number]
        else:
            gear_elements[location].append(part_number)

    for candidate_locations in gear_elements.keys():
        candidate_gears = gear_elements[candidate_locations]
        if len(candidate_gears) == 2:
            gear_ratios.append(candidate_gears[0]*candidate_gears[1])

    return gear_ratios
