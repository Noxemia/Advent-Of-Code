from dataclasses import dataclass
data = []

for line in open('input.txt', 'r').readlines():
	spl = line.split(" ")
	data.append([spl[0], int(spl[1])])



# init, start 0,0

@dataclass
class vars:
	coordsx: list
	coordsy: list

var = vars([0]*2,[0]*2)


scorecoords = [[0,0]]

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


def moveright(index) -> None:
	oldx:int = var.coordsx[index]
	oldy:int = var.coordsy[index]
	var.coordsx[index] = var.coordsx[index] + 1
	if not touching(var.coordsx[index],var.coordsy[index],var.coordsx[index+1],var.coordsy[index+1]):
		var.coordsx[index+1] = oldx
		var.coordsy[index+1] = oldy
		if [var.coordsx[index+1], var.coordsy[index+1]] not in scorecoords and index == 9:
			scorecoords.append([var.coordsx[index+1], var.coordsy[index+1]])

def moveleft(index):
	oldx:int = var.coordsx[index]
	oldy:int = var.coordsy[index]
	var.coordsx[index] = var.coordsx[index] - 1
	if not touching(var.coordsx[index],var.coordsy[index],var.coordsx[index+1],var.coordsy[index+1]):
		var.coordsx[index+1] = oldx
		var.coordsy[index+1] = oldy
		if [var.coordsx[index+1], var.coordsy[index+1]] not in scorecoords and index == 9:
			scorecoords.append([var.coordsx[index+1], var.coordsy[index+1]])

def moveup(index):
	oldx:int = var.coordsx[index]
	oldy:int = var.coordsy[index]
	var.coordsy[index] = var.coordsy[index] + 1
	if not touching(var.coordsx[index],var.coordsy[index],var.coordsx[index+1],var.coordsy[index+1]):
		var.coordsx[index+1] = oldx
		var.coordsy[index+1] = oldy
		if [var.coordsx[index+1], var.coordsy[index+1]] not in scorecoords and index == 9:
			scorecoords.append([var.coordsx[index+1], var.coordsy[index+1]])

def movedown(index):
	oldx:int = var.coordsx[index]
	oldy:int = var.coordsy[index]
	var.coordsx[index] = var.coordsx[index] - 1
	if not touching(var.coordsx[index],var.coordsy[index],var.coordsx[index+1],var.coordsy[index+1]):
		var.coordsx[index+1] = oldx
		var.coordsy[index+1] = oldy
		if [var.coordsx[index+1], var.coordsy[index+1]] not in scorecoords and index == 9:
			scorecoords.append([var.coordsx[index+1], var.coordsy[index+1]])







for ins in data:
	if ins[0] == "R":
		for _ in range(ins[1]):
			moveright()
	if ins[0] == "L":
		for _ in range(ins[1]):
			moveleft()
	if ins[0] == "U":
		for _ in range(ins[1]):
			moveup()
	if ins[0] == "D":
		for _ in range(ins[1]):
			movedown()
	#print(var.headx, var.heady, var.tailx, var.taily)

print(len(scorecoords))
