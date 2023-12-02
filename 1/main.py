def main():
    inputFile = open("input.txt", "r")
    lines = inputFile.readlines()
    calibration_values = []

    for line in lines:
        calibration_values.append(get_calibration_value(line))
    
    print("Sum of calibration values:")
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



if __name__ == "__main__":
    main()