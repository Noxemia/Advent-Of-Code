hmap: list[list[int]] = []

start: list[int, int] = []
end: list[int, int] = []

def toheight(x: str) -> int:
	if x == "S": return 0
	if x == "E": return 25
	return ord(x)-97

print(toheight('z'))

for y, line in enumerate(open('input.txt', 'r').readlines()):
	if 'S' in line: start = [line.index('S'), y]
	if 'E' in line: end = [line.index('E'), y]
	nums = [toheight(c) for c in line.strip("\n")]
	hmap.append(nums)

visited = [[False for i in range(len(hmap[0]))] for j in range(len(hmap))]

# tuples (length, x, y)
queue = [(0, start[0], start[1])]

# return all unvisited neighbours
def calcneighbours(x, y):
	neighbours = []
	# north
	if y != 0:
		coord = [x, y-1]
		if not visited[y-1][x]:
			neighbours.append(coord)
	# east
	if x != len(hmap[0]) -1:
		coord = [x+1, y]
		if not visited[y][x+1]:
			neighbours.append(coord)
	# south
	if y != len(hmap) -1:
		coord = [x, y+1]
		if not visited[y+1][x]:
			neighbours.append(coord)
	# west
	if x != 0:
		coord = [x-1, y]
		if not visited[y][x-1]:
			neighbours.append(coord)
	return neighbours

def sortqueue(item: tuple[int, int, int]):
	return item[0]

#for _ in range(5):
while True:
	cdist, cx, cy = queue.pop(0)
	if cx == end[0] and cy == end[1]:
		print(cdist)
		break
	for neighbour in calcneighbours(cx, cy):
		if hmap[cy][cx] == hmap[neighbour[1]][neighbour[0]] or hmap[cy][cx] + 1 == hmap[neighbour[1]][neighbour[0]]:
			queue.append((cdist+1,neighbour[0], neighbour[1]))
	visited[cy][cx] = True
	queue = sorted(queue, key=sortqueue)

