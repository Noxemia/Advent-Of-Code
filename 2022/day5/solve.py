from copy import deepcopy
data = []


stacks = []

for i, line in enumerate(open('input.txt', 'r').readlines()):
	if line.strip(" ")[0] == "[":
		linecrates = []
		for i in range(0, len(line), 4):
			linecrates.append((line[i] + line[i+1] + line[i+2]).strip(" []"))
		for i, elem in enumerate(linecrates):
			if elem != "":
				if (len(stacks) -1) != i:
					for _ in range(i-len(stacks)+1):
						stacks.append([])
				stacks[i].append(elem)
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