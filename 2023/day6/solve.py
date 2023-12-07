from time import time
data = []

for line in open('input.txt', 'r').readlines():
	line = line.strip("\n")
	line = line.split(":")[1]
	line = line.split(" ")
	nums = []
	for char in line:
		if char != '':
			nums.append(int(char))
	data.append(nums)
	 
winnings = [0]*len(data[0])
p1startime = time()
for i in range(len(data[0])):
	_time = data[0][i]
	distance = data[1][i]
	
	for ms in range(_time):
		cdistance = (_time - ms) * ms
		if cdistance > distance:
			winnings[i] += 1

p1mult = 1
for win in winnings:
	p1mult *= win
print("p1 time:", time()-p1startime)

#p2
_time = int("".join([str(x) for x in data[0]]))
dist = int("".join([str(x) for x in data[1]]))
p2times = 0

firstWin = 0
lastWin = 0

p1startime = time()

for ms in range(_time):
	cdistance = (_time - ms) * ms
	if cdistance > dist:
		firstWin = ms
		break

for ms in range(_time, 0, -1):
	cdistance = (_time - ms) * ms
	if cdistance > dist:
		lastWin = ms
		break

print("P2 time:", time()-p1startime)
p2times = lastWin - firstWin

print(p2times)

print(p1mult)