data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(int(line))



prev = 0
ans = 0
print(data[0])

for depth in data:
    if prev < depth:
        ans = ans + 1
    prev = depth

print("p1:", ans)

ans2 = 0
for i in range(len(data)-3):
    #    A         A           A
    if data[i] + data[i+1] + data[i+2] <  data[i+1] + data[i+2] + data[i+3]:
        ans2 = ans2+1

print(ans2)
