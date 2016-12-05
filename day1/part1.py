import re

# Get our input
f = open('input', 'r')
input_file = f.read().split(', ')
input_file[-1] = input_file[-1].strip()

coords = {'x': 0, 'y':0}
direction = 0
locations = []

# Direction control
# 0 = North
# 1 = East
# 2 = South
# 3 = West
def direction_control(orientation, steps):
    # See if we've visited this place before
    global direction
    if orientation == 'R':
        if direction == 3:
            direction = 0
        else: 
            direction += 1
    elif orientation == 'L':
        if direction == 0:
            direction = 3
        else:
            direction -= 1
    
    if direction == 0:
        coords['y'] += steps
    elif direction == 1:
        coords['x'] += steps
    elif direction == 2:
        coords['y'] -= steps
    elif direction == 3:
        coords['x'] -= steps

    locations.append([coords['x'], coords['y']])


print('Start coordinates: {0}, {1}'.format(coords['x'], coords['y']))

for i in input_file:
    orientation = i[0]
    steps = int(i[1:])
    direction_control(orientation, steps)


print('End coordinates: {0}, {1}'.format(coords['x'], coords['y']))
distance = abs(coords['x']) + abs(coords['y'])
print('distance travelled: {0}'.format(distance))

f.close()

