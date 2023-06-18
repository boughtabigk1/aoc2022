file1 = open('4.txt', 'r')
lines = file1.read().splitlines()
count = 0
for line in lines:
    assigns = line.split(",")
    a1 = assigns[0].split("-")
    a2 = assigns[1].split("-")
    s1 = int(a1[0])
    e1 = int(a1[1])    
    s2 = int(a2[0])
    e2 = int(a2[1])
    if s2 >= s1 and s2 <= e1:
        count +=1 
    elif e2 >= s1 and e2 <= e1:
        count +=1 
    elif s1 >= s2 and s1 <= e2:
        count +=1 
    elif e1 >= s2 and e1 <= e2:
        count +=1 
print("COUNT: " + str(count))