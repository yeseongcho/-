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

# max_x_point 조건을 다시 수정해서 작성해보자..! outlier 맞는거 같아 ㅠㅠ

def get_min(now, previous, max_rad,  max_list_copy) :
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
            if previous[1] >= Min : # Min같은데 과연 A/B가 맞을까?  
                return Min

            if sub_max < now[0] - Min :
                return Min
            
            previous = joint[previous]
        else :
            if previous[1] == max_rad :   
                return Min
            if previous[1] >= Min :  
                return Min
            if sub_max < now[0] - Min :
                return Min
          
            previous = parents[previous]

    return Min
        
max_rad = max(ballon[0][1], ballon[1][1])
result = 0
max_x_point = max(ballon[0][0] + ballon[0][1], ballon[1][0] + ballon[1][1])
max_list = []
max_list_copy = []
max_list.append(max_x_point)
max_list_copy = max_list
sub_max = 0
# max_point가 안되게 되면 어디가 문제인지 확인해본다.
# 우선 test1은 통과했으니 그대로 사용한다
# 추가적인 조건이 더 필요한가 보다


# sub_max를 통해 걸러주는 조건을 디밸롭해보자

for bal in range(2, len(ballon)) :
    if max_x_point <= ballon[bal][0] - ballon[bal][1] :
        print("%.3f" % float(ballon[bal][1]))
        parents[(ballon[bal][0], ballon[bal][1])] = (ballon[bal-1][0], ballon[bal-1][1])
        max_rad = max(max_rad, ballon[bal][1])
        max_x_point = ballon[bal][0] + ballon[bal][1]
        max_list.append(max_x_point)
    else :
        max_list_copy = max_list
        result = get_min((ballon[bal][0], ballon[bal][1]), (ballon[bal-1][0], ballon[bal-1][1]), max_rad, max_list_copy)
        ballon[bal] = (ballon[bal][0], result) # 지금 내 원 갱신
        parents[(ballon[bal][0], ballon[bal][1])] = (ballon[bal-1][0], ballon[bal-1][1]) # 바뀐 반지름 기준으로 부모값 갱신, 기본 옵션 3
        max_rad = max(max_rad, ballon[bal][1]) # 기본 옵션 1
        print("%.3f" % float(result))
        if max(max_x_point, ballon[bal][0] + ballon[bal][1]) ==  ballon[bal][0] + ballon[bal][1] :
            max_list.append(ballon[bal][0] + ballon[bal][1])
        max_x_point = max(max_x_point, ballon[bal][0] + ballon[bal][1])
        if max_x_point == ballon[bal][1] :
            max_list.append(max_x_point)
        
        
        
