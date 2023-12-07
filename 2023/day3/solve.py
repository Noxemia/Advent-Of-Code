map = []

for line in open('input.txt', 'r').readlines():
	map.append(list(line.strip("\n")))

onlyNumbersMap = []
for _ in range(len(map)):
	onlyNumbersMap.append([0]*len(map[0]))

allNumbers = [str(x) for x in range(10)]

# build the numbers map
for y, line in enumerate(map):
	tmpNumber = []
	for x, char in enumerate(line):
		if char not in allNumbers:
			if len(tmpNumber) != 0:
				parsedNumber = int("".join(tmpNumber))
				for i in range(len(tmpNumber)): onlyNumbersMap[y][x-i-1] = parsedNumber
				tmpNumber = []
		# if we get a number char
		else:
			tmpNumber.append(map[y][x])
	# if we exit one side with numbers left
	if len(tmpNumber) != 0:
			parsedNumber = int("".join(tmpNumber))
			for i in range(len(tmpNumber)): onlyNumbersMap[y][x-i] = parsedNumber

def getSurroundingCoords(x,y):
	res = []
	# Top
	if y != 0:
		if x != 0: res.append([x-1, y-1])
		res.append([x, y-1])
		if x != len(map[0]) -1: res.append([x+1, y-1])
	# Middle
	if x != 0: res.append([x-1, y])
	if x != len(map[0]) -1: res .append([x+1, y])
	
	# Bottom
	if y != len(map) -1:
		if x != 0: res.append([x-1, y+1])
		res.append([x, y+1])
		if x != len(map[0]) -1: res.append([x+1, y+1])
	return res

p1sum = 0
lastnum = 0
for y, line in enumerate(onlyNumbersMap):
	for x, num in enumerate(line):
		if num == lastnum:continue
		surroundingCoords = getSurroundingCoords(x,y)
		for coord in surroundingCoords:
			char = map[coord[1]][coord[0]]
			if char not in allNumbers and char != ".":
				p1sum += num
				lastnum = num
				break

p2sum = 0
for y, line in enumerate(map):
	for x, char in enumerate(line):
		numbers = []
		if char == "*":
			checkCoords = getSurroundingCoords(x,y)
			for coords in checkCoords:
				gottenNumber = onlyNumbersMap[coords[1]][coords[0]]
				if gottenNumber !=0:
					if gottenNumber not in numbers: numbers.append(gottenNumber)	
					
		if len(numbers) == 2:
			p2sum += numbers[0] * numbers[1]

print(p1sum, p2sum)