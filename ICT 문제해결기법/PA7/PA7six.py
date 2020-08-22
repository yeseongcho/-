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
def get_min(now, previous, max_rad, I_min) :
    Min = 10**20 # infinity value
    while previous != None :
        A = (now[0] - previous[0])**2
        B = 4*previous[1]

        if min(now[0], A/B) == A/B :
            Min = min(Min, A/B)

            if Min == A/B :
                I_min = (previous[0], previous[1])

            if previous[1] >= A/B :
                return Min, I_min

            if previous[1] == max_rad :
                return Min, I_min

            if previous in joint :
                previous = joint[previous]

            else :
                previous = parents[previous]
        else :
            Min = min(Min, now[0])
            if previous[1] >= now[0] :
                return Min, I_min
            if previous[1] == max_rad :
                return Min, I_min
            if previous in joint :
                previous = joint[previous]
            else :
                previous = parents[previous]

    return Min, I_min
                
max_rad = max(ballon[0][1], ballon[1][1])
result = 0
I_min = ()
max_x_point = 0
max_x_point = max(ballon[0][0] + ballon[0][1], ballon[1][0] + ballon[1][1])
for bal in range(2, len(ballon)) :
    if ballon[bal][0] - ballon[bal][1] > max_x_point :
        print("%.3f" % float(result))
        parents[(ballon[bal][0], ballon[bal][1])] = (ballon[bal-1][0], ballon[bal-1][1])
        max_x_point = ballon[bal][0] + ballon[bal][1]
    else :
        result, I_min = get_min((ballon[bal][0], ballon[bal][1]), (ballon[bal-1][0], ballon[bal-1][1]), max_rad, I_min)
        if result < ballon[bal][1] :
            joint[(ballon[bal][0], ballon[bal][1])] = (I_min[0], I_min[1])
        ballon[bal] = (ballon[bal][0], result) # 지금 내 원 갱신
        parents[(ballon[bal][0], ballon[bal][1])] = (ballon[bal-1][0], ballon[bal-1][1]) # 바뀐 반지름 기준으로 부모값 갱신
        max_x_point = max(max_x_point, ballon[bal][0] + ballon[bal][1])
        max_rad = max(max_rad, ballon[bal][1])
        print("%.3f" % float(result))

