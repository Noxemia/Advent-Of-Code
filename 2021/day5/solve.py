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


cordscopy = []
for line in cords:
    tmp = [0,0,0,0]
    for i, val in enumerate(line):
        tmp[i] = val
    cordscopy.append(tmp)


#print("before", cords)
# sort x1 = x2 or y1 = y2
indexs = []

for i, cord in enumerate(cords):
    if not (cord[0] == cord[2] or cord[1] == cord[3]):
        indexs.append(i)

for i in reversed(indexs):
    cords.pop(i)

#print("after",cords)

# create map
map = []
size = 1000 #10 for example 1000 for real

for i in range(size):
    tmp = []
    for j in range(size):
        tmp.append(0)
    map.append(tmp)


# paint map
#cords = [cords[0]]
for cord in cords:
    #if x is the same
    if cord[0] == cord[2]:
        x = cord[0]
        minimum = min(cord[1], cord[3])
        maximum = max(cord[1], cord[3])
        for i in range(maximum-minimum+1):
            map[i+minimum][x] +=1
    else:
        y = cord[1]
        minimum = min(cord[0], cord[2])
        maximum = max(cord[0], cord[2])
        for i in range(maximum-minimum+1):
            map[y][i+minimum] +=1

#diags after normals

for line in cords:
    cordscopy.remove(line)

print(cordscopy)


# always down and right or down and left
for cord in cordscopy:
    top = min(cord[1], cord[3])
    bot = max(cord[1], cord[3])
    # if x inc, as in right
    if cord[0] > cord[2]:
        y = top
        for i in range(cord[0]-cord[2]+1):
            map[y][i+cord[2]] +=1
            y+=1
    else:
        y = top
        for i in range(cord[2]-cord[0]+1):
            map[y][cord[2]-i] +=1
            y+=1

print()
for line in map:
    print(line)

sum = 0          
for line in map:
    for x in line:
        if x > 1:
            sum += 1

print(sum)