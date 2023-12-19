from typing import Dict, List, Tuple
from copy import deepcopy


items: List[Dict[str, int]] = [] # letter op, amt, nrule
rules: Dict[str, List] = {} # letter: [rules]/["any", next]

for line in open('input.txt', 'r').readlines():
    line = line.strip("\n")
    if line == "": continue

    if line[0] == "{":
        line = line[1:-1]
        amounts = line.split(",")
        itemDict = {}
        for amount in amounts:
                itemDict[amount.split("=")[0]] = int(amount.split("=")[1])
        items.append(itemDict)
    else:
        label = line.split("{")[0]
        
        _rules = line.split("{")[1][:-1].split(",")
        
        ruleset = []
        for rule in (_rules[:-1]):
            opandrule = rule.split(":")[0]
            letter = opandrule[0]
            op = opandrule[1]
            amt = int(opandrule[2:])
            nrule = rule.split(":")[1]
            ruleset.append([letter, op, amt, nrule])

        ruleset.append(["any", _rules[-1]])

        rules[label] = ruleset

accepted: List[Dict[str, int]] = []

for item in items:
    ruleLabel = "in"
    while True:
        if ruleLabel == "A": 
            accepted.append(item)
            break
        if ruleLabel == "R":
            break

        _rules = rules[ruleLabel]
        # go through each rules and check the condition
        for rule in _rules:
            letterRule = rule[0]
            if letterRule == "any":
                ruleLabel = rule[1]
                break

            op = rule[1]
            amount = rule[2]
            sendTo = rule[3]
            compAgainst = item[letterRule]
            passed = False
            if op == ">":
                if compAgainst > amount:
                    passed = True
            else: 
                if compAgainst < amount:
                    passed = True
            
            if passed:
                ruleLabel = sendTo
                break

p1sum = 0
for acpt in accepted:
    p1sum += sum(acpt.values())

### p2

acceptingRanges = []
def probability(ranges: dict, label):
    if label == "A" or label == "R": 
        if label == "A": acceptingRanges.append(ranges)
        return
    _rule = rules[label]

    for rule in _rule:
        if rule[0] == "any":
            probability(ranges, rule[1])
            break

        letter = rule[0]
        op = rule[1]
        limit = rule[2]
        nextLabel = rule[3]

        if op == "<":
            ## Check that we have any combinations that go that low
            lower = ranges[letter+"l"]
            if lower > limit: continue
            newRanges = deepcopy(ranges)
            # Set limit for remaining range
            ranges[letter+"l"] = limit
            newRanges[letter+"u"] = limit-1
            probability(newRanges, nextLabel)
        else:
            upper = ranges[letter+"u"]
            if upper < limit: continue
            newRanges = deepcopy(ranges)
            ranges[letter+"u"] = limit
            newRanges[letter+"l"] = limit +1 
            probability(newRanges, nextLabel)
             
srange = {"xu": 4000, "xl": 1, "mu": 4000, "ml": 1, "au": 4000, "al": 1, "su": 4000, "sl": 1}
probability(srange, "in")

p2sum = 0

for range in acceptingRanges:
    xu = range["xu"] +1
    xl = range["xl"] 
    mu = range["mu"] +1
    ml = range["ml"]
    au = range["au"] +1
    al = range["al"]
    su = range["su"] +1 
    sl = range["sl"]

    x = xu - xl
    m = mu - ml
    a = au - al
    s = su - sl

    p2sum += (x * m * a * s)

print("Part 1:", p1sum, "Part 2:", p2sum)
