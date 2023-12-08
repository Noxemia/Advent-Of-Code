from dataclasses import dataclass
from typing import List, Set
from math import lcm

@dataclass
class Node():
	label: str
	left: str
	right: str

data: Set[Node] = {}
instructions: List[str] = []
startingNodes: List[Node] = []

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
	newNode = Node(label, left, right)
	data[label] = (newNode)
	if label[-1] == "A":
		startingNodes.append(newNode)


def getNode(label: str) -> Node:
	return data[label]

def findForNode(node: Node) -> int:
    global instructions
    cnode = node
    stepCount = 0
    lInstructions = [*instructions]
    while True:
        stepCount += 1
        instr = lInstructions.pop(0)
        lInstructions.append(instr)
        if instr == "R":
            cnode = getNode(cnode.right)
        elif instr == "L":
            cnode = getNode(cnode.left)
        else: print("Error unknown node")
        if cnode.label[-1] == "Z":
            return stepCount
		
res = []
for node in startingNodes:
	res.append(findForNode(node))

print("P1:", res[0], "P2:", lcm(*res))