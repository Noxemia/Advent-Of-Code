data = []

for line in open('input.txt', 'r').readlines():
    data.append([x for x in line.strip("\n")] + ["L"])

data.append(["L"*len(data[2])])

part1, part2 = 0, 0

def checkXmas(ry, rx):
    global data, part1
    try:
        st = [data[ny][nx] for ny, nx in zip(ry, rx)]
        if "".join(st) == "XMAS": part1 +=1
    except: pass

for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == "X": 
            checkXmas(range(y, y-4, -1), [x]*4)             ### look up
            checkXmas(range(y, y-4, -1), range(x, x+4))     ### look diag up right
            checkXmas([y]*4, range(x, x+4))                 ### look right
            checkXmas(range(y, y+4), range(x, x+4))         ### look diag down right
            checkXmas(range(y, y+4), [x]*4)                 ### look down
            checkXmas(range(y, y+4), range(x, x-4, -1))     ### look down left
            checkXmas([y]*4, range(x, x-4,-1))              ### look left
            checkXmas(range(y, y-4, -1), range(x, x-4, -1)) ### look up left

        if c == "A": 
            try:
                ld = sorted([data[y-1][x-1]] + [data[y+1][x+1]])
                rd = sorted([data[y-1][x+1]] + [data[y+1][x-1]])

                if ld == ["M", "S"] and rd == ["M", "S"]:
                    part2 +=1
            except:pass

print("Part 1:", part1, "\nPart 2:", part2)