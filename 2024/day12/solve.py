garden = []
from typing import List, Tuple
for line in open('input.txt', 'r').readlines():
    garden.append([x for x in line.strip("\n")])


walked = set()
### DFS to find plot coords
def walkPlot(_x:int, _y:int, letter: str):
    toWalk = [(_x,_y)]
    dirs = [(0, -1), (1, 0), (0, 1), (-1,0)]
    walked.add((_x, _y))
    plots = []
    while toWalk:
        x, y = toWalk.pop(0)
        plots.append((x,y))
        for (dx, dy) in dirs:
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= len(garden[0]) or ny >= len(garden): continue
            if garden[ny][nx] == letter and (nx, ny) not in walked:
                toWalk.append((nx,ny))
                walked.add((nx, ny))
    return plots

### Look around each plot and count coords outside
def findPerimeter(plots):
    dirs = [(0, -1), (1, 0), (0, 1), (-1,0)]
    count = 0
    for x, y in plots:
        for (dx, dy) in dirs:
            nx, ny = x+dx, y+dy
            if (nx, ny) not in plots:
                count += 1
    return count

### Count edges, look at above to see if the edge is counted
def findSides(plots):
    xmax = max([plot[0] for plot in plots])
    xmin = min([plot[0] for plot in plots])
    ymax = max([plot[1] for plot in plots])
    ymin = min([plot[1] for plot in plots])
    sides = 0
    inedges = set()
    outedges = set()
    
    for y in range(ymin, ymax+2):
        outside = True
        for x in range(xmin, xmax+2):
            if (x,y) in plots:
                if outside:
                    if (x, y-1) not in inedges:
                        sides += 1
                    outside = False
                    inedges.add((x,y))
            else:
                if not outside:
                    if (x, y-1) not in outedges:
                        sides +=1
                    outside = True
                    outedges.add((x,y))
        
    for x in range(xmin, xmax+2):
        outside = True
        for y in range(ymin, ymax+2):
            if (x,y) in plots:
                if outside:
                    if (x-1, y) not in inedges:
                        sides += 1
                    outside = False
                    inedges.add((x,y))
            else:
                if not outside:
                    if (x-1, y) not in outedges:
                        sides +=1
                    outedges.add((x,y))
                    outside = True
    return sides

part1 = 0
part2 = 0
for y, row in enumerate(garden):
    for x, c in enumerate(row):
        if (x, y) not in walked:
            plots = walkPlot(x,y, c)
            perim = findPerimeter(plots)
            sides = findSides(plots)

            part1 += len(plots) * perim
            part2 += len(plots) * sides

print(part1, part2)