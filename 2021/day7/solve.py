data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)
numbers = list(map(lambda x: int(x), str.split(data[0], ",")))
cords = []

for _ in range(max(numbers)+1):
    cords.append(0)

def fuelcost(cord, pos):
    cost = 0
    for i in range(abs(cord - pos)):
        cost += i+1
    return cost

for i in range(len(cords)):
    for num in numbers:
        cords[i] += fuelcost(i,num)
print(min(cords))
