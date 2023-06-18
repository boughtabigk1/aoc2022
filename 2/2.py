file1 = open('2.txt', 'r')
lines = file1.read().splitlines()
scores = {
    'A': 1, #r
    'B': 2, #p 
    'C': 3 #s
}
outcomes = {
    'X': 0, #r
    'Y': 3, #p
    'Z': 6 #s
}
diffs = {
    'X': -1, #l
    'Y': 0, #d
    'Z': 1 #w
}
sumScore = 0
for line in lines:
    # print(line)
    vals = line.split(" ")
    # print("OUTCOMESCORE: " + str(outcomes[vals[1]]))
    sumScore += outcomes[vals[1]]
    add = (scores[vals[0]]+diffs[vals[1]])%3
    if add == 0:
        add = 3
    # print("ADDCORE: " + str(add))
    sumScore += add
    
print("SUMSCORE " + str(sumScore))