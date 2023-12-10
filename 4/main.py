dataInput = {}

# inputFile = open("4/test_input", "r")
inputFile = open("4/input", "r")
lines = inputFile.readlines()

for line in lines:
    line = line.strip("\n").split(":")
    dataInput.update({line[0]: line[1]})


def find_winners(numbers):
    results = {}
    winning, roll = numbers.split("|")
    winning = winning.strip()
    winning = winning.split(" ")
    roll = roll.strip()
    roll = roll.split(" ")

    for i in winning:
        matches = roll.count(i)
        if (matches > 0 and i != ''):
            results[i] = matches

    return (results)


def calculate_score(matches):
    total = 1
    if (not matches):
        return 0
    else:
        num_of_matches = sum(matches.values())
        for i in range(num_of_matches - 1):
            total = total * 2

        return total


def parse(cards):
    output = open("./output", "a")
    full_total = 0
    for card, numbers in cards.items():

        numbers = numbers.strip()
        card_winners = find_winners(numbers)
        # print("%d has %d winning numbers",
        #   (card, len(card_winners.values())))
        card_total = calculate_score(card_winners)
        full_total += card_total
        out_string = ""
        if (card_winners):
            for (key, value) in card_winners.items():
                out_string += " number: {}, {} | ".format(key, value)

        output.write(
            "{} has {} winning numbers({}) total score: {} \n".format(card, len(card_winners.keys()), out_string, card_total))

    print(full_total)


parse(dataInput)
