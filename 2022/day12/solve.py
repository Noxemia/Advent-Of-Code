from dataclasses import dataclass
from typing import Generic
from typing import TypeVar
from typing import Callable

hmap: list[list[int]] = []

start: list[int, int] = []
end: list[int, int] = []

D = TypeVar('D', bound=tuple[int, int, int])

@dataclass
class Minqueue(Generic[D]):
	items: list[D]
	sorter: Callable[[D], int]

	def add(self, x: D):
		self.items.append(x)
		self.items.sort(key=self.sorter)
 
	def pop(self) -> int:
		return self.items.pop(0)

def toheight(x: str) -> int:
	if x == "S": return 0
	if x == "E": return 25
	return ord(x)-97

for y, line in enumerate(open('input.txt', 'r').readlines()):
	if 'S' in line: start = [line.index('S'), y]
	if 'E' in line: end = [line.index('E'), y]
	nums: list[int] = [toheight(c) for c in line.strip("\n")]
	hmap.append(nums)

def nb(x: int, y: int, p1: bool=True) -> list[int]:
	neighbours: list[int] = []
	for modx, mody in [[0,1], [1,0], [0,-1], [-1,0]]:
		nx:int = x + modx
		ny:int = y + mody

		if not (0 <= nx < len(hmap[0]) and 0 <= ny < len(hmap)):
			continue
		
		if p1:
			if hmap[ny][nx] <= hmap[y][x] + 1:
				neighbours.append([nx, ny])
		else:
			if hmap[ny][nx] >= hmap[y][x] - 1:
				neighbours.append([nx, ny])
	return neighbours

visited: list[list[bool]] = None

def dijk() -> int:
	visited = [[False] * len(hmap[0]) for _ in range(len(hmap))]
	mq: Minqueue = Minqueue([(0, start[0], start[1])], lambda x: x[0])
	while True:
		cstep, cx, cy = mq.pop()
		if visited[cy][cx]:
			continue
		visited[cy][cx] = True

		if cx == end[0] and cy == end[1]:
			return cstep

		for neigh in nb(cx, cy):
			mq.add((cstep+1, neigh[0], neigh[1]))


def dijk2() -> int:
	visited = [[False] * len(hmap[0]) for _ in range(len(hmap))]
	mq: Minqueue = Minqueue([(0, end[0], end[1])], lambda x: x[0])
	while True:
		cstep, cx, cy = mq.pop()
		if visited[cy][cx]:
			continue
		visited[cy][cx] = True

		if hmap[cy][cx] == 0:
			return cstep

		for neigh in nb(cx, cy, False):
			mq.add((cstep+1, neigh[0], neigh[1]))

print(dijk())
print(dijk2())