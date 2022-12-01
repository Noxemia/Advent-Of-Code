data = []

with open("day12input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

print(data)
heading = 90
ycoord = 0
xcoord = 0

for row in data:
    print(line[1:]+"")
    if row[0] == "N":
        ycoord += int(row[1:])

    if row[0] == "E":
        xcoord += int(row[1:])

    if row[0] == "S":
        ycoord -= int(row[1:])

    if row[0] == "W":
        xcoord -= int(row[1:])

    if row[0] == "F":
        if heading == 0:
            ycoord += int(row[1:])
        elif heading == 90:
            xcoord += int(row[1:])
        elif heading == 180: 
            ycoord -= int(row[1:])
        elif heading == 270:
            xcoord -= int(row[1:])

    if row[0] == "R":
        heading = (heading + int(row[1:])) % 360
    if row[0] == "L":
        heading = (heading - int(row[1:])) % 360
    print(heading, xcoord, ycoord)

print(abs(xcoord) + abs(ycoord))