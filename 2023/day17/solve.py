from heapq import heappop, heappush

data = []

for line in open('input.txt', 'r').readlines():
	data.append([int(x) for x in list(line.strip())])

## (idx, idy, direction, dirTime)
visited = set()
## (TotDistance, idx, idy, cost, direction, dirTime)
queue = [(0,0,0,0,0,0)]

while len(queue) != 0:
	dist, idx, idy, cost, direction, dirTime = heappop(queue)
	if idx == len(data[0])-1 and idy == len(data)-1:
		print("Done:", dist + cost)
		break
	#print("Current: ", dist, idx, idy, cost, direction, dirTime)
	if (idx, idy, direction, dirTime) in visited: continue
	visited.add((idx, idy, direction, dirTime))

	directions = [(0,1), (1,0), (0, -1), (-1, 0)]
	
	if dirTime > 0 and dirTime < 4:
		newx = idx + directions[direction][0]
		newy = idy + directions[direction][1]
		if newx < 0 or newx > len(data[0])-1 or newy < 0 or newy > len(data)-1: continue
		heappush(queue, (dist+cost, newx, newy, data[newy][newx], direction, dirTime+1))
		continue
	else:
		for _dir, mod in enumerate(directions): # down right up left, 0,1,2,3
			if abs(_dir - direction) == 2 and dirTime != 0: continue
			newx = idx + mod[0]
			newy = idy + mod[1]
			if newx < 0 or newx > len(data[0])-1 or newy < 0 or newy > len(data)-1: continue
			newDirTime = dirTime + 1 if direction == _dir else 1
			if newDirTime > 10: continue
			heappush(queue, (dist+cost, newx, newy, data[newy][newx], _dir, newDirTime))