from dataclasses import dataclass
from copy import copy

data = []

for line in open('input.txt', 'r').readlines():
	data.append(line.strip("\n"))

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

galxCoords = []

for idy, row in enumerate(data):
	for idx, c in enumerate(row):
		if c == "#":
			galxCoords.append((idx, idy))

def calcDistance(coordsOne, coordsTwo, mult) -> int:
	#ydiff = abs(coordsOne[1] - coordsTwo[1])
	yindex = [y for y in range(min(coordsOne[1], coordsTwo[1])+1, max(coordsOne[1], coordsTwo[1])+1)]
	ytot = 0
	for y in yindex:
		if y in emptyrow: ytot += mult
		else: ytot += 1

	#xdiff = abs(coordsOne[0] - coordsTwo[0])
	xindex = [x for x in range(min(coordsOne[0], coordsTwo[0])+1, max(coordsOne[0], coordsTwo[0])+1)]
	xtot = 0
	for x in xindex:
		if x in emptycolumn: xtot += mult
		else: xtot += 1
	return xtot + ytot

p1sum = 0
p2sum = 0
for idx, coords in enumerate(galxCoords):
	otherCoords = copy(galxCoords[idx+1:])
	cCoord = galxCoords[idx]
	for coord in otherCoords:
		p1sum += calcDistance(cCoord, coord, 2)
		p2sum += calcDistance(cCoord, coord, 1_000_000)

print("p1", p1sum, "p2", p2sum)