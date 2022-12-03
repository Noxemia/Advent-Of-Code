data = []
data2 = []

file = open('input.txt', 'r')

for line in file.readlines():
	line = line.strip("\n") 
	data2.append(line)
	tmp = []
	tmp.append(line[:len(line)//2])
	tmp.append(line[len(line)//2:])
	data.append(tmp)

def getletterval(letter: str) -> int:
	letter = ord(letter)
	if letter >= 97:
		return letter - 96
	else:
		return letter - 64 + 26

count = 0
for line in data:
	for letter in line[0]:
		if letter in list(line[1]):
			count += getletterval(letter)
			break
print(f"Part 1:{count}")

count2 = 0
for i in range(0, len(data), 3):
	for letter in data2[i]:
		if letter in data2[i+1] and letter in data2[i+2]:
			count2 += getletterval(letter)
			break
print(f"Part 2:{count2}")




