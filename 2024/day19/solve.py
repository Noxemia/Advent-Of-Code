from functools import cache
towels = set()
patterns = []

for line in open('input.txt', 'r').readlines():
    if line == "\n": continue
    elif "," in line: 
        line = [x.strip(" ") for x in line.strip("\n").split(",")]
        towels = set(line)
    else:
        patterns.append(line.strip("\n"))

@cache
def validPattern(pattern: str) -> int:
    res = 0

    if pattern in towels: res += 1
    for i in range(1, len(pattern)):
        cons, rest = pattern[:i], pattern[i:]
        if cons in towels:
            res += validPattern(rest)
            
    return res

p1 = 0
p2 = 0
for pattern in patterns:
    
    res = validPattern(pattern)
    if res: p1 += 1
    p2 += res
        

        
print(p1, p2)