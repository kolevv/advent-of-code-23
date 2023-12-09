from enum import Enum


class Direction(Enum):
    LEFT = -1
    RIGHT = 1


dataInput = []
# inputFile = open("3/input", "r")
inputFile = open("3/test_input", "r")

# Build a 2D array from the input file
for line in inputFile.readlines():
    stripped_line = line.strip("\n")
    dataInput.append(list(stripped_line))


def get_neighbours(array, row, column):
    y = len(dataInput)
    x = len(dataInput[0])  # Evey line is the same length
    adjacent = []
    for dy in range(-1 if (row > 0) else 0, 2 if (row < y - 1) else 1):
        for dx in range(-1 if column > 0 else 0, 2 if (column < x-1) else 1):
            if (dy != 0 or dx != 0):
                adjacent.append(array[row+dy][column + dx])

    return adjacent


def find_full_number(y_pos, start_idx):
    number_bufer = [dataInput[y_pos][start_idx]]
    for direction in (Direction):
        length = len(dataInput[y_pos])
        # print("Looking ", direction.name)
        next_idx = start_idx + direction.value
        while True:
            observed_element = dataInput[y_pos][next_idx]
            if next_idx < 0 or next_idx > length or not observed_element.isnumeric():
                # print("Terminating looking", direction.name)
                break
            if direction.name == "LEFT":
                number_bufer.insert(0, observed_element)
            else:
                number_bufer.append(observed_element)
            next_idx += direction.value
    print(number_bufer)


def get_adjacent_numbers(row, column):
    y = len(dataInput)
    x = len(dataInput[0])  # Evey line is the same length
    adjacent = []
    for dy in range(-1 if (row > 0) else 0, 2 if (row < y - 1) else 1):
        for dx in range(-1 if column > 0 else 0, 2 if (column < x-1) else 1):
            if (dy != 0 or dx != 0):
                element = dataInput[row+dy][column + dx]
                if (element.isnumeric()):
                    print("Found numeric neighbour", element)
                    find_full_number(row+dy, column+dx)

    return adjacent

# def get_adjacent_numbers(row, column):
#     processed_locations = set()
#     max_rows = len(dataInput)
#     max_columns = len(dataInput[0])
#     for d_row in range(-1 if (row > 0) else 0, 2 if (row < max_rows) else 1):
#         for d_column in range(-1 if column > 0 else 0, 2 if (column < max_columns) else 1):
#             if (d_row != 0 or d_column != 0):
#                 element = dataInput[row+d_row][column+d_column]
#                 print("Found adjacent",
#                       dataInput[row+d_row][column+d_column])
#                 if (element not in processed_locations):
#                     processed_locations.add(element)
#                     if (element.isdigit()):
#                         print("Found digit!", element)


def get_full_number(y_pos, start_idx):
    end_idx = start_idx
    value_buf = []
    while end_idx < len(dataInput[y_pos]) and dataInput[y_pos][end_idx].isnumeric():
        value_buf.append(dataInput[y_pos][end_idx])
        end_idx += 1
    return end_idx - 1, int("".join(value_buf))


# def solve_part_2(array):

#     full_numbers = list()
#     for y in range(len(array)):
#         x = 0
#         while (x < len(array[0])):
#             if array[y][x].isnumeric():
#                 endIdx, value = get_full_number(y, x)
#                 full_numbers.append({
#                     "start": (y, x),
#                     "end": (y, endIdx),
#                     "value": value

#                 })
#                 x = endIdx
#                 # print("Looking at gear at ", x, y)
#                 # get_adjacent_numbers(y, x)
#             x += 1
#     print(full_numbers)


def solve_part_2(array):
    for y in range(len(array)):
        x = 0
        while (x < len(array[0])):
            if array[y][x] == "*":
                # print("Looking at gear at ", x, y)
                get_adjacent_numbers(y, x)
            x += 1


solve_part_2(dataInput)
