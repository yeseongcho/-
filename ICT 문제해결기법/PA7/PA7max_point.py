import math
sqrt = math.sqrt

N = int(input())
ballon = []

parents = {}

joint = {}

for i in range(N) :
    n, k = [int(x) for x in input().split()]
    ballon.append((n, k))


# fact finding!

# 접한 원들 사이의 비교는 joint {} 써서 비교를 생략하여 시간을 절약하고

# 인접원의 경우, min값이 되면서 동시에 나보다 큰 원이 되면 그 때 루프를 탈출하는 알고리즘을 구현해본다

# joint를 언제 갱신해주는지를 온전히 구현해야 한다!!

# 종료 조건 1. 앞에 애가 나보다 클때

# 종료 조건 2. 앞에 애가 max 애일 때

# 그래도 Timelimit...

# max_x_point 조건을 다시 수정해서 작성해보자..! outlier 맞는거 같아 

# max_rad보다 내가 더 큰 경우...
print("%.3f" % ballon[0][1])
max_rad = max(ballon[0][1], ballon[1][1])
result = 0
max_point = []
max_x_point = 0
Min = 0
if max(ballon[0][0] + ballon[0][1], ballon[1][0] + ballon[1][1]) == ballon[0][0] + ballon[0][1] :
    max_x_point = ballon[0][0] + ballon[0][1]
    max_point = [ballon[0][0], ballon[0][1]]
else :
    max_x_point = ballon[1][0] + ballon[1][1]
    max_point = [ballon[1][0], ballon[1][1]]

for bal in range(1, len(ballon)) :
    A = (ballon[bal][0] - max_point[0])**2
    B = 4*max_point[1]
    Min = min(A/B, ballon[bal][1])
    ballon[bal] = (ballon[bal][0], Min)
    print("%.3f" % float(Min))
    if max(max_x_point, ballon[bal][1]+ballon[bal][0]) == ballon[bal][1] + ballon[bal][0]:
        max_point = [ballon[bal][0], ballon[bal][1]]
        max_x_point = ballon[bal][1]+ballon[bal][0]
        
    
       
        

