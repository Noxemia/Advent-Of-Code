from typing import List, Dict, Tuple

data: List[str] = []

for line in open('input.txt', 'r').readlines():
	splitLine = line.split(",")
	for line in splitLine: data.append(line)

def _hash(input: str):
	result = 0
	for c in input:
		result += ord(c)
		result *= 17
		result = result % 256
	return result

p1sum = 0
for line in data:
	p1sum += _hash(line)
print(p1sum)

boxes: Dict[int, Dict[str, int]] = {}
for i in range(256):
	boxes[i] = {}

for line in data:
	## Add
	if "=" in line:
		label = line.split("=")[0]
		fl = int(line.split("=")[1])
		boxnumber = _hash(label)
		boxes[boxnumber][label] = fl
	# Remove
	else:
		label = line[:-1]
		boxnumber = _hash(label)
		if label in boxes[boxnumber]: boxes[boxnumber].pop(label)
		
p2sum = 0
for bn in range(256):
	boxmult = bn+1
	for idx, key in enumerate(boxes[bn].keys()): 
		p2sum += boxmult*(idx+1)*boxes[bn][key]
print(p2sum)
			