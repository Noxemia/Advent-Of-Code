from typing import Tuple, List
from functools import cache

datap1: List[Tuple[str, List[int]]] = []
datap2: List[Tuple[str, List[int]]] = []

for line in open('input.txt', 'r').readlines():
    line = line.strip("\n")
    justSprings = line.split(" ")[0]
    numbers = list(map(int, line.split(" ")[1].split(",")))
    expandedLine = ""
    expandedNumbers = numbers*5
    for _ in range(5):
        expandedLine += justSprings + "?"
    expandedLine = expandedLine[:-1]
    datap1.append((justSprings, numbers))
    datap2.append((expandedLine, expandedNumbers))


def groupsToStr(input) -> str:
    return "".join([str(x)+"," for x in list(input)])[:-1]

def strToGroup(input: str) -> List[int]:
    return [int(x) for x in input.split(",")]

consumeaccess = 0

@cache
def consume(line: str, groups: str) -> int:
    global consumeaccess
    consumeaccess += 1
    groups = strToGroup(groups)
    group = groups.pop(0)

    ## if line is less chars than the group length, always return []
    if len(line) < group: return 0

    next: List[str] = []

    ## Loop with window over string
    ## return back a string that is from the last . or eol
    ## if we go past a # and we have not used it, its not valid
    hashtagseen = False
    firstHastagIndex = 0
    for i in range(0,len(line)-group+1):
        window = line[i:i+group]
        if "#" in window and not hashtagseen: 
            hashtagseen = True
            firstHastagIndex = window.index("#") + i
        if hashtagseen:
            if "#" in window:
                if i > firstHastagIndex: break
            else: break
        
        # no dots in window
        if any([x == "." for x in window]): continue

        # check that to the right is either a dot or a questionmark
        leftchar = "." if i == 0 else line[i-1]
        rightchar = "." if i+group == len(line) else line[i+group]
        if leftchar == "#" or rightchar == "#": continue
        _next = line[i+group+1:]
        next.append(_next)


    ## if we have no next groups but groups is not empty we return 0
    if len(next) == 0: 
        return 0
    
    ## if we have used all groups, we just return the number groups that do not contains any #
    if len(groups) == 0:
        res = 0
        for _group in next:
            if "#" not in _group: 
                res += 1
        return res
    
    ## Else we recursivly call consume for each in next
    res = 0
    for _line in next:
        ret = consume(_line, groupsToStr(groups))
        res += ret
    return res


p1tot = 0
for (line, groups) in datap1:
    ret = consume(line, groupsToStr(groups))
    p1tot += ret

p2tot = 0
for (line, groups) in datap2:
    p2tot += consume(line, groupsToStr(groups))

print("Part 1:", p1tot, "Part 2:", p2tot)