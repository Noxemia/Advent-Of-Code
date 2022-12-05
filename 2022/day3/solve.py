import time
start_time = time.time()
data = []
data2 = []
data3 = []

def getletterval(letter: str) -> int:
	letter = ord(letter)
	if letter >= 97:
		return letter - 96
	else:
		return letter - 64 + 26


file = open('input.txt', 'r')

for line in file.readlines():
	line = line.strip("\n") 
	data2.append(line)
	tmp = [None] * 56
	for char in line:
		tmp[getletterval(char)] = 1
	data3.append(tmp)
	tmp = []
	tmp.append(line[:len(line)//2])
	tmp.append(line[len(line)//2:])
	data.append(tmp)

count = 0
for line in data:
	for letter in line[0]:
		if letter in list(line[1]):
			count += getletterval(letter)
			break
print(f"Part 1:{count}")

count2 = 0
for i in range(0, len(data2), 3):
	for letter in data2[i]:
		if letter in data2[i+1] and letter in data2[i+2]:
			count2 += getletterval(letter)
			break
print(f"Part 2 O(n^3):{count2}")

count3 = 0
for i in range(0, len(data3), 3):
	for letter in data2[i]:
		tmpval = getletterval(letter)
		if data3[i+1][tmpval] != None and data3[i+2][tmpval] != None:
			count3 += tmpval
			break # ?

print(f"Part 2 O(n):{count2}")


print("--- %s seconds ---" % (time.time() - start_time))


