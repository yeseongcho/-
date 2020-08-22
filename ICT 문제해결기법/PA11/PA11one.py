# 출처 : https://www.geeksforgeeks.org/longest-bitonic-subsequence-onlogn/
def ceilIndex(arr, l, r, x) :
    if (l > r) :
        return -1

    mid = l + (r-l)//2
    if (arr[mid] == x) :
        return mid

    if (x < arr[mid]) :
        return ceilIndex(arr, l, mid-1, x)

    return ceilIndex(arr, mid+1, r, x)

def reverseArr(arr, n) :
    i = 0
    j = n-1
    while (i < j) :
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        i += 1
        j -= 1

def getLBSLengthLogn(arr, n) :
    if (n==0) :
        return 0

    increasing = [0 for i in range(n)]
    
    tail1 = [0 for i in range(n)]

    decreasing = [0 for i in range(n)]
    
    tail2 = [0 for i in range(n)]

    increasing[0] = arr[0]

    ind = 1

    tail1[0] = 0
    # 1,n이 맞을까 그냥 n이 맞을까
    for i in range(1,n) :
        if (arr[i] < increasing[0]) :
            increasing[0] = arr[i]
            tail1[i] = 0
        elif (arr[i] > increasing[ind-1]) :
            increasing[ind] = arr[i]
            ind += 1
            tail1[i] = ind-1
        else :
            increasing[ceilIndex(increasing, -1, ind-1, arr[i])] = arr[i]
            tail1[i] = ceilIndex(increasing, -1, ind-1, arr[i])
    #print(increasing)
    #print(tail1)

    ind = 1

    reverseArr(arr, n)
    decreasing[0] = arr[0]
    tail2[0] = 0

    for i in range(1,n) :
        if(arr[i] < decreasing[0]) :
            decreasing[0] = arr[i]
            tail2[i] = 0
        elif (arr[i] > decreasing[ind-1]) :
            decreasing[ind] = arr[i]
            ind += 1
            tail2[i] = ind - 1
        else :
            decreasing[ceilIndex(decreasing, -1, ind-1, arr[i])] = arr[i]
            tail2[i] = ceilIndex(decreasing,-1,ind-1,arr[i])
    #print(decreasing)
    #print(tail2)
    reverseArr(arr, n)
    reverseArr(tail2, n)
    #print(tail1)
    #print(tail2)
    ans = 0
    for i in range(n) :
        ans = max((tail1[i] + tail2[i]+1), ans)
    return ans

N = int(input())
arr = []
m = 0
for i in range(N) :
    m = int(input())
    arr.append(m)
n = len(arr)
result = 0
result = getLBSLengthLogn(arr, n)
print(result)
    

# input
# 0 1 2 3 2 4 1 2 3 5 6 2 3 5 8 1
# 얘가 왜 답이 9가 나올까

