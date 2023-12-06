
def is_symbol(char):
    return not (char.isdigit() or char == '.')


def get_neighbours(array, row, column):
    y = len(dataInput)
    x = len(dataInput[0])  # Evey line is the same length
    adjacent = []
    for dy in range(-1 if (row > 0) else 0, 2 if (row < y) else 1):
        for dx in range(-1 if column > 0 else 0, 2 if (column < x) else 1):
            if (dy != 0 or dx != 0):
                adjacent.append(array[row+dy][column + dx])

    return adjacent


def is_valid_digit(array, row, column):
    neighbours = get_neighbours(array, row, column)
    for el in neighbours:
        if (is_symbol(el)):
            return True
    return False


def find_number(array):
    num_buffer = []
    for row in array:

        iterator = iter(row)
        i = next(iterator, False)
        while (i):
            i = next(iterator, False)
            print("LOOPING", i)
            if (i.isdigit()):
                while (i.isdigit() and i):
                    num_buffer.append(i)
                    i = next(iterator, False)
                print(num_buffer)

        print("DONE LOOPING")


dataInput = []


inputFile = open("3/input", "r")
# Build a 2D array from the input file
for line in inputFile.readlines():
    dataInput.append(list(line))

# get_neighbours(dataInput, 0, 28)
find_number(dataInput)
