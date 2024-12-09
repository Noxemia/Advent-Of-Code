from typing import List, Tuple, Dict

dmap = ""

for line in open('input.txt', 'r').readlines():
    dmap = line

### build map in terms of counter: fileid, blocksize, free, content

filecount = 0
isfree = False
diskmap = []
for blocksize in [x for x in dmap]:
    blocksize = int(blocksize)
    content = []
    if not isfree:   
        diskmap += [filecount for _ in range(blocksize)]
        filecount +=1
    else:
        diskmap += [-1 for _ in range(blocksize)]
    isfree = not isfree
#print(diskmap)

def printDiskMap():
    dbug = ""
    for x in diskmap:
        if x == -1: dbug += "."
        else: dbug += str(x)
    print(dbug)

tested = set()
for b in range(len(diskmap)-1, -1, -1):
    if b > len(diskmap)-1: continue
    if diskmap[b] == -1: continue

    cons = diskmap[b]
    if cons in tested: continue
    #print("cons", cons)
    conslist = [cons]
    bi = b-1
    while cc := diskmap[bi] == cons:
        conslist.append(cons)
        bi -= 1
    found = False
    for i, c in enumerate(diskmap[:b]):
        if i > b: break
        nlist = diskmap[i:i+len(conslist)]
        if any(c != -1 for c in nlist) or len(nlist) < len(conslist): 
            tested.add(cons)
            continue
        #print("i", i)
        for y in range(i, i+len(conslist)):
            diskmap[y] = cons
        for z in range(b, b-len(conslist), -1):
            diskmap[z] = -1
        break

    #printDiskMap()

part1 = 0
for i, num in enumerate(diskmap):
    if num == -1: continue
    part1 += i*num

print(part1)