import random

def get_result(List, n, k, compare_list, origin_k, Max) :
    m = min(List)
    M = max(List)
    t = int((M-m)/(k-1))
    Min = M - m
    ## 특수 케이스

    # 최악의 경우 시간복잡도 : O(n) -- n번 전부 서칭
    if n == k :
        Min = 0
        List = sorted(List)
        for j in range(len(List)-1) :
            Min = max((List[j+1]-List[j]), Min)
        return Min
    
    if k == 2 :
        return Min

    ## 구분자(눈금자) 생성
    threshold = []

    # 시간복잡도 : O(k)
    for i in range(1, k-1, 1) :
        threshold.append(m+t*i)
    
    List2 = []
    # 시간복잡도 : O(nlongn)
    List2 = sorted(List+threshold)

    length = len(List2)
    p = 0
    compare_list.append(List2[0])

    # threshold의 수만큼
    for j in threshold :
        if min((List2[List2.index(j)]-List2[List2.index(j)-1]), (List2[List2.index(j)+1]- List2[List2.index(j)])) == List2[List2.index(j)+1] - List2[List2.index(j)] :
            if (List2[List2.index(j)+1] not in compare_list) and (List2[List2.index(j)+1] in List) :
                compare_list.append(List2[List2.index(j)+1])
                if p > 0 :
                    Min = min(compare_list[p] - compare_list[p-1], Min)
                    #print(Min)
                p = p + 1
            
        elif min((List2[List2.index(j)]-List2[List2.index(j)-1]), (List2[List2.index(j)+1]-List2[List2.index(j)])) == List2[List2.index(j)] - List2[List2.index(j)-1] :
            if (List2[List2.index(j)-1] not in compare_list) and (List2[List2.index(j)-1] in List) :
                compare_list.append(List2[List2.index(j)-1])
                if p > 0 :
                    Min = min(compare_list[p] - compare_list[p-1], Min)
                p = p + 1


    if List2[0] not in compare_list :
        compare_list.insert(0, List2[0])

    if Max not in compare_list :
        compare_list.insert(len(compare_list), Max)
    
    if len(compare_list) != origin_k :
        List = List[:len(List)-1]
        k = k - 1
        return get_result(List, n, k, compare_list, origin_k, Max)

    Min = min(compare_list[1] - compare_list[0], Min)
    Min = min(compare_list[len(compare_list)-1] - compare_list[len(compare_list)-2], Min)
    
    return Min
        
def main() :
    List = []
    n, k = [int(x) for x in input().split()]
    for i in range(n) :
        a = int(input())
        List.append(a)
        
    result = 0
    compare_list = []
    origin_k = k
    Max = max(List)
    result = get_result(List, n, k, compare_list, origin_k, Max)
    print(result)


main()
