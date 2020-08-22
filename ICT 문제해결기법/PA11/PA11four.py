def binary_search(arr, end, val) :
    low = 0
    high = end
    if val < arr[0] :
        return 0
    if val > arr[end] :
        return end+1
    while (low <= high) :
        mid = (low+high)//2
        if(low == high) :
            return low
        else :
            if(arr[mid] == val) :
                return mid
            if (val < arr[mid]) :
                high = mid
            else :
                low = mid + 1
def reverseArr(arr, n) :
    i = 0
    j = n-1
    while(i<j) :
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        i += 1
        j -= 1

def lis(arr, n) :
    t = [0]*n
    t[0] = arr[0]
    end = 0

    lis = [0]*n
    lis[0] = 1
    index = 0
    for i in range(1, n) :
        index = binary_search(t, end, arr[i])
        t[index] = arr[i]
        if (index > end) :
            end += 1
        lis[i] = end + 1
        
    return lis

def lds(arr, n) :
    d = [0]*n
    end = 0
    lds = [0]*n
    lds[0] = 1
    index = 0
    reverseArr(arr,n)
    #print(arr)
    for i in range(1, n) :
        index = binary_search(d, end, arr[i])
        d[index] = arr[i]
        if (index > end) :
            end += 1
        lds[i] = end + 1
        
    return lds

def lbs(arr, n) :
    lis_list = []
    lds_list = []
    lis_list = lis(arr, n)
    lds_list = lds(arr, n)
    #print(lis_list)
    #print(lds_list)
    Max = lis_list[0] + lds_list[0] - 1
    for i in range(1, n) :
        Max = max(Max, lis_list[i] + lds_list[i] - 1)
    return Max


N = int(input())
arr = []
m = 0
for i in range(N) :
    m = int(input())
    arr.append(m)
n = len(arr)
result = 0
result = lbs(arr, n)
print(result)
