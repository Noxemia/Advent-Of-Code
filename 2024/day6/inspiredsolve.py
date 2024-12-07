from typing import Tuple, List
from copy import deepcopy, copy

gmap, pos = [], ()
for y, line in enumerate(open('input.txt', 'r').readlines()):
    line = [x for x in line.strip("\n")]
    if "^" in line:
        pos = (line.index("^"), y)
    gmap.append(line)

def getNXNY(x, y, angle):
    if angle == 0: return (x, y-1)
    if angle == 1: return (x+1, y)
    if angle == 2: return (x, y+1)
    if angle == 3: return (x-1, y)

part1, part2 = 0,0
for cy in range(len(gmap)):
    for cx  in range(len(gmap[1])):
        x, y = pos
        angle = 0
        visited = set()
        visited2 = set()

        while True:
            if (x,y, angle) in visited:
                part2+=1
                break
            visited.add((x,y,angle))
            visited2.add((x,y))
            nx, ny = (g := getNXNY(x, y, angle))[0], g[1]

            if ny < 0 or nx < 0 or nx > len(gmap[0])-1 or ny > len(gmap)-1:
                if gmap[cy][cx] == "#":
                    part1=len(visited)
                break
            
            if gmap[ny][nx] == "#" or ny == cy and nx == cx:
                angle = (angle +1) % 4
            else:
                x, y = nx, ny

print(part1, part2)