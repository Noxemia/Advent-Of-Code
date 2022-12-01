from typing import final


data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

# create cords
cords = []
for line in data:
    tmp = [0, 0, 0, 0]
    first = str.split(line, ",")
    tmp[0] = int(first[0])
    tmp[3] = int(first[2])
    second = str.split(first[1], "-")
    tmp[1] = int(second[0])
    tmp[2] = int(second[1][1:])

    cords.append(tmp)

finalcords = []
print(finalcords)


def xequal(cord):
    xs = [cord[0], cord[2]]
    ys = [cord[1], cord[3]]
    for i in range(abs(ys[0] - ys[1])+1):
        finalcords.append([xs[0], min(ys[0], ys[1])+i])


def yequals(cord):
    xs = [cord[0], cord[2]]
    ys = [cord[1], cord[3]]
    for i in range(abs(xs[0] - xs[1])+1):
        finalcords.append([min(xs[0], xs[1])+i, ys[0]])


def diagonal(cord, out=finalcords):
    topy = max(cord[1], cord[3])
    boty = min(cord[1], cord[3])
    startx = None
    dirx = 0
    if cord[1] > cord[3]:
        dirx = cord[0] - cord[2]
        startx = cord[2]
    else:
        dirx = cord[2] - cord[0]
        startx = cord[0]
    if dirx < 0:
        dirx = -1
    else:
        dirx = 1
    y = 0
    
    for i in range(boty, topy+1):
        out.append([startx+(y*dirx), i])
        y += 1


for cord in cords:
    amt = 0
    xs = [cord[0], cord[2]]
    ys = [cord[1], cord[3]]
    if xs[0] == xs[1]:
        xequal(cord)
    elif ys[0] == ys[1]:
        yequals(cord)
    else:
        diagonal(cord)

map = []
size = 1000  # 10 for example 1000 for real

for i in range(size):
    tmp = []
    for j in range(size):
        tmp.append(0)
    map.append(tmp)

for cord in finalcords:
    map[cord[0]][cord[1]] += 1


sum = 0
for line in map:
    for x in line:
        if x > 1:
            sum += 1

print(sum)