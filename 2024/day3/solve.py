
import re
data = ""
for line in open('input.txt', 'r').readlines():
    data += line

pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))"
matches = re.findall(pattern, data)
operations = []
for m, do, dont in matches:
    if m != '':
        m = m[4:-1].split(",")
        f,s = int(m[0]), int(m[1])
        operations.append(f*s)
    if do != '': operations.append(-1)
    if dont != '': operations.append(-2)

part1, part2 = 0, 0
enabled = True
for op in operations:
    if op == -1: enabled = True
    elif op == -2: enabled = False
    else:
        part1 += op
        if enabled: part2 += op

print("Part 1:", part1, "\nPart 2:", part2)