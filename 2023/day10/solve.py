from dataclasses import dataclass
from typing import List
from collections import Counter
@dataclass
class Tile:
	x: int
	y: int
	pipe: str
	cameFrom: List
	dist: int = -1

	def __repr__(self) -> str:
		return f"Pipe: {self.pipe}, x: {self.x}, y: {self.y}"
	
	def __eq__(self, other) -> bool:
		if other == None: return False
		if self.x == other.x and self.y == other.y:
			return True
		return False



data: List[List[Tile]] = []

startTile: Tile = None


idy = 0
for line in open('input.txt', 'r').readlines():
	line = line.strip("\n")
	charList = list(line)
	res: List[Tile] = []
	for idx, char in enumerate(charList):
		res.append(Tile(idx, idy, char, []))
		if char == "S":
			startTile = Tile(idx, idy, char, [])
	data.append(res)
	idy += 1

### findNextPipe

def findNextPipe(tile: Tile) -> List[Tile]:
	pipe = tile.pipe
	xcoord = tile.x
	ycoord = tile.y
	res: List[Tile] = []

	north = data[ycoord-1][xcoord] if ycoord != 0 else None
	south = data[ycoord+1][xcoord] if ycoord != len(data) -1 else None
	east = data[ycoord][xcoord+1] if xcoord != len(data[0])-1 else None
	west = data[ycoord][xcoord-1] if xcoord != 0 else None
	#print(tile)
	#print(north, south, east, west)

	if pipe == "|":
		res.append(north)
		res.append(south)
	elif pipe == "-":
		res.append(east)
		res.append(west)
	elif pipe == "L":
		res.append(north)
		res.append(east)
	elif pipe == "J":
		res.append(north)
		res.append(west)
	elif pipe == "7":
		res.append(south)
		res.append(west)
	elif pipe == "F":
		res.append(south)
		res.append(east)
	elif pipe == "S":
		res.append(north)
		res.append(east)
		res.append(west)
		res.append(south)
	res = [x for x in res if x != None]
	res = [x for x in res if x not in tile.cameFrom]
	for _tile in res:
		_tile.dist = tile.dist +1
		_tile.cameFrom.append(tile)
	return res

### Determine Starting Pipes
#print(startTile)
#print(findNextPipe(startTile))
startTile.dist = 0

possibleStarts: List[Tile] = [tile for tile in findNextPipe(startTile) if tile.pipe != "."]
currentTiles: List[Tile] = []

sx = startTile.x
sy = startTile.y

for tile in possibleStarts:
	pipe = tile.pipe
	xcoord = tile.x
	ycoord = tile.y

	# | : | needs to be under or above
	# S
	# |
	if pipe == "|":
		if ycoord == sy+1 or ycoord == sy -1:
			currentTiles.append(tile)
	# - S - : - needs to be to east or west
	elif pipe == "-":
		if xcoord == sx+1 or xcoord == sx-1:
			currentTiles.append(tile)
	# S
	# L S : L needs to be under or to the left
	elif pipe == "L":
		if ycoord == sy+1 or xcoord == sx-1:
			currentTiles.append(tile)
	#   S
	# S J : J needs to be under or to the right
	elif pipe == "J":
		if ycoord == sy+1 or xcoord == sx+1:
			currentTiles.append(tile)
	# S 7 : 7 needs to be to the right or above
	#   S
	elif pipe == "7":
		if ycoord == sy-1 or xcoord == sx+1:
			currentTiles.append(tile)
	# F S : F needs to be to the left or above
	# S
	elif pipe == "F":
		if ycoord == sy-1 or xcoord == sx-1:
			currentTiles.append(tile)
	else:
		print("Error in starting poss")

#### Take step for single tile

def takeStep(tile: Tile) -> Tile:
	nextStep = findNextPipe(tile)
	return nextStep[0]


p2map = []
for _ in range(len(data)):
	p2map.append(["."]*len(data[0]))

p2map[startTile.y][startTile.x] = "-"

print("Starting Tiles", currentTiles, "\n")
while True:
	for idx, tile in enumerate(currentTiles):
		p2map[tile.y][tile.x] = tile.pipe
		currentTiles[idx] = takeStep(tile)

	tileOne: Tile = currentTiles[0]
	tileTwo: Tile = currentTiles[1]
	if tileOne.x == tileTwo.x and tileOne.y == tileTwo.y:
		p2map[tileOne.y][tileOne.x] = tileOne.pipe #TODO
		print("Found:", tileOne, tileOne.dist)
		break

### Part two
### Hecking raycasting algorithm that surely everyone knows
p2count = 0
for y, line in enumerate(p2map):
	for x, char in enumerate(line):
		if char == ".":
			count = 0
			left = line[:x]
			for c in left:
				if c in ["J", "L", "|"]: count += 1
			if count % 2 == 1:
				p2count += 1
  	
#for line in p2map:
#	print(line)

print(p2count)