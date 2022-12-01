import os

from datetime import date

daynum = str(date.today())[-2:]
if daynum[0] == '0': daynum = daynum[1:2]
newpath = f"./day{daynum}"
os.mkdir(newpath)

open(f"{newpath}/solve.py", "x").write(
    "data = []\n\nfile = open('input.txt', 'r')\n\nfor line in file.readlines():\n\tdata.append(line)"
)

open(f"{newpath}/input.txt", "x")