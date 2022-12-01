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

maxi = 0
max1 = 0

for i, elem in enumerate(cals):
    if elem > max1:
        max1 = elem
        maxi = i
print(f"Answer 1: {max1}")
cals.pop(maxi)

maxi = 0
max2 = 0

for i, elem in enumerate(cals):
    if elem > max2:
        max2 = elem
        maxi = i

cals.pop(maxi)

maxi = 0
max3 = 3

for i, elem in enumerate(cals):
    if elem > max3:
        max3 = elem
        maxi = i

print(f"Answer 2: {max1 + max2 +max3}") 