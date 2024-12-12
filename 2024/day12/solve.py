garden = []
from typing import List, Tuple
for line in open('input.txt', 'r').readlines():
    garden.append([x for x in line.strip("\n")])


walked = set()
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


def findPerimeter(plots):
    dirs = [(0, -1), (1, 0), (0, 1), (-1,0)]
    count = 0
    perims = []
    for x, y in plots:
        for (dx, dy) in dirs:
            nx, ny = x+dx, y+dy
            if (nx, ny) not in plots:
                perims.append((nx, ny))
                count += 1
    return (count, perims)


def walkPerimiter(perims):
    pwalked = set()
    dirChanges = 0
    dirs = [(0, -1), (1, 0), (0, 1), (-1,0)]
    sides = 0
    #dirs = [(1, -1), (1, 1), (-1, 1), (-1,-1)]
    for _x, _y in perims:
        if (_x, _y) in pwalked: continue
        toWalk = [(_x,_y)]
        while toWalk:
            x, y = toWalk.pop()
            for (dx, dy) in dirs:
                nx, ny = x+dx, y+dy
                if (nx, ny) in perims and (nx, ny) not in pwalked: 
                    toWalk.append((nx, ny))
                    pwalked.add((nx, ny))
        sides += 1
    return sides


def walkPerim2(perims: List[Tuple[int,int]]):
    cdir = 1
    dirs = [(0, -1), (1, 0), (0, 1), (-1,0)]
    ndirs = [(-1, -1), (1, -1), (1, 1), (-1,+1)]
    cx, cy = perims.pop(0)
    sides = 0
    while perims:
        print("Current:", cx, cy)
        ### Check if we can walk in the current direction
        dx, dy = dirs[cdir]
        nx, ny = cx + dx, cy + dy
        if (nx, ny) in perims:
            cx, cy = nx, ny
            perims.remove((cx, cy))
            continue

        ### If we cant walk further look "right down" to continue path, if not in path break
        ## sanity check
        cdir = (cdir +1) % 4
        print("Change dir to", cdir)
        dx, dy = ndirs[cdir]
        nx, ny = cx + dx, cy + dy
        print(nx, ny)
        if (nx, ny) not in perims:
            print("MEGACRINGE")
            return sides 
        cx, cy = nx, ny
        perims.remove((cx, cy))
        sides +=1
    return sides

 
    

part1 = 0
part2 = 0
for y, row in enumerate(garden):
    for x, c in enumerate(row):
        if (x, y) not in walked:
            plots = walkPlot(x,y, c)
            #print("Char size", c, len(plots))
            #print(plots)
            perim = findPerimeter(plots)
            #print("Perim size", perim)
            part1 += len(plots)*perim[0]
            sides = walkPerim2(perim[1])
            print("Sides:", sides, c)
            print("Perim blocks", perim[1], c)
            part2 += len(plots) * sides
print(part1, part2)

### to low 768852.0
###        579813