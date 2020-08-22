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
    if L == U :
        return L
    Mid = (L+U)//2
    return Mid

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

L = 1
U = th

distance = (1 + th)//2
distance_max = 0
now = 0; compare = 1; count = 1

count = get_count(now, compare, count)
while (L <= U)  :
    if count == k :
        now = 0; compare = 1; count = 1
        distance = max(distance_max, distance)
        L = distance+1
        distance = len_search(L, U)
        count = get_count(now, compare, count)
    elif count > k :
        now = 0; compare = 1; count = 1
        L = distance+1
        distance = len_search(L, U)
        count = get_count(now, compare, count)
    else :
        now = 0; compare = 1; count = 1
        U = distance-1
        distance = len_search(L, U)
        count = get_count(now, compare, count)

print(distance)
#print("####")
