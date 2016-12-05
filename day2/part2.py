instructions = [[] for _ in range(5)]
i = 0
last_button = 5
bathroom_code = []

fd = open('input', 'r')
for line in fd:
    line = line.strip()
    for c in line:
        instructions[i].append(c)
    i += 1
fd.close()

def one(instruction):
    if instruction == 'D':
        return 3
    else: return 1


def two(instruction):
    if instruction == 'R':
        return 3
    elif instruction == 'D':
        return 6
    else: return 2


def three(instruction):
    if instruction == 'D':
        return 7
    elif instruction == 'L':
        return 2
    elif instruction == 'R':
        return 4
    elif instruction == 'U':
        return 1


def four(instruction):
    if instruction == 'D':
        return 8
    elif instruction == 'L':
        return 3
    else: return 4


def five(instruction):
    if instruction == 'R':
        return 6
    else: return 5


def six(instruction):
    if instruction == 'L':
        return 5
    elif instruction == 'D':
        return 10
    elif instruction == 'U':
        return 2
    elif instruction == 'R':
        return 7


def seven(instruction):
    if instruction == 'R':
        return 8
    elif instruction == 'U':
        return 3
    elif instruction == 'L':
        return 6
    elif instruction == 'D':
        return 11


def eight(instruction):
    if instruction == 'L':
        return 7
    elif instruction == 'R':
        return 9
    elif instruction == 'U':
        return 4
    elif instruction == 'D':
        return 12


def nine(instruction):
    if instruction == 'L':
        return 8
    else: return 9


def ten(instruction):
    if instruction == 'U':
        return 6
    elif instruction == 'R':
        return 11
    else: return 10


def eleven(instruction):
    if instruction == 'U':
        return 7
    elif instruction == 'R':
        return 12
    elif instruction == 'L':
        return 10
    elif instruction == 'D':
        return 13


def twelve(instruction):
    if instruction == 'U':
        return 8
    elif instruction == 'L':
        return 11
    else: return 12


def thirteen(instructions):
    if instructions == 'U':
        return 11
    else: return 13


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
        elif last_button == 10:
            last_button = ten(direction)
        elif last_button == 11:
            last_button = eleven(direction)
        elif last_button == 12:
            last_button = twelve(direction)
        elif last_button == 13:
            last_button = thirteen(direction)
    i += 1
    bathroom_code.append(last_button)

bathroom_code = ["A" if x==10 else x for x in bathroom_code]
bathroom_code = ["B" if x==11 else x for x in bathroom_code]
bathroom_code = ["C" if x==12 else x for x in bathroom_code]
bathroom_code = ["D" if x==13 else x for x in bathroom_code]
bathroom_code = [str(x) for x in bathroom_code]
print("Bathroomcode: {0}".format("".join(bathroom_code)))

