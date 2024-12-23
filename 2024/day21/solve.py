from itertools import permutations, product
from functools import cache
keypad = []
keypad.append(['7','8','9'])
keypad.append(['4','5','6'])
keypad.append(['1','2','3'])
keypad.append(['.','0','A'])
kppos = (2,3)

dirpad = []
dirpad.append(['.', '^', 'A'])
dirpad.append(['<', 'v', '>'])
dppos = (2, 0)

def findPath(fr, to, padnum):
    pad = None
    if padnum == 0:
        pad = keypad
    else:
        pad = dirpad
        
    startx, starty = 0,0
    endx, endy, = 0,0
    
    for y, row in enumerate(pad):
        if to in row: endx, endy = row.index(to), y
        if fr in row: startx, starty = row.index(fr), y
    
    if startx == endx and starty == endy: return set({'A'})

        
    toWalk = [(startx, starty, [])]
    res = set()
    md = abs(startx-endx) + abs(starty-endy)
    
    while toWalk:
        x, y, dirs = toWalk.pop()
        if len(dirs) > md+1: continue
        if (x,y) == (endx, endy):
            res.add("".join(dirs)+'A')
            continue
        for d, dx, dy in [('^', 0, -1), ('>', 1, 0), ('v', 0, 1), ('<', -1, 0)]:
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= len(pad[0]) or ny >= len(pad) or pad[ny][nx] == '.': continue
            toWalk.append((nx, ny, dirs+[d]))
        
    return res 

def getKPcombinations(code: str):
    code = 'A' + code
    combinations = []
    for i in range(0, len(code)-1):
        combinations.append(findPath(code[i], code[i+1], 0))
    combinations = product(*combinations)
    combinations = ["".join(x) for x in combinations ]
    minlen = min([len(x) for x in combinations])
    combinations = [x for x in combinations if len(x) == minlen]
    return combinations

@cache
def recSolve(fr: str, to:str, depth) -> int:
    out = list(findPath(fr, to, 1))
    if depth == 1:
        return len(out[0])
    
    minlen = float('inf')
    for seq in out:
        localLen = 0
        seq = 'A' + seq
        for i in range(0, len(seq)-1):
            localLen += recSolve(seq[i], seq[i+1], depth -1)
        if localLen < minlen: minlen = localLen
    return minlen


def solve(code, depth):
    minlen = float('inf')
    for seq in getKPcombinations(code):
        seq = 'A' + seq
        testsum = 0
        for i in range(0, len(seq)-1):
            testsum += recSolve(seq[i], seq[i+1], depth)
        if testsum < minlen: minlen = testsum
    return minlen

    
part1 = 0
part2 = 0
for line in open('input.txt', 'r').readlines():
    line = line.strip("\n")
    mult = int(line[:-1])
    res = solve(line, 2)
    part1 += mult * res
    res = solve(line, 25)
    part2 += mult * res
    
    
print(part1, part2)
