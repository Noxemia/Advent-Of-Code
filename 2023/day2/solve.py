from typing import List
data = []

def parseGame(games: List[str]):
	res = [0,0,0]
	games = games.split(",")
	for color in games:
		color = color.strip(" ")
		amount = int(color.split(" ")[0])
		gameColor = color.split(" ")[1]
		if gameColor == "red": res[0] += amount
		if gameColor == "green": res[1] += amount
		if gameColor == "blue": res[2] += amount
	return res

def parse(string: str):
	res = []
	splitcolon = string.split(":")
	game = int(splitcolon[0].strip("Game "))
	rounds = [x.strip(" ") for x in splitcolon[1].split(";")]
	for round in rounds:
		res.append(parseGame(round))
	return [game, res]
	
for line in open('input.txt', 'r').readlines():
	data.append(line.strip("\n"))

#RGB
limits = [12,13,14]

def possibleGame(game):
	if game[0] > limits[0]: return False
	if game[1] > limits[1]: return False
	if game[2] > limits[2]: return False
	return True

## solve loop
correct = 0
power = 0
for line in data:
	gamesParse = parse(line)
	#p1
	if all([possibleGame(game) for game in gamesParse[1]]): correct += gamesParse[0]
	#p2
	maxRed = max([game[0] for game in gamesParse[1]])
	maxGreen = max([game[1] for game in gamesParse[1]])
	maxBlue = max([game[2] for game in gamesParse[1]])
	power += maxRed*maxGreen*maxBlue
		
print(correct, power)