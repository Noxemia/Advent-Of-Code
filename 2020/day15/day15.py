import time

data = [16,12,1,0,15,7,11]

#with open("day12input.txt", "r") as reader:
#    for line in reader:
#        line = line.strip()
#        data.append(line)

memory = {}




for i, elem in enumerate(data):
    memory[elem] = i+1


## Start at the turn after the starting numbers
## Since the first turn after the intial rounds will always be someone saying zero we skip that round 
## and assume that the last number said was 0
startIndex = len(memory) + 2

start = time.time()
lastNumber = 0
for turnIndex in range(startIndex, 30000001):
    if lastNumber in memory.keys():
        thisRoundsNumber = turnIndex - 1 - memory[lastNumber]
    else:
        thisRoundsNumber = 0

    memory[lastNumber] = turnIndex-1
    lastNumber = thisRoundsNumber
print(lastNumber)
end = time.time()
print(end-start)

#print(max(memory.keys()))
#print(min(memory.keys()))