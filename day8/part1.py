import re, time, sys

screen_width = 50
screen_height = 6

def init_input():
    with open('small_input') as f:
        o = f.readlines()
        o = [x.strip() for x in o]
        return o

def init_display():
    global screen_width, screen_height
    s_x = []
    for _ in range(screen_width): s_x.append('.')
    screen = {}
    for i in range(screen_height): screen[i] = s_x
    return screen

def print_screen(s):
    sys.stdout.write('\033c')
    for c in s: print(''.join(s[c]))

def rect(o):
    global screen
    coords = re.search('(\d+)x(\d+)', o)
    x = int(coords.group(1))
    y = int(coords.group(2))
    # draw a x by y rectangle in our screen
    for i in range(y):
        new_row = []
        for _ in range(x):
            new_row.append('#')
        for _ in range(x, screen_width):
            new_row.append('.')
        screen[i] = new_row

def rotate_row(o):
    pass

def rotate_col(o):
    pass

operations = init_input()
screen = init_display()

for o in operations:
    if o.startswith('rect'): rect(o);
    elif o.startswith('rotate r'): rotate_row(o)
    else: rotate_col(o)
    time.sleep(.2)
    print_screen(screen)

