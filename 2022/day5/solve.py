from copy import deepcopy
data = []

stacks = None

for i, line in enumerate(open('input.txt', 'r').readlines()):
	# init stacks
	if stacks == None: stacks = [[] for _ in range(len(line)//4)]

	if line[0] == "[":
		linecrates = [x for y, x in enumerate(line) if y % 4 == 1]
		for i, elem in enumerate(linecrates):
			if elem != " ": stacks[i].append(elem)

	if line[0] == "m":
		spl = line.split(" ")
		data.append([int(spl[1]), int(spl[3]), int(spl[5])])

stacks2 = deepcopy(stacks)

def move( frm: int, to: int):
	stacks[to-1].insert(0, stacks[frm -1].pop(0))

def move2(amt: int, frm: int, to: int):
	stacks2[to-1] =  stacks2[frm-1][:amt] + stacks2[to-1]
	stacks2[frm-1] = stacks2[frm-1][amt:]

for line in data:
	for _ in range(line[0]):
		move(line[1], line[2])
	move2(line[0], line[1], line[2])


print(f"Part 1: {''.join([x[0] for x in stacks])}")
print(f"Part 2: {''.join([x[0] for x in stacks2])}")