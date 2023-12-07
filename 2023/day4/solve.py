cards = []

for line in open('input.txt', 'r').readlines():
	line=line.strip("\n")
	headingremoved = line.split(":")[1]
	cardNumber = int(line.split(":")[0].strip("Card "))

	winningNumbers = headingremoved.split("|")[0].strip(" ")
	winningNumbersSplit = winningNumbers.split(" ")
	winningNumbersParsed = []
	for number in winningNumbersSplit:
		if number != "":
			winningNumbersParsed.append(int(number))

	myNumbers = headingremoved.split("|")[1].strip(" ")
	myNumbersSplit = myNumbers.split(" ")
	myNumbersParsed = []
	for number in myNumbersSplit:
		if number != "":
			myNumbersParsed.append(int(number))

	cards.append([myNumbersParsed, winningNumbersParsed,cardNumber])

p1sum = 0
for card in cards:
	currentPoint = 0
	for myNumber in card[0]:
		if myNumber in card[1]:
			if currentPoint == 0:
				currentPoint = 1
			else:
				currentPoint *= 2
	p1sum += currentPoint

p2count = 0
cardpile = [] + cards



# index is the card number
# 
cache = []
for _ in range(0, len(cards) +2):
	cache.append(-1)

def solveCard(currentCard):
	cardNumber = currentCard[2]
	myNumbers = currentCard[0]
	winningNumbers = currentCard[1]

	if cache[cardNumber] != -1:
		return cache[cardNumber]
	
	countWins = 0
	for number in myNumbers:
		if number in winningNumbers:
			countWins +=1

	cardsToSearch = []
	for i in range(cardNumber, cardNumber+countWins):
		cardsToSearch.append(cards[i])

	total = 1
	for card in cardsToSearch:
		total += solveCard(card)

	cache[cardNumber] = total
	return total


for card in cardpile:
	p2count += solveCard(card)


print(p1sum, p2count)
