from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Monkey:
	items: list
	ontrue: int
	onfalse: int
	inspectcount: int
	operation: classmethod
	testdiv: classmethod

totmod: int = 0
monkeys: list[Monkey] = []
tmp: list[str] = []

def parsetmp():
	global totmod
	items: list[int] = [int(x.strip(",")) for x in tmp[1].split(" ")[4:]]
	tmpoparg: str = tmp[2].split(" ")[-1]
	tmpoperator: str = tmp[2].split(" ")[-2]
	mod = int(tmp[3].split(" ")[-1])
	totmod = mod if totmod == 0 else totmod*mod
	ontrue = int(tmp[4].split(" ")[-1])
	onfalse = int(tmp[5].split(" ")[-1])
	testdiv =  lambda x: x % mod == 0
	operation = None
	if tmpoparg == "old":
		operation = lambda x: x*x
	else:
		if tmpoperator == "+":
			operation = lambda x: x + int(tmpoparg)
		else:
			operation = lambda x: x * int(tmpoparg)
	monkey = Monkey(items, ontrue, onfalse, 0, operation, testdiv)
	return monkey

for line in open('input.txt', 'r').readlines():
	if line == "\n": continue
	tmp.append(line.strip("\n"))
	if len(tmp) == 6:
		monkeys.append(parsetmp())
		tmp = []
		

	
def inspects(monkey: Monkey, p1: bool):
	items = monkey.items
	for item in items:
		monkey.inspectcount += 1
		worry = monkey.operation(item)
		if p1: worry = worry//3
		if monkey.testdiv(worry):
			monkeys[monkey.ontrue].items.append(worry)
		else:
			monkeys[monkey.onfalse].items.append(worry)
	monkey.items = []

def minimizeworry():
	for monkey in monkeys:
		monkey.items = [x % totmod for x in monkey.items]

def round(p1: bool):
	for monkey in monkeys:
		inspects(monkey, p1)
	minimizeworry()

def p1():
	global monkeys
	ogmonkeys = deepcopy(monkeys)
	for _ in range(20): round(True)
	monkeys = sorted(monkeys, key=lambda mon: mon.inspectcount, reverse=True)
	print(f"Part 1: {monkeys[0].inspectcount * monkeys[1].inspectcount}")
	monkeys = ogmonkeys

def p2():
	global monkeys
	for _ in range(10000): round(False)
	monkeys = sorted(monkeys, key=lambda mon: mon.inspectcount, reverse=True)
	print(f"Part 2: {monkeys[0].inspectcount * monkeys[1].inspectcount}")
p1()
p2()