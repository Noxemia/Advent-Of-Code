from typing import List, Tuple
data: List[Tuple[int,int,int,int]] = []

for line in open('input.txt', 'r').readlines():
    line = line.split(" ")
    p = line[0].strip("p=").split(",")
    px, py = int(p[0]), int(p[1])
    v = line[1].strip("v=").split(",")
    vx, vy = int(v[0]), int(v[1])
    data.append([px, py, vx, vy])
    
time: int = 100 ### Seconds
sizex = 101
sizey = 103

def moveRobot(robot: Tuple[int,int,int,int]):
    px, py, vx, vy = robot
    
    px = (px + vx) % sizex
    py = (py + vy) % sizey
    robot[0] = px
    robot[1] = py
    ### Quadrants
    # topleft
    if px < sizex // 2 and py < sizey // 2: return 0
    # top right
    if px > sizex // 2 and py < sizey // 2: return 1
    ## bottom left
    if px < sizex // 2 and py > sizey // 2: return 2
    ## bottomr right
    if px > sizex // 2 and py > sizey // 2: return 3

part1 = 0
minsf = float("inf")
minsfIt = 0
for i in range(1,sizex*sizey):
    time = i
    quadrants = [0,0,0,0]

    for robot in data:
        qi = moveRobot(robot)
        if qi != None:
            quadrants[qi] += 1
    res = 1
    for num in quadrants:
        res = res * num
    if res < minsf: 
        minsf = res
        minsfIt = i
    if i == 100:
        part1 = res

print(part1, minsfIt, minsf)