dataInput = {}

inputFile = open("4/test_input", "r")
lines = inputFile.readlines()

for line in lines:
    line = line.strip("\n").split(":")
    dataInput.update({line[0]: line[1]})

print(dataInput)
