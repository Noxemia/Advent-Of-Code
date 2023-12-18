from typing import List, Tuple
from enum import Enum
from dataclasses import dataclass
from copy import deepcopy
from heapq import heappop, heappush

class Dir(Enum):
	R = ">"
	L = "<"
	U = "^"
	D = "v"
	S = "s"

@dataclass
class Instr():
	idx: int
	idy: int
	cost: int
	TotDist: int #totaldistance
	LastDirs: List[Dir] # 3 lasts directions

data = []

for line in open('input.txt', 'r').readlines():
	data.append([int(x) for x in list(line.strip())])

visited = {}
Nexts: List[Instr] = []

def getCoords(x:int,y:int, disallowedDir: Dir, backTrack: Dir) -> List[Tuple[int, int, Dir]]:
	res = []
	if x != 0 and disallowedDir != Dir.L and backTrack != Dir.R:
		res.append((x-1, y, Dir.L))
	if x != len(data[0]) -1 and disallowedDir != Dir.R and backTrack != Dir.L:
		res.append((x+1, y, Dir.R))
	if y != 0 and disallowedDir != Dir.U and backTrack != Dir.D:
		res.append((x, y-1, Dir.U))
	if y != len(data)-1 and disallowedDir != Dir.D and backTrack != Dir.U:
		res.append((x, y+1, Dir.D))
	return res

def sortNexts():
	global Nexts
	Nexts = sorted(Nexts, key=lambda x: x.TotDist)

#Nexts.append(Instr(0, 0, 0, 0, [Dir.R]))
Nexts.append(Instr(0, 0, 0, 0, [Dir.S]))
ans: Instr = None
while len(Nexts) != 0:
	instr: Instr = Nexts.pop(0)
	newDist = instr.TotDist + instr.cost
	if newDist > 1500: continue
	## Check that we have not been in the same state before
	if len(instr.LastDirs) == 3:
		currentDirection = instr.LastDirs[2]
		walkLenght = 1
		if instr.LastDirs[1] == currentDirection:
			walkLenght += 1
			if instr.LastDirs[0] == currentDirection:
				walkLenght += 1


		if (instr.idx, instr.idy, currentDirection, walkLenght) in visited: continue
		visited[(instr.idx, instr.idy, currentDirection, walkLenght)] = 0

	## Check if we are done
	if instr.idx == (len(data[0])-1) and instr.idy == (len(data)-1):
		print(instr.TotDist+instr.cost)
		ans = instr
		break


	## Check that we have not gone in the same direction 3 times
	canNotWalkSameDir = all([node == instr.LastDirs[0] for node in instr.LastDirs]) and len(instr.LastDirs) >= 3 
	disallowedDir = None
	if canNotWalkSameDir:
		disallowedDir = instr.LastDirs[0]

	nextCoords = getCoords(instr.idx, instr.idy, disallowedDir, instr.LastDirs[-1])

	for (idx, idy, _dir) in nextCoords:
		dirCopy = deepcopy(instr.LastDirs)
		newDir = []
		for x in dirCopy: newDir.append(x)
		newDir.append(_dir)
		if len(newDir) > 3: newDir.pop(0)
		
		Nexts.append(Instr(idx, idy, data[idy][idx], newDist, newDir))
	#print(len(Nexts))
	sortNexts()

print("?")