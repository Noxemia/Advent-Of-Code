from typing import List, Tuple
from dataclasses import dataclass
from enum import Enum
import sys
sys.setrecursionlimit(4000)

class Direction(Enum):
	RIGHT = ">"
	LEFT = "<"
	UP = "^"
	DOWN = "v"
	NONE = "."

@dataclass
class Tile:
	char: str
	energized: bool
	visited: List[Direction]


tileMap: List[List[Tile]] = []

for line in open('input.txt', 'r').readlines():
	row: List[Tile] = []
	line = line.strip("\n")
	line = list(line)
	for c in line:
		row.append(Tile(c, False, []))
	tileMap.append(row)


def takeStep(x: int, y:int, dir: Direction):
	# Check out of bounds
	if x < 0 or x > len(tileMap[0])-1: return
	if y < 0 or y > len(tileMap)-1: return
	#print(x,y, dir, data[y][x].char, len(data[0])-1)
	# energize the tile
	tile = tileMap[y][x]
	if dir in tile.visited: return
	tile.energized = True
	tile.visited.append(dir)

	# continue path
	if tile.char == ".":
		if dir == Direction.RIGHT: 
			takeStep(x+1, y, dir)
			return
		if dir == Direction.LEFT: 
			takeStep(x-1, y, dir)
			return
		if dir == Direction.UP: 
			takeStep(x, y-1, dir)
			return
		if dir == Direction.DOWN: 
			takeStep(x, y+1, dir)
			return

	## if mirror pipe
	if tile.char == "|":
		# if passing throug
		if dir == Direction.UP: 
			takeStep(x, y-1, dir)
			return
		if dir == Direction.DOWN: 
			takeStep(x, y+1, dir)
			return

		# if split
		if dir == Direction.RIGHT or dir == Direction.LEFT: 
			takeStep(x, y-1, Direction.UP)
			takeStep(x, y+1, Direction.DOWN)
			return
		
	## if mirror dash
	if tile.char == "-":
		# if passing throug
		if dir == Direction.RIGHT: 
			takeStep(x+1, y, dir)
			return
		if dir == Direction.LEFT: 
			takeStep(x-1, y, dir)
			return

		# if split
		if dir == Direction.UP or dir == Direction.DOWN: 
			takeStep(x+1, y, Direction.RIGHT)
			takeStep(x-1, y, Direction.LEFT)
			return
	
	## if "/"
	if tile.char == "/":
		if dir == Direction.RIGHT: 
			takeStep(x, y-1, Direction.UP)
			return
		if dir == Direction.LEFT: 
			takeStep(x, y+1, Direction.DOWN)
			return
		if dir == Direction.UP: 
			takeStep(x+1, y, Direction.RIGHT)
			return
		if dir == Direction.DOWN: 
			takeStep(x-1, y, Direction.LEFT)
			return

	## if "\"
	if tile.char == "\\":
		if dir == Direction.RIGHT: 
			takeStep(x, y+1, Direction.DOWN)
			return
		if dir == Direction.LEFT: 
			takeStep(x, y-1, Direction.UP)
			return
		if dir == Direction.UP: 
			takeStep(x-1, y, Direction.LEFT)
			return
		if dir == Direction.DOWN: 
			takeStep(x+1, y, Direction.RIGHT)
			return


takeStep(0,0, Direction.RIGHT)

def calcEnergized() -> int:
	res = 0
	for tiles in tileMap:
		for tile in tiles:
			if tile.energized: res += 1
	return res

p1ans = calcEnergized()

#### Part 2

def resetTiles():
	global tileMap
	for tiles in tileMap:
		for tile in tiles:
			tile.energized = False
			tile.visited = []

startingTiles: List[Tuple[int, int, Direction]] = []

#toprow
for idx in range(len(tileMap[0])):
	startingTiles.append((idx, 0, Direction.DOWN))
#bottomrow
for idx in range(len(tileMap[0])):
	startingTiles.append((idx, len(tileMap)-1, Direction.UP))
#leftrow
for idy in range(len(tileMap)):
	startingTiles.append((0, idy, Direction.RIGHT))
# rightrow
for idy in range(len(tileMap)):
	startingTiles.append((len(tileMap[0])-1, idy, Direction.LEFT))

p2ans = 0
for (idx, idy, dir) in startingTiles:
	resetTiles()
	takeStep(idx, idy, dir)
	res = calcEnergized()
	p2ans = max(res, p2ans)

print("Part 1:", p1ans, "Part 2:", p2ans)