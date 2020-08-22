import math
sqrt = math.sqrt

N = int(input())
ballon = []

parents = {}

joint = {}

for i in range(N) :
    n, k = [int(x) for x in input().split()]
    ballon.append((n, k))

parents[(ballon[0][0], ballon[0][1])] = None

print("%.3f" % ballon[0][1])

A = (ballon[1][0] - ballon[0][0])**2
B = 4*(ballon[0][1])

if min(ballon[1][1], A/B) == A/B :
    ballon[1][1] = A/B
    parents[(ballon[1][0], ballon[1][1])] = (ballon[0][0], ballon[0][1])
    joint[(ballon[1][0], ballon[1][1])] = (ballon[0][0], ballon[0][1])
    print("%.3f" % ballon[1][1])

elif min(ballon[1][1] , A/B) == ballon[1][1] :
    parents[(ballon[1][0], ballon[1][1])] = (ballon[0][0], ballon[0][1])
    print("%.3f" % ballon[1][1])

def is_joint(previous, now) :
    Min = ballon[len(ballon)-1][0] - ballon[0][0]
    prev = previous
    while parents[previous] != None :
        A = (now[0] - previous[0])**2
        B = 4*(previous[1])
        if previous in joint :
            if min(now[1], A/B) == now[1] :
                previous = joint[previous]
            elif min(now[1], A/B) == A/B :
                #joint[(now[0], now[1])] = (previous[0], previous[1])
                Min = min(Min, A/B)
                previous = joint[previous]

        else :
            if min(now[1], A/B) == now[1] :
                previous = parents[previous]
            elif min(now[1], A/B) == A/B :
                #joint[(now[0], now[1])] = (previous[0], previous[1])
                Min = min(Min, A/B)
    parents[(now[0], Min)] = (prev[0], prev[1])
    
    return Min
    
    
for bal in range(2, len(ballon)) :
    #parents[(ballon[bal][0], ballon[bal][1])] = (ballon[bal-1][0], ballon[bal-1][1])
    Min = is_joint((ballon[bal-1][0], ballon[bal-1][1]), (ballon[bal][0], ballon[bal][1]))
    
    print("%.3f" % Min)


    
        
        
    
    
    

