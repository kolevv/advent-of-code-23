dataInput = []
# inputFile = open("3/input", "r")
inputFile = open("3/test_input", "r")

# Build a 2D array from the input file
for line in inputFile.readlines():
    stripped_line = line.strip("\n")
    dataInput.append(list(stripped_line))


def is_symbol(char):
    return not (char.isdigit() or char == '.')


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


def get_neighbours(array, row, column):
    y = len(dataInput)
    x = len(dataInput[0])  # Evey line is the same length
    adjacent = []
    for dy in range(-1 if (row > 0) else 0, 2 if (row < y - 1) else 1):
        for dx in range(-1 if column > 0 else 0, 2 if (column < x-1) else 1):
            if (dy != 0 or dx != 0):
                adjacent.append(array[row+dy][column + dx])

    return adjacent


def is_valid_digit(array, row, column):
    neighbours = get_neighbours(array, row, column)
    for el in neighbours:
        if (is_symbol(el)):
            return True
    return False


def convert_buffer_to_int(number_buffer):
    result = int("".join(number_buffer))
    return result


def solve_part_1(array):

    sum_of_valid_numbers = 0
    for row_idx, row in enumerate(array):
        column = 0
        while (column < len(row) - 1):
            valid_flag = False
            num_buffer = []
            if (row[column].isdigit()):
                while True:
                    if (column >= len(row) or not row[column].isdigit()):
                        break
                    if (is_valid_digit(array, row_idx, column)):
                        valid_flag = True
                    num_buffer.append(row[column])
                    column += 1
            else:
                column += 1

            if (num_buffer and valid_flag):
                sum_of_valid_numbers += convert_buffer_to_int(num_buffer)

    print(sum_of_valid_numbers)


def solve_part_2(array):
    for y in range(len(array)):
        x = 0
        while (x < len(array[0])):
            if array[y][x] == "*":
                # print("Looking at gear at ", x, y)
                get_adjacent_numbers(y, x)
            x += 1


solve_part_1(dataInput)
solve_part_2(dataInput)
