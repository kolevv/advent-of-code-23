loaded_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def parse(inputFile):
    sum = 0
    for line in inputFile:
        gameId, game = line.strip("\n").split(": ")
        gameId = gameId.split()[1]
        if isGamePossible(game):
            sum += int(gameId)

    return sum


def isGamePossible(game):
    draws = game.split("; ")
    for cube_set in draws:
        cubes = cube_set.split(", ")
        for cube in cubes:
            number, colour = cube.split()
            if int(number) > loaded_cubes[colour]:
                return False
    return True


if __name__ == "__main__":
    inputFile = open("2\input", "r")
    print(parse(inputFile))
