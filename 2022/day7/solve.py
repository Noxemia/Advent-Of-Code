from dataclasses import dataclass
data = []

for line in open('input.txt', 'r').readlines():
	data.append(line.strip("\n"))

@dataclass
class Node:
	parentdir: None
	dirname: str
	filessize: int
	directories: dict
	def __init__(self, parent, name:str):
		self.dirname = name
		self.parentdir = parent
		self.filessize = 0
		self.directories = {}

root = Node(None, "/")

currentdir = root
data.pop(0)
allnodes = [root]
for line in data:
	line = line.split()
	# command
	if line[0] == "$":
		# cd
		if line [1] == "cd":
			if line[2] == "..":
				currentdir = currentdir.parentdir
			else:
				currentdir = currentdir.directories[line[2]]
		# ls has no impact
	# dir file
	elif line[0] == "dir":
		newnode = Node(currentdir, line[1])
		allnodes.append(newnode)
		currentdir.directories[line[1]] = newnode
	# regular file
	else:
		currentdir.filessize += int(line[0])

def findsize(node: Node) -> int:
	size = node.filessize
	for dir in node.directories.keys():
		size += findsize(node.directories[dir])
	return size

p1cnt = 0
for node in allnodes:
	val = findsize(node)
	if val <= 100000:
		p1cnt += val

print(f"Part 1: {p1cnt}")

rootsize = findsize(root)
mindeletesize = 30000000 - (70000000 - rootsize)

currentmin = 70000000
for node in allnodes:
	val = findsize(node)
	if val > mindeletesize and val < currentmin:
		currentmin = val

print(f"Part 2: {currentmin}")