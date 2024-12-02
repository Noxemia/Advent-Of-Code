from collections import Counter
left, right = zip(*((int(line.split("  ")[0]), int(line.split("  ")[1])) for line in open('input.txt', "r").readlines()))

left, right = sorted(left), sorted(right)
tot1 = sum(abs(r-l) for l,r in zip(left, right))
print("Part 1:", tot1)

rcount = Counter(right)
tot2 = sum(l * rcount[l] for l in left)
print("Part 2:", tot2)