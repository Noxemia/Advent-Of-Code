from typing import Tuple, List
from copy import deepcopy
from functools import lru_cache

data:List[Tuple[str, List[int]]] = []

for line in open('input.txt', 'r').readlines():
	line = line.strip("\n")
	data.append((line.split(" ")[0], list(map(int, line.split(" ")[1].split(",")))))

def groupsToStr(input):
    return "".join([str(x)+"," for x in list(input)])[:-1]

def strToGroup(input: str):
    return [int(x) for x in input.split(",")]

def consume(line: str, groups: list[int], groupstr: str) -> int:

    sgroup = strToGroup(groupstr)
    group = groups.pop(0)

    ## if line is less chars than the group length, always return []
    if len(line) < group: return 0

    next: List[str] = []

    ## Loop with window over string
    ## return back a string that is from the last . or eol
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
        ret = consume(deepcopy(_line), deepcopy(groups), groupsToStr(groups))
        res += ret
    return res


#exit(0)
p1tot = 0
for (line, groups) in data:
    ret = consume(line, groups, groupsToStr(groups))
    seen = []
    p1tot += ret


print(p1tot)