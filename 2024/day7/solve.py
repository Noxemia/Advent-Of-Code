from typing import Tuple, List
from enum import Enum
from copy import copy

class Op(Enum):
   Add = "+"
   Mul = "*"
   Con = "||"
   
eqs: List[Tuple[int, List[int]]] = []

for line in open('input.txt', 'r').readlines():
   line = line.split(":")
   eqs.append((int(line[0]), [int(x) for x in line[1].split(" ")[1:]]))
   
operators = [Op.Add, Op.Mul, Op.Con]
nccfound = False
ccfound = False
def recSolve(target: int, cval: int, nums: List[int], listindex:int, coperator: Op, concatUsed: bool):
    global nccfound, ccfound
    if ccfound and concatUsed: return

    if cval > target: return
    if len(nums) == listindex:
        if cval == target:
            if concatUsed: 
                ccfound = True
            else:
                nccfound = True
            return
        return
    # add do current operator
    if coperator == Op.Add:
        cval += nums[listindex]
    elif coperator == Op.Mul:
        cval *= nums[listindex]
    elif coperator == Op.Con:
        concatUsed = True
        cval = int(str(cval) + str(nums[listindex]))
    
    for noperator in operators:
        if ccfound and concatUsed: return
        recSolve(target, cval, nums, listindex+1, noperator, concatUsed)

part1, part2 = 0, 0
for eq in eqs:
    for nop in operators[:3]: recSolve(eq[0], 0, eq[1], 0, nop, False)
    if nccfound: part1  += eq[0]
    if ccfound: part2   += eq[0]
    nccfound, ccfound = False, False
       
print(part1, part2)