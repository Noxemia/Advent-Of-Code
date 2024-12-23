from collections import defaultdict
from functools import cache
from copy import copy
pointers = defaultdict(set)


for line in open('input.txt', 'r').readlines():
    f, s = line.strip("\n").split("-")
    pointers[f].add(s)
    pointers[s].add(f)
    
threeGroups = set()
for groupi in pointers:
    group = pointers[groupi]
    for comp in group:
        group2 = pointers[comp]
        for comp2 in group:
            if comp2 in group2:
                content = sorted([groupi, comp, comp2])
                threeGroup = (content[0], content[1], content[2])
                threeGroups.add(threeGroup)
        
p1 = 0
for (f,s,t) in threeGroups:
    if f[0] == 't': 
        p1 += 1
        continue
    if s[0] == 't': 
        p1 += 1
        continue
    if t[0] == 't': 
        p1 += 1
        continue
    
print(p1)

largestSet = []
seen = set()
def search(current_node, group):
    global largestSet
    if current_node in seen: return
    seen.add(current_node)
    if len(group) > len(largestSet): largestSet = group
    
    forwardGroup = pointers[current_node]

    for connectedNode in forwardGroup:
        if connectedNode in group: continue
        if all([node in pointers[connectedNode] for node in group]):
            search(connectedNode, group | {connectedNode})
            
for node in pointers.keys():
    search(node, {node})

largestSet = list(largestSet)
print("".join([x+"," for x in sorted(largestSet)])[:-1])
