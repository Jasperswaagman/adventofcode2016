amount_of_triangles = 0
sides = []

fd = open('single_column', 'r')
for line in fd:
    line = line.strip()
    sides.append(line)
    sides = [int(x) for x in sides]
    if len(sides) == 3:
        if sides[0] + sides[1] > sides[2]:
            if sides[0] + sides[2] > sides[1]:
                if sides[2] + sides[1] > sides[0]:
                    amount_of_triangles += 1
        sides = []

print("Amount of triangles: {0}".format(amount_of_triangles))

fd.close()
