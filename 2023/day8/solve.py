from dataclasses import dataclass
from typing import List



@dataclass
class Node():
	label: str
	left: str
	right: str

data: List[Node] = []
instructions = []

for line in open('input.txt', 'r').readlines():
	if instructions == []:
		instructions = list(line.strip("\n"))
		continue
	if line == "\n": continue
	line = line.strip("\n")
	label = line.split("=")[0].strip()
	lr = line.split("=")[1].strip()[1:-1]
	left = lr.split(",")[0]
	right = lr.split(",")[1].strip()
	
	data.append(Node(label, left, right))


def getNode(label: str):
	for node in data:
		if node.label == label:
			return node
	print("Error didnt find")

p1count = 0

cnode = getNode("AAA")
while True:
	p1count += 1
	instr = instructions.pop(0)
	instructions.append(instr)
	print(instr)
	if instr == "R":
		cnode = getNode(cnode.right)
	elif instr == "L":
		cnode = getNode(cnode.left)
	else: print("Error unknown node")

	print("New Node", cnode)
	if cnode.label == "ZZZ":
		print("Got end in", p1count)
		break
