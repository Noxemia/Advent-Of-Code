from copy import deepcopy

data = []

for line in open('input.txt', 'r').readlines():
	data.append(list(line.strip("\n")))

def tryMoveNorth(x,y):
	if y == 0: return
	if data[y][x] != "O": return
	if data[y-1][x] != ".": return

	data[y-1][x] = "O"
	data[y][x] = "."
	tryMoveNorth(x, y-1)


def tryMoveWest(x,y):
	if x == 0: return
	if data[y][x] != "O": return
	if data[y][x-1] != ".": return

	data[y][x-1] = "O"
	data[y][x] = "."
	tryMoveWest(x-1, y)

def tryMoveSouth(x,y):
	if y == len(data)-1: return
	if data[y][x] != "O": return
	if data[y+1][x] != ".": return

	data[y+1][x] = "O"
	data[y][x] = "."
	tryMoveSouth(x, y+1)

def tryMoveEast(x,y):
	if x == len(data[0])-1: return
	if data[y][x] != "O": return
	if data[y][x+1] != ".": return

	data[y][x+1] = "O"
	data[y][x] = "."
	tryMoveEast(x+1, y)

def calcWeight():
	p1sum = 0
	for idy, line in enumerate(data):
		rowpoint = len(data) - idy
		for idx, c in enumerate(line):
			if c == "O": p1sum += rowpoint
	return p1sum

p1 = True
def moveNorth():
	global p1
	for idy in range(len(data)):
		for idx in range(len(data[0])):
			tryMoveNorth(idx,idy)
	if p1: 
		print("Part 1:", calcWeight())
		p1 = False

def moveWest():
	for idx in range(len(data[0])):
		for idy in range(len(data)):
			tryMoveWest(idx, idy)

def moveEast():
	for idx in range(len(data[0])-1,-1, -1):
		for idy in range(len(data)):
			tryMoveEast(idx, idy)

def moveSouth():
	for idy in range(len(data)-1, -1, -1):
		for idx in range(len(data[0])):
			tryMoveSouth(idx, idy)
	


def cycle():
	moveNorth()
	moveWest()
	moveSouth()
	moveEast()

def stringifyData():
	res = ""
	for idy in range(len(data)):
		res += "".join(data[idy])
	return res

cache = {}
count = 0
firstocc = 0

while True:
	if count > 10000: break
	count += 1 
	cycle()
	string = stringifyData()
	if string in cache:
		firstocc = cache[string]
		break
	else:
		cache[string] = count

print(count)
diff = count - firstocc
p2cycles = 1_000_000_000 - firstocc
remaining = p2cycles % diff

for _ in range(remaining):
	cycle()

print("Part 2:", calcWeight())




