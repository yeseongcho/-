def b_search(List2, j, low, high) :
    mid = (low+high)//2

    if List2[mid] == j :
        return mid

    elif List2[mid] < j :
        return b_search(List2, j, mid+1, high)

    elif List2[mid] > j :
        return b_search(List2, j, low, mid-1)

    

def get_result(List, n, k, length, M, outlier, outlier_value) :
    m = min(List)
    M = max(List)
    t = int((M-m)/(k-1))
    #print(List)
    #print(k)
    ## 특수 케이스
    if n == k :
        Min = M-m
        #List = sorted(List)
        for j in range(len(List)-1) :
            Min = min((List[j+1]-List[j]), Min)
        return Min
    if k == 2 and outlier == []:
        Min = M-m
        #List = sorted(List)
        for u in range(len(List)-1) :
            Min = min((List[u+1]-List[u]), Min)
        return Min

    # 눈금자 알고리즘에서 어떻게 이상치를 통제하지?
    if sum(List[:length-1]) <= M :
        outlier.append(length-1)
        outlier_value.append(M)
        List = List[:length-1]
        length = len(List)
        k = k - 1
        return get_result(List, n, k, length, M, outlier, outlier_value)
        
    outlier = sorted(outlier)
    #print(outlier)
    #print(outlier_value)
    threshold = []

    ## 시간복잡도 k-1
    for i in range(1, k-1, 1) :
        threshold.append(m+t*i)
    List2 = []
    #print(threshold)

    # n*nlogn
    List2 = sorted(List+threshold)
    #print(List2)
    # k*logk
    ## binary search를 써주는 게 맞는 걸까?
    index_t = []
    for j in threshold :
        b = b_search(List2, j, 0, len(List2)-1)
        index_t.append(b)
    #print(index_t)
    

    ### binary search로 위치를 찾았으니 그 전 후로 차이의 대소를 비교하는 반복문 구성
    compare_list = []
    for s in index_t :
        if min((List2[s]-List2[s-1]), (List2[s+1]- List2[s])) == List2[s] - List2[s-1] :
            if (s-1) not in compare_list :
                compare_list.append(s-1)
            else :
                compare_list.append(s+1)
        elif min((List2[s]-List2[s-1]), (List2[s+1]-List2[s])) == List2[s+1] - List2[s] :
            if (s+1) not in compare_list :
                compare_list.append(s+1)
            else :
                compare_list.append(s-1)
    ## 여기까지 비교하는 리스트 구성
    # 잘 구성이 되었나 compare_list를 확인하면 되!
    #print(List2)
    compare_list.insert(0, 0)
    compare_list.insert(len(compare_list), len(List2)-1)
    List2 = List2 + outlier_value
    for o in outlier :
        compare_list.insert(len(compare_list), len(List2)-1)
    print(compare_list)
    Min = M-m
    for f in range(1, len(compare_list), 1) :
        Min = min((List2[compare_list[f]] - List2[compare_list[f-1]]), Min)
    return Min

def main() :
    List = []
    n, k = [int(x) for x in input().split()]
    for i in range(n) :
        a = int(input())
        List.append(a)

    result = 0
    length = len(List)
    M = 0
    outlier = []
    outlier_value = []
    List = sorted(List)
    result = get_result(List, n, k, length, M, outlier, outlier_value)
    print(result)
            

main()
        
