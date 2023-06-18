
class Monkey():
    def __init__(self):
        self.items = []
        self.operation = lambda x : x
        self.test = lambda x : True
        self.trueMonkey = -1
        self.falseMonkey = -1
    
    def setItems(self, items):
        self.items = items
    def setOperation(self, fx):
        self.operation = fx
    def setTest(self, fx):
        self.test = fx
    def setTrueMonkey(self, i):
        self.trueMonkey = i
    def setFalseMonkey(self, i):
        self.falseMonkey = i
        
numMonkeys = 8
monkeys = [Monkey() for x in range(numMonkeys)]
    
monkeys[0].setItems([59, 65, 86, 56, 74, 57, 56])
monkeys[0].setOperation(lambda x : x*17)
monkeys[0].setTest(lambda x : x%3 == 0)
monkeys[0].setTrueMonkey(3)
monkeys[0].setFalseMonkey(6)

monkeys[1].setItems([63, 83, 50, 63, 56])
monkeys[1].setOperation(lambda x : x+2)
monkeys[1].setTest(lambda x : x%13 == 0)
monkeys[1].setTrueMonkey(3)
monkeys[1].setFalseMonkey(0)

monkeys[2].setItems([93, 79, 74, 55])
monkeys[2].setOperation(lambda x : x+1)
monkeys[2].setTest(lambda x : x%2 == 0)
monkeys[2].setTrueMonkey(0)
monkeys[2].setFalseMonkey(1)

monkeys[3].setItems([86, 61, 67, 88, 94, 69, 56, 91])
monkeys[3].setOperation(lambda x : x+7)
monkeys[3].setTest(lambda x : x%11 == 0)
monkeys[3].setTrueMonkey(6)
monkeys[3].setFalseMonkey(7)

monkeys[4].setItems([76, 50, 51])
monkeys[4].setOperation(lambda x : x*x)
monkeys[4].setTest(lambda x : x%19 == 0)
monkeys[4].setTrueMonkey(2)
monkeys[4].setFalseMonkey(5)

monkeys[5].setItems([77, 76])
monkeys[5].setOperation(lambda x : x+8)
monkeys[5].setTest(lambda x : x%17 == 0)
monkeys[5].setTrueMonkey(2)
monkeys[5].setFalseMonkey(1)

monkeys[6].setItems([74])
monkeys[6].setOperation(lambda x : x*2)
monkeys[6].setTest(lambda x : x%5 == 0)
monkeys[6].setTrueMonkey(4)
monkeys[6].setFalseMonkey(7)

monkeys[7].setItems([86, 85, 52, 86, 91, 95])
monkeys[7].setOperation(lambda x : x+6)
monkeys[7].setTest(lambda x : x%7 == 0)
monkeys[7].setTrueMonkey(4)
monkeys[7].setFalseMonkey(5)

# DEBUG MONKEYS!
# monkeys[0].setItems([79, 98])
# monkeys[0].setOperation(lambda x : x*19)
# monkeys[0].setTest(lambda x : x%23 == 0)
# monkeys[0].setTrueMonkey(2)
# monkeys[0].setFalseMonkey(3)

# monkeys[1].setItems([54, 65, 75, 74])
# monkeys[1].setOperation(lambda x : x+6)
# monkeys[1].setTest(lambda x : x%19 == 0)
# monkeys[1].setTrueMonkey(2)
# monkeys[1].setFalseMonkey(0)

# monkeys[2].setItems([79, 60, 97])
# monkeys[2].setOperation(lambda x : x*x)
# monkeys[2].setTest(lambda x : x%13 == 0)
# monkeys[2].setTrueMonkey(1)
# monkeys[2].setFalseMonkey(3)

# monkeys[3].setItems([74])
# monkeys[3].setOperation(lambda x : x+3)
# monkeys[3].setTest(lambda x : x%17 == 0)
# monkeys[3].setTrueMonkey(0)
# monkeys[3].setFalseMonkey(1)
#END DEBUG MONKEYS!

LCM = 9699690
# LCM =  96577
counts = [0 for x in range(numMonkeys)]
for round in range(10000):
    # print("ENTER ROUND #" + str(round))
    for i, monkey in enumerate(monkeys):
        # print("monkey #" + str(i))
        while len(monkeys[i].items) > 0:
            
            # print(monkeys[i].items)
            monkeys[i].items[0] = monkeys[i].operation(monkeys[i].items[0])
            # monkeys[i].items[0] = monkeys[i].items[0] //3
            monkeys[i].items[0] = monkeys[i].items[0] % LCM
            
            # print("b4: " + str(monkeys[i].items[0]))
            throwTo = monkeys[i].trueMonkey if monkeys[i].test(monkeys[i].items[0]) else monkeys[i].falseMonkey
            
            # print("throw2 before")
            # print(monkeys[throwTo].items)
            monkeys[throwTo].items.append(monkeys[i].items.pop(0))
            # print("throw2 after")
            # print(monkeys[throwTo].items)
            # if  len(monkeys[i].items) > 0:
            #     print("after: " + str(monkeys[i].items[0]))
            # else: 
            #     print("empty")
            counts[i] += 1
    # for j, monkey in enumerate(monkeys):
    #     print("MONKEY#" + str(j))
    #     print(monkeys[j].items)
top1 = 0
top2 = 0
print(counts)
for count in counts:
    if count > top1:
        top2 = top1
        top1 = count
    elif count > top2:
        top2 = count
print("TOP1: " + str(top1))
print("TOP2: " + str(top2))
print("MONKEYBUSINESS: " + str(top1*top2))