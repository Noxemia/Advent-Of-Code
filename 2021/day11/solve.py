data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

octpy = []

for line in data:
    tmp = []
    for c in line:
        tmp.append(int(c))
    octpy.append(tmp)

def oprint():
    for row in octpy:
        print(row)


def incall(input=octpy):
    for y in range(len(input)):
        for x in range(len(input[y])):
            input[y][x] += 1


def getsurrounding(x,y):
    neighbours = []
    #top row
    if y != 0:
        neighbours.append([y-1, x])
        if x != 0:
            neighbours.append([y-1, x-1])
        if x != len(octpy[0])-1:
             neighbours.append([y-1, x+1])
    # same row
    if x != 0:
        neighbours.append([y, x-1])
    if x != len(octpy[0])-1:
        neighbours.append([y, x+1])
    #row under
    if y != len(octpy)-1:
        neighbours.append([y+1,x])
        if x != 0:
            neighbours.append([y+1, x-1])
        if x != len(octpy[0])-1:
            
            neighbours.append([y+1, x+1])
    return neighbours
    

flashcnt = 0

def flash(x,y):
    global flashcnt 
    flashcnt += 1
    octpy[y][x] = 0
    neighbours = getsurrounding(x,y)
    for neighbour in neighbours:
        if octpy[neighbour[0]][neighbour[1]] != 0:
            octpy[neighbour[0]][neighbour[1]] +=1




def triggerflash(input=octpy):
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] > 9:
                flash(x,y)

def step():
    incall()
    for _ in range(20):
        triggerflash()

stepcnt = 0

def allzeros():
    global stepcnt
    stepcnt += 1
    res = True
    for row in octpy:
        for cell in row:
            if cell != 0:
                res = False
    return res


for _ in range(1000 ):
    step()
    if allzeros():
        print(stepcnt)
        break


#print(flashcnt)