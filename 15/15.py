file1 = open('15.txt', 'r')
input = file1.read().splitlines()

sensors = [(-1,-1) for x in range(len(input))] 
radii = [-1 for x in range(len(input))] 
beacons = {}
intervals = []

# checkY = 10
checkY = 2000000
for i, line in enumerate(input):
    words = line.split(" ")
    sensorX = int(words[2][2:len(words[2])-1])
    sensorY = int(words[3][2:len(words[3])-1])
    beaconX = int(words[8][2:len(words[8])-1])
    beaconY = int(words[9][2:len(words[9])])
    
    sensors[i] = (sensorY, sensorX)
    beacons[(beaconY, beaconX)] = None
    radii[i] = abs(beaconY-sensorY) + abs(beaconX-sensorX)

for i, sensor in enumerate(sensors):
    startX = sensor[1] - radii[i] + abs(sensor[0]-checkY)
    endX = sensor[1] + radii[i] - abs(sensor[0]-checkY)
    if startX <= endX:
        intervals.append((startX, endX))
    
intervals = sorted(intervals)
mergedintervals = []
ni = 0
for i, interval in enumerate(intervals):
    if i != 0:
        if mergedintervals[ni][1] >= interval[0]:
            newEnd = max(mergedintervals[ni][1], interval[1])
            mergedintervals[ni] = (mergedintervals[ni][0], newEnd)
        else:
            mergedintervals.append(interval)        
            ni += 1
    else:
        mergedintervals.append(interval)

sum = 0
for mergedinterval in mergedintervals:
    sum += mergedinterval[1] - mergedinterval[0] + 1
for beacon in beacons:
    if beacon[0]==checkY:
        sum -= 1
# print(intervals)
# print(mergedintervals)
print("ANS: " + str(sum))