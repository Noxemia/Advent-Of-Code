
from collections import defaultdict
from dataclasses import dataclass
import sys
sys.setrecursionlimit(20000)
data = []

for line in open('input.txt', 'r').readlines():
	data.append(line.strip("\n"))

def def_value():
	return [0,[]]
#dir = [size, [files], [dirs],recsize]

fs = {}

currentdirectory = ""

for line in data:
	line = line.split(" ")
	if line[0] == "$":
		if line[1] == "cd": 
			if line[2] == "..":
				continue
			else: 
				currentdirectory = line[2]
				if not currentdirectory in fs.keys():
					fs[currentdirectory] = [0,[],[],0]
		# ls
		else: continue
	
	elif line[0] == "dir":
		if not line[1] in fs[currentdirectory][2]:
			fs[currentdirectory][2].append(line[1])
	else:
		if not line[1] in fs[currentdirectory][1]:
			fs[currentdirectory][1].append(line[1])
			fs[currentdirectory][0] += int(line[0])


def dir_size(dirname) -> int:
	size = 0
	size += fs[dirname][0]
	for nextdir in fs[dirname][2]:
		if size > 100000: return 100001
		size += dir_size(nextdir)
	if size > 100000: return 100001
	return size


for dir in fs.keys():
	size = dir_size(dir)
	print(dir)
	fs[dir][3] = size

p1cnt = 0
for dir in fs.keys():
	if fs[dir][3] <= 100000:
		p1cnt += fs[dir][3]

print(fs)
print(p1cnt)

