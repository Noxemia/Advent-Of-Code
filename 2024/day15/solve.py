smap = []
smap2 = []
moves = []
cx, cy = 0,0
cx2, cy2 = 0,0
from copy import copy
for y, line in enumerate(open('input.txt', 'r').readlines()):
    if line == "\n": continue
    elif '#' in line: 
        line = [x for x in line.strip("\n")]
        nline = []
        for x in line:
            if x == "#":
                nline.append("#")
                nline.append("#")
            if x == "O":
                nline.append("[")
                nline.append("]")
            if x == ".":
                nline.append(".")
                nline.append(".")
            if x == "@":
                nline.append("@")
                nline.append(".")
        
        if '@' in line:
            cy = y
            cx = line.index('@')
            line[cx] = "."

        if '@' in nline:
            cy2 = y
            cx2 = nline.index('@')
            nline[cx2] = "."
            
        smap.append(line)
        smap2.append(nline)
            
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
            

### Recursivly try to find what boxes move other boxes and if they can move
### If any box fails we don't move any box
### If we can move all boxes we return a list where all the boxes will end up
def tryPushVert(px, py, dx, dy, first):
    global smap2
    canPush = False
    toBePushed = []
    nx, ny = px+dx, py+dy
    if smap2[ny][nx] == ".":
        canPush = True
        toBePushed.append((px, py, nx, ny))
    elif smap2[ny][nx] == "#":
        return (False, [])
    else:
        res = tryPushVert(px, py+dy, dx, dy, True)
        if res[0] == False:
            return (False, [])
        else:
            canPush = True
            toBePushed.append((px, py, nx, ny))
            toBePushed = toBePushed + res[1]
    
    if first:
        snx = 0
        if smap2[py][px] == "]": snx = -1
        else: snx = 1
        res = tryPushVert(px+snx, py, dx, dy, False)
        if res[0] == False:
            return (False, [])
        else:
            return (True, toBePushed+res[1])
    return (canPush, toBePushed)
    
### Look left or right until we meet an obstacle on an empty space and then write in how we moved the boxes
def tryPushHori(px, py, dx, dy):
    global smap2
    canMove = False
    lx, ly = px+dx, py+dy
    
    while True:
        if smap2[ly][lx] == ".":
            canMove = True
            break
        elif smap2[ly][lx] == "#":
            return False
        lx, ly = lx+dx, ly+dy
        
    if canMove:
        smap2[py][px] = "."
        if dx == -1:
            for ux in range(lx, px, 2):
                smap2[py][ux] = "["
                smap2[py][ux+1] = "]"
        else:
            for ux in range(px+1, lx, 2):
                smap2[py][ux] = "["
                smap2[py][ux+1] = "]"
    return True    

for c in moves:
    ### For each direction we look one ahead,   if its an obstacle we dont move
    ###                                         if its a box we try to move it, if we can we move ourselves also
    ###                                         if its an empty space we move there
    toBeWritten = []
    if c == "<":
        nextPlace = smap2[cy2][cx2-1]
        if nextPlace == "#":
            pass
        elif nextPlace == ".":
             cx2 -= 1
        else:
            res = tryPushHori(cx2-1, cy2, -1, 0)
            if res: cx2 -= 1
            
    if c == ">":
        nextPlace = smap2[cy2][cx2+1]
        if nextPlace == "#":
            pass
        elif nextPlace == ".":
             cx2 += 1
        else:
            res = tryPushHori(cx2+1, cy2, 1, 0)
            if res: cx2 += 1
            
    if c == "^":
        nextPlace = smap2[cy2-1][cx2]
        if nextPlace == "#":
            pass
        elif nextPlace == ".":
             cy2 -= 1
        else:
            res = tryPushVert(cx2, cy2-1, 0, -1, True)
            if res[0]:
                ### Old X and new X
                ### For every box to be moved we read their current str on the map and save it together with the new coordinate
                ### And then we overwrite all the coordinates with empty spaces
                for ox, oy, nx, ny in res[1]:
                    toBeWritten.append((nx, ny, copy(smap2[oy][ox])))
                for ox, oy, nx, ny in res[1]:
                    smap2[oy][ox] = "."
                cy2 -= 1
                
    if c == "v":
        nextPlace = smap2[cy2+1][cx2]
        if nextPlace == "#":
            pass
        elif nextPlace == ".":
             cy2 += 1
        else:
            res = tryPushVert(cx2, cy2+1, 0, 1, True)
            if res[0]:
                for ox, oy, nx, ny in res[1]:
                    toBeWritten.append((nx, ny, copy(smap2[oy][ox])))
                for ox, oy, nx, ny in res[1]:
                    smap2[oy][ox] = "."
                cy2 += 1
    ### Here we write the new coordinates of where to save the boxes
    for x, y, nc in toBeWritten:
        smap2[y][x] = nc              
            
for c in moves:
    walk(c)
    
part1 = 0
for y, row in enumerate(smap):
    for x, c in enumerate(row):
        if c == "O": part1 += 100*y + x
        
part2 = 0
for y, row in enumerate(smap2):
    for x,c in enumerate(row):
        if c == "[": part2 += 100*y +x 
        
print(part1, part2)