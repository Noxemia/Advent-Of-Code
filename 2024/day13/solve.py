data = []
tmp = []
for line in open('input.txt', 'r').readlines():
    if line == "\n": 
        data.append(tmp)
        tmp = []
        continue
    splitchr = "+" if "+" in line else "="
    line = line.split(":")[1]
    x = int(line.split(",")[0].split(splitchr)[1])
    y = int(line.split(",")[1].split(splitchr)[1])
    tmp.append((x,y))

data.append(tmp)

def solve(ax, ay, bx, by, tx, ty):
    ### Treat as    a-xdiff*apress + b-xdiff*bpress = x target
    ###             a-ydiff*apress + b-ydiff*bpress = y target
    ### Remove apress by cross multiplying the a deltas and then divide the difference
    ### between the new bigger targets and the difference with the b deltas
    nbx = bx*ay
    ntx = tx*ay
    
    nby = by*ax
    nty = ty*ax
    
    b = (nty - ntx) / (nby - nbx)
    a = (tx - bx*b) / ax
    return((a,b))

part1, part2 = 0, 0
for t in data:  
    ax = t[0][0]
    ay = t[0][1]
    bx = t[1][0]
    by = t[1][1]
    tx = t[2][0] 
    ty = t[2][1]
    a, b = solve(ax, ay, bx, by, tx, ty)
    if int(a) == a and int(b) == b:
        part1 += int(3*a + b)
    a, b = solve(ax, ay, bx, by, tx+10000000000000, ty+10000000000000)
    if int(a) == a and int(b) == b:
        part2 += int(3*a + b)
    
print(part1, part2)