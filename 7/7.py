file1 = open('7.txt', 'r')
commands = file1.read().splitlines()

x = 0
class TreeNode():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = {}
    
    def addChild(self, dir):
        dir.parent = self
        self.children.append(dir)
        
    def addfile(self, filename, filesize):
        self.files[filename] = filesize
        
    def sumfiles(self):
        sum = 0
        for size in self.files.values():
            sum += int(size)
        return sum
    
    def dfsAdd(self, atMost, ans):
        mySize = self.sumfiles()
        # basicMySize = mySize
        for child in self.children:
            mySize += child.dfsAdd(atMost, ans)
        if mySize <= atMost:
            # print("NODE " + self.name + " MYSIZE " + str(basicMySize), end='')
            # print(" TOT " + str(mySize))
            ans[0] += mySize
        return mySize    
    
    def dfsSearchMin(self, atLeast, ans):
        mySize = self.sumfiles()
        # basicMySize = mySize
        for child in self.children:
            mySize += child.dfsSearchMin(atLeast, ans)
        # print("NODE " + self.name + " MYSIZE " + str(basicMySize), end='')
        # print(" TOT " + str(mySize))
        if mySize >= atLeast:
            ans[0] = min(ans[0], mySize)
        return mySize
    
    def child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    
rootNode = TreeNode('root')
startNode = TreeNode('/')
rootNode.addChild(startNode)
startNode = rootNode.child('/')
path = rootNode
for command in commands:
    parts = command.split(" ")
    # print("@" + path.name + " C: " + command)
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "/":
                path = startNode
            elif parts[2] == "..":
                path = path.parent
            else:
                path = path.child(parts[2])
        else: 
            continue
    elif parts[0] == "dir":
        newNode = TreeNode(parts[1])
        path.addChild(newNode)
    elif parts[0].isnumeric():
        path.addfile(parts[1], int(parts[0]))
    else:
        print("how did we get here?")
# print("OUT")
# startNode.dfsPrint()
arr=[0]
arr2=[70000000000]
# rootNode.dfsAdd(100000, arr)
totUsed = rootNode.dfsAdd(100000, arr)
print("TOTUSED " + str(totUsed))
emptySpace = 70000000 - totUsed
print("EMPTY " + str(emptySpace))
weNeed = 30000000 - emptySpace
weNeed2 = 30000000 - 23447691
print("WENEED " + str(weNeed))
print("WENEED2 " + str(weNeed2))
rootNode.dfsSearchMin(weNeed, arr2)
print("ANS: " + str(arr2[0]))


    
        