data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

cords = []

for row in data:
    tmp = []
    for c in row:
        tmp.append(int(c))
    cords.append(tmp)

lowpoints = []

produced = []
def islow(x,y,val):
    other = []
    #get top
    if y != 0:
        other.append(cords[y-1][x])
    #get right
    if x != len(cords[0])-1:
        other.append(cords[y][x+1])
    #get bot
    if y != len(cords)-1:
        other.append(cords[y+1][x])
    #get left
    if x != 0:
        other.append(cords[y][x-1])
    if val < min(other):
        produced.append(val)
        return True
    return False

lowpointcords = []

res = 0
for y in range(len(cords)):
    for x in range(len(cords[0])):
        if islow(x,y,cords[y][x]):
            res +=1
            lowpoints.append(cords[y][x])
            lowpointcords.append([x,y])

print(res + sum(lowpoints))


def getneighbours(x,y):
    neighbours = []
    #get top
    if y != 0:
        if cords[y-1][x] != 9:
            neighbours.append([x, y-1])
    #get right
    if x != len(cords[0])-1:
        if cords[y][x+1] != 9:
            neighbours.append([x+1,y])
    #get bot
    if y != len(cords)-1:
        if cords[y+1][x] != 9:
            neighbours.append([x,y+1])
    #get left
    if x != 0:
        if cords[y][x-1] != 9:
            neighbours.append([x-1,y])
    return neighbours
    
allvisited = []
visited = []
def findbasin(x,y):
    if [x,y] in visited:
        return 
    visited.append([x,y])
    allvisited.append([x,y])
    neighbours = getneighbours(x,y)
    for neighbour in neighbours:
        findbasin(neighbour[0],neighbour[1])

basins = []
for y in range(len(cords)):
    for x in range(len(cords[0])):
        if cords[y][x] == 9 or [x,y] in allvisited: continue
        visited = []
        findbasin(x,y)
        basins.append(len(visited))

first = max(basins)
basins.remove(first)
second = max(basins)
basins.remove(second)
third = max(basins)

print(first*second*third)
