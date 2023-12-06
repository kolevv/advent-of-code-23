
def is_symbol(char):
    return not (char.isdigit() or char == '.')


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


def parse(array):
    sum_of_valid_numbers = 0
    for row_idx, row in enumerate(array):
        index = 0
        while (index < len(row) - 1):
            valid_flag = False
            num_buffer = []
            if (row[index].isdigit()):
                while (row[index].isdigit() and index < len(row) - 1):
                    if (is_valid_digit(array, row_idx, index)):
                        valid_flag = True
                    num_buffer.append(row[index])
                    index += 1
            if (num_buffer and valid_flag):
                print("FOUND VALID NUMBER:",
                      convert_buffer_to_int(num_buffer))
                sum_of_valid_numbers += convert_buffer_to_int(num_buffer)

            index += 1
    print(sum_of_valid_numbers)


dataInput = []
# inputFile = open("3/input", "r")
inputFile = open("3/test_input", "r")

# Build a 2D array from the input file
for line in inputFile.readlines():
    stripped_line = line.strip("\n")
    print(stripped_line)
    add_line = list(stripped_line)
    dataInput.append(add_line)

parse(dataInput)
