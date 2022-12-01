data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

ans = []
for _ in range(len(line)):
    ans.append(0)

for i in range(len(line)):
    for line in data:
        if line[i] == "1":
            ans[i] = ans[i] + 1

gamma = ""
epsilon = ""
for i in range(len(ans)):
    if ans[i] > (len(data)/2):
        gamma += "1"
    else:
        gamma += "0"

for i in range(len(ans)):
    if ans[i] > (len(data)/2):
        epsilon += "0"
    else:
        epsilon += "1"


def tobin(numb):
    res = 0
    for i in range(len(epsilon)):
        if numb[len(numb)-i-1] == "1":
            res = res + 2**(i)
    return res


print(tobin(gamma) * tobin(epsilon))

# Part 2

oxygen = []
scrubber = []

for line in data:
    oxygen.append(line)
    scrubber.append(line)


index = 0
high = True


def filterCheck(line):
    if high:
        if line[index] == "1":
            return True
    else:
        if line[index] == "0":
            return True
    return False


def updateAns(list):
    for i in range(len(ans)):
        ans[i] = 0
    for i in range(len(ans)):
        for line in list:
            if line[i] == "1":
                ans[i] = ans[i] + 1


for i in range(len(ans)):

    if ans[i] >= float(len(oxygen))/float(2):
        high = True
    else:
        high = False

    oxygen = filter(filterCheck, oxygen)
    index += 1
    updateAns(oxygen)
    if len(oxygen) == 1:
        break

index = 0
high = True
updateAns(scrubber)
for i in range(len(ans)):
    if ans[i] >= float(len(scrubber))/float(2):
        high = False
    else:
        high = True

    scrubber = filter(filterCheck, scrubber)
    index += 1
    updateAns(scrubber)
    if len(scrubber) == 1:
        break

print(tobin(oxygen[0]) * tobin(scrubber[0]))
