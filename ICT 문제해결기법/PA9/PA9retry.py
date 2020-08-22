import collections

n = 0
d = 0
m = 0

n, d, m = [int(x) for x in input().split()]

date = [int(x) for x in input().split()]
book = {}
for i in date :
    if i not in book :
        book[i] = 1
    else :
        book[i] += 1

L = 1
U = max(book.values())
Mid = 0
def binary_search(L, U) :
    Mid = (L+U)//2
    return Mid
def check_k(book, n, k, d) :
    waiting = 0
    limit = k*d
    for i in range(1, n+1) :
        if i not in book :
            book[i] = 0
        waiting += book[i] - k
        if waiting<0 : waiting=0
        if waiting>limit : return False
    return True
k = binary_search(L, U)
result = 0
while L != U :
    if check_k(book, n, k, d) :
        result = k
        U = k - 1
        k = binary_search(L, U)
    else :
        L = k + 1
        k = binary_search(L, U)

if check_k(book, n, k, d) : result = k

print(result)



