data = []

for line in open('input.txt', 'r').readlines():
    data.append(int(line))
    
def mix(snum: int, val: int):
    return snum ^ val


def prune(snum: int):
    return snum % 16777216
    
def inc(snum: int):
    notedSeq = dict() ### sequence str to number
    sequence = []
    lastones = int(str(snum)[-1])
    
    for _ in range(0, 2000):
        val = snum * 64
        snum = mix(snum, val)
        snum = prune(snum)

        val = snum // 32
        snum = mix(snum, val)
        snum = prune(snum)

        val = snum * 2048
        snum = mix(snum, val)
        snum = prune(snum)
        
        ones = int(str(snum)[-1])
        diff = ones - lastones
        sequence.append(diff)
        lastones = ones

        if len(sequence) == 4:
            seqstr = ""
            
            for n in sequence:
                seqstr += str(n) + ','
            if seqstr not in notedSeq:
                notedSeq[seqstr] = ones
            sequence.pop(0)
    
    return (snum, notedSeq)
    

p1sum = 0
allKeys = set()
seqMaps = []
for n in data:

    tsnum, tns, = inc(n)
    p1sum += tsnum
    seqMaps.append(tns)
    for key in tns.keys():
        allKeys.add(key)
    

part2 = 0
part2seq = ""
for seq in allKeys:
    tmpsum = 0
    for seqmap in seqMaps:
        if seq in seqmap:
            tmpsum += seqmap[seq]
    if tmpsum > part2:
        part2 = tmpsum
        part2seq = seq
    tmpsum = 0
print(p1sum, part2, part2seq)
