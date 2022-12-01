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

res = 0

for arr in output:
    for val in arr:
        if len(val) == 2 or len(val) == 3 or len(val) == 4 or len(val) == 7:
            res += 1

alpha = ["a","b","c","d","e","f","g",]



def findsegments(arr, out):
    one = None
    four = None
    seven = None
    eight = None
    sixzeronine = ""
    twothreefive = ""
    for string in arr:
        if len(string) == 2:
            one = string
        if len(string) == 4:
            four = string
        if len(string) == 3:
            seven = string
        if len(string) == 7:
            eight = string
        if len(string) == 6:
            sixzeronine += string
        if len(string) == 5:
            twothreefive += string
    #print(sixzeronine)
    ### Find top segment
    top = None
    for c in seven:
        if not c in one:
            top = c
    ### bottomleft & bottom
    bottomleft = None
    bottom = None
    neweight = []
    for c in eight:
        neweight.append(c)
    neweight.remove(top)
    for c in four:
        neweight.remove(c)
    bottoms = [0,0]
    for i, c in enumerate(neweight):
        res = 0
        for c2 in sixzeronine:
            if c == c2:
                res += 1
        bottoms[i] = res
    if bottoms[0] > bottoms[1]:
        bottomleft = neweight[1]
        bottom = neweight[0]
    else:
        bottomleft = neweight[0]
        bottom = neweight[1]
    #print(top,bottomleft, bottom)
    #### top right and top left and middle
    threefive = ""
    mid = None
    topright = None
    topleft = None
    bottomright = None
    for string in arr:
        if len(string) == 5 and not bottomleft in string:
            threefive += string
    threefivearr = []
    for c in threefive:
        threefivearr.append(c)
    threefivearr = list(filter(lambda c: c != bottom, threefivearr))
    threefivearr = list(filter(lambda c: c != top, threefivearr))
    #print(threefivearr)
    midandtopleft = threefivearr.copy()
    for ch in seven:
        midandtopleft = list(filter(lambda c: c != ch, midandtopleft))
    #print(midandtopleft, threefivearr)
    res = [0,0]
    for i,c in enumerate(list(dict.fromkeys(midandtopleft))):
        for ch in midandtopleft:
            if ch == c:
                res[i] +=1
    if res[0] > res[1]:
        mid = list(dict.fromkeys(midandtopleft))[0]
        topleft = list(dict.fromkeys(midandtopleft))[1]
   
    toprightandbotright = list(filter(lambda val: not (val == mid or val == topleft), threefivearr))
    res = [0,0]
    for i,c in enumerate(list(dict.fromkeys(toprightandbotright))):
        for ch in toprightandbotright:
            if ch == c:
                res[i] +=1
    if res[0] > res[1]:
        topright = list(dict.fromkeys(toprightandbotright))[1]
        bottomright = list(dict.fromkeys(toprightandbotright))[0]
    print(top,bottomleft, bottom, mid, topleft, topright, bottomright)
    
    #print(out, "xd")

    res = []
    i = 0
    for output in out:
        ### for definableby length
        #print(output)
        
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
        elif top in output and topleft in output and mid in output and bottomright in output and bottom in output and not topright in output:
            res.append(5)
        elif top in output and topright in output and mid in output and bottomright in output and bottom in output and not topleft in output:
            #print("added three on: ", output)
            res.append(3)
        elif top in output and topleft in output and mid in output and bottom in output and bottomright in output and bottomright in output and not topright in output:
            res.append(6)
        elif top in output and topleft in output and mid in output and bottom in output and bottomright in output and topright in output :
            res.append(9)
        elif top in output and topleft in output and mid in output and bottom in output and bottomright in output and topright in output and bottomright in output:
            res.append(0)
        else:
            
            print("Fucking panic boys", i, output, )
        i+=1
    strres = ""
    for c in res:
        strres += str(c)
    print(strres)
    





test2 = "abc"
test3 = "b"
#print(test3 in test2)

test = input[0]
for i in range(len(input)):
    findsegments(input[i], output[i])
