import random

def b_search(List2, j, low, high) :
    mid = (low+high)//2

    if List2[mid] == j :
        return mid

    elif List2[mid] < j :
        return b_search(List2, j, mid+1, high)

    elif List2[mid] > j :
        return b_search(List2, j, low, mid-1)

def get_result(List, n, k) :
    m = min(List)
    M = max(List)
    t = int((M-m)/(k-1))
    # worst case
    if n == k :
        Max = 0
        List = sorted(List)
        for j in range(len(List)-1) :
            Max = max(Max, (List[j+1]-List[j]))
        return Min
    # easiest case
    if k == 2 :
        Max = 0
        List = sorted(List)
        for u in range(len(List)-1) :
            Max = max((List[u+1]-List[u]), Max)
        return Min
        
    threshold = []
    doubles = [] # 중복을 처리해주기 위함..
    for i in range(1, k-1, 1) :
        if m+t*i in List :
            doubles.append(m+t*i)
        threshold.append(m+t*i)
        
    
    #print(doubles)
    print(threshold)
    List2 = sorted(List + threshold)
    print(List2)
    
    index_t = []

    for j in threshold :
        b = b_search(List2, j, 0, len(List2)-1)
        if List2[b] == List2[b+1] :
            index_t.append(b+1)
        else :
            index_t.append(b)
    #print(index_t)
    compare = []
    # special case
    if k == 3 :
        compare.append(min(List2[index_t[0]+1:]))
        compare.insert(0, m)
        compare.insert(len(compare), M)
        if doubles != [] :
            compare = compare + doubles
            compare = sorted(compare)
        #print(compare)
        Min = M-m
        for s in range(len(compare)-1) :
            Min = min(Min, compare[s+1]-compare[s])
        return Min
    ## th를 포함하고 안하고 여부를 디버깅해야한다. --- 04/25 기준!
    for r in range(len(index_t)-1) :
        if List2[index_t[r+1]] == List2[index_t[r+1]-1] :
            if List2[index_t[r]] == List2[index_t[r]-1] :
                compare.append(List2[index_t[r]])
                compare.append(List2[index_t[r+1]])
            else :
                #print(List2[index_t[r+1]-1])
                compare.append(max(List2[index_t[r]:index_t[r+1]-1]))
                compare.append(List2[index_t[r+1]])
                #print(compare)
                #print("###")
        else :
            compare.append(max(List2[index_t[r]:index_t[r+1]]))
    if max(List2[:index_t[0]]) not in compare :
        compare.insert(0, max(List2[:index_t[0]]))
    if m not in compare :
        compare.insert(0, m)
    if M not in compare :
        compare.insert(len(compare), M)
    print(compare)
    ## 여기 doubles도 손을 좀 봐야할 듯..
    #if doubles != [] :
    #    for d in doubles :
    #        if d not in compare :
    #            compare.append(d)
    #    compare = sorted(compare)
    #print("############################")
    #print(compare)
    Min = M-m
    for s in range(len(compare)-1) :
        Min = min(Min, compare[s+1]-compare[s])
    return Min
def main() :
    List = []
    n, k = [int(x) for x in input().split()]
    for i in range(n) :
        a = int(input())
        List.append(a)

    
    ### 난수를 돌려보니까 왜 0이 나오지... 
    #n = random.randint(10, 100)
    #k = random.randint(2, 10)
    #for i in range(n):
    #    number = random.randint(1, 100)
    #    if number not in List :
    #        List.append(number)
    #result = 0
    
  
    print(n)
    print(k)
    print(sorted(List))
    result = get_result(List, n, k)

    print(result)

main()
        
### 난수를 돌려보니까 왜 0이 나오지... 
#    n = random.randint(10, 100)
#    k = random.randint(2, 10)
#    for i in range(n):
#        number = random.randint(1, 100)
#        if number not in List :
#            List.append(number)


