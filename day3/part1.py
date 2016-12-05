i = 0

fd = open('input', 'r')
for line in fd:
    sides = [int(s) for s in line.split() if s.isdigit()]
    if sides[0] + sides[1] > sides[2]:
        if sides[0] + sides[2] > sides[1]:
            if sides[2] + sides[1] > sides[0]:
                i += 1

print("total triangles: {0}".format(i))    
	
fd.close()

