matrix = []

for line in open('input.txt', 'r').readlines():
	matrix.append(
		[int(x) for x in [*line.strip("\n")]]
	)

def visiblerow(x: int, y:int) -> bool:
	row = matrix[y]
	height = matrix[y][x]
	if max(row[:x]) < height: return True
	if max(row[x+1:]) < height: return True
	return False

def visiblecol(x: int, y:int) -> True:
	column = [row[x] for row in matrix]
	height = matrix[y][x]
	if max(column[y+1:]) < height: return True
	if max(column[:y]) < height: return True
	return False

p1cnt = len(matrix) * 4 - 4

for y in range(1,len(matrix)-1):
	for x in range(1, len(matrix[0])-1):
		if visiblecol(x, y) or visiblerow(x, y):
			p1cnt += 1

print(f"Part 1: {p1cnt}")

def rowscenic(x: int, y:int) -> int:
	row = matrix[y]
	height = matrix[y][x]
	lscore = 0
	for tree in list(reversed(row[:x])):
		lscore += 1
		if tree >= height: break
	rscore = 0
	for tree in row[x+1:]:
		rscore += 1
		if tree >= height: break
	return rscore * lscore

def colscenic(x: int, y:int) -> int:
	column = [row[x] for row in matrix]
	height = matrix[y][x]
	tscore = 0
	for tree in list(reversed(column[:y])):
		tscore += 1
		if tree >= height:
			break
	bscore = 0
	for tree in column[y+1:]:
		bscore += 1
		if tree >= height:
			break
	return bscore * tscore

p2score = 0
for y in range(len(matrix)):
	for x in range(len(matrix[0])):
		val = colscenic(x, y) * rowscenic(x, y)
		if val > p2score:
			p2score = val
print(f"Part 2: {p2score}")