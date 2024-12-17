import heapq
from copy import copy
# networkx
data = []
startx, starty = 0,0
endx, endy = 0,0
for c,line in enumerate(open('input.txt', 'r').readlines()):
    line = [x for x in line.strip("\n")]
    if 'S' in line:
        startx, starty = line.index('S'), c
    if 'E' in line:
        endx, endy = line.index('E'), c
        line[endx] = "."
    data.append(line)
        
nodes = [(0, startx, starty, 1, set())]
visited = {(startx, starty, 1)}
directions = [(0,-1), (1,0), (0,1), (-1,0)]
bestSeats = set()
part1 = float('inf')

while nodes:
    ccost, cx, cy, cdir, lv = heapq.heappop(nodes)
    visited.add((cx,cy,cdir))
    lv.add((cx,cy))
    if (cx, cy) == (endx, endy):
        if ccost < part1:
            part1 = ccost
        if ccost == part1:
            for seat in lv:
                bestSeats.add(seat)
        if ccost > part1: break
    
    for di in [(cdir-1)%4, (cdir+1)%4]:
        if (cx, cy, di) in visited: continue
        heapq.heappush(nodes, (ccost+1000, cx, cy, di, copy(lv)))
    dx, dy = directions[cdir]
    nx, ny = cx+dx, cy+dy
    if (nx, ny, cdir) not in visited and data[ny][nx] == ".":
        heapq.heappush(nodes, (ccost+1, nx, ny, cdir, copy(lv)))
        
print(part1, len(bestSeats))