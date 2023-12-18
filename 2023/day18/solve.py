data = []

for line in open('input.txt', 'r').readlines():
	line = line.strip()
	direction = line.split(" ")[0]
	amount = line.split(" ")[1]
	data.append((direction, int(amount)))


#print(data)
curx = 0
cury = 0
minx = 0
maxx = 0
miny = 0
maxy = 0

finalCoords = [(0,0)]
cnt = 0
for (direction, amount) in data:
	#if cnt > 7: break
	cnt += 1
	if direction == "R":
		for newx in range(1+curx, amount+1+curx):
			curx = newx
			minx = min(minx, curx)
			maxx = max(maxx, curx)
			finalCoords.append((curx, cury))
	if direction == "L":
		for newx in range(curx, curx-amount-1, -1):
			curx = newx
			minx = min(minx, curx)
			maxx = max(maxx, curx)
			finalCoords.append((curx, cury))
	if direction == "D":
		for newy in range(1+cury, amount+1+cury):
			cury = newy
			miny = min(miny, cury)
			maxy = max(maxy, cury)
			finalCoords.append((curx, cury))
	if direction == "U":
		for newy in range(cury, cury-amount-1, -1):
			cury = newy
			miny = min(miny, cury)
			maxy = max(maxy, cury)
			finalCoords.append((curx, cury))

digMap = []
for _ in range(maxy+1+abs(miny)):
	digMap.append(["."]*(maxx+1+abs(minx)))

for (x,y) in finalCoords:
	digMap[y+abs(miny)][x+abs(minx)] = "#"

for line in digMap:
	print(line)

## flood fill

visited = set()

nexts = [(61,11)]

while nexts:
	idx, idy = nexts.pop()
	digMap[idy][idx] = "x"
	
	directions = [(0,1), (1,0), (0, -1), (-1, 0)]
	visited.add((idx, idy))

	newCoords = []
	for (dx, dy) in directions:
		nx = idx + dx
		ny = idy + dy
		if digMap[ny][nx] == "#": continue
		if (nx, ny) in visited: continue
		nexts.append((nx,ny))

print("#########")
for line in digMap:
	print(line)

p1sum = 0
for line in digMap:
	for c in line:
		if c != ".": p1sum += 1

print(p1sum)