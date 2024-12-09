from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Brick:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int
    letter: str
    supportedBy: List[str]
    supports: List[str]

bricks: List[Brick] = []
bricks2: List[Brick] = []

count = 0
for line in open('input.txt', 'r').readlines():
    for chr in [" ", ",", "~", "<", "-", "\n"]:
        line = line.replace(chr, "")
    bricks.append(Brick(int(line[0]), int(line[3]), int(line[1]), int(line[4]), int(line[2]), int(line[5]), str(count), [], []))
    count +=1

bricks = sorted(bricks, key=lambda x: x.z1)
totOccuped = set([])

def genOccupied(brick: Brick) -> list[str]:
    occupied = []
    if brick.x1 != brick.x2:
        for x in range(brick.x1, brick.x2+1):
            tx = f"{x},{brick.y1},{brick.z1}"
            occupied.append(tx)
    if brick.y1 != brick.y2:
        for y in range(brick.y1, brick.y2+1):
            tx = f"{brick.x1},{y},{brick.z1}"
            occupied.append(tx)
    if brick.z1 != brick.z2:
        for z in range(brick.z1, brick.z2+1):
            tx = f"{brick.x1},{brick.y1},{z}"
            occupied.append(tx)
    return occupied
    
def fall(brick: Brick):
    global totOccuped
    ## if at bottom
    if brick.z1 == 1 or brick.z2 == 1:
        occ =  genOccupied(brick)
        for g in occ:
            totOccuped.add(g)
        return

    brick.z1 = brick.z1 - 1
    brick.z2 = brick.z2 - 1

    ## gen coords
    occ = genOccupied(brick)
  
    ## check if colided
    if any([c in totOccuped for c in occ]):
        brick.z1 = brick.z1 + 1
        brick.z2 = brick.z2 + 1
        occ2 = genOccupied(brick)
        for g in occ2:
            totOccuped.add(g)
        return
    
    fall(brick)

for brick in bricks:

    fall(brick)    



bricks = list(reversed(bricks))

def genUnder(brick: Brick) -> List[str]:
    occupied = []
    if brick.x1 != brick.x2:
        for x in range(brick.x1, brick.x2+1):
            tx = f"{x},{brick.y1},{brick.z1-1}"
            occupied.append(tx)
    if brick.y1 != brick.y2:
        for y in range(brick.y1, brick.y2+1):
            tx = f"{brick.x1},{y},{brick.z1-1}"
            occupied.append(tx)
    if brick.z1 != brick.z2:
            tx = f"{brick.x1},{brick.y1},{brick.z1-1}"
            occupied.append(tx)
    return occupied

for i, brick in enumerate(bricks):
    ## for each brick look under and see what supports them
    under = genUnder(brick)

    ## look at bricks under
    for ubrick in bricks[i:]:
        if any([c in under for c in genOccupied(ubrick)]):
            brick.supportedBy.append(ubrick.letter)

bricks = list(reversed(bricks))

brickset: Dict[str, Brick] = {}

for brick in bricks:
    brickset[brick.letter] = brick

for brick in bricks:
    for s in brick.supportedBy:
        brickset[s].supports.append(brick.letter)

for brick in bricks:
    print(brick, "\n")

count = 0
for brick in bricks:
    if len(brick.supports) == 0:
        print("Can Remove", brick.letter)
        count +=1
        continue
    if all([len(brickset[sb].supportedBy) > 1 for sb in brick.supports]):
        count+=1

print(count)