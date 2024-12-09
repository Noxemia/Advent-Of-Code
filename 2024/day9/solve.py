dmap = []

for line in open('input.txt', 'r').readlines():
    dmap = [int(x) for x in line]

### part 1
rightFileCounter = len(dmap) // 2
leftfileCounter = 0
leftBlockCounter = 0
lp = 0
rp = len(dmap)-1
writable = False
cache = []
part1 = 0
shouldBreak = False
while True:
    if lp == rp: shouldBreak = True
    if not writable:
        for y in range(dmap[lp]):
            part1 += leftfileCounter*leftBlockCounter
            leftBlockCounter += 1
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
            part1 += cache.pop(0)*leftBlockCounter
            leftBlockCounter += 1
        lp += 1
        writable = not writable
    if shouldBreak: break

for cached in cache:
    part1 += cached*leftBlockCounter
    leftBlockCounter += 1
## p2

### Check to left of movable file but only once. Build datastructure to allow checking left


### list of (startindex, endindex, size)
freespace = []
blockCounter = 0
writable = False
for num in dmap:
    if not writable:
        blockCounter += num
        writable = True
    else:
        writable = False
        lb = blockCounter
        rb = blockCounter+num-1
        size = rb-lb+1
        if size == 0: continue
        freespace.append((size, lb, rb))
        blockCounter+=num

fileindex = len(dmap) // 2
writable = False
completed = dict()
for numi, num in enumerate(reversed(dmap)):
    if not writable:
        writable = True
        hasMoved = False
        for index, (size, lb, rb) in enumerate(freespace):
            if rb >= blockCounter: break
            if num > size: 
                continue

            elif size == num:
                completed[fileindex] = (lb, lb+num-1)
                freespace.pop(index)
                fileindex-=1
                hasMoved = True
                break

            elif size > num:
                completed[fileindex] = (lb, lb+num-1)
                fileindex-=1
                freespace[index] = ((rb-(lb+num))+1, lb+num, rb)
                hasMoved = True
                break 
        if not hasMoved: 
            fileindex -= 1          
    else:
        writable = False
    blockCounter -= num
        
part2 = 0
fileindex = 0
blockindex = 0
writable = False
for index, num in enumerate(dmap):
    if not writable:
        if fileindex not in completed:
            for y in range(num):
                part2 += fileindex*blockindex
                blockindex += 1
        else:
            blockindex += num
        writable = not writable
        fileindex +=1
    else:
        blockindex += num
        writable = not writable

for k in completed.keys():
    lb, rb = completed[k]
    for v in range(lb, rb+1):
        part2 += k*v

print("Part 1:", part1, "\nPart 2:", part2)
