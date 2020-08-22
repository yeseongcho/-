def find_index_p(func, p, start, end) :
    mid = (start+end)//2
    if p < func[0][0] :
        return 0
    elif p == func[mid][0] :
        return mid
    elif p < func[mid][0] :
        if p >= func[mid-1][0] and p < func[mid][0] :
            return mid-1
        else :
            return find_index_p(func, p, 0, mid)
    elif p > func[mid][0] :
        if p > func[mid][0] and p < func[mid+1][0] :
            return mid
        elif p == func[mid+1][0] :
            return mid+1
        else :
            return find_index_p(func, p, mid, len(func)-1)

        
def find_index_q(func, q) :
    mid = len(func)//2
    if q > func[len(func)-1][0] :
        return func[len(func)-1][1]
    elif q == func[mid][0] :
        return mid
    elif q < func[mid][0] :
        if q >= func[mid-1][0] and q < func[mid][0] :
            return mid-1
        else :
            return find_index_q(func[:mid], q)
    elif q > func[mid][0] :
        if q > func[mid][0] and q <= func[mid+1][0] :
            return mid+1
        else :
            return find_index_q(func[mid:], q)   


def main() :
    f_data = int(input())
    f_func = []
    for i in range(f_data) :
        f_input = [int(x) for x in input().split()]
        f_func.append((f_input[0], f_input[1]))
    g_data = int(input())
    g_func = []
    for i in range(g_data) :
        g_input = [int(x) for x in input().split()]
        g_func.append((g_input[0], g_input[1]))
    #f_func = quick_sort(f_func)
    #g_func = quick_sort(g_func)  ## sorting이 되어서 들어오는 건가? 아니면 우리가 sorting을 해주어야 하는가?
    p, q = [int(x) for x in input().split()]
    print(find_index_p(f_func, p, 0, len(f_func)-1))
    #print(find_index_q(g_func, q))
main()
