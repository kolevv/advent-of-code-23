words_to_numbers = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

def parse(lines, part_two = False):
    calibration_values = []

    for line in lines:
        if(part_two == True):
            line = replace_words(line)
        calibration_values.append(get_calibration_value(line))
    
    print(sum(calibration_values))

def get_calibration_value(line):
    first_digit = None
    last_digit = None
    for ch in line:
        if(ch.isdigit()):
            if(first_digit != None):
                last_digit = ch
            else:
                first_digit = ch
                last_digit = ch

    calibration_value = first_digit + last_digit
    return int(calibration_value)

def replace_words(input): 
    for match, replacement in words_to_numbers.items():
        input = input.replace(match, replacement)
    return input

if __name__ == "__main__":
    inputFile = open("1\input.txt", "r")
    lines =inputFile.readlines()

    print("Part 1 sum of calibration values:")
    parse(lines)

    print("---------------------------------")

    print("Part 2 sum of calibration values:")
    parse(lines, True)