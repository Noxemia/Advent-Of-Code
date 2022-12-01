data = []

with open("day14input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

testDec = 10
testBin = 0b0101
testArr = [0,1,2]

# OBSERVATIONS
# printing a binary number gets you its decimal representation
# You can add together decimal and binary numbers to get a decimal number
# Using binary numbers as index is allowed
# To get binary in text use str(bin(x))
# This languages is pog


#### Part1

## Memory
memory = [0] * 10000000
## init memory

## Current mask
mask = ""
## Current address
addr = 0
## Current binary value as string
value = ""

for elem in data:
    elemSplit = elem.split(" ")
    ## Check if second letter is a to check if mask
    if elem[1] == "a":
        mask = elemSplit[2]
        
    ## if not assume memory addressing
    else:
        ## Parse out memory adress
        addLength = len(elemSplit[0])-1
        addr = int(elemSplit[0][4:addLength])
        ## Parse out binary value as string
        tempVal = int(elemSplit[2])
        value = str(bin(tempVal))[2:]
        for x in range(len(mask) - len(value)):
            value = "0" + value
        ## Apply mask to value using for each in val to not get out of index
        indexCorretion = len(mask)-1
        for i, _ in enumerate(value):
            if mask[indexCorretion-i] != "X":
                value = value[0:indexCorretion-i] + mask[indexCorretion-i] + value[indexCorretion-i+1:]
        ## Print int value for val to memory address
        memory[addr] = int(value, 2)

## Compute total
total = 0
for val in memory:
    total += val

print("Part1:", total)



### part 2




## Function and global array to replace X:s with either 1 or one for all combinations recursivly
addrs = []
def traverseAddr(mask):
    
    foundX = False
    ## Recurse everytime we find an x and break out of the loop
    for i, char in enumerate(mask):
        if char == "X":
            foundX = True
            zeroMask = mask[0:i] + "0" + mask[i+1:]
            oneMask = mask[0:i] + "1" + mask[i+1:]
            traverseAddr(zeroMask)
            traverseAddr(oneMask)
            break
    ## if there are no x:s in the string add the finished addr to the global array
    if not foundX:
        addrs.append(mask)



### clear memory for part 2
memory = [[0,0]] * 1#00000 
memory2 = {}


## cant do 36bit adress space in python therefor we update cells depening on their given address and updates the values
## Wow imagine someone new to python and not knowing about dictionarys so they try to impement their own datastructure, which is comically slower than dicts :)
def updateMem(addr, val):
    #print(addr, value)
    for i, cell in enumerate(memory):
        if cell[0] == addr:
            memory[i] = [addr, val]
            return
        elif cell[0] == 0:
            memory[i] = [addr, val]
            return
                    



for elem in data:
    elemSplit = elem.split(" ")
    ## Check if second letter is a to check if mask
    if elem[1] == "a":
        mask = elemSplit[2]
    ## if not assume memory addressing
    else:
        ## Parse Value as int
        value = int(elemSplit[2])
        ## Parse address as binary string and extend to 36 chars
        addLength = len(elemSplit[0])-1
        tempAddr = int(elemSplit[0][4:addLength])
        addr = str(bin(tempAddr))[2:]
        for x in range(len(mask) - len(addr)):
            addr = "0" + addr
        ## Apply rules on addres
        for i, char in enumerate(mask):
            if char != "0":
                if char == "1":
                    addr = addr[0:i] + "1" + addr[i+1:] 
                if char == "X":
                    addr = addr[0:i] + "X" + addr[i+1:] 
        ## Create all addrs
        addrs = [] # reset global addrs
        traverseAddr(addr)
        
        for yeet in addrs:
            #updateMem(int(yeet, 2), value) #uncomment this for a fun time, also see line 92
            memory2[yeet] = value


total = 0
for cell in memory:
    total += cell[1]

ans = 0
for k,v in memory2.items():
    ans += v

print("Part2:", ans, total)
