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
U = m

Mid = 0

def binary_search(L, U) :
    Mid = (L+U)//2
    return Mid

def check_k(book, n, k, d) :
    c_dict = {}
    for date in book :
        delayed = 0
        num_tasks = book[date]
        while delayed <= d and num_tasks > k :
            if date not in c_dict :
                c_dict[date] = k
            else : c_dict[date] += k
            delayed += 1; date += 1; num_tasks -= k
        if delayed > d : return False
        c_dict[date] = num_tasks
    for date in c_dict :
        if c_dict[date] > k or date > n : return False
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

if check_k(book, n, k, d) :
    result = k

print(result)

         
