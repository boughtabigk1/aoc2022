file1 = open('3.txt', 'r')
lines = file1.read().splitlines()
sum = 0
sum3 = 0
set3 = {}
counter3 = 0
for line in lines:
    currSet = {}
    amt = len(line)//2
    # print("AMT: " + str(amt))
    sack1 = line[:amt]
    sack2 = line[amt:]
    for c in sack1:
        currSet[c] = 1
    for c in sack2:
        if c in currSet:
            if c.islower():
                sum += ord(c)-96
            else:
                sum += ord(c)-38
            break
    # print("SET"+str(counter3))
    if counter3 == 0:
        for c in line: 
            set3[c] = 1
        print(set3)
    else:
        common = {}
        for c in line: 
            if c in set3:
                common[c] = 1
        set3 = common 
        print(set3)
    counter3 +=1 
    if counter3 ==3:
        counter3 = 0
        for badge in set3:
            # print("BADGE: " + badge)
            if badge.islower():
                sum3 += ord(badge)-96
            else:
                sum3 += ord(badge)-38
        set3 = {}
print("SUM: " + str(sum))
print("SUM3: " + str(sum3))