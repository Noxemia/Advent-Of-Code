smap = []
moves = []
cx, cy = 0,0
for y, line in enumerate(open('input.txt', 'r').readlines()):
    if line == "\n": continue
    elif '#' in line: 
        line = [x for x in line.strip("\n")]
        if '@' in line:
            cy = y
            cx = line.index('@')
            
            line[cx] = "."
        smap.append(line)
            
    else:
        line = [x for x in line.strip("\n")]
        moves += line

def walk(dir: str):
    global cx, cy, smap
    directions = [(0, -1), (1,0), (0,1), (-1,0)]
    dx, dy = 0,0
    if dir == "^": dx, dy = directions[0]
    elif dir == ">": dx, dy = directions[1]
    elif dir == "v": dx, dy = directions[2]
    elif dir == "<": dx, dy = directions[3]
    else: print("Unknown direction")
    
    ### first check if there is nothing in the direction
    if smap[cy+dy][cx+dx] == ".":
        cx, cy = cx + dx, cy + dy
        return ## Move in that direction 
    elif smap[cy+dy][cx+dx] == "#":
        return ## Dont even move
    else:
        ### if we move into a builder we see if we can move the boulder
        ### if we can we just swap places with the boulder and the first empty spot
        canMove = False
        fbxi, fbyi = cx + dx, cy + dy
        lx, ly = cx + dx * 2, cy + dy * 2
        while True:
            if smap[ly][lx] == ".":
                canMove = True
                break
            elif smap[ly][lx] == "#":
                break
            else:
                lx, ly = lx + dx, ly + dy

        if canMove:
            smap[ly][lx] = "O"
            smap[fbyi][fbxi] = "."
            cx, cy = cx + dx, cy + dy
            
            
for c in moves:
    walk(c)
    #print(cx, cy, c)
    for row in smap:
        break
        print(row)
    
part1 = 0
for y, row in enumerate(smap):
    for x, c in enumerate(row):
        if c == "O": part1 += 100*y + x
        
print(part1)