data = []

for line in open('input.txt', 'r').readlines():
    line = line.strip("\n")
    line = [x for x in line]
    line.insert(0, "L")
    line.append("L")
    line = "".join(line)
    data.append([x for x in line])

data.insert(0, ["L"*len(data[2])])
data.insert(0, ["L"*len(data[2])])

count = 0

def checkXmas(ry, rx):
    global data, count
    try:
        st = []
        for ny, nx in zip(ry, rx):
            st.append(data[ny][nx])
        if "".join(st) == "XMAS":
            count +=1
    except: pass

for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c != "X": continue
        st = []
        ### look up
        try:
            st = []
            for ny in range(y, y-4, -1):
                st.append(data[ny][x])
            if "".join(st) == "XMAS":
                count +=1
        except: pass
        checkXmas()

        ### look diag up right
        try:
            st = []
            for ny, nx in zip(range(y, y-4, -1), range(x, x+4)):
                st.append(data[ny][nx])
            if "".join(st) == "XMAS":
                count += 1
        except: pass

        ### look right
        try:
            st = []
            for nx in range(x, x+4):
                st.append(data[y][nx])
            if "".join(st) == "XMAS":
                count +=1
        except: pass

        ### look diag down right
        try:
            st = []
            for ny, nx in zip(range(y, y+4), range(x, x+4)):
                st.append(data[ny][nx])
            if "".join(st) == "XMAS":
                count += 1
        except: pass

        ### look down

        try:
            st = []
            for ny in range(y, y+4):
                st.append(data[ny][x])
            if "".join(st) == "XMAS":
                count +=1
        except: pass

        ### look down left
        try:
            st = []
            for ny, nx in zip(range(y, y+4), range(x, x-4, -1)):
                st.append(data[ny][nx])
            if "".join(st) == "XMAS":
                count += 1
        except: pass

        ### look left
        try:
            st = []
            for nx in range(x, x-4,-1):
                st.append(data[y][nx])
            if "".join(st) == "XMAS":
                count +=1
        except: pass

        ### look up left
        try:
            st = []
            for ny , nx in zip(range(y, y-4, -1), range(x, x-4, -1)):
                st.append(data[ny][nx])
            if "".join(st) == "XMAS":
                count += 1
        except: pass

count2 = 0
for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c != "A": continue

        try:
            tl = [data[y-1][x-1]]
            tr = [data[y-1][x+1]]
            bl = [data[y+1][x-1]]
            br = [data[y+1][x+1]]

            ld = sorted(tl + br)
            rd = sorted(tr + bl)

            if ld == ["M", "S"] and rd == ["M", "S"]:
                count2 +=1

        except:pass



print(count)
print(count2)