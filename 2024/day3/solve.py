data = ""

for line in open('input.txt', 'r').readlines():
    data += line

data = [x for x in data]
tot = 0
enabled = True
for i, c in enumerate(data):
    dnt = "".join(data[i:i+7])
    print(dnt)
    if dnt == "don't()":
        enabled = False
    do = "".join(data[i:i+4])
    if do == "do()": 
        enabled = True



    try:
        cons = "".join(data[i:i+4])

        ## Check for mul(
        if cons != "mul(": 
            continue

        ## look for and )
        iparen = 0
        for ii, cc in enumerate(data[i+4:i+13]):
            if cc == ')':
                iparen = i + ii + 4
                break
                
        print(iparen)
        if iparen == 0: continue
        
        nums = "".join(data[i+4:iparen])
        nums = nums.split(",")
        f = int(nums[0])
        s = int(nums[1])
        if enabled: 
            tot += f*s
        print("###", f,s)
    except:
        pass
print(tot)