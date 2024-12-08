from typing import Tuple, List
from enum import Enum
from copy import copy

class Op(Enum):
    Add = "+"
    Mul = "*"
    Con = "||"

eqs: List[Tuple[int, List[int]]] = []
for line in open("input.txt", "r").readlines():
    line = line.split(":")
    eqs.append((int(line[0]), [int(x) for x in line[1].split(" ")[1:]]))

operators = [Op.Add, Op.Mul, Op.Con]
found = False
gconUsed = False

def recSolve(target: int, cval: int, rest: List[int], coperator: Op, conUsed: bool):
    global found, gconUsed
    if found: return False
    if cval > target: return False

    # add do current operator
    if coperator == Op.Add:
        cval += rest.pop(0)
    elif coperator == Op.Mul:
        cval *= rest.pop(0)
    elif coperator == Op.Con:
        conUsed = True
        cval = int(str(cval) + str(rest.pop(0)))

    # Check if list is empty that we reached target
    if (len(rest)) == 0:
        if cval == target:
            if conUsed:
                gconUsed = True
            found = True
            return True
        return False

    return any(recSolve(target, cval, copy(rest), noperator, conUsed) for noperator in operators)

part1 = 0
part2 = 0
for eq in eqs:
    if any(recSolve(eq[0], 0, eq[1], nop, False) for nop in operators):
        if not gconUsed:
            part1 += eq[0]
        part2 += eq[0]
    found = False
    gconUsed = False

print(part1, part2)
