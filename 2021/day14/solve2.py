data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)
polymer = data.pop(0)
data.pop(0)

rules = {}
paircount = {}


for line in data:
    spl = str.split(line,"-")
    key = spl[0].strip()
    val = spl[1][2]
    rules[key] = val
    paircount[key] = 0



def createPairs(polymer: str):
    tmp = []
    for i in range(len(polymer)-1):
        tmp.append(polymer[i] + polymer[i+1])
    return tmp

initpairs = createPairs(polymer)
for pair in initpairs:
    paircount[pair] +=1


def step():
    global paircount
    paircountcp = paircount.copy()
    for pair in paircount.keys():
        if paircount[pair] == 0: continue
        val = paircount[pair]
        paircountcp[pair] -= val
        newpair = pair[0] + rules[pair]
        paircountcp[newpair] += val
        newpair = rules[pair] + pair[1]
        paircountcp[newpair] += val
    paircount = paircountcp




for _ in range(40):
    step()

print(paircount)

keys = []

for rule in rules.keys():
    if not rule[0] in keys:
        keys.append(rule[0])
    if not rule[1] in keys:
        keys.append(rule[1])

count = dict.fromkeys(keys)

for l in count.keys():
    count[l] = 0
    for pair in paircount:
        if pair[0] == pair[1] and pair[0] == l:
            count[l] += paircount[pair]*2
        elif l in pair:
            count[l] += paircount[pair]

count[polymer[0]] += 1
count[polymer[len(polymer)-1]] += 1

for l in count:
    count[l] = count[l]/2

print(max(count.values()) - min (count.values()), count)