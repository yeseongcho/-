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

# joint를 언제 갱신해주는지를 온전히 구현해야 한다!!

# 종료 조건 1. 앞에 애가 나보다 클때

# 종료 조건 2. 앞에 애가 max 애일 때

# 그래도 Timelimit...

def get_min(now, previous, max_rad) :
    Min = 10**20 # infinity value
    # 초반 연산
    A = (now[0] - previous[0])**2
    B = 4*previous[1]
    Min = min(A/B, now[1])
    if previous in joint :
        previous = joint[previous]
    else :
        previous = parents[previous]
    joint[now] = previous
    while previous != None :
        A = (now[0] - previous[0])**2
        B = 4*previous[1]
        Min = min(A/B, Min)
        if Min == A/B :
            joint[now] = previous
        if previous in joint :
            if previous[1] == max_rad :     
                return Min
            elif previous[1] >= Min :  
                return Min
            previous = joint[previous]
        else :
            if previous[1] == max_rad :   
                return Min
            elif previous[1] >= Min :  
                return Min
            previous = parents[previous]

    return Min
        
max_rad = max(ballon[0][1], ballon[1][1])
result = 0
for bal in range(2, len(ballon)) :
    result = get_min((ballon[bal][0], ballon[bal][1]), (ballon[bal-1][0], ballon[bal-1][1]), max_rad)
    ballon[bal] = (ballon[bal][0], result) # 지금 내 원 갱신
    parents[(ballon[bal][0], ballon[bal][1])] = (ballon[bal-1][0], ballon[bal-1][1]) # 바뀐 반지름 기준으로 부모값 갱신
    max_rad = max(max_rad, ballon[bal][1])
    print("%.3f" % float(result))
