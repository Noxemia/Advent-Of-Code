from copy import copy
instructions = []
out = []
part1input = 0

for line in open('input.txt', 'r').readlines():
    if line == "\n": continue
    elif "A:" in line:
        part1input = int(line.split(":")[1])
    else:
        line = line.split(":")[1]
        instructions = [int(x) for x in line.split(",")]
    
def getCombo(op: int, rega, regb, regc):
    if op == 0: return 0
    elif op == 1: return 1
    elif op == 2: return 2
    elif op == 3: return 3
    elif op == 4: return copy(rega)
    elif op == 5: return copy(regb)
    elif op == 6: return copy(regc)
    elif op == 7: 
        print("NOT ALLOWED")
        exit(0)

def tryAVal(val: int):
    global instructions
    ip = 0
    rega = val
    regb = 0
    regc = 0
    out = []
    while ip <= len(instructions)-1:
        instr = instructions[ip]
        op = instructions[ip+1]
        cop = getCombo(op, rega, regb, regc)
        
        if instr == 0:
            rega = rega // 2**cop
            
        elif instr == 1: 
            regb = regb ^ op
            
        elif instr == 2: 
            regb = cop % 8
            
        elif instr == 3:
            if rega != 0: ip = op-2
                
        elif instr == 4: 
            regb = regb ^ regc
            
        elif instr == 5: 
            out.append(cop % 8)
            
        elif instr == 6: 
            regb = rega // 2**cop
            
        elif instr == 7: 
            regc = rega // 2**cop
            
        ip+=2
    part1 = ""
    for n in out:
        part1 += f"{n},"
    part1 = part1[:-1]
    print(part1)
    
tryAVal(part1input)

def findByte(result, instructions):
    if len(instructions) == 0: return result
    comp = instructions[-1]
    for x in range(8):
        a = (result * 8) + x
        b = a % 8
        b = b ^ 3
        c = a // 2**b
        b = b ^ 5
        b = b ^ c
        o = b % 8
        if o == comp:
            res = findByte(a, instructions[:-1])
            if res != None: return res
            
        
print(findByte(0, instructions))
