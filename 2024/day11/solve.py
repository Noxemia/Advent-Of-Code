from functools import cache

stones = []

for line in open('input.txt', 'r').readlines():
    stones = [int(x) for x in line.split(" ")]


@cache
def blink(stone: int, blinks: int) -> int:
    if blinks == 75: return stone

    if stone == 0: return blink(1, blinks+1)
    stonestr: str = str(stone)
    if (sl := len(stonestr)) % 2 == 0:
        lh = stonestr[:(sl//2)]
        rh = stonestr[sl//2:]
        return blink(int(lh), blinks+1) + blink(int(rh), blinks+1)
    
    return blink(stone*2024, blinks+1)

part1 = 0
for stone in stones:
    part1 += blink(stone, 0)

print(part1)