import random
# 이게 아마 run error의 원인일 수도 있다. 꼭 점검해야 한다..
def b_search(List2, j, low, high) :
    mid = (low+high)//2

    if List2[mid] == j :
        return mid

    elif List2[mid] < j :
        return b_search(List2, j, mid+1, high)

    elif List2[mid] > j :
        return b_search(List2, j, low, mid-1)


def get_result(List, n, k, compare_list, origin_k, Max) :
    m = min(List)
    M = max(List)
    t = int((M-m)/(k-1))
    
    ## 특수 케이스
    # 최악의 경우 시간복잡도 : O(n) -- n번 전부 서칭
    if n == k :
        Min = 0
        List = sorted(List)
        for j in range(len(List)-1) :
            Min = max((List[j+1]-List[j]), Min)
        return Min
    if k == 2 :
        List = sorted(List)
        Min = List[len(List)-1] - List[0]
        return Min
    ## 구분자(눈금자) 생성
    threshold = []
    # 시간복잡도 : O(k)
    for i in range(1, k-1, 1) :
        threshold.append(m+t*i)
    #print(threshold)
    List2 = []
    # 시간복잡도 : O(nlongn)
    List2 = sorted(List+threshold)
    length = len(List2)
    index_t = []
    # binary search 시간 복잡도 -- (k-2)log(k-2)
    for j in threshold :
        b = b_search(List2, j, 0, len(List2)-1)
        index_t.append(b)
    # 시간복잡도 O(k-2) -- k-2개 threshold
    for s in index_t :
        if min((List2[s]-List2[s-1]), (List2[s+1]- List2[s])) == List2[s+1] - List2[s] :
            if (List2[s+1] not in compare_list) and (List2[s+1] in List) :
                compare_list.append(List2[s+1])
            
        elif min((List2[s]-List2[s-1]), (List2[s+1]-List2[s])) == List2[s] - List2[s-1] :
            if (List2[s-1] not in compare_list) and (List2[s-1] in List) :
                compare_list.append(List2[s-1])
    if List2[0] not in compare_list :
        compare_list.append(List2[0])
    if Max not in compare_list :
        compare_list.append(Max)

    if len(compare_list) != origin_k :
        List = List[:len(List)-1]
        k = k - 1
        return get_result(List, n, k, compare_list, origin_k, Max)
    compare_list = sorted(compare_list)
    print(compare_list)
    Min = compare_list[len(compare_list)-1] - compare_list[0]
    # compare_list 내 min 경우 서칭 -- 추가적 시간 복잡도 소요
    for f in range(len(compare_list)-1) :
        Min = min(Min, compare_list[f+1] - compare_list[f])
    return Min
        
def main() :
    List = []
    n, k = [int(x) for x in input().split()]
    for i in range(n) :
        a = int(input())
        List.append(a)

    #n = random.randint(100, 1000)
    #k = random.randint(2, 10)
    #for i in range(n):
    #    number = random.randint(1, 1000)
    #    if number not in List :
    #        List.append(number)


    result = 0
    compare_list = []
    origin_k = 0
    origin_k = k
    #print(n)
    #print(k)
    #print(sorted(List))
    Max = max(List)
    result = get_result(List, n, k, compare_list, origin_k, Max)
    print(result)


main()

