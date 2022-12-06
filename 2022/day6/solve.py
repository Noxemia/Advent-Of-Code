data = []

for line in open('input.txt', 'r').readlines():
	data = line

def solver(matchlength: int) -> int:
	for i in range(0, len(data)):
		if len(dict(zip(iter(data[i:i+matchlength]), range(matchlength))).keys()) == matchlength: 
			return i+matchlength

print(f"Part 1: {solver(4)}")
print(f"Part 2: {solver(14)}")
	
	