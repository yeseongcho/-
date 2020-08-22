# https://shoark7.github.io/programming/algorithm/3-LIS-algorithms
def lis(arr):
    # C[i] means smallest last number of lis subsequences whose length are i
    INF = float('inf')
    C = [INF] * (len(arr)+1)
    C[0] = -INF
    C[1] = arr[0]
    tmp_longest = 1
    for n in arr:
        if C[tmp_longest] < n:
            tmp_longest += 1
            C[tmp_longest] = n
        else:
            next_loc = search(0, tmp_longest, n, C)
            #print(next_loc)
            C[next_loc] = n

    return tmp_longest

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

arr = [1,4,6,8,3,5,6,7]
tmp_longest = 0
tmp_longest = lis(arr)
print(tmp_longest)
