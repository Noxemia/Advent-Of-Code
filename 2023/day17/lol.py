from typing import List, Tuple
from enum import Enum
from dataclasses import dataclass
from copy import deepcopy

class Dir(Enum):
	R = ">"
	L = "<"
	U = "^"
	D = "v"

@dataclass
class Instr():
	idx: int
	idy: int
	cost: int
	TotDist: int #totaldistance
	#md: int #manhattan distance to end
	LastDirs: List[Dir] # 3 lasts directions
	visited: List[Tuple[int, int]] # hold visited with (x,y) tuples

data = []

for line in open('input.txt', 'r').readlines():
	data.append([int(x) for x in list(line.strip())])

for line in data:
	print(line)


## need to hold x, y, tot, manhattan distance, last dirs
## held in (x,y,md,ld)


def getManhattanDist(x: int, y:int):
	return ((len(data[0])-1) - x) + ((len(data)-1) - y)

def getCoordsAroundFiltered(x:int,y:int, _visited: List[Tuple[int,int]]) -> List[Tuple[int, int, Dir]]:
	res = []
	if x != 0:
		if (x-1, y) not in _visited:
			res.append((x-1, y, Dir.L))
	if x != len(data[0]) -1:
		if (x+1, y) not in _visited:
			res.append((x+1, y, Dir.R))
	if y != 0:
		if (x, y-1) not in _visited:
			res.append((x, y-1, Dir.U))
	if y != len(data)-1:
		if (x, y+1) not in _visited:
			res.append((x, y+1, Dir.D))
	return res

nexts: List[Instr] = []
def sortNexts():
	global nexts
	nexts = sorted(nexts, key=lambda x: x.TotDist)
	#print("Sorted", nexts)

solves = []

nexts.append(Instr(0,0,2,0,[],[]))
while len(nexts) != 0:
#for _ in range(6):
	# get next instruction
	next: Instr = nexts.pop(0)
	
	## Check that we have not gone in the same direction 3 times
	if all([node == next.LastDirs[0] for node in next.LastDirs]) and len(next.LastDirs) >= 3: 
		#print("xd")
		continue

	# On last coord
	if next.idx == (len(data[0])-1) and next.idy == (len(data)-1): 
		print("DONE", next)
		solves.append(next.TotDist)
		break
	newTotalDistance = next.TotDist + next.cost
	nextCoords = getCoordsAroundFiltered(next.idx, next.idy, next.visited)

	## Add the current coordinate to visited
	nwvc = deepcopy(next.visited)
	newVisited = []
	for x in nwvc: newVisited.append(x)
	newVisited.append((next.idx, next.idy))

	for (idx, idy, _dir) in nextCoords:
		## add the new direction to the list and if we have more than 3 pop the last one
		if (idx, idy) in next.visited: continue

		dirCopy = deepcopy(next.LastDirs)
		newDir = []
		for x in dirCopy: newDir.append(x)
		newDir.append(_dir)
		if len(newDir) > 3: newDir.pop(0)
		newInstr: Instr = Instr(idx, idy, data[idy][idx], newTotalDistance, newDir, newVisited)
		nexts.append(newInstr)
	sortNexts()
