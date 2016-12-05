i = 0

fd = open('input', 'r')
for line in fd:
    sides = [int(s) for s in line.split() if s.isdigit()]
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        i += 1

print("total triangles: {0}".format(i))    
	
fd.close()

