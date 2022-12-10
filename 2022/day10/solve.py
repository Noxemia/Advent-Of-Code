data = []

for line in open('input.txt', 'r').readlines():
	if line[0] == "n":
		data.append([line])
	else:
		spl = line.split(" ")
		data.append([spl[0], int(spl[1])])

register = 1
cycle = 0
startofnext = 0
out = []
mods = [20, 60, 100, 140, 180, 220]

for line in data:
	if cycle in mods:
		out.append([cycle, register])
	if cycle == 221:
		break

	if startofnext != 0:
		register += startofnext
		startofnext = 0

	if line[0][0] == "n":
		cycle += 1 
		continue
	else:
		cycle += 1
		if cycle in mods:
			out.append([cycle, register])
		cycle += 1
		startofnext = line[1]

outsum = [x[0]*x[1] for x in out]

print(sum(outsum))

register = 1
screen = []
crtrow = ["."]*40
cycle = 0
command = data[0]
ci = 0
delayadd = 0
delay = False
screenmods = [40, 80, 120, 160, 200, 240]
drawcnt = 0
while True:
	cycle += 1
	if cycle in screenmods:
		screen.append(crtrow)
		crtrow = ["."]*40
	if cycle == 240: break
	pixelindex = (cycle-1) % 40
	if pixelindex in [register-1, register, register+1]:
		drawcnt += 1
		crtrow[pixelindex] = "#"
	if delay:
		register += delayadd
		delay = False
		ci += 1
		command = data[ci]
		continue
	if command[0][0] == "n":
		ci += 1
		command = data[ci]
		continue
	else:
		delayadd = command[1]
		delay = True

for line in screen:
	for i in range(len(line)):
		if (i+1) % 5 == 0:
			line[i] = "\t"
	print("".join(line))



