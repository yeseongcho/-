def quick_sort(lists) :
    if len(lists) <= 1 :
        return lists
    pivot = lists[len(lists)//2]
    less_arr, equal_arr, big_arr = [], [], []
    for i in lists :
        if i < pivot :
            less_arr.append(i)
        elif i > pivot :
            big_arr.append(i)
        else :
            equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)

def make_short(f_func, g_func, p, q) :
    for i in range(len(f_func)):
        if f_func[i][0] < p :
            f_func.remove(f_func[i])
        if f_func[i][0] >= p :
            break

    for a in range(len(f_func)-1, -1, -1) :
        #print(f_func)
        if f_func[a][0] > q :
            f_func.remove(f_func[a])
        if f_func[a-1][0] <= q :   ## 큰 부분부터 자르는 거에서 indexing 문제
            break

    for j in range(len(g_func)) :
        if g_func[j][0] < p :
            g_func.remove(g_func[j])
        if g_func[j][0] >= p :
            break

    for b in range(len(g_func)-1, -1, -1) :
        if g_func[b][0] > q :
            g_func.remove(g_func[b])
        if g_func[b-1][0] <= q :
            break

    print(f_func)
    print(g_func)

    return f_func, g_func
    
def make_quarter(f_func, g_func):
    all_func = f_func + g_func
    quarter = []
    for i in all_func :
        if i[0] not in quarter :
            quarter.append(i[0])

    quarter = quick_sort(quarter)

    #print(quarter)
    return quarter

def find_result(f_func, g_func, quarter) :
    m = 0
    n = 0
    cum = 0
    cum2 = 0
    diff = 0
    pre = 0
    Max = 0
    for i in quarter :
        cum = 0
        cum2 = 0
        if i != f_func[len(f_func)-1][0] :
            if i >= f_func[m][0] and i < f_func[m+1][0] : ## 해당 경우가 아닌 다음 경우는 언제 m을 늘려줘야지?
                cum = cum + f_func[m][1]
            if i >= f_func[m+1][0] :
                m = m + 1
        else :
            cum = f_func[len(f_func)-1][1]


        if i != g_func[len(g_func)-1][0] :
            if i >= g_func[n][0] and i < g_func[n+1][0] :
                cum2 = cum2 + g_func[n][1]
            if i >= g_func[n+1][0] :  ##
                n = n + 1
        else :
            cum2 = g_func[len(g_func)-1][1]
            break


        if i == quarter[0] :
            pre = max(cum, cum2)
            index = quarter[0]
            continue

        if cum == cum2 :
            #pre = cum
            diff = i - index

        if cum != cum2 :
            Max = max(cum, cum2)
            index = i
            result = result + diff*pre
    
    result = result + max(cum, cum2)
    return result
            
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
    
    p, q = [int(x) for x in input().split()]
    short_f_x = []
    short_f_y = []
    short_g_x = []
    short_g_y = []
    f_func, g_func = make_short(f_func, g_func, p, q)
    
    
main()
