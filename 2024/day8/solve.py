from typing import List, Dict, Tuple
chars = ['0']
for i in range(65, 122): chars.append(chr(i))
for i in range(1, 10): chars.append(str(i))
    
antennas: Dict[str, List[Tuple[int, int]]] = dict()
for char in chars: antennas[char] = []

amap = []
for line in open('input.txt', 'r').readlines(): amap.append([x for x in line.strip("\n")])
    
for y, row in enumerate(amap):
    for x, char in enumerate(row):
        if char == '.': continue
        antennas[char].append((x,y))

p1set = set()
def calcNodes(fa: Tuple[int, int], sa: Tuple[int, int]):
    global p1set
    xdiff = abs(fa[0] - sa[0])
    ydiff = abs(fa[1] - sa[1])
    
    fxn = fa[0] - xdiff if fa[0] < sa[0] else fa[0] + xdiff
    fyn = fa[1] - ydiff if fa[1] < sa[1] else fa[1] + xdiff
    sxn = sa[0] + xdiff if fa[0] < sa[0] else sa[0] - xdiff
    syn = sa[1] + ydiff if fa[1] < sa[1] else sa[1] - xdiff
    #print(xdiff, ydiff)
    if not (fxn < 0 or fyn < 0 or fxn >= len(amap[0]) or fyn >= len(amap)): p1set.add((fxn, fyn))
    if not (sxn < 0 or syn < 0 or sxn >= len(amap[0]) or syn >= len(amap)): p1set.add((sxn, syn))

p2set = set()
for char in chars:
    for i, fa in enumerate(antennas[char]):
        for sa in antennas[char][i+1:]:
            calcNodes(fa, sa)
            
            p2set.add(fa)
            p2set.add(sa)
            
            xdiff = fa[0] - sa[0]
            ydiff = fa[1] - sa[1] 
            
            nx, ny = fa
            while True:
                nx += xdiff
                ny += ydiff
                if nx < 0 or ny < 0 or nx >= len(amap[0]) or ny >= len(amap): 
                    break
                p2set.add((nx,ny))
                
            xdiff *= -1
            ydiff *= -1
            nx, ny = fa

            while True:
                nx += xdiff
                ny += ydiff
                if nx < 0 or ny < 0 or nx >= len(amap[0]) or ny >= len(amap): break
                p2set.add((nx,ny))

print("Part 1", len(p1set), "\nPart 2:", len(p2set))               
