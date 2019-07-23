import sys

variables = {}

def getValue(v1):
    if v1 in variables:
        return variables[v1]

    return int(v1)

def print_1():
    if "_1" in variables:
        print(variables["_1"])

def processLine(line):
    tokens = line.split(" ")
    # Case: var = v1
    if len(tokens) == 3 and tokens[1] == "=":
        variables[tokens[0]] = getValue(tokens[2])
        return

    if len(tokens) == 1:
        print_1()
        return

for line in sys.stdin:
    line = line.strip()
    if line == "stop":
        break
    processLine(line)
    print("Current variables: ", variables)
