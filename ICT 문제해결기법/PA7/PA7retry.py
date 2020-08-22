import math
sqrt = math.sqrt

N = int(input())
ballon = []

carling = {}

result = 0

now = ( )
for i in range(N) :
    n, k = [int(x) for x in input().split()]
    ballon.append((n, k))


carling[(ballon[0][0], ballon[0][1])] = None

# 첫 번째 원
print("%.3f" % float(ballon[0][1]))

A = (ballon[1][0] - ballon[0][0])**2
B = 4*ballon[0][1]

if min(ballon[1][1], A/B) == A/B :
    # 새로들어온 원이 이전 원보다 작으면..
    ballon[1] = (ballon[1][0], A/B)
    print("%.3f" % float(ballon[1][1]))
    if ballon[1][1] < ballon[0][1] :
        carling[(ballon[1][0], ballon[1][1])] = (ballon[0][0], ballon[0][1])
    # 새로들어온 원이 이전 원보다 크면..
    else :
        carling[(ballon[1][0], ballon[1][1])] = None

elif min(ballon[1][1] , A/B) == ballon[1][1] :
    print("%.3f" % float(ballon[1][1]))
   
    if ballon[1][1] < ballon[0][1] :
        carling[(ballon[1][0], ballon[1][1])] = (ballon[0][0], ballon[0][1])
    else :
        carling[(ballon[1][0], ballon[1][1])] = None
    
def get_min(now, previous) :
    #Min = 10**20 # infinity value
    C = (now[0] - previous[0])**2
    D = 4*previous[1]
    Min = min(C/D, now[1])
    while previous != None :
        C = (now[0] - previous[0])**2
        D = 4*previous[1]
        Min = min(C/D, Min)
        if Min == C/D :
            if Min < previous[1] :
                now = (now[0], Min)
                carling[now] = previous
                return Min, now
            if carling[previous] == None :
                now = (now[0], Min)
                return Min, now
            else :
                previous = carling[previous]
        else :
            if Min < previous[1] :
                now = (now[0], Min)
                carling[now] = previous
                return Min, now
            if carling[previous] == None :
                now = (now[0], Min)
                return Min, now
            else :
                previous = carling[previous]

    now = (now[0], Min)
    carling[now] = None
    return Min, now
        
for bal in range(2, len(ballon)) :
    result, now = get_min((ballon[bal][0], ballon[bal][1]), (ballon[bal-1][0], ballon[bal-1][1]))
    ballon[bal] = now  
    print("%.3f" % float(result))
