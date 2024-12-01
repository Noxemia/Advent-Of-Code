from collections import Counter
left = []
right = []
for line in open('input.txt', 'r').readlines():
    line = line.strip("\n").split("  ")
    left.append(int(line[0]))
    right.append(int(line[1]))

tot1 = sum([abs(r-l) for l,r in zip(sorted(left), sorted(right))])

print("Part 1:", tot1)

rcount = Counter(right)
tot2 = sum([l * rcount.get(l, 0) for l in left])

print("Part 2:", tot2)