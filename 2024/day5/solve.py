from typing import Dict, List, Tuple
from collections import defaultdict
rules: Dict[int, List[int]] = defaultdict(list)
updates: List[List[int]] = []

for line in open('input.txt', 'r').readlines():
    if line == "\n": continue
    elif "|" in line:
        v1, v2 = line.split("|")
        rules[int(v1)].append(int(v2))
    else:
        updates.append(list(reversed([int(x) for x in line.split(",")])))

def tryOrder(update: List[int]) -> Tuple[bool, int, int]:
    for i, page in enumerate(update):
        if page not in rules: continue
        r = rules[page]
        for next in update[i+1:]:
            if next in r:
                return (False, page, next)
    return (True, 0, 0)

count, count2 = 0, 0 
for update in updates:
    if tryOrder(update)[0]: 
        count += update[len(update)//2]
        continue
    while True:
        correct, i, y = tryOrder(update)
        if correct: 
            count2 += update[len(update)//2]
            break

        update[update.index(y)] = i
        update[update.index(i)] = y

print(count, count2)