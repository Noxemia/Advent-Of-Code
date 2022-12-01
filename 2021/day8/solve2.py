data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

output = []
input = []

test = [data[0]]
for val in data:
    tmpout = []
    tmpin = []
    delimsplit = str.split(val, "|")
    for var in str.split(delimsplit[0]):
        tmpin.append(var)
    for var in str.split(delimsplit[1]):
        tmpout.append(var) 

    output.append(tmpout)
    input.append(tmpin)


def findsegments(arr, out):
    top = None
    topleft = None
    topright = None
    mid = None
    bottomleft = None
    bottomright = None
    bottom = None

    one = list(filter(lambda val: len(val) == 2, arr))[0]
    seven = list(filter(lambda val: len(val) == 3, arr))[0]
    four = list(filter(lambda val: len(val) == 4, arr))[0]
    eight = list(filter(lambda val: len(val) == 7, arr))[0]
    top = list(filter(lambda c: c not in one, seven))[0]
    bottomandbottomleft = list(filter(lambda c: c not in four and c not in seven, eight))
    twothreefive = list(filter(lambda val: len(val) == 5, arr))
    ttfstr = ""
    for elem in twothreefive:
        ttfstr += elem
    ttfbots = list(filter(lambda c: c ==  bottomandbottomleft[0] or c == bottomandbottomleft[1], ttfstr))
    tftcnt = [0,0]
    tftres = list(dict.fromkeys(ttfbots))
    for i, val in enumerate(tftres):
        for c in ttfbots:
            if val == c:
                tftcnt[i] +=1
    if tftcnt[0] > tftcnt[1]:
        bottom = tftres[0]
        bottomleft = tftres[1]
    else:
        bottom = tftres[1]
        bottomleft = tftres[0]
    #print(top, bottom, bottomleft)
    twothreefive = list(filter(lambda val: len(val) == 5, arr))
    ttfstr = ""
    for elem in twothreefive:
        ttfstr += elem
    ttfstr = list(filter(lambda c: c not in seven and c not in bottomleft and not c in bottom, ttfstr))
    #print(ttfstr)
    tftcnt = [0,0,0]
    for i,c in enumerate(list(dict.fromkeys(ttfstr))):
        for ch in ttfstr:
            if c == ch:
                tftcnt[i] +=1
    if tftcnt[0] > tftcnt[1] and tftcnt[0] > tftcnt[2]:
        mid = list(dict.fromkeys(ttfstr))[0]
    if tftcnt[1] > tftcnt[0] and tftcnt[1] > tftcnt[2]:
        mid = list(dict.fromkeys(ttfstr))[1]
    if tftcnt[2] > tftcnt[1] and tftcnt[2] > tftcnt[0]:
        mid = list(dict.fromkeys(ttfstr))[2]
    #print(tftcnt, "pog")
    topleft = list(filter(lambda c: c not in mid and c not in seven, four))[0]
    zerosixnine = list(filter(lambda val: len(val) == 6, arr))
    zsnres = []
    for elem in zerosixnine:
        zsnres.append(list(filter(lambda c: c not in top and c not in topleft and c not in mid and c not in bottomleft and c not in bottom, elem)))
    zsnstr = ""
    for elem in zsnres:
        for c in elem:
            zsnstr += c
    zsncnt = [0,0]
    #print(list(dict.fromkeys(zsnstr)))
    for i,c in enumerate(list(dict.fromkeys(zsnstr))):
        for ch in zsnstr:
            if ch == c:
                zsncnt[i] +=1
    if zsncnt[0] > zsncnt[1]:
        topright = list(dict.fromkeys(zsnstr))[1]
        bottomright = list(dict.fromkeys(zsnstr))[0]
    else:
        topright = list(dict.fromkeys(zsnstr))[0]
        bottomright = list(dict.fromkeys(zsnstr))[1]
    #print(top, topleft, topright, mid, bottomleft, bottomright, bottom)

    res = []
    i = 0
    for output in out:
        ### for definableby length
        #print(output)
        #print(top, topleft, mid, bottom, bottomright, bottom)
        if len(output) == 2:
            res.append(1)
        elif len(output) == 3:
            res.append(7)
        elif len(output) == 4:
            res.append(4)
        elif len(output) == 7:
            res.append(8)
        elif top in output and topright in output and mid in output and bottomleft in output and bottom in output:
            res.append(2)
        elif top in output and topleft in output and mid in output and bottomright in output and bottom in output and not topright in output and not bottomleft in output:
            res.append(5)
        elif top in output and topright in output and mid in output and bottomright in output and bottom in output and not topleft in output:
            res.append(3)
        elif top in output and topleft in output and mid in output and bottom in output and bottomright in output and bottomright in output and not topright in output:
            res.append(6)
        elif top in output and topleft in output and mid in output and bottom in output and bottomright in output and topright in output :
            res.append(9)
        else:
            res.append(0)
        i+=1
    strres = ""
    for c in res:
        strres += str(c)
    return int(strres)

summation = 0
for i in range(len(output)):
    summation += findsegments(input[i], output[i])

print(summation)