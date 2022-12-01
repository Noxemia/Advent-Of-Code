import time

starttime = time.time()

data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)
polymer = data.pop(0)
data.pop(0)

rules = {}

for line in data:
    spl = str.split(line,"-")
    key = spl[0].strip()
    val = spl[1][2]
    rules[key] = val


def createPairs(polymer: str):
    tmp = []
    for i in range(len(polymer)-1):
        tmp.append(polymer[i] + polymer[i+1])
    return tmp



def step():
    global polymer
    pairs = createPairs(polymer)
    newpolymer = ""
    for pair in pairs:
        addition = rules.get(pair)
        newpolymer += pair[0]
        newpolymer += addition
        #print(pair, pair[0], addition, pair[1])
    newpolymer += pair[1]
    polymer = newpolymer


for i in range(40):
    print("On step:", i)
    step()

letters = dict.fromkeys(polymer)



for let in letters.keys():
    letters[let] = 0
    for c in polymer:
        if c == let:
            letters[let] += 1

print(letters)



#print(time.time() - starttime)