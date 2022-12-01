
data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

command = []
value = []



for line in data:
    val = str.split(line)
    command.append(val[0])
    value.append(int(val[1]))

forward = 0
depth = 0
print(command[0][0])

for i in range(len(command)):
    if command[i][0] == "f":
        forward = forward + value[i]
    if command[i][0] == "d":
        depth = depth + value[i]
    if command[i][0] == "u":
        depth = depth - value[i]

print(depth * forward)

aim = 0
forward2 = 0
depth2 = 0

for i in range(len(command)):
    if command[i][0] == "f":
        forward2 = forward2 + value[i]
        depth2 = depth2 + (value[i] * aim)
    if command[i][0] == "d":
        aim = aim + value[i]
    if command[i][0] == "u":
        aim = aim - value[i]

print(depth2 * forward2)