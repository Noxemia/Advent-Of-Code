from typing import Tuple, List, Set
from copy import deepcopy, copy
from enum import Enum

class Dir(Enum):
    up = 0
    right = 1
    down = 2
    left = 3

gmap, pos = [], ()
for y, line in enumerate(open('input.txt', 'r').readlines()):
    line = [x for x in line.strip("\n")]
    if "^" in line:
        pos = (line.index("^"), y)
    gmap.append(line)

savedmap = deepcopy(gmap)
saved: List[Tuple[int,int,int]] = []
originalPos = copy(pos)

angle = 0

def getNXNY(x, y, ang=None):
    global angle
    _angle = ang if ang != None else angle 
    if _angle == 0: return (x, y-1)
    if _angle == 1: return (x+1, y)
    if _angle == 2: return (x, y+1)
    if _angle == 3: return (x-1, y)

while True:
    x, y = pos
    nx, ny = (g := getNXNY(x, y))[0], g[1]

    if ny < 0 or nx < 0 or nx > len(gmap[0])-1 or ny > len(gmap)-1:
        gmap[y][x] = "X"
        break

    if gmap[ny][nx] == "#":
        angle = (angle +1) % 4
        continue
    pos = nx, ny
    if (x,y,angle) not in saved:
        saved.append((x,y,angle))
    gmap[y][x] = "X"

count = 0
for row in gmap:
    for c in row:
        if c == "X": count+=1

print(count)

placed = set()
def solve2(visited: List[Tuple[int,int,int]], startx:int, starty: int, startangle: int):
    global originalPos, savedmap, placed
    newmap = deepcopy(savedmap)
    pos = (startx, starty)
    x, y = pos
    nx, ny = (g := getNXNY(x, y, startangle))[0], g[1]

    ### place new stone and save coords for that stone    
    if  nx == originalPos[0] and ny == originalPos[1] and (nx, ny) not in placed: return
    newmap[ny][nx] = "#"
    px, py = nx, ny
    ### traverse
    angle = 0
    while True:
        x, y = pos
        if ((x,y,angle)) in visited:
            placed.add((px, py))
            return
        visited.append((x,y, angle))
        nx, ny = (g := getNXNY(x, y))[0], g[1]

        if ny < 0 or nx < 0 or nx > len(newmap[0])-1 or ny > len(newmap)-1:
            return

        if newmap[ny][nx] == "#":
            angle = (angle +1) % 4
            continue
        pos = nx, ny

glvisited: List[Tuple[int,int,int]] = []
for i, (x, y, angle) in enumerate(saved):
    solve2([], x,y,angle)    
print(len(placed))