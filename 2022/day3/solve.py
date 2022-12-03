data = []

file = open('input.txt', 'r')

for line in file.readlines():
	line = line.strip("\n") 
	tmp = []
	tmp.append(line[0:int((len(line)/2))])
	tmp.append(line[int((len(line)/2)):])
	data.append(tmp)

count = 0
for line in data:
	inboth = ''
	for letter in line[0]:
		if letter in list(line[1]):
			inboth = letter
			break
	val = ord(inboth)
	if val >= 97:
		count += val -96
	else:
		count += val - 64 + 26

print(f"Part 1:{count}")
count = 0

for i in range(0, len(data), 3):
	str1 = data[i][0] + data[i][1]
	str2 = data[i+1][0] + data[i+1][1]
	str3 = data[i+2][0] + data[i+2][1]
	inboth = ''
	for letter in str1:
		if letter in str2 and letter in str3:
			inboth = letter
			break
	val = ord(inboth)
	if val >= 97:
		count += val -96
	else:
		count += val - 64 + 26

print(f"Part 2:{count}")



