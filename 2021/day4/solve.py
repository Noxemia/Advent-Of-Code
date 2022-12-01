data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        if line == "":
            continue
        data.append(line)

numbers = data.pop(0)
numbers = str.split(numbers, ",")
for i, number in enumerate(numbers):
    numbers[i] = int(numbers[i])

#construct boards [[[]]]
boards = []



board = 0
tmp = []
for i, line in enumerate(data):
    #print(line)
    vals = str.split(line)
    row = []
    for val in vals:
        row.append(int(val))
    if i % 5 == 0:
        boards.append(tmp)
        tmp = []
    tmp.append(row)

# add last board stored in tmp   
boards.append(tmp)
boards.pop(0)

# copy the board - uneccessary :)
boardscopy = []

for board in boards:
    boardscopy.append([])

for board in boardscopy:
    
    for i in range(5):
        board.append([])
        for _ in range(5):
            board[i].append(0)
            
for i, board in enumerate(boardscopy):
        for j, row in enumerate(board):
            for k, val in enumerate(row):
                boardscopy[i][j][k] = boards[i][j][k]     

#print(boardscopy)

#print(data, "\n", boards, "\n", len(boards))

#win checking

winneri = None
winnerrow = None
winnercol = False

def checkrow(row):
    win = True
    for val in row:
        if val != -1:
            win = False
    return win



def checkwin(board):
    global winnercol, winnerrow
    for i, row in enumerate(board):
        if checkrow(row):
            winnerrow = i
            return True

    # columns into rows
    cols = []
    col = []
    for i in range(len(board)):
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        cols.append(col)

    for i, row in enumerate(cols):
        if checkrow(row):
            winnerrow = i
            winnercol = True
            return True

    return False

def checkall():
    global winneri
    for i, board in enumerate(boards):
        if checkwin(board):
            winneri = i
            return True
    return False

# test
#for i in range(5):
#    boards[0][0][i] = -1

#for i in range(5):
#    boards[0][i][0] = -1

def updateboards(number, boards):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, val in enumerate(row):
                if val == number:
                    boards[i][j][k] = -1


winningnumber = 0
print(boards)
for number in numbers:
    updateboards(number, boards)
    if checkall():
        #print("Someone won on: ", number, "! Winner is: ", boards[winneri], " with winning row: ", winnerrow)
        winningnumber = number
        #break - p1
        boards.pop(winneri)

# lol then just calculate by hand 4head


for number in numbers:
    updateboards(number, boardscopy)
    for i, board in enumerate(boardscopy):
        if checkwin(board):
            boardscopy.pop(i)
            print(board, number)

