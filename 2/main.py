loaded_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def parse(inputFile):
    sum_of_possible_games = 0
    sum_of_cube_powers = 0
    for line in inputFile:
        gameId, game = line.strip("\n").split(": ")
        gameId = gameId.split()[1]
        is_possible, fewest_possible_cubes = is_game_possible(game)
        if is_possible:
            sum_of_possible_games += int(gameId)
        cube_power = 1
        for cube in fewest_possible_cubes:
            cube_power = cube_power * int(fewest_possible_cubes[cube])
        sum_of_cube_powers += cube_power

    return sum_of_possible_games, sum_of_cube_powers


def is_game_possible(game):
    fewest_possible_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    is_possible = True
    draws = game.split("; ")
    for cube_set in draws:
        cubes = cube_set.split(", ")
        for cube in cubes:
            number, colour = cube.split()
            number = int(number)
            if number > fewest_possible_cubes[colour]:
                fewest_possible_cubes[colour] = number
            if number > loaded_cubes[colour]:
                is_possible = False

    return is_possible, fewest_possible_cubes


if __name__ == "__main__":
    inputFile = open("2/input", "r")
    possible_games, cube_powers = parse(inputFile)
    print("Sum of possible games: ", possible_games)
    print("Sum of cube powers: ", cube_powers)
