data = []

for line in open('input.txt', 'r').readlines():
	data.append([[*range(int(y[0]), int(y[1])+1)] for y in 
		[spl.split("-") for spl in line.strip("\n").split(",")]])
	
countp1 = 0
countp2 = 0
for line in data:
	if any([x for x in line[0] if x in line[1]]): countp2 += 1
	if (complist := [x for x in line[0] if x in line[1]]) == line[0] or complist == line[1]: countp1 += 1

print(countp1, countp2)

