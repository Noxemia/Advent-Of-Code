
import re
import time
data = ""
for line in open('input.txt', 'r').readlines():
    data += line

st1 = time.time_ns()
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
ed1 = time.time_ns()
print("Part 1:", part1, "\nPart 2:", part2)

data = [x for x in data]
st2 = time.time_ns()

part1, part2 = 0, 0
enabled = True
for i, c in enumerate(data):
    dnt = "".join(data[i:i+7])
    if dnt == "don't()":
        enabled = False
    do = "".join(data[i:i+4])
    if do == "do()": 
        enabled = True
    try:
        cons = "".join(data[i:i+4])
        ## Check for mul(
        if cons != "mul(": 
            continue
        ## look for and )
        iparen = 0
        for ii, cc in enumerate(data[i+4:i+13]):
            if cc == ')':
                iparen = i + ii + 4
                break
        if iparen == 0: continue
        
        nums = "".join(data[i+4:iparen])
        nums = nums.split(",")
        f = int(nums[0])
        s = int(nums[1])
        part1 += f*s
        if enabled: 
            part2 += f*s
    except:
        pass
ed2 = time.time_ns()

print("Part 1:", part1, "\nPart 2:", part2)
print("Time regex: \t", ed1-st1, "\nTime ownparse\t", ed2-st2)
