import copy
from dataclasses import dataclass
from typing import List

seeds = []
updatedSeeds = []

def rangeUpdater(destinationStart: int, sourceStart: int, length: int ):
	for i, seed in enumerate(seeds):
		# Bigger or equal to 11 and smaller or equal to 11 + 42 -1 = 52
		if seed >= sourceStart and seed <= sourceStart + length -1:
			diff = seed - sourceStart
			newPos = destinationStart + diff
			updatedSeeds[i] = newPos

allNums = [str(x) for x in range(0, 10)]
for line in open('input.txt', 'r').readlines():
	line = line.strip("\n")
	if len(line) == 0:
		seeds = copy.copy(updatedSeeds)
		continue
	if seeds == []:
		line = line.strip("seeds: ")
		for num in line.split(" "):
			seeds.append(int(num))
			updatedSeeds.append(int(num))
		continue
	if line[0] in allNums:
		numbers = [int(x) for x in line.split(" ")]
		rangeUpdater(numbers[0], numbers[1], numbers[2])

print(min(updatedSeeds))

@dataclass
class instruction:
	sourceStart: int
	sourceEnd: int
	destination: int
	def astuple(self):
		return (self.sourceStart, self.sourceEnd, self.destination)
	
@dataclass
class seedRange:
	start: int
	end: int
	
def updateRange(instructions, range):
	ret = []
	ranges: List[seedRange] = [range]
	for instr in instructions:
		(ss, se, dest) = instr.astuple()
		nextRanges = []
		while ranges:
			cRange: seedRange = ranges.pop()
			rStart = cRange.start
			rEnd = cRange.end
			before = seedRange(rStart, min(rEnd, ss-1))
			middle = seedRange(max(rStart, ss), min(se, rEnd))
			end = seedRange(max([se+1, rStart]), rEnd)

			if before.end >= before.start:
				nextRanges.append(before)
			if middle.end >= middle.start:
				ret.append(seedRange(middle.start-ss+dest, middle.end-ss+dest))
			if end.end >= end.start:
				nextRanges.append(end) 
		ranges = nextRanges
	return ret + ranges

ranges: List[seedRange] = []
newRanges: List[seedRange] = []
instructions: List[instruction] = []

for line in open('input.txt', 'r').readlines():
	line = line.strip("\n")
	if len(line) == 0:
		tmpRanges = []
		while ranges:
			range = ranges.pop()
			tmpRanges += updateRange(instructions, range)
		ranges = tmpRanges
		instructions = []
		continue
	if ranges == []:
		line = line.strip("seeds: ")
		splitSeeds = [int(x) for x in line.split(" ")]
		for i in range(0, len(splitSeeds), 2):
			ranges.append(seedRange(splitSeeds[i], splitSeeds[i]+splitSeeds[i+1]-1))
		continue
	if line[0] in allNums:
		numbers = [int(x) for x in line.split(" ")]
		instructions.append(instruction(numbers[1], numbers[1] + numbers[2], numbers[0]))
		continue

tmpRanges = []
while ranges:
		range = ranges.pop()
		tmpRanges += updateRange(instructions, range)
ranges = tmpRanges

minSeed = 999999999999999999999999999999999999999999999999
for _range in ranges:
	minSeed = min(_range.start, minSeed)

print(minSeed)