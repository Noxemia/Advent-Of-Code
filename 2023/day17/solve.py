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
	td: int #totaldistance
	md: int #manhattan distance to end
	ld: List[Dir] # 3 lasts directions
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
	nexts = sorted(nexts, key=lambda x: x.md )

solves = [200]
nexts.append(Instr(0,0,2,0,0,[],[]))
for _ in range(100000000000):
	# get next instruction
	next: Instr = nexts.pop(0)
	#print("Next instruction:", next)
	# On last coord
	if next.idx == (len(data[0])-1) and next.idy == (len(data)-1): 
		print("DONE", next)
		solves.append(next.td)
		continue
	if next.td > min(solves): continue
	# check that not 3 in a row
	if all([node == next.ld[0] for node in next.ld]) and len(next.ld) >= 3: 
		#print("xd")
		continue

	nextCoords = getCoordsAroundFiltered(next.idx, next.idy, next.visited)
	#print("NextCoords for", (next.idx, next.idy), "is", nextCoords, "\n")

	newTotal = next.td + next.cost
	nwvc = deepcopy(next.visited)
	newVisited = []
	for x in nwvc: newVisited.append(x)
	newVisited.append((next.idx, next.idy))
	for (idx, idy, _dir) in nextCoords:
		newManhattan: int = getManhattanDist(idx, idy) + next.td
		dirCopy = deepcopy(next.ld)
		newDir = []
		for x in dirCopy: newDir.append(x)
		newDir.append(_dir)
		#print(dirCopy, newDir, next.ld, _dir)
		if len(newDir) > 3: newDir.pop(0)
		nexts.append(Instr(idx, idy, data[idy][idx], newTotal, newManhattan, newDir, newVisited ))
	sortNexts()
	#print(nexts)

		

	

	