file1 = open('8.txt', 'r')
input = file1.read().splitlines()

gridLen = len(input[0])
gridHeight = len(input)
grid = [[0 for _ in range(gridLen)] for _ in range(gridHeight)]

def search(mygrid, i, j):
    isVis = searchUp(mygrid, i, j) or searchDown(mygrid, i, j) or searchLeft(mygrid, i, j) or searchRight(mygrid, i, j)
    if isVis:
        return 1
    else:
        return 0
    
def searchDown(mygrid, i, j):
    height = mygrid[i][j]
    for x in range(i+1, gridHeight):
        curr = mygrid[x][j]
        if curr >= height:
            return False
    return True
def searchUp(mygrid, i, j):
    height = mygrid[i][j]
    for x in range(i-1, -1, -1):
        curr = mygrid[x][j]
        if curr >= height:
            return False
    return True
def searchLeft(mygrid, i, j):
    height = mygrid[i][j]
    for y in range(j-1, -1, -1):
        curr = mygrid[i][y]
        if curr >= height:
            return False
    return True

def searchRight(mygrid, i, j):
    height = mygrid[i][j]
    for y in range(j+1, gridLen):
        curr = mygrid[i][y]
        if curr >= height:
            return False
    return True

def look(mygrid, i, j):
    if i == 3 and j == 2:
        print("L:" + str(lookLeft(mygrid, i, j)) + " R:" + str(lookRight(mygrid, i, j)) + " D:" + str(lookDown(mygrid, i, j)) + " U:" + str(lookUp(mygrid, i, j)))
    ss = lookUp(mygrid, i, j) * lookDown(mygrid, i, j) * lookLeft(mygrid, i, j) * lookRight(mygrid, i, j)
    return ss
    
def lookDown(mygrid, i, j):
    height = mygrid[i][j]
    count = 0
    for x in range(i+1, gridHeight):
        curr = mygrid[x][j]
        if curr >= height:
            return count+1
        else: 
            count +=1
    return count
def lookUp(mygrid, i, j):
    height = mygrid[i][j]
    count = 0
    for x in range(i-1, -1, -1):
        curr = mygrid[x][j]
        if curr >= height:
            return count+1
        else:
            count +=1
    return count
def lookLeft(mygrid, i, j):
    height = mygrid[i][j]
    count = 0
    for y in range(j-1, -1, -1):
        curr = mygrid[i][y]
        if curr >= height:
            return count+1
        else:
            count += 1
    return count

def lookRight(mygrid, i, j):
    height = mygrid[i][j]
    count = 0
    for y in range(j+1, gridLen):
        curr = mygrid[i][y]
        if curr >= height:
            return count+1
        else:
            count +=1
    return count


for i, row in enumerate(input):
    for j, tree in enumerate(row): 
        grid[i][j] = tree
counter=0
maxSS = 0
maxI = 0
maxJ = 0
ss = 0
for i in range(gridHeight):
    for j in range(gridLen):
        if i == 0 or j == 0 or i == gridHeight-1 or j == gridLen-1:
            counter +=1
            ss=0
        else:
            counter += search(grid, i, j)
            ss = look(grid, i, j)
            if ss > maxSS:
                maxSS = ss
                maxI = i
                maxJ = j
print("COUNTER = " + str(counter))
print("SS = " + str(maxSS))
print("MAX I: " + str(maxI) + " , J: " + str(maxJ))