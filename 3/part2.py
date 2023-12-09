from enum import Enum


class Direction(Enum):
    LEFT = -1
    RIGHT = 1


dataInput = []
inputFile = open("3/input", "r")
# inputFile = open("3/test_input", "r")

# Build a 2D array from the input file
for line in inputFile.readlines():
    stripped_line = line.strip("\n")
    dataInput.append(list(stripped_line))


def find_num_sequence(y_pos, start_idx):
    number_bufer = [dataInput[y_pos][start_idx]]
    processed_x_positions = {start_idx}
    for direction in (Direction):
        length = len(dataInput[y_pos]) - 1
        next_idx = start_idx + direction.value
        while True:
            if next_idx > length:
                break
            observed_element = dataInput[y_pos][next_idx]
            if next_idx < 0 or next_idx > length or not observed_element.isnumeric():
                break
            processed_x_positions.add(next_idx)
            if direction.name == "LEFT":
                number_bufer.insert(0, observed_element)
            else:
                number_bufer.append(observed_element)
            next_idx += direction.value

    return number_bufer, processed_x_positions


def get_adjacent_numbers(row, column):
    y = len(dataInput)
    x = len(dataInput[0])  # Evey line is the same length
    adjacent_nums = []
    for dy in range(-1 if (row > 0) else 0, 2 if (row < y - 1) else 1):
        processed_x_positions = set()
        for dx in range(-1 if column > 0 else 0, 2 if (column < x-1) else 1):
            if (dy != 0 or dx != 0):
                element = dataInput[row+dy][column + dx]
                if (element.isnumeric() and column+dx not in processed_x_positions):
                    number, processed_x = find_num_sequence(
                        row+dy, column+dx)
                    processed_x_positions = processed_x_positions | processed_x
                    adjacent_nums.append(number)
    return adjacent_nums


def calc_gear_ratio(part_numbers_list):
    converted_list = [int("".join(part)) for part in part_numbers_list]
    if len(converted_list) != 2:
        raise ValueError(
            "Something weird happened when converting part numbers list buffer to numbers")
    return converted_list[0] * converted_list[1]


def solve_part_2(array):
    gear_ratio_sum = 0
    for y in range(len(array)):
        x = 0
        while (x < len(array[0])):
            if array[y][x] == "*":
                part_numbers = get_adjacent_numbers(y, x)
                if len(part_numbers) == 2:
                    gear_ratio_sum += calc_gear_ratio(part_numbers)
            x += 1
    print(gear_ratio_sum)


solve_part_2(dataInput)
