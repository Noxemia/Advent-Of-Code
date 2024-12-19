import heapq
from copy import copy
data = []

for line in open('input.txt', 'r').readlines():
    line = line.split(",")
    data.append((int(line[0]), int(line[1])))
        
widht = 70
height = 70
fallen = 1024
memmap = []

for y in range(height+1):
    memmap.append(["."]*(widht+1))

for i in range(fallen):
    x, y = data[i]
    memmap[y][x] = "#"

def tryWalk():
    global memmap
    goal = (70,70)
    toWalk = [(0, 0, 0, [])]

    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    cost_so_far = dict()
    visited = set()
    while toWalk:
        c, x, y, lv = heapq.heappop(toWalk)
        if (x,y) == goal:
            return c
        lv.append((x,y))
        visited.add((x,y))
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if (nx, ny) in visited: continue
            if nx < 0 or ny < 0 or nx > widht or ny > height or memmap[ny][nx] == '#': continue
            if (nx, ny) not in cost_so_far or c+1 < cost_so_far[(nx,ny)]:
                cost_so_far[(nx, ny)] = c+1
                heapq.heappush(toWalk, (c+1, nx, ny, copy(lv)))
print(tryWalk())
    
def updateStones(to, c, inc):
    global fallen
    for i in range(fallen, to+inc, inc):
        x, y = data[i]
        memmap[y][x] = c
    fallen = to
        
for inc in [1000, 500, 100, 50, 10]:
    while tryWalk() != None:
        updateStones(fallen+inc, "#", 1)
    updateStones(fallen-inc, ".", -1)

for i in range(fallen, fallen+100):
        x, y = data[i]
        memmap[y][x] = "#"
        if tryWalk() == None:
            print(x,y)
            break
        
## 0.13
## 0.05
