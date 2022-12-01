data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

data = str.split(data[0],",")
fishes = []
for val in data:
    fishes.append(int(val))

def day(fishes=fishes):
    new = 0
    for i, _ in enumerate(fishes):
        fishes[i] -= 1
        #if fishes[i] == 0:
            
        if fishes[i] == -1:
            fishes[i] = 6
            new +=1

    for _ in range(new):
        fishes.append(8)
print(fishes)
test = [0,0,0,0,0,0,0,0,0]
for _ in range(80):
    None
    #day()
    #     #print(fishes)
for fish in fishes:
    test[fish] +=1
print(test)

#print(len(fishes))
fishtank = [0,0,0,0,0,0,0,0,0] 
#print(fishes)

#init
for val in fishes:
    fishtank[val] += 1

def day2():
    zero = fishtank[0]
    for i in range(len(fishtank)-1):
        print(i)
        fishtank[i] = fishtank[i+1]
    fishtank[8] = zero
    fishtank[6] += zero
        
for _ in range(256):
    day2()
    None
print(fishtank)
print(sum(fishtank))