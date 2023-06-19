file1 = open('14.txt', 'r')
input = file1.read().splitlines()
lenX = 1000
lenY = 200
pourX = 500
pourY = 0
cave = [['.' for x in range(lenX)] for y in range(lenY)]

# for part 2
# instead of pouring one at a time you could just pour 3x starting from the top and not set the current grain back to .
# if you just count the grains of sand you'll get the same answer as the simulation
# but i did this first and it was fun watching it run for ten minutes so im not implementing that kuk
def pourOne(cave):
    resting = 0
    for y in range(lenY-1, -1, -1):
        for x in range(lenX):
            if cave[y][x] == 's':
                resting += fallDown(cave, y, x)
    cave[0][500] = 's'
    return resting
                    
def isSandOrRock(cave, y, x):
    return cave[y][x] == '#' or cave[y][x] == 's'
def fallDown(cave, y, x):
    if y+1 < lenY:
        if not isSandOrRock(cave, y+1, x):
            cave[y+1][x] = 's'
            cave[y][x] = '.'
            return 0
        elif not isSandOrRock(cave, y+1, x-1):
            cave[y+1][x-1] = 's'
            cave[y][x] = '.'
            return 0
        elif not isSandOrRock(cave, y+1, x+1):
            cave[y+1][x+1] = 's'
            cave[y][x] = '.'
            return 0
        else:
            return 1
    else:
        cave[y][x] = '.'
        return 0
        
        
for line in input:
    parts = line.split(" -> ")
    path = []
    lastPair = (-1,-1)
    for part in parts:
        coords = part.split(",")
        y = int(coords[1])
        x = int(coords[0])
        pair = (y,x)
        if lastPair[0] != -1:
            if pair[0] != lastPair[0]:
                for y in range(min(pair[0], lastPair[0]), max(pair[0], lastPair[0])+1, 1):
                    cave[y][x] = '#'
            elif pair[1] != lastPair[1]:
                for x in range(min(pair[1], lastPair[1]), max(pair[1], lastPair[1])+1, 1):
                    cave[y][x] = '#'
        lastPair = pair
        
#lets see the cave here actually
maxY = 0
for y in range(lenY):
    for x in range(lenX):
        if cave[y][x] == '#':
            maxY = max(maxY, y)
print("MAXY: " + str(maxY))

for x in range(lenX):
    cave[maxY+2][x] = '#'

sameCounter = 0
lastResting = 0
for t in range(100000):
    if t%100 == 0:
        print("T = " + str(t))
    resting = pourOne(cave)
    if resting == lastResting:
        sameCounter +=1 
    else:
        lastResting = resting
        sameCounter = 0
    if sameCounter == 300:
        print("STOPPED POURING AT T=" + str(t))
        print("amount resting= " + str(resting))
        break

#lets see the cave here actually
for y in range(10):
    for x in range(490, 510):
        print(cave[y][x], end="")
    print("")