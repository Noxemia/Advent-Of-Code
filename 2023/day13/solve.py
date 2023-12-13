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


def findVerticalMatches(map):
	res = []
	for idx in range(len(map[0])-1):
		leftline = [line[idx] for line in map]
		rightline = [line[idx+1] for line in map]
		if leftline == rightline:
			res.append(idx)
	return res

def findHorziontalMatches(map):
	res = []
	for idx in range(len(map)-1):
		topline = map[idx]
		botline = map[idx+1]
		if topline == botline:
			res.append(idx)
	return res
	
def isMirroredVertical(map, _leftIndex):
	leftindex = _leftIndex -1
	rightindex = _leftIndex+2

	while leftindex >= 0 and rightindex <= len(map[0]) -1:
		leftline = [line[leftindex] for line in map]
		rightline = [line[rightindex] for line in map]
		if leftline != rightline:
			return 0
		leftindex -= 1
		rightindex += 1
	return _leftIndex+1

def isMirroredHorizontal(map, _topIndex):
	topindex = _topIndex-1
	botindex = _topIndex + 2
	#print(topindex, botindex)

	while topindex >= 0 and botindex <= (len(map) -1):
		print(topindex, botindex)
		topline = map[topindex]
		botline = map[botindex]
		if topline != botline:
			return 0
		topindex -= 1
		botindex += 1

	return _topIndex+1
	
p1sum = 0
for map in data:
	vm = findVerticalMatches(map)
	hm = findHorziontalMatches(map)
	print(vm, hm)
	for m in vm:
		p1sum += isMirroredVertical(map, m)
	
	for m in hm:
		p1sum += isMirroredHorizontal(map, m) * 100
	

print(p1sum)