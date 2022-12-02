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
	data.append(line)


def vscore(abc, xyz) -> int:
	if abc == xyz: return 3 # draw
	if abc == 1 and xyz == 3: return 0 # rock vs paper lose
	if abc == 1 and xyz == 2: return 6 # rock vs scissor win
	if abc == 2 and xyz == 3: return 0 # paper vs scissor lose
	if abc == 2 and xyz == 1: return 6 # paper vs rock win
	if abc == 3 and xyz == 1: return 0 # scissor vs rock lose
	if abc == 3 and xyz == 2: return 6 # scissor vs paper win

score = 0
for line in data:
	elves = line[0]
	me = line [1]
	score += vscore(elves, me) + me


print(f"Part 1: {score}")

# score2 = 0

# for line in data:
# 	elves = line[0:1]
# 	outcome = line [2:3]
# 	if elves == 'A':
# 		if outcome == 'X':
# 			score2 += 3 # pick scissor + lose
# 		if outcome == 'Y':
# 			score2 += 4 # pick rock + draw
# 		if outcome == 'Z':
# 			score2 += 8 # pick paper + win
# 	if elves == 'B':
# 		if outcome == 'X':
# 			score2 += 1 # pick rock + lose
# 		if outcome == 'Y':
# 			score2 += 5 # pick paper + draw
# 		if outcome == 'Z':
# 			score2 += 9 # pick scissors + win	
# 	if elves == 'C':
# 		if outcome == 'X':
# 			score2 += 2 # pick paper + lose
# 		if outcome == 'Y':
# 			score2 += 6 # pick Scissors + draw
# 		if outcome == 'Z':
# 			score2 += 7 # pick rock + win				

# print(f"Part 2: {score2}")