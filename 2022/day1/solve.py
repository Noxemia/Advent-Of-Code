data = []

file = open("input.txt", "r")

for line in file.readlines():
    if line == "\n":
        data.append("-")
    else:
       data.append(int(line[:-1]))

cals = []
cnt = 0
for elem in data:
    if elem == "-":
        cals.append(cnt)
        cnt = 0
    else:
        cnt += elem

cals = sorted(cals, reverse=True)
print(f"Answer 1: {cals[0]}") 
print(f"Answer 2: {sum(cals[0:3])}") 