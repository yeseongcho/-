# https://shoark7.github.io/programming/algorithm/3-LIS-algorithms
def lis(arr):
    # C[i] means smallest last number of lis subsequences whose length are i
    C = [0] * (len(arr))
    C[1] = arr[0]
    tmp_longest = 0
    for n in arr:
        if C[tmp_longest] < n:
            tmp_longest += 1
            C[tmp_longest] = n
        else:
            next_loc = search(0, tmp_longest, n, C)
            #print(next_loc)
            C[next_loc] = n

    return C

# Find i that matches C[i-1] < n <= C[i]
def search(lo, hi, n, C):
    if lo == hi:
        return lo
    elif lo + 1 == hi:
        return lo if C[lo] >= n else hi

    mid = (lo + hi) // 2
    if C[mid] == n:
        return mid
    elif C[mid] < n:
        return search(mid+1, hi, n,C)
    else:
        return search(lo, mid, n,C)

def lds(arr):
    # C[i] means smallest last number of lis subsequences whose length are i
    D = [0] * (len(arr))
    D[1] = arr[0]
    tnp_longest = 0
    for n in arr:
        if D[tnp_longest] > n:
            tnp_longest += 1
            D[tnp_longest] = n
        else:
            next_loc = search(0, tnp_longest, n, D)
            #print(next_loc)
            D[next_loc] = n

    return D
def reverseArr(arr, n) :
    i = 0
    j = n-1
    while (i < j) :
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        i += 1
        j -= 1
N = int(input())
arr = []
m = 0
for i in range(N) :
    m = int(input())
    arr.append(m)
increasing = []
decreasing = []
increasing = lis(arr)
reverseArr(arr, len(arr))
decreasing = lds(arr)
result = 0
print(increasing)
print(decreasing)
for i in range(len(arr)) :
    result = max(result, increasing[i]+decreasing[i]-1)

print(result)
