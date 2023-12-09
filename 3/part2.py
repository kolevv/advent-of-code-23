dataInput = []
# inputFile = open("3/input", "r")
inputFile = open("3/test_input", "r")

# Build a 2D array from the input file
for line in inputFile.readlines():
    stripped_line = line.strip("\n")
    dataInput.append(list(stripped_line))


def get_adjacent_numbers(row, column):
    processed_locations = set()
    max_rows = len(dataInput)
    max_columns = len(dataInput[0])
    for d_row in range(-1 if (row > 0) else 0, 2 if (row < max_rows) else 1):
        for d_column in range(-1 if column > 0 else 0, 2 if (column < max_columns) else 1):
            if (d_row != 0 or d_column != 0):
                element = dataInput[row+d_row][column+d_column]
                print("Found adjacent",
                      dataInput[row+d_row][column+d_column])
                if (element not in processed_locations):
                    processed_locations.add(element)
                    if (element.isdigit()):
                        print("Found digit!", element)


def get_full_number(y_pos, start_idx):
    end_idx = start_idx
    value_buf = []
    while end_idx < len(dataInput[y_pos]) and dataInput[y_pos][end_idx].isnumeric():
        value_buf.append(dataInput[y_pos][end_idx])
        end_idx += 1
    return end_idx - 1, int("".join(value_buf))


def solve_part_2(array):
    full_numbers = list()
    for y in range(len(array)):
        x = 0
        while (x < len(array[0])):
            if array[y][x].isnumeric():
                endIdx, value = get_full_number(y, x)
                full_numbers.append({
                    "start": (y, x),
                    "end": (y, endIdx),
                    "value": value

                })
                x = endIdx
                # print("Looking at gear at ", x, y)
                # get_adjacent_numbers(y, x)
            x += 1
    print(full_numbers)


solve_part_2(dataInput)
