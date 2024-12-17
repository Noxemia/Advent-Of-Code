import math
from copy import copy
rega = 0
regb = 0
regc = 0
instructions = []
out = []

for line in open('input.txt', 'r').readlines():
    if line == "\n": continue
    if line[0] == 'R':
        line1 = line.split(":")
        
        num = int(line1[1])
        line1 = line1[0].split(" ")[1]
        if line1 == "A":
            rega = num
        elif line1 == 'B':
            regb = num
        else:
            regc = num
    else:
        line = line.split(":")[1]
        instructions = [int(x) for x in line.split(",")]
    
def getCombo(op: int):
    global rega, regb, regc
    if op == 0: return 0
    elif op == 1: return 1
    elif op == 2: return 2
    elif op == 3: return 3
    elif op == 4: return copy(rega)
    elif op == 5: return copy(regb)
    elif op == 6: return copy(regc)
    elif op == 7: print("NOT ALLOWED")
    print("Wtf")

def tryAVal(val: int):
    global instructions
    ip = 0
    rega = val
    regb = 0
    regc = 0
    out = []
    
    while ip <= len(instructions)-1:
        inc = True
        instr = instructions[ip]
        op = instructions[ip+1]
        
        if instr == 0:
            rega = rega // 2**getCombo(op)
        elif instr == 1: 
            regb = regb ^ op
        elif instr == 2: 
            regb = getCombo(op) % 8
        elif instr == 3:
            if rega != 0:
                ip = op
                inc = False
        elif instr == 4: 
            regb = regb ^ regc
        elif instr == 5: 
            out.append(getCombo(op) % 8)
        elif instr == 6: 
            regb = rega // 2**getCombo(op)
        elif instr == 7: 
            regc = rega // 2**getCombo(op)
        if inc: ip+=2
    print(out)
    
tryAVal(729)

