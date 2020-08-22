def get_count(distance, List, now, compare, count) :
    while List[now + compare] != List[len(List)-1] :
        #print(count)
        if List[now] + distance > List[now+compare] :
            compare = compare + 1
        elif List[now] + distance <= List[now+compare] :
            now = now+compare
            count = count + 1
            compare = 1
    if List[now] <= List[len(List)-1] :
        count = count + 1
    return count


def len_search(L, U, th) :
    Mid = (L+U)//2
    if Mid == U :
        return Mid
    if L == U-2 and U == th :
        return L
    elif L == U-2 and L == 0 :
        return U
    return Mid


def main() :
    List = []
    n, k = [int(x) for x in input().split()]
    for i in range(n) :
        a = int(input())
        List.append(a)

    M = max(List)
    m = min(List)

    #List = sorted(List)

    th = int((M-m)/(k-1))

    distance = int((0+th)//2)
    #print(distance)

    now = 0

    compare = 1

    count = 1

    count = get_count(distance, List, now, compare, count)
    #print(count)
    #print("###")
    while count != k :
        if count > k :
            distance = len_search(distance+1, th, th)
            now = 0
            compare = 1
            count = 1
            count = get_count(distance, List, now, compare, count)
        elif count < k :
            distance = len_search(0, distance-1, th)
            now = 0
            compare = 1
            count = 1
            count = get_count(distance, List,  now, compare, count)
    #print("###")
    #print(count)
    #print(distance)
    distance_max = distance
    distance = len_search(distance+1, th, th)
    #print(distance)
    now = 0
    compare = 1
    count = 1
    count = get_count(distance, List, now, compare, count)
    #distance_max = max(distance, distance_max)
    more_distance = distance + 1
    
    while distance != th :
        if count > k :
            distance = len_search(distance+1, th, th)
            now = 0
            compare = 1
            count = 1
            count = get_count(distance, List,  now, compare, count)
        elif count < k :
            distance = len_search(more_distance, distance-1, th)
            now = 0
            compare = 1
            count = 1
            count = get_count(distance, List,  now, compare, count)
        else :
            now = 0
            compare = 1
            count = 1
            distance_max = max(distance, distance_max)
            distance = len_search(distance+1, th, th)
            count = get_count(distance, List,  now, compare, count)

    print(distance_max)

main()

    
            
    
    
