data = [[int(i) for i in x.split()] for x in open('input.txt', 'r').readlines()]

def validateReport(report):   
    if report != sorted(report) and report != sorted(report, reverse=True): return False
    for i in range(len(report)-1):
        if (x := report[i]) == (y := report[i+1]) or abs(x-y) > 3: return False
    return True

tot1, tot2 = 0, 0
for report in data:
    if validateReport(report): 
        tot1, tot2 = tot1 + 1, tot2 + 1
        continue
    for i in range(len(report)):
        if validateReport(report[:i] + report[i+1:]):
            tot2 += 1
            break

print("Part 1:", tot1, "\nPart 2:", tot2)