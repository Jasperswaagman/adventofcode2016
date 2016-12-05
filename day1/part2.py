import re, sys

# Get our input
f = open("input", "r")
input_file = f.read().split(", ")
input_file[-1] = input_file[-1].strip()

coords = [0, 0]
direction = 0
locations = [[0, 0]]

# Direction control
# 0 = North
# 1 = East
# 2 = South
# 3 = West
def direction_control(orientation, steps):
    # See if we"ve visited this place before
    global direction
    if orientation == "R":
        if direction == 3:
            direction = 0
        else: 
            direction += 1
    elif orientation == "L":
        if direction == 0:
            direction = 3
        else:
            direction -= 1
    
    if direction == 0:
        coords[1] += steps
    elif direction == 1:
        coords[0] += steps
    elif direction == 2:
        coords[1] -= steps
    elif direction == 3:
        coords[0] -= steps
    
    print("new coordinates: {0} direction:{1} steps:{2}".format(coords, direction, steps))
   
    store_locations(direction, steps)

def store_locations(direction, steps):
    last_place = locations[-1]
    
    if direction == 0:
        for ii in range(1, steps + 1):
            new_coord = []
            new_coord.append(last_place[0])
            new_coord.append(last_place[1] + ii)
            check_history(new_coord)
    if direction == 1:
        for ii in range(1, steps + 1):
            new_coord = []
            new_coord.append(last_place[0] + ii)
            new_coord.append(last_place[1])
            check_history(new_coord)
    if direction == 2:
        for ii in range(1, steps + 1):
            new_coord = []
            new_coord.append(last_place[0])
            new_coord.append(last_place[1] - ii)
            check_history(new_coord)
    if direction == 3:
        for ii in range(1, steps + 1):
            new_coord = []
            new_coord.append(last_place[0] - ii)
            new_coord.append(last_place[1])
            check_history(new_coord)


def check_history(final_coord):
        if final_coord not in locations:
            locations.append(final_coord)
        else:
            print("We've reached bunnyHQ on coords: {0}".format(final_coord))
            sys.exit("")

print("Start coordinates: {0}, {1}".format(coords[0], coords[1]))

for i in input_file:
    orientation = i[0]
    steps = int(i[1:])
    direction_control(orientation, steps)

print(locations)

print("End coordinates: {0}, {1}".format(coords[0], coords[1]))
distance = abs(coords[0]) + abs(coords[1])
print("distance travelled: {0}".format(distance))

f.close()
