data = []

file = open('input.txt', 'r')

for line in file.readlines():
	newline = []
	if line[0:1] == 'A': newline.append(1)
	if line[0:1] == 'B': newline.append(2)
	if line[0:1] == 'C': newline.append(3)
	if line[2:3] == 'X': newline.append(1)
	if line[2:3] == 'Y': newline.append(2)
	if line[2:3] == 'Z': newline.append(3)
	data.append(newline)

print(data[0])

def pickscore(elves, me) -> int:
	if elves == me: return 3 # draw
	if elves == 1 and me == 3: return 0 # rock vs scissor lose
	if elves == 1 and me == 2: return 6 # rock vs paper win
	if elves == 2 and me == 1: return 0 # paper vs rock lose
	if elves == 2 and me == 3: return 6 # paper vs scissor win
	if elves == 3 and me == 2: return 0 # scissor vs paper lose
	if elves == 3 and me == 1: return 6 # scissor vs rock win

score = 0
for line in data:
	elves = line[0]
	me = line [1]
	score += pickscore(elves, me) + me


print(f"Part 1: {score}")


def outcomescore(elves, outcome) -> int:
	if outcome == 1:
		if elves == 1: return 3 # elves rock lose
		if elves == 2: return 1 # elves paper lose
		if elves == 3: return 2 # elves scissor lose
	if outcome == 2:
		return 3 + elves
	if outcome == 3:
		if elves == 1: return 2 + 6 # elves rock win
		if elves == 2: return 3 + 6 # elves paper win
		if elves == 3: return 1 + 6 # elves scissor win
	
score2 = 0

for line in data:
	elves = line[0]
	me = line [1]
	score2 += outcomescore(elves, me)

print(f"Part 2: {score2}")