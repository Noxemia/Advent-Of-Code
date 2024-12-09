data = []

for line in open('input.txt', 'r').readlines():
    line = [x for x in line]
    if line[-1] == "\n": line = line[0:-1]
    data.append(line)

garden = data

def printGarden():
    for row in garden:
        print(row)
    print("-----------------")

startx = 0
starty = 0
# findstart
for y, row in enumerate(garden):
    for x, place in enumerate(row):
        if place == "S":
            startx = x
            starty = y
print(startx, starty)

garden[starty][startx] = "X"
def takeStep():
    global garden
    for y, row in enumerate(garden):
            for x, place in enumerate(row):
                if place == "X":
                    try:
                        #up
                        if garden[y-1][x] != "#":
                            garden[y-1][x] = "N"
                    except: pass
                    try:
                        #right
                        if garden[y][x+1] != "#":
                            garden[y][x+1] = "N"
                    except: pass
                    try:
                        #down
                        if garden[y+1][x] != "#":
                            garden[y+1][x] = "N"
                    except: pass
                    try:
                        #left
                        if garden[y][x-1] != "#":
                            garden[y][x-1] = "N"
                    except: pass

def clean():
    global garden
    for y, row in enumerate(garden):
            for x, place in enumerate(row):
                if place == "X":
                    garden[y][x] = "."
    for y, row in enumerate(garden):
            for x, place in enumerate(row):
                if place == "N":
                    garden[y][x] = "X"

steps = 64
for _ in range(steps):
    takeStep()
    clean()

def countX():
    global garden
    count = 0
    for y, row in enumerate(garden):
            for x, place in enumerate(row):
                if place == "X":
                     count += 1
    print(count)

countX()
