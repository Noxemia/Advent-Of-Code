from typing import List, Tuple
data: List[Tuple[int,int,int,int]] = []

for line in open('input.txt', 'r').readlines():
    line = line.split(" ")
    p = line[0].strip("p=").split(",")
    px, py = int(p[0]), int(p[1])
    v = line[1].strip("v=").split(",")
    vx, vy = int(v[0]), int(v[1])
    data.append((px, py, vx, vy))
    
for robot in data:
    break
    print(*robot)
    
time: int = 100 ### Seconds
sizex = 101
sizey = 103

def moveRobot(robot: Tuple[int,int,int,int]):
    px, py, vx, vy = robot
    for _ in range(time):
        px = (px + vx) % sizex
        py = (py + vy) % sizey
    ### Quadrants
    # topleft
    if px < sizex // 2 and py < sizey // 2: return 0
    # top right
    if px > sizex // 2 and py < sizey // 2: return 1
    ## bottom left
    if px < sizex // 2 and py > sizey // 2: return 2
    ## bottomr right
    if px > sizex // 2 and py > sizey // 2: return 3

#moveRobot((2,4,2,-3))

quadrants = [0,0,0,0]
for robot in data:
    res = moveRobot(robot)
    if res != None:
        quadrants[res] += 1
    
print(quadrants)

p1 = 1
for num in quadrants:
    p1 = p1 * num
print(p1)