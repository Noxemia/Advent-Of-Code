garden = []

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
    #dirs = [(0, -1), (1, 0), (0, 1), (-1,0)]
    dirs = [(1, -1), (1, 1), (-1, 1), (-1,-1)]
    for x, y in perims:
        if (x,y) in pwalked: continue
        pwalked.add(x,y)
        for (dx, dy) in dirs:
            nx, ny = x+dx, y+dy
            if (nx, ny) in perims: dirChanges +=1
    return dirChanges /2



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
            sides = walkPerimiter(perim[1])
            print("Sides:", sides)
            print("Perim blocks", perim[1])
            part2 += len(plots) * sides
print(part1, part2)

### to low 768852.0