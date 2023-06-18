file1 = open('10.txt', 'r')
commands = file1.read().splitlines()

numCycles = len(commands)*2
cycles = [0]*numCycles
currCycle = 0
total = 1
totalScore = 0
row = ""
rows = [row for x in range(6)]
for command in commands:
    parts = command.split(" ")
    if parts[0] == "addx":
        currCycle +=2 
        cycles[currCycle] += int(parts[1])
    else: 
        currCycle +=1 
for i, diff in enumerate(cycles):
    total += diff
    if i > 239:
        break
    pos = i%40
    rows[(i//40)] += '#' if pos >= total-1 and pos <= total+1 else '.'
for row in rows:
    print(row)
