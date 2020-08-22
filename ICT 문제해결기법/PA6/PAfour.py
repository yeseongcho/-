def b_search(List2, j, low, high) :
    mid = (low+high)//2

    if List2[mid] == j :
        return mid

    elif List2[mid] < j :
        return b_search(List2, j, mid+1, high)

    elif List2[mid] > j :
        return b_search(List2, j, low, mid-1)




def main() :
    List = []
    n, k = [int(x) for x in input().split()]
    for i in range(n) :
        a = int(input())
        List.append(a)
    
    m = min(List)
    M = max(List)
    mean = int(sum(List)/(n))
    
    List.append(mean)
    List = sorted(List)
    #print(List)
    mean_index = b_search(List, mean, 0, len(List)-1)
    #print(mean_index)
    i = mean_index - 1
    j = mean_index + 1
    compare = []
    #print(List[j]-List[mean_index])
    #print(List[mean_index]-List[i])
    while(len(compare) != k-2) :
        if List[j] - List[mean_index] == List[mean_index] - List[i] :
            if (List[j+1] - List[mean_index]) > (List[mean_index] - List[i-1]) :
                compare.append(List[j])
                j = j + 1
            elif (List[j+1] - List[mean_index]) < (List[mean_index] - List[i-1]) :
                compare.append(List[i])
                i = i - 1
        elif (min((List[j] - List[mean_index]), (List[mean_index] - List[i])) == List[j] - List[mean_index])  :
            #print("####")
            compare.append(List[j])
            j = j + 1
        elif  (min((List[j] - List[mean_index]), (List[mean_index] - List[i])) == List[mean_index] - List[i])  :
            compare.append(List[i])
            i = i - 1
        else :
            break

    compare = sorted(compare)
    compare.insert(0, m)
    compare.insert(len(compare), M)
    #print(compare)
    Min = M - m
    for p in range(len(compare)-1) :
        Min = min(Min, compare[p+1] - compare[p])

    print(Min)

main()
        
    
        
            
    
