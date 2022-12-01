data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

lines = []
for line in data:
    tmp = []
    for c in line:
        tmp.append(c)
    lines.append(tmp)

openers = ["(", "{", "[", "<"]
closers = [")", "}", "]", ">"]

bad = []
stack = []
badlines = []
def processline(i, line):
    stack = []
    for c in line:
        if c in openers:
            stack.append(c)
        if c in closers:
            val = stack.pop()
            if c != closers[openers.index(val)]:
                bad.append(c)
                badlines.append(i)
    return stack

for i, line in enumerate(lines):
    processline(i, line)

res = 0
for c in bad:
    if c == ")":
        res += 3
    if c == "]":
        res += 57
    if c == "}":
        res += 1197
    if c == ">":
        res += 25137

print(res)

#p2

print(badlines)

for i in reversed(badlines):
    lines.pop(i)

results = []

for line in lines:
    stack = processline(0, line)
    results.append(list(reversed(stack)))

def calcline(line):
    sum = 0
    for c in line:
        sum *= 5
        if c == "(":
            sum += 1
        if c == "[":
            sum += 2
        if c == "{":
            sum += 3
        if c == "<":
            sum += 4
    return sum

compres = []

for res in results:
    compres.append(calcline(res))
print(sorted(compres)[int((len(compres)/2))])