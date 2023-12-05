
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

    print("Neighbours:")
    print(adjacent)
    return dataInput


dataInput = []
testInpuit = [["a", "b", "c", "d"],
              ["1", "2", "3", "4"],
              ["+", "-", "!", "?"]
              ]

inputFile = open("3/input", "r")
# Build a 2D array from the input file
for line in inputFile.readlines():
    dataInput.append(list(line))

# get_neighbours(dataInput, 0, 28)
get_neighbours(testInpuit, 1, 2)
