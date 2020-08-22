### 나중에 꼭 피드백 받자
# Binary search의 맹점을 다루어야 한다
List = []
n, k = [int(x) for x in input().split()]
for i in range(n) :
    a = int(input())
    List.append(a)

M = max(List)
m = min(List)

#List = sorted(List)

th = int((M-m)/(k-1))

def len_search(L, U, th) :
    Mid = (L+U)//2
    if Mid == U :
        return Mid
    if L == U-2 and U == th :
        return L

    elif L == U-2 and L == 0 :
        return U
    return Mid

distance = (0 + th)//2

# 이러한 초기화과정은 매번 필요하다
now = 0
compare = 1
count = 1

# pole들을 count해주는 알고리즘은 괜찮은건가? 여기도 무언가 문제가 있는 것 같다..
def get_count(now, compare, count) :
    while List[now+compare] != List[len(List)-1] :
        if List[now] + distance > List[now+compare] :
            compare = compare + 1
        elif List[now] + distance <= List[now+compare] :
            now = now+compare
            count = count + 1
            compare = 1
    if List[now] + distance <= List[len(List)-1] :
        count = count + 1
    return count


count = get_count(now, compare, count)

now = 0
compare = 1
count = 1
distance_max = 0

correct = 0

while (distance + 1 != th)  :
    if count == k :
        distance_max = max(distance_max, distance)
        correct = distance_max
        break
    elif count > k :
        now = 0
        compare = 1
        count = 1
        distance = len_search(distance + 1, th, th)
        count = get_count(now, compare, count)
    else :
        now = 0
        compare = 1
        count = 1
        distance = len_search(0, distance-1, th)
        count = get_count(now, compare, count)

distance_max = distance
#print(distance)
distance = distance + 1
now = 0
compare = 1
count = 1
count = get_count(now,compare,count)
#print(count)
# 같은 값을 발견한 뒤 더 큰 값이 있는지 linear search..! -- 이 곳을 다시 binary search하는 거 같아..!(그런데 종료 조건을 도저히 못찾겠다...ㅠㅠㅠ)
while distance + 1 != th :
    if count == k :
        distance_max = max(distance_max, distance)
        #print(distance)
        distance = distance + 1
        count = get_count(now, compare, count)
    else :
        distance = distance + 1
        count = get_count(now, compare, count)
       
# 마지막 th일때!!
now = 0
compare = 1
count = 1
count = get_count(now, compare, count)
if count == k :
    distance_max = distance
distance = distance + 1
now = 0
compare = 1
count = 1
count = get_count(now, compare, count)
if count == k :
    distance_max = distance
print(distance_max)

