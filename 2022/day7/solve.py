
from collections import defaultdict
from dataclasses import dataclass
import sys
sys.setrecursionlimit(20000)
data = []

for line in open('input.txt', 'r').readlines():
	data.append(line.strip("\n"))

@dataclass

@dataclass
class node:
	parent: str
	name: str
	files: list
	filessize: int
	childs: list
	childssize: int

	def __init__(self, parent, name):
		self.name = name
		self.parent = parent
		self.files = []
		self.filessize = 0
		self.childs = []
		self.childssize = 0

	
root = node(None, "/")


