from typing import List

data = []

for line in open('input.txt', 'r').readlines():
	data.append([int(x) for x in line.strip("\n").split(" ")])


def nextSequence(seq: List[int]):
	res = []
	for i in range(len(seq)-1):
		res.append(seq[i+1] - seq[i])
	return res

def calcSequence(seq: List[int], p1):
	allSequences: List[List[int]] = []
	allSequences.append(seq)
	currentSeq:List[int] = seq

	while True:
		currentSeq = nextSequence(currentSeq)
		allSequences.append(currentSeq)
		if all([x == 0 for x in currentSeq]): break
	##p1 
	if p1:
		allSequences[-1].append(0)
		for i in range(len(allSequences)-2, -1, -1):
			cur = allSequences[i]
			prev = allSequences[i+1]
			newVal = prev[-1] + cur[-1]
			cur.append(newVal)
		return allSequences[0][-1]
	#p2
	else:
		allSequences[-1].insert(0, 0)
		for i in range(len(allSequences)-2, -1, -1):
			cur = allSequences[i]
			prev = allSequences[i+1]
			newVal = cur[0] - prev[0]
			cur.insert(0, newVal)
		return allSequences[0][0]
#calcSequence(data[0])

p1sum = 0
for line in data:
	p1sum += calcSequence(line, True)

p2sum = 0
for line in data:
	p2sum += calcSequence(line, False)
print(p1sum, p2sum)