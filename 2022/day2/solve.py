data = []

file = open('input.txt', 'r')

for line in file.readlines():
	data.append(line)

score = 0
for line in data:
	elves = line[0:1]
	me = line [2:3]
	#elves rock
	if elves == 'A':
		if me == 'X':
			score += 4 # draw + rock
		if me == 'Y':
			score += 8 # paper + win
		if me == 'Z':
			score += 3 # scissor + lose
	# elves scissor
	if elves == 'C':
		if me == 'X':
			score += 7 # win + rock
		if me == 'Y':
			score += 2 # paper + loose
		if me == 'Z':
			score += 6 # scissor + draw
	# elves paper
	if elves == 'B':
		if me == 'X':
			score += 1 # loose + rock
		if me == 'Y':
			score += 5 # paper + draw
		if me == 'Z':
			score += 9 # scissor + win

print(f"Part 1: {score}")

score2 = 0

for line in data:
	elves = line[0:1]
	outcome = line [2:3]
	if elves == 'A':
		if outcome == 'X':
			score2 += 3 # pick scissor + lose
		if outcome == 'Y':
			score2 += 4 # pick rock + draw
		if outcome == 'Z':
			score2 += 8 # pick paper + win
	if elves == 'B':
		if outcome == 'X':
			score2 += 1 # pick rock + lose
		if outcome == 'Y':
			score2 += 5 # pick paper + draw
		if outcome == 'Z':
			score2 += 9 # pick scissors + win	
	if elves == 'C':
		if outcome == 'X':
			score2 += 2 # pick paper + lose
		if outcome == 'Y':
			score2 += 6 # pick Scissors + draw
		if outcome == 'Z':
			score2 += 7 # pick rock + win				

print(f"Part 2: {score2}")