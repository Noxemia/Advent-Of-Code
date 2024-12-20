course = []
start = 0
end = 0


for y, line in enumerate(open('input.txt', 'r').readlines()):
    line = [x for x in line.strip("\n")]
    if 'S' in line: 
        start = (line.index('S'), y)
    if 'E' in line:
        end = (line.index('E'), y)
        line[line.index('E')] = "."
    course.append(line)

nodes = dict()
toWalk = (start[0], start[1], 0)
maxlen = 0
while toWalk:
    x, y, dist = toWalk
    nodes[(x,y)] = dist
    if (x,y) == end: 
        maxlen = dist
        break
    
    for dx, dy in ((0, -1), (1, 0), (0,1), (-1,0)):
        nx, ny = x+dx, y+dy
        if (nx, ny) in nodes or course[ny][nx] != '.': continue
        toWalk = (nx, ny, dist+1)
        break

mincheat = 20
from collections import defaultdict
cheats = defaultdict(int)
for x, y in nodes:
    owalked = nodes[(x,y)]
    for dx, dy in ((0, -2), (2, 0), (0,2), (-2,0)):
        nx, ny = x+dx, y+dy
        if (nx, ny) not in nodes: continue
        nwalked = nodes[(nx, ny)]
        if owalked <= nwalked: continue
        cheatdist = abs((nwalked - owalked) +2)
        if cheatdist == 0: continue
        cheats[cheatdist] = cheats[cheatdist]+1
        
p1 = 0      
for dist in cheats.keys():
    if dist >= 100:
        p1 += cheats[dist]


print(p1)