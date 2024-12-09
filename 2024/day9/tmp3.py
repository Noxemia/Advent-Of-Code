from typing import List, Tuple, Dict
from copy import copy
dmap = []

for line in open('input.txt', 'r').readlines():
    dmap = [int(x) for x in line]

### part 1
rightFileCounter = len(dmap) // 2
leftfileCounter = 0
leftBlockCounter = 0
lp = 0 # 0
rp = len(dmap)-1
writable = False
cache = []
p1 = 0
while True:
    if lp == rp: break
    if not writable:
        print("Calculating", dmap[lp], leftfileCounter, leftBlockCounter)
        for y in range(dmap[lp]):
            p1 += leftfileCounter*leftBlockCounter
            leftBlockCounter += 1
        writable = not writable
        leftfileCounter +=1
        lp+=1
        print("Score", p1)
    elif writable:
        while len(cache) < dmap[lp]:
            print("Bringing in", dmap[rp])
            for i in range(dmap[rp]):
                cache.append(rightFileCounter)
            rp -= 2
            rightFileCounter -= 1

            print(cache)
        print("Inserting", dmap[lp], cache[:3])
        for y in range(dmap[lp]):
            p1 += cache.pop()*leftBlockCounter
            leftBlockCounter += 1
        lp += 1
        writable = not writable
        print("Score", p1)

print(cache)
for cached in cache:
    p1 += leftfileCounter*leftBlockCounter
    leftBlockCounter += 1
print(p1)

            