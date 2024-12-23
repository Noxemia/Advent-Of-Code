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
                tucnt = (content[0], content[1], content[2])
                threeGroups.add(tucnt)
        
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
print(pointers)
p2 = 4

allsets = set()

def search(cnode, group):
    cgroup = pointers[cnode]
    
    l = ""
    for n in sorted(list(group)):
        l+=n + ","
    l = l[:-1]
    if l in allsets: return
    allsets.add(l)
    
    for node in cgroup:
        if node in group: continue
        if all([n in pointers[node] for n in group]):
            search(node, group | {node})
            
for node in pointers.keys():
    search(node, {node})

allsets = list(allsets)
allsets = sorted(allsets, key=lambda x: len(x), reverse=True)
print(allsets[0])
