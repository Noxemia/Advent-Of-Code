import os
from datetime import date
from requests import get

daynum = str(date.today())[-2:]
if daynum[0] == '0': daynum = daynum[1:2]
newpath = f"./day{daynum}"

os.mkdir(newpath)

open(f"{newpath}/solve.py", "x").write(
    "data = []\n\nfor line in open('input.txt', 'r').readlines():\n    data.append(line)"
)

# cookie starts with session= and then the cookie
cookie = open(f"./session.env", "r").readlines()[0]

input = get(f'https://adventofcode.com/{date.year}/day/{daynum}/input', headers={'cookie': cookie})

open(f"{newpath}/input.txt", "x").write(input.content.decode('utf-8'))