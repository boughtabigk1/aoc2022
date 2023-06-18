file1 = open('9.txt', 'r')
commands = file1.read().splitlines()
gridLen = 500
gridHeight = 500
ropeLen = 10
grid = [[0 for _ in range(gridLen)] for _ in range(gridHeight)]

rope = [[gridHeight//2 for x in range(2)] for y in range(ropeLen)]

def moveHeadLeft(head):
    head[1] -= 1
    
def moveTailLeft(head, tail):
    if head[1] == tail[1]-2:
        tail[1] -= 1
        if tail[0] > head[0]:
            tail[0] -= 1
        elif tail[0] < head[0]:
            tail[0] += 1

def moveHeadRight(head):
    head[1] += 1
    
def moveTailRight(head, tail):
    if head[1] == tail[1]+2:
        tail[1] += 1
        if tail[0] > head[0]:
            tail[0] -= 1
        elif tail[0] < head[0]:
            tail[0] += 1

def moveHeadUp(head):
    head[0] += 1
    
def moveTailUp(head, tail):
    if head[0] == tail[0]+2:
        tail[0] += 1
        if tail[1] > head[1]:
            tail[1] -= 1
        elif tail[1] < head[1]:
            tail[1] += 1

    
def moveHeadDown(head):
    head[0] -= 1
    
def moveTailDown(head, tail):
    if head[0] == tail[0]-2:
        tail[0] -= 1
        if tail[1] > head[1]:
            tail[1] -= 1
        elif tail[1] < head[1]:
            tail[1] += 1

def moveTailAll(head, tail):
    moveTailLeft(head, tail)
    moveTailRight(head, tail)
    moveTailDown(head, tail)
    moveTailUp(head, tail)

for command in commands: 
    print(command)
    parts = command.split(" ")
    dir = parts[0]
    dist = int(parts[1])
    moved = 0
    
    while moved < dist:
        if dir == 'L':
            moveHeadLeft(rope[0])
        if dir == 'R':
            moveHeadRight(rope[0])
        if dir == 'U':
            moveHeadUp(rope[0])
        if dir == 'D':
            moveHeadDown(rope[0])
        for ropeIndex in range(1, ropeLen):
            moveTailAll(rope[ropeIndex-1], rope[ropeIndex])
        moved +=1
        grid[rope[ropeLen-1][0]][rope[ropeLen-1][1]] = 1
        
count = 0
for i in range(gridHeight):
    for j in range(gridLen):
        count += grid[i][j]
print("COUNT = " + str(count))
# print(rope)



            