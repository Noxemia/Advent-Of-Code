from typing import Tuple, List, Set
from copy import deepcopy, copy


gmap = []
pos = ()
for y, line in enumerate(open('input.txt', 'r').readlines()):
    line = [x for x in line.strip("\n")]
    if "^" in line:
        pos = (line.index("^"), y)
    gmap.append(line)

savedmap = deepcopy(gmap)
saved: List[Tuple[int,int,int]] = []
originalPos = copy(pos)
angle = 0
while True:
    x, y = pos
    nx, ny = x, y
    if angle == 0: nx, ny = x, y-1
    if angle == 1: nx, ny = x+1, y
    if angle == 2: nx, ny = x, y+1
    if angle == 3: nx, ny = x-1, y
    
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

placed = set()
def solve2(visited: List[Tuple[int,int,int]], startx:int, starty: int, startangle: int):
    global originalPos, savedmap, placed
    newmap = deepcopy(savedmap)
    visited = []
    pos = (startx, starty)
    x, y = pos
    nx, ny = 0,0

    ### place new stone and save coords for that stone
    if startangle == 0:
        nx, ny = x, y-1
        if not (((nx, ny) == originalPos) and (nx, ny) not in placed): newmap[ny][nx] = "#"
    if startangle == 1:
        nx, ny = x+1, y
        if not (((nx, ny) == originalPos) and (nx, ny) not in placed): newmap[ny][nx] = "#"
    if startangle == 2: 
        nx, ny = x, y+1
        if not (((nx, ny) == originalPos) and (nx, ny) not in placed): newmap[ny][nx] = "#"
    if startangle == 3:
        nx, ny = x-1, y 
        if not (((nx, ny) == originalPos) and (nx, ny) not in placed): newmap[ny][nx] = "#"
    px, py = nx, ny

    ### traverse
    angle = 0
    while True:
        x, y = pos
        if ((x,y,angle)) in visited:
            placed.add((px, py))
            return
        visited.append((x,y, angle))
        nx, ny = x, y
        if angle == 0: nx, ny = x, y-1
        if angle == 1: nx, ny = x+1, y
        if angle == 2: nx, ny = x, y+1
        if angle == 3: nx, ny = x-1, y

        if ny < 0 or nx < 0 or nx > len(newmap[0])-1 or ny > len(newmap)-1:
            return

        if newmap[ny][nx] == "#":
            angle = (angle +1) % 4
            continue
        pos = nx, ny

glvisited: List[Tuple[int,int,int]] = []
for i, (x, y, angle) in enumerate(saved):
    #print(i, part2)
    solve2(deepcopy(glvisited), x,y,angle)    
print(len(placed))