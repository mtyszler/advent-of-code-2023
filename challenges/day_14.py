from functions_day_14 import *

# challenge 1
print("challenge 1")
grid = parse_input_file("../input_files/input_day_14.txt")

north = to_north_west(grid)
adjusted_grid = move_to_left(north)

load = comp_load(adjusted_grid)

print(load)

print("challenge 2")
grid = parse_input_file("../input_files/input_day_14.txt")
checked = [grid]
counter = 0
repeated = False
for c in range(1000000000):

    north = to_north_west(grid)
    grid = move_to_left(north)


    west = to_north_west(grid)
    grid = move_to_left(west)

    south = to_south(grid)
    grid = move_to_left(south)

    east = to_east(grid)
    grid = move_to_left(east)
    flipped = []
    for x in grid:
        x.reverse()
        flipped.append(x)
    grid = flipped
    counter += 1
    if grid in checked:
        print("repeat", checked.index(grid))
        key = checked.index(grid)
        f_key = (1000000000 - (key+1)) % (counter - 1 - (key+1)) + key+1+1
        print(counter, comp_load(to_north_west(checked[f_key])))
        repeated = True


    else:
        checked.append(grid)
        print(counter, comp_load(to_north_west(grid)))

    if repeated:
        north = to_north_west(checked[-2])
        final_grid = north
        break

load = comp_load(final_grid)
print(load+1)
