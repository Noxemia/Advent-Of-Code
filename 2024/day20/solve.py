from collections import defaultdict
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


cheats2 = defaultdict(int)
cheats1 = defaultdict(int)

for x, y in nodes:
    coordsToCheck = set()
    
    for yi in range(-20, 21):
        _y = y + yi      
        for _x in range(x-20+abs(yi), x+21-abs(yi)):
            if (_x, _y) in nodes:
                dist = abs(x-_x) + abs(y-_y)
                coordsToCheck.add((_x,_y, dist))
                
    owalked = nodes[(x,y)]
    for nx, ny, dist in coordsToCheck:            
        if (nx, ny) not in nodes: continue
        nwalked = nodes[(nx, ny)]
        if owalked <= nwalked: continue
        cheatdist = abs((nwalked - owalked) + dist)
        if cheatdist < 100: continue
        cheats2[cheatdist] = cheats2[cheatdist]+1
        if dist == 2:
            cheats1[cheatdist] = cheats1[cheatdist]+1

p1 = 0      
for dist in cheats1.keys():
    if dist >= 100:
        p1 += cheats1[dist]
                
p2 = 0      
for dist in cheats2.keys():
    if dist >= 100:
        p2 += cheats2[dist]
        

print(p1, p2)

