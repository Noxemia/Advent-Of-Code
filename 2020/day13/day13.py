
data = []

with open("day13input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

data1 = data[:]
data2 = data[:]


timer = int(data1[0])
times = []

splittedData = data1[1].split(",")
for elem in splittedData:
    if elem != "x":
        times.append(int(elem))


res = []

for interval in times:
    counter = 0
    while counter < timer:
        counter += interval
    res.append(counter)

index = 0
minIndex = 0
compare = 10000000000000
for time in res:
    if time < compare:
        compare = time
        minIndex = index
    index += 1

#print((res[minIndex] - timer) * times[minIndex])


#PART 2

busses = [] ## The number of the busses
differencesInTime = []

splittedData = data2[1].split(",")
for elem in splittedData:
    if elem != "x":
        busses.append(int(elem))

for x, elem in enumerate(splittedData):
    if elem == "x":
        continue
    differencesInTime.append(x)


## To compensate for each row to the same answer we use a + k ≡ b + k (mod n)
## since a + k is the timestamp and we are looking for the next ones over we can assume k to be the difference in minutes in the input
## we adjust for this difference on the RHS by removing the difference
for i, _ in enumerate(differencesInTime):
    differencesInTime[i] = busses[i] - differencesInTime[i]

## Buss timing intervals are the mods
## Difference between time that busses leave are the remainders

M = 1 # Product of all moduli
for elem in busses:
    M *= elem

## Mod inverse by definition by some website when GCD is 1, why? idk :')
def modinv(n, mod):
    return pow(n, mod-2, mod)

## Algorithm taken of wikipedia for CRT
sum = 0
for i, m_i in enumerate(busses):
    a_i = differencesInTime[i]
    b_i = M // (m_i ) 

    binv_i = modinv(b_i,(m_i))
    sum += a_i*b_i*binv_i

## I assume the % M is to get the lowest possible answer since many should be available
print(sum % M)