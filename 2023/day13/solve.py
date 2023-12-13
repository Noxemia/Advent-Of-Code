data = []

tmp = []
for line in open('input.txt', 'r').readlines():
	line = line.strip("\n")

	if line == "":
		data.append(tmp)
		tmp = []
		continue

	tmp.append([x for x in line])

for map in data:
	break
	for line in map:
		print(line)
	print("--------------")


def findVertical(map):
	leftindexs = []
	for i in range(0, len(map[0])-1):
		columnLeft = [line[i] for line in map]
		columnRight = [line[i+1] for line in map]
		
		if columnLeft == columnRight:
			leftindexs.append(i)
	if len(leftindexs) == 0: return 0
	leftIndex = int((sum(leftindexs) / len(leftindexs)) -1)
	rightIndex = leftIndex +3 
	while leftIndex >= 0 and rightIndex <=len(map[0])-1:
		leftline = [line[leftIndex] for line in map]
		rightline = [line[rightIndex] for line in map]
		#print("LL", leftline)
		#print("RL", rightline)
		if  leftline != rightline:
			#print("False vert")
			return 0
		leftIndex -= 1
		rightIndex += 1
	#print("True vert")
	return i+1


def findHorizontal(map):
	topindexs = []
	for i in range(len(map)-1):
		rowTop = map[i]
		rowBot = map[i+1]
		
		if rowTop == rowBot:
			topindexs.append(i)
			print(i)
	if len(topindexs) == 0: return 0
	topIndex = int((sum(topindexs) / len(topindexs))-1)
	botIndex = topIndex	+ 3	
	
	while topIndex >= 0 and botIndex <= len(map)-1:
		topline = map[topIndex]
		botline = map[botIndex]
		#print("TL", topline)
		#print("BL", botline)
		if topline != botline:
			#print("False hori")
			return 0
		topIndex -= 1
		botIndex += 1
	return (i+1)*100
		
p1sum = 0
for map in data:
	vs = findVertical(map)
	hs = findHorizontal(map)
	if vs == 0 and hs == 0:
		for line in map:
			print(line)
		print("BADD")
	p1sum += vs+hs
	

print(p1sum)