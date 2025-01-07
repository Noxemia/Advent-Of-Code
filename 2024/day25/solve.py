locks = []
keys = []
tmp = []
for line in open('input.txt', 'r').readlines():
    if line == "\n":
        ### lock
        if all(x == '#' for x in tmp[0]):
            lock = []
            key = []
            for x in range(len(tmp[0])):
                stackHashtags = 0
                for y in range(len(tmp)):
                    if tmp[y][x] == '#': stackHashtags += 1
                lock.append(stackHashtags-1)
                key.append(len(tmp) - stackHashtags -1)
            locks.append(lock)
            #keys.append(key)
            #print("key", key)
        else:
            lock = []
            key = []
            for x in range(len(tmp[0])):
                stackHashtags = 0
                for y in range(len(tmp)):
                    if tmp[y][x] == '#': stackHashtags += 1
                key.append(stackHashtags-1)
                lock.append(len(tmp) - stackHashtags -1)
            #locks.append(lock)
            keys.append(key)
            #print("lock", lock)
            
        tmp = []
    else:
        tmp.append(line.strip("\n"))
        
        
part1 = 0
for lock in locks:
    for key in keys:
        # if lockstack is 0 keystack can be 5 or less than 5
        # if lockstack is 1 keystack can be 4
        # if lockstack is 2 keystack can be 3
        # if lockstack is 3 keystack can be 2
        # if lockstack is 4 keystack can be 1
        # if lockstack is 5 keystack can be 0
        if all(k + l <= 5 for l,k in zip(lock, key)): part1 += 1
        
print(part1)