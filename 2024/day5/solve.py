from typing import Dict, List, Tuple
rules: Dict[int, List[int]] = {}
updates: List[List[int]] = []

for line in open('input.txt', 'r').readlines():
    if line == "\n": continue
    elif "|" in line:
        v1, v2 = line.split("|")
        if int(v1) in rules.keys():
            rules[int(v1)].append(int(v2))
        else:
            rules[int(v1)] = [int(v2)]
    else:
        updates.append(list(reversed([int(x) for x in line.split(",")])))

def tryOrder(update: List[int]) -> Tuple[bool, int, int]:
    for i, page in enumerate(update):
        if page not in rules: continue
        r = rules[page]
        for y, next in enumerate(update[i+1:]):
            if next in r:
                return (False, page, next)
    return (True, 0, 0)

count = 0
for update in updates:
    if tryOrder(update)[0]: count += update[len(update)//2]

count2 = 0
for update in updates:
    if tryOrder(update)[0]: continue
    correct, i, y = False, 0, 0
    while True:
        correct, i, y = tryOrder(update)
        if correct: 
            count2 += update[len(update)//2]
            break

        ni = update.index(i)
        ny = update.index(y)
        update[ny] = i
        update[ni] = y

print(count, count2)
