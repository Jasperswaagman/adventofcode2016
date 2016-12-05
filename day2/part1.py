import re,sys

last_button = 5
bathroom_code= []
instructions = [[] for _ in range(5)]
i = 0

fd = open('input', 'r')
for line in fd:
    line = line.strip()
    for c in line:
        instructions[i].append(c)
    i += 1
fd.close()

def one(instruction):
    if instruction == 'R':
        return 2
    elif instruction == 'D':
        return 4
    else: return 1

def two(instruction):
    if instruction == 'R':
        return 3
    if instruction == 'D':
        return 5
    if instruction == 'L':
        return 1
    else: return 2

def three(instruction):
    if instruction == 'D':
        return 6
    if instruction == 'L':
        return 2
    else: return 3

def four(instruction):
    if instruction == 'R':
        return 5
    if instruction == 'D':
        return 7
    if instruction == 'U':
        return 1
    else: return 4

def five(instruction):
    if instruction == 'R':
        return 6
    if instruction == 'D':
        return 8
    if instruction == 'U':
        return 2
    if instruction == 'L':
        return 4

def six(instruction):
    if instruction == 'L':
        return 5
    if instruction == 'D':
        return 9
    if instruction == 'U':
        return 3
    else: return 6

def seven(instruction):
    if instruction == 'R':
        return 8
    if instruction == 'U':
        return 4
    else: return 7

def eight(instruction):
    if instruction == 'L':
        return 7
    if instruction == 'R':
        return 9
    if instruction == 'U':
        return 5
    else: return 8

def nine(instruction):
    if instruction == 'U':
        return 6
    if instruction == 'L':
        return 8
    else: return 9

i = 0

while i < len(instructions):
    for direction in instructions[i]:
        if last_button == 1:
            last_button = one(direction)
        elif last_button == 2:
            last_button = two(direction)
        elif last_button == 3:
            last_button = three(direction)
        elif last_button == 4:
            last_button = four(direction)
        elif last_button == 5:
            last_button = five(direction)
        elif last_button == 6:
            last_button = six(direction)
        elif last_button == 7:
            last_button = seven(direction)
        elif last_button == 8:
            last_button = eight(direction)
        elif last_button == 9:
            last_button = nine(direction)
    i += 1
    bathroom_code.append(last_button)

bathroom_code = [str(x) for x in bathroom_code]
print("Bathroomcode: {0}".format("".join(bathroom_code)))

