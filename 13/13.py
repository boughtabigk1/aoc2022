from functools import cmp_to_key

file1 = open('13.txt', 'r')
input = file1.read().splitlines()
compareLine = 0
pairIndex = 1
correctSum = 0
packets = []
def compare(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return -1
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
        elif isinstance(left[i], list) and isinstance(right[i], list):
            res= compare(left[i], right[i])
            if res != 0:
                return res
        elif isinstance(left[i], int) and isinstance(right[i], list):
            res= compare([left[i]], right[i])
            if res != 0:
                return res
        elif isinstance(left[i], list) and isinstance(right[i], int):
            res= compare(left[i], [right[i]])
            if res != 0:
                return res
    if len(left) < len(right):
        return 1
    return 0
            
        
while compareLine < len(input):
    left = eval(input[compareLine])
    right = eval(input[compareLine+1])
    packets.append(left)
    packets.append(right)
    if compare(left, right) >= 0:
        print("FOUNDONE: #" + str(pairIndex))
        correctSum += pairIndex
    compareLine += 3
    pairIndex += 1

packets.append([[2]])
packets.append([[6]])

packets.sort(key=cmp_to_key(compare), reverse=True)

index1 = packets.index([[2]])+1
index2 = packets.index([[6]])+1
ans = index1 * index2

print("CORRECTSUM: " + str(correctSum))
# print(index1)
# print(index2)
print("NEWANS: " + str(ans))
# print(packets)