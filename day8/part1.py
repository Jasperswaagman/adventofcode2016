# vim: et sw=4 ts=4 autoindent
import re, copy
from collections import Counter

class Display:
    def __init__(self, width, height):
        self.grid = [['.' for x in range(width)] for y in range(height)]
    
    def render(self):
        print("\033c")
        for row in self.grid:
            print(''.join([str(x) for x in row]))

    def shift_col(self, x):
        tmp = self.grid[-1][x]
        copyGrid = copy.deepcopy(self.grid)
        for i in range(len(self.grid) - 1):
            self.grid[1+i][x] = copyGrid[i][x]
        self.grid[0][x] = tmp
    
    def shift_row(self, x):
        tmp = self.grid[x][-1]
        copyGrid = copy.deepcopy(self.grid)
        for i in range(len(self.grid[0]) - 1):
            self.grid[x][1+i] = copyGrid[x][i]
        self.grid[x][0] = tmp

    def rect(self, width, height):
        for row in range(height):
            for x in range(width):
               self.grid[row][x] = '#' 
        self.render()

    def rotate(self, t, x, amount):
        if t == 'column':
            for i in range(amount):
                self.shift_col(x)
        else:
            for i in range(amount):
                self.shift_row(x)
        self.render()


with open('input') as f:
    instructions = f.readlines()
    instructions = [x.strip() for x in instructions]

display = Display(50,6)

for i in instructions:
    wordList = re.sub('[^\w]', ' ', i).split()
    if wordList[0] == 'rect': 
        coordinates = re.findall('\d+', wordList[1])
        display.rect(int(coordinates[0]), int(coordinates[1]))
    elif wordList[0] == 'rotate':
        display.rotate(wordList[1], int(wordList[3]), int(wordList[5]))
    else:
        print('Bad instruction: {0}'.format(i))
        raise SystemExit(1)

c = Counter([i for s in display.grid for i in s])
print(c['#'])

