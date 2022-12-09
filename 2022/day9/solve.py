from dataclasses import dataclass
data = []

for line in open('input.txt', 'r').readlines():
	spl = line.split(" ")
	data.append([spl[0], int(spl[1])])

@dataclass
class vars:
	tailx: list
	taily: list

def touching(x1,y1, x2,y2) -> bool:
	#tail is one above
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


def moveright():
	var.tailx[0] = var.tailx[0] + 1

def moveleft():
	var.tailx[0] = var.tailx[0] - 1

def moveup():
	var.taily[0] = var.taily[0] + 1

def movedown():
	var.taily[0] = var.taily[0] - 1

def updatetail():
	taillen = len(var.tailx)
	for i in range(1,taillen):
		if not touching(var.tailx[i-1],var.taily[i-1],var.tailx[i],var.taily[i]):
			# same col move
			if var.tailx[i-1] == var.tailx[i]:
				if var.taily[i-1] > var.taily[i]: var.taily[i] += 1
				if var.taily[i-1] < var.taily[i]: var.taily[i] -= 1
			# same row move
			elif var.taily[i-1] == var.taily[i]:
				if var.tailx[i-1] > var.tailx[i]: var.tailx[i] += 1
				if var.tailx[i-1] < var.tailx[i]: var.tailx[i] -= 1
			#diag move
			else:
				if var.taily[i-1] > var.taily[i]: var.taily[i] += 1
				if var.taily[i-1] < var.taily[i]: var.taily[i] -= 1
				if var.tailx[i-1] > var.tailx[i]: var.tailx[i] += 1
				if var.tailx[i-1] < var.tailx[i]: var.tailx[i] -= 1
		else:
			break
	coords = [var.tailx[taillen-1], var.taily[taillen-1]]
	if not coords in scorecoords:
		scorecoords.append(coords)



def calc(taillengt: int):
	global var 
	global scorecoords
	var = vars([0]*taillengt, [0]*taillengt)
	scorecoords = [[0,0]]
	for ins in data:
		if ins[0] == "R":
			for _ in range(ins[1]):
				moveright()
				updatetail()
		if ins[0] == "L":
			for _ in range(ins[1]):
				moveleft()
				updatetail()
		if ins[0] == "U":
			for _ in range(ins[1]):
				moveup()
				updatetail()
		if ins[0] == "D":
			for _ in range(ins[1]):
				movedown()
				updatetail()
	print(len(scorecoords))
calc(2)
calc(10)
