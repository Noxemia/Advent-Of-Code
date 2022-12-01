import time

start = time.time()

data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

#print(data)

strcords = []
stillstr = True
folds = []
for line in data:
    if line == '':
        stillstr = False
        continue
    if stillstr:
        strcords.append(line)
    else:
        folds.append(line)

cords = []
for line in strcords:
    vals = str.split(line, ",")
    cords.append([int(vals[0]), int(vals[1])])
tmpfolds = []
for line in folds:
    spl = str.split(line)[2]
    vals = str.split(spl, "=")
    tmpfolds.append([vals[0], int(vals[1])])

folds = tmpfolds

paper = []

maxx = 0
maxy = 0
for cord in cords:
    if cord[0] > maxx: maxx = cord[0]
    if cord[1] > maxy: maxy = cord[1]

for y in range(maxy+1):
    tmp = []
    for x in range(maxx+1):
        tmp.append('.')
    paper.append(tmp)

def ppaper():
    for line in paper:
        tmp = " "
        for c in line:
            tmp += c
        print(tmp)

for cord in cords:
        paper[cord[1]][cord[0]] = '#'


def fold_horizontal(y):
    global paper
    upper = []
    tmplower = []
    for i, line in enumerate(paper):
        if i == y:
            continue
        if i < y:
            upper.append(line)
        if i > y:
            tmplower.append(line)
    lower = list(reversed(tmplower))
    if len(lower) >= len(upper):
        ymod = len(lower) - len(upper)
        for yi, row in enumerate(upper):
            for x, c in enumerate(row):
                if c == '#':
                    lower[yi+ymod][x] = '#'
        paper = lower
    else:
        ymod = len(upper) - len(lower)   
        for yi, row in enumerate(lower):
            for x, c in enumerate(row):
                if c == '#':
                    upper[yi+ymod][x] = '#'
        paper = upper

def fold_vertical(x):
    global paper
    leftside = []
    for line in paper:
        leftside.append(line[0:x])
    tmprightside = []
    rightside = []
    for line in paper:
        tmprightside.append(line[x+1:])
    for line in tmprightside:
        rightside.append(list(reversed(line)))
    if len(rightside[0]) >= len(leftside[0]):
        xmod = len(rightside[0]) - len(leftside[0])
        for r, line in enumerate(leftside):
            for i, c in enumerate(line):
                if c == '#':
                    rightside[r][i+xmod] = '#'
        paper = rightside
    else:
        xmod = len(leftside[0]) - len(rightside[0])
        for r, line in enumerate(rightside):
            for i, c in enumerate(line):
                if c == '#':
                    leftside[r][i+xmod] = '#'
        paper = leftside

#print(folds)

for fold in folds:
    if fold[0] == 'y':
       fold_horizontal(fold[1])
    else:
        fold_vertical(fold[1])

dotcnt = 0
for row in paper:
    for x in range(len(row)):
        if row[x] == '#':
            dotcnt += 1

ppaper()

print(time.time() - start)