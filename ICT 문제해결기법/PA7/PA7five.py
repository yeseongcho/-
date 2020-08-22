import math
sqrt = math.sqrt

N = int(input())
ballon = []

parents = {}

joint = {}

for i in range(N) :
    n, k = [int(x) for x in input().split()]
    ballon.append((n, k))

##### basic setting
parents[(ballon[0][0], ballon[0][1])] = None

print("%.3f" % float(ballon[0][1]))

A = (ballon[1][0] - ballon[0][0])**2
B = 4*ballon[0][1]

if min(ballon[1][1], A/B) == A/B :
    parents[(ballon[1][0], A/B)] = (ballon[0][0], ballon[0][1])
    joint[(ballon[1][0], A/B)] = (ballon[0][0], ballon[0][1])
    #print(ballon[1])
    ballon[1] = (ballon[1][0], A/B)
    print("%.3f" % float(A/B))

elif min(ballon[1][1] , A/B) == ballon[1][1] :
    parents[(ballon[1][0], ballon[1][1])] = (ballon[0][0], ballon[0][1])
    print("%.3f" % float(ballon[1][1]))
######

# fact finding!

# 접한 원들 사이의 비교는 joint {} 써서 비교를 생략하여 시간을 절약하고

# 인접원의 경우, min값이 되면서 동시에 나보다 큰 원이 되면 그 때 루프를 탈출하는 알고리즘을 구현해본다

def get_min(now, previous) :
    Min = 10**20 # infinity value
    while previous != None :
        A = (now[0] - previous[0])**2
        B = 4*previous[1]
        if min(now[1], A/B) == A/B :
            Min = min(A/B, Min)
            if previous in joint :
                #print("#")
                if previous[1] > Min :
                    joint[now] = previous
                    return Min
                previous = joint[previous]
            else :
                if previous[1] > Min :
                    joint[now] = previous
                    return Min
                #print(previous)
                #print(parents)
                previous = parents[previous]
        else :
            Min = min(now[1], Min)
            if previous in joint :
                if previous[1] > Min :
                    joint[now] = previous
                    return Min
                previous = joint[previous]
            else :
                if previous[1] > Min :
                    
                    joint[now] = previous
                    return Min
                previous = parents[previous]
    return Min
        
result = 0
for bal in range(2, len(ballon)) :
   # 시간을 벌기 위한 특수 케이스 제거
   C = (ballon[bal][0] - ballon[bal-1][0])**2
   D = (ballon[bal][1] - ballon[bal-1][1])**2
   if sqrt(C+D) >= ballon[bal][1] + ballon[bal-1][1] :
        print("%.3f" % float(ballon[bal][1]))
        parents[(ballon[bal][0], ballon[bal][1])] = (ballon[bal-1][0], ballon[bal-1][1])
   else :
        result = get_min((ballon[bal][0], ballon[bal][1]), (ballon[bal-1][0], ballon[bal-1][1]))
        ballon[bal] = (ballon[bal][0], result) # 지금 내 원 갱신
        parents[(ballon[bal][0], result)] = (ballon[bal-1][0], ballon[bal-1][1]) # 바뀐 반지름 기준으로 부모값 갱신
        print("%.3f" % float(result))

    
        
