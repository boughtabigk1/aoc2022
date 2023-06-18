import copy
import sys

sys.setrecursionlimit(9999) 

file1 = open('12.txt', 'r')
input = file1.read().splitlines()
lenY = len(input)
lenX = len(input[0])
heights = [[0 for x in range(lenX)] for y in range(lenY)]
startY = -1
startX = -1
endY = -1
endX = -1

for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == 'S':
            startX = x
            startY = y
            heights[y][x] = ord('a')
        elif char == 'E':
            endX = x
            endY = y
            heights[y][x] = ord('z')
        else:
            heights[y][x] = ord(char)

visited = [[0 for x in range(lenX)] for y in range(lenY)]
distances = [[9999 for x in range(lenX)] for y in range(lenY)]

def dijkstra(visited, distances, heights):
    distances[startY][startX] = 0
    queue = []
    queue.append((startY, startX))
    
    while len(queue) > 0:
        x = queue[0][1]
        y = queue[0][0]
        print("CURRNODE- X:"+str(x)+',Y:'+str(y))
        if visited[y][x] == 1:
            queue.pop(0)
            continue

        if y + 1 < lenY and heights[y][x]+1 >= heights[y+1][x]:
            distances[y+1][x] = min(distances[y][x] + 1, distances[y+1][x])
            queue.append((y+1, x))
        if y - 1 >= 0 and heights[y][x]+1 >= heights[y-1][x]:
            distances[y-1][x] = min(distances[y][x] + 1, distances[y-1][x])    
            queue.append((y-1, x))
        if x + 1 < lenX and heights[y][x]+1 >= heights[y][x+1]:
            distances[y][x+1] = min(distances[y][x] + 1, distances[y][x+1])    
            queue.append((y, x+1))
        if x - 1 >= 0 and heights[y][x]+1 >= heights[y][x-1]:
            distances[y][x-1] = min(distances[y][x] + 1, distances[y][x-1])
            queue.append((y, x-1))
        
        visited[y][x] = 1
        queue.pop(0)
        
def dijkstraBackwards(visited, distances, heights):
    distances[endY][endX] = 0
    queue = []
    queue.append((endY, endX)) # now we start at the end
    
    while len(queue) > 0:
        x = queue[0][1]
        y = queue[0][0]
        print("CURRNODE- X:"+str(x)+',Y:'+str(y))
        if visited[y][x] == 1:
            queue.pop(0)
            continue
        # same bound checks but now we can only go down one level
        if y + 1 < lenY and heights[y][x]-1 <= heights[y+1][x]:
            distances[y+1][x] = min(distances[y][x] + 1, distances[y+1][x])
            queue.append((y+1, x))
        if y - 1 >= 0 and heights[y][x]-1 <= heights[y-1][x]:
            distances[y-1][x] = min(distances[y][x] + 1, distances[y-1][x])    
            queue.append((y-1, x))
        if x + 1 < lenX and heights[y][x]-1 <= heights[y][x+1]:
            distances[y][x+1] = min(distances[y][x] + 1, distances[y][x+1])    
            queue.append((y, x+1))
        if x - 1 >= 0 and heights[y][x]-1 <= heights[y][x-1]:
            distances[y][x-1] = min(distances[y][x] + 1, distances[y][x-1])
            queue.append((y, x-1))
        
        visited[y][x] = 1
        queue.pop(0)
    
# dijkstra(visited, distances, heights)
# print("ROUTE DISTANCE: " + str(distances[endY][endX]))
dijkstraBackwards(visited, distances, heights)
minimum = 69696969
for y in range(lenY):
    for x in range(lenX):
        if heights[y][x] == ord('a'):
            minimum = min(minimum, distances[y][x])
print("MIN DISTANCE TO A= " + str(minimum))