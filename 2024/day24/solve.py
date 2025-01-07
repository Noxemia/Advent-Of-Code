from copy import deepcopy, copy
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
#### 

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


def findResRule(reg):
    for l, op, r, resreg in rules:
        if reg == resreg:
            slr = sorted([l,r])
            return (slr[0], slr[1])

oldValRegL, oldValRegR = findResRule('z01')
lastRegNumber = '01'
### check that correct registers are used
for i in range(2, 40):
    regstr = str(i)
    if len(regstr) == 1:
        regstr = '0' + regstr
    currentReg = 'z' + regstr
    # spt    #vjn
    valRegL, valRegR = findResRule(currentReg)
    try:
        # jnh    # qkj                #spt
        LExpand, RExpand = findResRule(valRegL)
        # rsq   # bdk               #jhn
        lcomp1, lcomp2 = findResRule(LExpand)
        rcomp1, rcomp2 = findResRule(RExpand)
    except:
                # jnh    # qkj                #spt
        LExpand, RExpand = findResRule(valRegR)
        # rsq   # bdk               #jhn
        lcomp1, lcomp2 = findResRule(RExpand)
        rcomp1, rcomp2 = findResRule(LExpand)
    #### ASSERT any order
    compListNew = [lcomp1, lcomp2, rcomp1, rcomp2]
    complistOld = [oldValRegL, oldValRegR, 'x'+lastRegNumber, 'y'+lastRegNumber]
    if not sorted(compListNew) == sorted(complistOld):
        print((lcomp1, lcomp2), "-", (oldValRegL, oldValRegR))
        print(('y'+lastRegNumber, 'x'+lastRegNumber), "-", (rcomp1, rcomp2))
        print("Error on", currentReg)
        
    oldValRegL, oldValRegR = valRegL, valRegR
    lastRegNumber = currentReg[1:]

xd = sorted(["hmk", "z16", "z20", "fhp", "tpc", "rvf", "z33", "fcd"])
xd = "".join([x+"," for x in xd])
print(xd[:-1])