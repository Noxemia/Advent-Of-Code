from dataclasses import dataclass
data = []

for line in open('input.txt', 'r').readlines():
	spl = line.split(" ")
	data.append([spl[0], int(spl[1])])

def touching(x1,y1, x2,y2) -> bool:
	# tail is one above
	if y1 +1 == y2:
		if x1 == x2: return True
		if x1-1 == x2: return True
		if x1+1 == x2: return True
	# tails one row below
	if y1 -1 == y2:
		if x1 == x2: return True
		if x1-1 == x2: return True
		if x1+1 == x2: return True
	# on same row
	if y1 == y2:
		if x1 == x2: return True
		if x1-1 == x2: return True
		if x1+1 == x2: return True
	return False

def updatetail():
	taillen = len(tailx)
	for i in range(1,taillen):
		if not touching(tailx[i-1],taily[i-1],tailx[i],taily[i]):
			# same col move
			if tailx[i-1] == tailx[i]:
				if taily[i-1] > taily[i]: taily[i] += 1
				if taily[i-1] < taily[i]: taily[i] -= 1
			# same row move
			elif taily[i-1] == taily[i]:
				if tailx[i-1] > tailx[i]: tailx[i] += 1
				if tailx[i-1] < tailx[i]: tailx[i] -= 1
			#diag move
			else:
				if taily[i-1] > taily[i]: taily[i] += 1
				if taily[i-1] < taily[i]: taily[i] -= 1
				if tailx[i-1] > tailx[i]: tailx[i] += 1
				if tailx[i-1] < tailx[i]: tailx[i] -= 1
		else:
			break
	coords = [tailx[taillen-1], taily[taillen-1]]
	if not coords in scorecoords:
		scorecoords.append(coords)

def calc(taillengt: int):
	global tailx, taily, scorecoords
	tailx = [0]*taillengt
	taily = [0]*taillengt
	scorecoords = [[0,0]]
	for ins in data:
		if ins[0] == "R":
			for _ in range(ins[1]):
				tailx[0] = tailx[0] + 1
				updatetail()
		if ins[0] == "L":
			for _ in range(ins[1]):
				tailx[0] = tailx[0] - 1
				updatetail()
		if ins[0] == "U":
			for _ in range(ins[1]):
				taily[0] = taily[0] + 1
				updatetail()
		if ins[0] == "D":
			for _ in range(ins[1]):
				taily[0] = taily[0] - 1
				updatetail()
	print(len(scorecoords))
calc(2)
calc(10)
