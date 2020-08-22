N = int(input())
ballon = []
for i in range(N) :
    n, k = [int(x) for x in input().split()]
    ballon.append((n, k))
    

previous = {}
previous[0] = (ballon[0][0], ballon[0][1])

## 1초 안에 print...
pre = 0
print("%.3f" % previous[0][1])
for bal in range(1, len(ballon)) :
    A = (ballon[bal][0]-previous[pre][0])**2
    B = 4*previous[pre][1]
    if ballon[bal][1] > A/B :
        pre = pre + 1
        #print(pre)
        previous[pre] = (ballon[bal][0], A/B)
        print("%.3f" % previous[pre][1])
    else :
        if bal != len(ballon)-1 :
            A = (ballon[bal+1][0] - ballon[bal][0])**2
            B = 4*ballon[bal][1]
            if ballon[bal+1][1] > A/B :
                pre = pre + 1
                previous[pre] = (ballon[bal+1][0], A/B)
                continue
        print("%.3f" % ballon[bal][1])
