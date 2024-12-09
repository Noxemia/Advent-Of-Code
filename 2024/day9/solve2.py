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
        diskmap += [str(filecount) for x in range(blocksize)]
        filecount +=1
    else:
        diskmap += [-1 for x in range(blocksize)]
    isfree = not isfree
#print(diskmap)

correcttil = 0
for b in range(len(diskmap)-1, -1, -1):
    cons = diskmap.pop()
    if cons == -1: continue
    found = False
    for i, c in enumerate(diskmap[correcttil:]):
        if c == -1:
            diskmap[i+correcttil] = cons
            found = True
            correcttil += i
            #print("".join(diskmap)) 
            break
    if not found:
        diskmap.append(cons) 
        break


disknums = [int(x) for x in diskmap]

part1 = 0
for i, num in enumerate(disknums):
    part1 += i*num

print(part1)