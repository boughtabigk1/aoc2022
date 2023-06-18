file1 = open('1.txt', 'r')
lines = file1.readlines()
currSum = 0
topThree = [0, 0, 0]
for line in lines:
    line = line.strip()
    if line == "":
        minIndex = topThree.index(min(topThree))
        topThree[minIndex] = max(topThree[minIndex], currSum)
        currSum = 0
    else:
        currSum += int(line)
print("top3: ")
print(topThree)
print("SUM: " + str(sum(topThree)))