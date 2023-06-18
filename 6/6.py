file1 = open('6.txt', 'r')
signal = file1.read()
ans = ""
for i, c in enumerate(signal):
    ans += c
    if len(ans) ==15:
        ans = ans[1:]
    if len(ans) ==14:
        set = {}
        for c2 in ans:
            set[c2] = 1
        if len(set) == 14:
            print("FOUND AT " + str(i+1))
            break