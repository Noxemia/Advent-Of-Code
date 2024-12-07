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

operators = [Op.Add, Op.Mul]
def recSolve(target: int, cval: int, rest: List[int], coperator: Op):
    if cval > target: return False
    ## add do current operator
    if coperator == Op.Add:
       cval += rest.pop(0)
    elif coperator == Op.Mul:
        cval *= rest.pop(0)
    elif coperator == Op.Con:
       cval = int(str(cval)+str(rest.pop(0)))

    ## Check if list is empty that we reached target
    if (len(rest)) == 0:
       return True if cval == target else False
    
    return any(recSolve(target, cval, copy(rest), noperator) for noperator in operators)

part1 = 0
for eq in eqs:
    if any(recSolve(eq[0], 0, copy(eq[1]), nop) for nop in operators):
       part1+= eq[0]

operators.append(Op.Con)
part2 = 0
for eq in eqs:
    if any(recSolve(eq[0], 0, copy(eq[1]), nop) for nop in operators):
       part2+= eq[0]

print(part1, part2)
    