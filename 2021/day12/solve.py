import time
start = time.time()

data = []

with open("input.txt", "r") as reader:
    for line in reader:
        line = line.strip()
        data.append(line)

pathtouples = []

for line in data:
    spl = str.split(line, "-")
    pathtouples.append([spl[0], spl[1]])


nodes = []
for path in pathtouples:
    if not path[0] in nodes:
        nodes.append(path[0])
    if not path[1] in nodes:
        nodes.append(path[1])

paths = {}
for node in nodes:
    paths[node] = []

for path in pathtouples:
    klist = paths[path[0]]
    if path[1] != 'start': klist.append(path[1])
    klist = paths[path[1]]
    if path[0] != 'start': klist.append(path[0])

print(paths)

endcnt = 0
def walk(node: str, visited: list,):
    global endcnt
    if node == 'end':
        endcnt += 1
        return
    if not node.isupper():
        visited.append(node)
    neighbours = paths.get(node)
    for neighbour in neighbours:
        if neighbour in visited:
            continue
        walk(neighbour, visited.copy())

walk('start', [])
print(endcnt)

res = []

endcnt = 0
def walk2(node: str, visited: list, twice, path: list):
    global endcnt
    path.append(node)
    if node == 'end':
        res.append(path)
        endcnt += 1
        return
    if not node.isupper():
        visited.append(node)
    neighbours = paths.get(node)
    for neighbour in neighbours:
        if neighbour in visited:
            continue
        walk2(neighbour, visited.copy(), twice, path.copy())
        if not twice and not node.isupper():
            tvisited = visited.copy()
            tvisited.remove(node)
            walk2(neighbour, tvisited, True, path.copy())


walk2('start', [], False, [])

compressedpaths = []
for path in res:
    tmp = ""
    for cave in path:
        tmp += cave
    compressedpaths.append(tmp)

print(len(list(dict.fromkeys(compressedpaths))))

print(time.time() - start)




