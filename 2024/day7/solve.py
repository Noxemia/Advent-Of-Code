from typing import Tuple, List
   
eqs: List[Tuple[int, List[int]]] = []

for line in open('input.txt', 'r').readlines():
   line = line.split(":")
   eqs.append((int(line[0]), [int(x) for x in line[1].split(" ")[1:]]))
   
nccfound = False
ccfound = False
numl = 0
def recSolve(target: int, cval: int, nums: List[int], listindex:int, coperator: int, concatUsed: bool):
    global nccfound, ccfound
    if ccfound and concatUsed: return

    if cval > target: return
    if numl == listindex:
        if cval == target:
            if concatUsed: 
                ccfound = True
            else:
                nccfound = True
            return
        return
    # add do current operator
    if coperator == 0:
        cval += nums[listindex]
    elif coperator == 1:
        cval *= nums[listindex]
    elif coperator == 2:
        concatUsed = True
        cval = int(str(cval) + str(nums[listindex]))
    
    if ccfound and concatUsed: return
    recSolve(target, cval, nums, listindex+1, 0, concatUsed)
    recSolve(target, cval, nums, listindex+1, 1, concatUsed)
    recSolve(target, cval, nums, listindex+1, 2, concatUsed)


part1, part2 = 0, 0
for eq in eqs:
    numl = len(eq[1])
    for nop in [0,1]: recSolve(eq[0], 0, eq[1], 0, nop, False)
    if nccfound: part1  += eq[0]
    if ccfound: part2   += eq[0]
    nccfound, ccfound = False, False
       
print(part1, part2)