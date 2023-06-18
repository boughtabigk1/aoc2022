file1 = open('5.txt', 'r')
moves = file1.read().splitlines()

boxstax = [""]*9
boxstax[0] = "SMRNWJVT"
boxstax[1] = "BWDJQPCV"
boxstax[2] = "BJFHDRP"
boxstax[3] = "FRPBMND"
boxstax[4] = "HVRPTB"
boxstax[5] = "CBPT"
boxstax[6] = "BJRPL"
boxstax[7] = "NCSLTZBW"
boxstax[8] = "LSG"
ans = ""
print("OBSERVE THE BOX")
print(boxstax)
mc = 0

def reverse(s):
    ans = ""
    slen = len(s)
    for i, _ in enumerate(s):
        ans += s[slen-1-i]
    return ans

for move in moves:
    # if mc > 10: 
    #     break
    instruct = move.split(" ")
    quant = int(instruct[1])
    fromInd = int(instruct[3])-1
    toInd = int(instruct[5])-1
    
    # print("M " + str(quant) + " F " + str(fromInd) + " to " + str(toInd))
    # print(boxstax[fromInd])
    # print(boxstax[toInd])
    # print("MOVING " + (boxstax[fromInd])[len(boxstax[fromInd])-quant:] + " wlen " + str(len((boxstax[fromInd])[len(boxstax[fromInd])-quant:])))
    # boxstax[toInd] = boxstax[toInd] + reverse((boxstax[fromInd])[len(boxstax[fromInd])-quant:])
    boxstax[toInd] = boxstax[toInd] + (boxstax[fromInd])[len(boxstax[fromInd])-quant:]
    boxstax[fromInd] = boxstax[fromInd][:len(boxstax[fromInd])-quant]
    
    # print(boxstax[fromInd])
    # print(boxstax[toInd])
    # print("~~~~~~~~~~~~~~")
    # mc += 1
for box in boxstax:
    if len(box) != 0:
        ans = ans + box[len(box)-1]
print("MC: " + str(mc))
print(ans)
print(boxstax)