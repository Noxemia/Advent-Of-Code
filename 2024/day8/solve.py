from typing import List, Dict, Tuple
from copy import copy
chars = ['0']
for i in range(65, 122):
    chars.append(chr(i))
for i in range(1, 10):
    chars.append(str(i))
    
antennas: Dict[str, List[Tuple[int, int]]] = dict()

for char in chars:
    antennas[char] = []

amap = []
for line in open('input.txt', 'r').readlines():
    amap.append([x for x in line.strip("\n")])
    
for y, row in enumerate(amap):
    for x, char in enumerate(row):
        if char == '.': continue
        antennas[char].append((x,y))
    
def calcNodes(fa: Tuple[int, int], sa: Tuple[int, int]):
    xdiff = abs(fa[0] - sa[0])
    ydiff = abs(fa[1] - sa[1])
    
    fxn = fa[0] - xdiff if fa[0] < sa[0] else fa[0] + xdiff
    fyn = fa[1] - ydiff if fa[1] < sa[1] else fa[1] + xdiff
    
    sxn = sa[0] + xdiff if fa[0] < sa[0] else sa[0] - xdiff
    syn = sa[1] + ydiff if fa[1] < sa[1] else sa[1] - xdiff
    #print(xdiff, ydiff)
    return [(fxn, fyn), (sxn, syn)]

for row in amap:
    break
    print("".join(row))

antcount = set()
#print(antennas["a"])
for char in chars:
    break
    for i, l in enumerate(antennas[char]):
        for r in antennas[char][i+1:]:
            antinodes = calcNodes(l, r)
            print("anti", char, l, r, antinodes)

            for x,y in antinodes:
                if x < 0 or y < 0 or x >= len(amap[0]) or y >= len(amap): continue
                antcount.add((x,y))
                try:
                    if amap[y][x] == ".": amap[y][x] = "#"
                except: pass

#print(len(amap))
#print("##############")

    
print(len(antcount))
antcount = set()
for char in chars:
    for i, fa in enumerate(antennas[char]):
        for sa in antennas[char][i+1:]:
            antcount.add(fa)
            antcount.add(sa)
            xdiff = fa[0] - sa[0]
            ydiff = fa[1] - sa[1] 
            xd = copy(fa)
            nx, ny = xd
            for i in range(1000):
                nx += xdiff
                ny += ydiff
                if nx < 0 or ny < 0 or nx >= len(amap[0]) or ny >= len(amap): 
                    break
                antcount.add((nx,ny))
            xd = copy(fa)
            nx, ny = xd
            xdiff *= -1
            ydiff *= -1

            for i in range(1000):
                nx += xdiff
                ny += ydiff
                if nx < 0 or ny < 0 or nx >= len(amap[0]) or ny >= len(amap): break
                antcount.add((nx,ny))

print(len(antcount))               
