from typing import List, Tuple
from copy import copy
emap = []

for line in open('input.txt', 'r').readlines():
    emap.append([(int(x) if x != "." else -1) for x in line.strip("\n")])

heads: List[Tuple[int,int]] = []
for y, row in enumerate(emap):
    for x, cell in enumerate(row):
        if cell == 0: heads.append((x,y))

def getAround(x,y, elevation) -> List[Tuple[int,int]]:
    global emap
    res = []
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if nx < 0 or ny < 0 or nx >= len(emap[0]) or ny >= len(emap): continue
        if emap[ny][nx] == elevation +1: res.append((nx,ny))
    return res

p1 = 0
p2 = 0
found = set()
def moveRec(visited: List[Tuple[int,int]], score: int, cx:int, cy:int, ce: int) -> int:
    global found, p1, p2
    if emap[cy][cx] == 9:
        if (cx, cy) not in found:
            found.add((cx,cy))
            p1 += 1
        p2 +=1
        return
    visited.append((cx,cy))
    ### get around
    around = getAround(cx,cy, ce)
    for x,y in around:
        if (x,y) in visited: continue
        moveRec(copy(visited), score, x,y,ce+1)

for x,y in heads:
    moveRec([], 0, x,y,0)
    found = set()

print(p1,p2)