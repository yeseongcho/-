List = []
n, k = [int(x) for x in input().split()]

for i in range(n) :
    a = int(input())
    List.append(a)
M = max(List)
m = min(List)
List = sorted(List)
th = int((M-m)/(k-1))
def len_search(L, U) :
    Mid = int((L+U)//2)
    return Mid

distance = 0
count = 1
now = 0
compare = 1
distance = len_search(0, th)
distance_max = 0
print(distance)
while True :
    while List[now + compare] != List[len(List)-1] :
       
        if List[now] + distance > List[now+compare] :
            compare = compare + 1
        elif List[now] + distance <= List[now+compare] :
            now = now+compare
            count = count + 1
            compare = 1

    if List[now] + distance <= List[len(List)-1] :
        count = count + 1

    if count > k :
        distance = len_search(distance+1, th)
        count = 1
        compare = 1
        now = 0
        
       
    elif count < k :
        distance = len_search(0, distance-1)
        count = 1
        compare = 1
        now = 0
        
    else :
        count = 1
        compare = 1
        now = 0
        break
    print(distance)

distance_max = distance
distance = len_search(distance+1, th)
while True :
    while List[now + compare] != List[len(List)-1] :
       
        if List[now] + distance > List[now+compare] :
            compare = compare + 1
        elif List[now] + distance <= List[now+compare] :
            now = now+compare
            count = count + 1
            compare = 1
    
    if List[now] + distance <= List[len(List)-1] :
        count = count + 1
    if count == k :
        distance_max = max(distance_max, distance)
        if distance+1 == th :
            break
        else :
            distance = len_search(distance+1, th)
            compare = 1
            count = 1
            now = 0
    else :
        if distance+1 == th :
            break
        else :
            distance = len_search(distance+1, th)
            compare = 1
            count = 1
            now = 0
print(distance_max)
           
           






        

