from functools import cache

stones = []

for line in open('input.txt', 'r').readlines():
    stones = [int(x) for x in line.split(" ")]

cache = dict()
def blink(stone: int, blinks: int) -> int:
    if (stone, blinks) in cache: return cache[(stone,blinks)]
    if blinks == 0: 
        cache[(stone,blinks)] = 1
        return 1

    if stone == 0: 
        res = blink(1, blinks-1)
        cache[(stone,blinks)] = res
        return res
    stonestr: str = str(stone)
    if (sl := len(stonestr)) % 2 == 0:
        lh = stonestr[:(sl//2)]
        rh = stonestr[sl//2:]
        res = blink(int(lh), blinks-1) + blink(int(rh), blinks-1)
        cache[(stone,blinks)] = res
        return res
    
    res = blink(stone*2024, blinks-1)
    cache[(stone,int)] = res
    return res

part1, part2 = 0, 0
for stone in stones:
    part2 += blink(stone, 75)
    part1 += blink(stone, 25)

print(part1, part2)