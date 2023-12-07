data = []
for line in open('input.txt', 'r').readlines():
	data.append(line.strip("\n"))

# Part 1	
#p1sum = 0

#for line in data:
#	nums = [x for x in line if x in allNums]
#	p1sum += int(nums[0] + nums[len(nums)-1])
	
#print(p1sum)

# Part 2
allNums = [str(x) for x in range(1,10)]
spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
zipped = list(zip(spelled+allNums, allNums*2))

def findFirst(input: str, rev: bool = False):
	for i in range(0, len(input)): 
		for spelledNum, y in zipped:
			if rev: spelledNum = spelledNum[::-1]
			if spelledNum == input[i:i+len(spelledNum)]: return y

print(sum([int(findFirst(line) + findFirst(line[::-1], True)) for line in data]))
