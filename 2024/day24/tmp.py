from copy import deepcopy
registers = dict()
rules = []

for line in open('input.txt', 'r').readlines():
    line = line.strip("\n")
    if ':' in line:
        lsplit = line.split(':')
        reg, val = lsplit[0], int(lsplit[1])
        registers[reg] = val
    if '->' in line:
        lsplit = line.split(' ')
        rules.append((lsplit[0], lsplit[1], lsplit[2], lsplit[4]))

ogRegisters = deepcopy(registers) 
def solve(rules, registers):
    while True:
        anyUpdates = False
        for l, op, r, resreg in rules:
            ### Skip the ones we don't know
            if l not in registers or r not in registers: continue
            lval = registers[l]
            rval = registers[r]
            ### Do calc
            newRes = 0
            if op == 'OR':
                newRes = lval | rval
            if op == 'AND':
                newRes = lval & rval
            if op == 'XOR':
                newRes = lval ^ rval

            ### if no value written add the register
            if resreg not in registers:
                registers[resreg] = newRes
                anyUpdates = True
            ### if the value is different update it
            elif registers[resreg] != newRes:
                registers[resreg] = newRes
                anyUpdates = True 

            ### break loop if no updates
        if not anyUpdates:
            break
    
    bits = []
    for key in sorted(registers.keys()):
        if key[0] == 'z':
            bits.insert(0, str(registers[key]))

    bits = "".join(bits)
    bitsval = int(bits, 2)
    return bitsval

bitsval = solve(rules, registers)
print(bitsval)
#### Part 2

xbits = []
for key in sorted(registers.keys()):
    if key[0] == 'x':
        xbits.insert(0, str(registers[key]))

ybits = []
for key in sorted(registers.keys()):
    if key[0] == 'y':
        ybits.insert(0, str(registers[key]))
        
xbits = "".join(xbits)
xbitsval = int(xbits, 2)
ybits = "".join(ybits)
ybitsval = int(ybits, 2)

xyres = xbitsval + ybitsval
print(xbitsval, ybitsval, xyres)
print(bin(xyres))
print(bin(bitsval))

resregs = set()
    
xyresstr = str(bin(xyres))[2:]
ansstr = str(bin(bitsval))[2:]

goodIndices = []

for i in range(len(ansstr)):
    if xyresstr[i] == ansstr[i]:
        goodIndices.append(i)
        
print(goodIndices)

        
canSwap = []

for a, (l1, op1, r1, reg1) in enumerate(rules):
    for b, (l2, op2, r2, reg2) in enumerate(rules):
        ### check that they dont include each other
        if a == b: continue
        if reg2 == l1 or reg2 == r1 or reg2 == reg1: continue
        if reg1 == l2 or reg1 == l2: continue
        
        ### check which to pop first
        fp = 0
        sp = 0
        if b > a: 
            fp = b
            sp = a
        else:
            fp = a
            sp = b
            
        newRegister = deepcopy(ogRegisters)
        newRules = deepcopy(rules)
        newRules.pop(fp)
        newRules.pop(sp)
        
        newRules.append((l1, op1, r1, reg2))
        newRules.append((l2, op2, r2, reg1))
        
        res = solve(newRules, newRegister)
        resstr = str(bin(res))[2:]
        if len(resstr) != len(ansstr): continue
        passed = True
        for i in goodIndices:
            if resstr[i] != ansstr[i]:
                passed = False
                break
        
        if passed: canSwap.append((reg1, a, reg2, b))
        
print(len(canSwap))

for a, (l1, op1, r1, reg1) in enumerate(rules):
    for b, (l2, op2, r2, reg2) in enumerate(rules):
        ### check that they dont include each other
        if a == b: continue
        if reg2 == l1 or reg2 == r1 or reg2 == reg1: continue
        if reg1 == l2 or reg1 == l2: continue
        
        ### check which to pop first
        fp = 0
        sp = 0
        if b > a: 
            fp = b
            sp = a
        else:
            fp = a
            sp = b
            
        newRegister = deepcopy(ogRegisters)
        newRules = deepcopy(rules)
        newRules.pop(fp)
        newRules.pop(sp)
        
        newRules.append((l1, op1, r1, reg2))
        newRules.append((l2, op2, r2, reg1))
        
        res = solve(newRules, newRegister)
        resstr = str(bin(res))[2:]
        if len(resstr) != len(ansstr): continue
        passed = True
        for i in goodIndices:
            if resstr[i] != ansstr[i]:
                passed = False
                break
        
        if passed: canSwap.append((reg1, reg2))
        
        