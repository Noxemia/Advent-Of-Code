from copy import deepcopy

data = []

tmp = []
for line in open('input.txt', 'r').readlines():
	line = line.strip("\n")

	if line == "":
		data.append(tmp)
		tmp = []
		continue

	tmp.append([x for x in line])

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

	while topindex >= 0 and botindex <= (len(map) -1):
		topline = map[topindex]
		botline = map[botindex]
		if topline != botline:
			return 0
		topindex -= 1
		botindex += 1

	return _topIndex+1


correctIndexv = [-1]*100
correctIndexh = [-1]*100
p1sum = 0
for idx, map in enumerate(data):
	vm = findVerticalMatches(map)
	hm = findHorziontalMatches(map)
	for m in vm:
		res = isMirroredVertical(map, m)
		if res != 0:
			correctIndexv[idx] = m
			p1sum += res
	
	for m in hm:
		res = isMirroredHorizontal(map, m) * 100
		if res != 0:
			correctIndexh[idx] = m
			p1sum += res

############## p2 #############

def findVerticalMatches2(map, mapid):
	res = []
	for idx in range(len(map[0])-1):
		leftline = [line[idx] for line in map]
		rightline = [line[idx+1] for line in map]
		if leftline == rightline and idx != correctIndexv[mapid]:
			res.append(idx)
	return res

def findHorziontalMatches2(map, mapid):
	res = []
	for idx in range(len(map)-1):
		topline = map[idx]
		botline = map[idx+1]
		if topline == botline and idx != correctIndexh[mapid]:
			res.append(idx)
	return res

def swap(c):
	if c == "#": return "."
	if c == ".": return "#"
	print("Swap Error")


#### Loop through map and try different changes
def checkMap(map, mapid):
	for idy, line in enumerate(map):
		for idx, c in enumerate(line):
			mapcopy = deepcopy(map)
			mapcopy[idy][idx] = swap(c)

			vm = findVerticalMatches2(mapcopy, mapid)
			hm = findHorziontalMatches2(mapcopy, mapid)
			res = 0

			for m in vm:
				res += isMirroredVertical(mapcopy, m)
			for m in hm:
				res += isMirroredHorizontal(mapcopy, m) * 100
			if res != 0:
				return res
	return 0 

p2sum = 0
for mapid, map in enumerate(data):
	p2sum += checkMap(map, mapid)
	
print("Part1:", p1sum, "Part2:", p2sum)
