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
inslist = []
shouldBreak = False
while True:
    if lp == rp: shouldBreak = True
    if not writable:
        for y in range(dmap[lp]):
            p1 += leftfileCounter*leftBlockCounter
            leftBlockCounter += 1
            inslist.append(leftfileCounter)
        writable = not writable
        leftfileCounter +=1
        lp+=1
    elif writable:
        while len(cache) < dmap[lp]:
            for i in range(dmap[rp]):
                cache.append(rightFileCounter)
            rp -= 2
            rightFileCounter -= 1
        for y in range(dmap[lp]):
            inslist.append(cache[0])
            p1 += cache.pop(0)*leftBlockCounter
            leftBlockCounter += 1
        lp += 1
        writable = not writable
    if shouldBreak: break

for cached in cache:
    p1 += cached*leftBlockCounter
    leftBlockCounter += 1
    inslist.append(cached)
print(p1)

#print("".join([str(x) for x in inslist]))

            