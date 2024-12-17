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
         
def op0(op: int):
    global rega, regb, regc
    rega = rega // int(math.pow(2,op))
        
def op1(op: int):
    global rega, regb, regc
    tmp = regb ^ op
    regb = tmp
    
def op2(op: int):
    global rega, regb, regc
    regb = op % 8
    
def op3(op: int):
    global rega, regb, regc, ip
    if rega != 0:
        ip = op
        return False
    return True

def op4(op: int):
    global rega, regb, regc
    tmp = regb ^ regc
    regb = tmp
    
def op5(op: int):
    global rega, regb, regc, out
    out.append(op % 8)
    
def op6(op: int):
    global rega, regb, regc
    regb = rega // int(math.pow(2,op))
    
def op7(op: int):
    global rega, regb, regc
    regc = rega // int(math.pow(2,op))
    
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

def tryInitValue(init_val:int ):
    global rega, regb, regc, instructions, out
    ip = 0
    rega = init_val
    regb = 0
    regc = 0
    out = []
    while ip <= len(instructions)-1:
        for i, c in enumerate(out):
            
            if c != instructions[i]: 
                print("break")
                return False

        inc = True
        instr = instructions[ip]
        opfield = instructions[ip+1]
        if instr == 0: 
            op0(getCombo(opfield))
        elif instr == 1: 
            op1(opfield)
        elif instr == 2: 
            op2(getCombo(opfield))
        elif instr == 3:
            inc = op3(opfield)
        elif instr == 4: 
            op4(0)
        elif instr == 5: 
            op5(getCombo(opfield))
        elif instr == 6: 
            op6(getCombo(opfield))
        elif instr == 7: 
            op7(getCombo(opfield))
        if inc: ip+=2
    print(out)
    if len(out) == len(instructions):
        return True
    else:
        return False

print(tryInitValue(117440))
print(out)
for i in range(117430, 117445):
    break
    if tryInitValue(i): 
        print(i)
        print(out)
        break