from collections import defaultdict
data = []

for line in open('input.txt', 'r').readlines():
	line = line.strip()
	direction = line.split(" ")[0]
	amount = line.split(" ")[1]
	#data.append((direction, int(amount)))
	# hexconversion
	hexstr = line.split(" ")[2][2:-1]
	hamount = int(hexstr[:-1], 16)
	_dirs = ["R", "D", "L", "U"]
	hdirection = _dirs[int(hexstr[-1])]
	data.append((hdirection, hamount))

curx = 0
cury = 0

rowSpans = defaultdict(list)

for (direction, amount) in data:
	if direction == "R":
		spanStart = curx
		spanEnd = curx+amount
		curx = spanEnd
		rowSpans[cury].append((spanStart,spanEnd))

	if direction == "L":
		spanStart = curx
		spanEnd = curx-amount
		curx = spanEnd
		rowSpans[cury].append((spanEnd, spanStart))
	if direction == "D":
		for newy in range(cury+1, amount+cury):
			rowSpans[newy].append((curx,curx))
		cury = newy+1
	if direction == "U":
		for newy in range(cury-1, cury-amount, -1):
			rowSpans[newy].append((curx,curx))
		cury = newy-1
		
def isTrueEdge(x1, x2, y):
	#toprow
	if y-1 in rowSpans:
		x1in = False
		x2in = False
		for (sx1, sx2) in rowSpans[y-1]:
			if sx1 <= x1 <=sx2: x1in = True
			if sx1 <= x2 <=sx2: x2in = True
		
		if x1in and x2in: return True

	# bottomrow
	if y+1 in rowSpans:
		
		x1in2 = False
		x2in2 = False
		for (sx1, sx2) in rowSpans[y+1]:
			if sx1 <= x1 <= sx2: x1in2 = True
			if sx1 <= x2 <= sx2: x2in2 = True
		if x1in2 and x2in2: return True 
	return False


p1sum = 0
for key in sorted(rowSpans.keys()):
	inner = False
	innerStart = 0
	for (x1, x2) in sorted(rowSpans[key], key=lambda x: x[0]):
		# for a out side
		
		if x1 != x2:
			p1sum += abs(x1 - x2) + 1
			if not inner:
				if not isTrueEdge(x1,x2, key):
					inner = True
					innerStart = x2+1
			else:
				if isTrueEdge(x1,x2, key):
					p1sum += abs(innerStart - (x1-1)) +1
					innerStart = x2+1
				else:
					inner = False
					p1sum += abs(innerStart - (x1-1)) +1
		
		# if we are on an single piece
		elif x1 == x2:
			## if we outside of the shape going into it
			if not inner:
				inner = True
				innerStart = x1
			else:
				inner = False
				p1sum += abs(innerStart - x1) +1

print("Sum: ", p1sum)