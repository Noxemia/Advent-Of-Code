from dataclasses import dataclass

@dataclass
class Monkey:
	index: int
	items: list
	fun: classmethod
	operator: str
	oparg: int
	testdiv: int
	ontrue: int
	onfalse: int
	inspectcount: int

monkeys = []

tmp = []
for line in open('input.txt', 'r').readlines():
	if line == "\n": continue
	tmp.append(line)
	if len(tmp) == 6:
		index = int(tmp[0].split(" ")[1].strip(":\n"))
		items = [int(x.strip(",")) for x in tmp[1].split(" ")[4:]]
		opop = tmp[2].split(" ")[-2]
		tmpoparg = tmp[2].split(" ")[-1]
		oparg = None
		if tmpoparg[0] == "o":
			oparg = 0
		else:
			oparg = int(tmpoparg)
		testdiv = int(tmp[3].split(" ")[-1])
		ontrue = int(tmp[4].split(" ")[-1])
		onfalse = int(tmp[5].split(" ")[-1])
		monkeys.append(Monkey(index, items, opop, oparg, testdiv, ontrue, onfalse, 0))
		tmp = []

def inspects(monkey: Monkey):
	items = monkey.items
	for item in items:
		monkey.inspectcount += 1
		worry = 0
		if monkey.oparg == 0:
			worry = item*item
		else:
			if monkey.operator == "+":
				worry = item + monkey.oparg
			else:
				worry = item * monkey.oparg
		newworry = worry
		if newworry % monkey.testdiv == 0:
			monkeys[monkey.ontrue].items.append(newworry)
		else:
			monkeys[monkey.onfalse].items.append(newworry)
	monkey.items = []


mod = monkeys[0].testdiv
for monkey in monkeys[1:]:
	mod *= monkey.testdiv

def minimizeworry():
	for monkey in monkeys:
		monkey.items = [x % mod for x in monkey.items]

def round():
	for monkey in monkeys:
		inspects(monkey)
	minimizeworry()

def sorting(monkey: Monkey):
	return monkey.inspectcount

for _ in range(10000 ): round()
monkeys = sorted(monkeys, key=sorting, reverse=True)


print(monkeys[0].inspectcount * monkeys[1].inspectcount)
