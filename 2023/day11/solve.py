from dataclasses import dataclass
from copy import copy

data = []

for line in open('input.txt', 'r').readlines():
	data.append(line.strip("\n"))

for line in data:
	print(line)

# find empty column
emptycolumn = []
emptyrow = []

for idx in range(len(data[0])):
	colum = [_row[idx] for _row in data]
	if not "#" in colum:
		emptycolumn.append(idx)
	row = data[idx]
	if not "#" in row:
		emptyrow.append(idx)

print(emptycolumn)
print(emptyrow)

newmap = []

## add new columns
newRowSize = len(data[0]) + len(emptycolumn)

for idy, row in enumerate(data):
	newRow = []
	for idx, c in enumerate(row):
		newRow.append(c)
		if idx in emptycolumn:
			newRow.append(".")
	newmap.append(newRow)
	if idy in emptyrow:
		newmap.append(["."]*newRowSize)
print("---------------")
for line in newmap:
	print(line)

###
galxCoords = []

for idy, row in enumerate(newmap):
	for idx, c in enumerate(row):
		if c == "#":
			galxCoords.append((idx, idy))

def calcDistance(coordsOne, coordsTwo) -> int:
	ydiff = abs(coordsOne[1] - coordsTwo[1])
	xdiff = abs(coordsOne[0] - coordsTwo[0])
	return xdiff + ydiff

p1sum = 0
times = 0
for idx, coords in enumerate(galxCoords):
	otherCoords = copy(galxCoords[idx+1:])
	print(idx, len(otherCoords))
	cCoord = galxCoords[idx]
	for coord in otherCoords:
		p1sum += calcDistance(cCoord, coord)
		times += 1

print(p1sum, times)