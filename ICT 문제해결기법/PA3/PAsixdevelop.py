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

## runtime error는 해결했지만... time limit이 남았다
def find_index_p(func, p, start, end) :
    mid = (start+end)//2
    if p <= func[0][0] :
        return 0
    elif p == func[mid][0] :
        return mid
    elif p < func[mid][0] :
        if p >= func[mid-1][0] and p < func[mid][0] :
            return mid-1
        else :
            return find_index_p(func, p, start, mid-1)
    else : 
        if p > func[mid][0] and p < func[mid+1][0] :
            return mid
        elif p == func[mid+1][0] :
            return mid+1
        else :
            return find_index_p(func, p, mid+1, end)
    

def find_index_q(func, q, start, end) :
    mid = (start+end)//2
    if q >= func[len(func)-1][0] :
        return len(func)-1
    elif q == func[mid][0] :
        return mid
    elif q < func[mid][0] :
        if q >= func[mid-1][0] and q < func[mid][0] :
            return mid-1
        else :
            return find_index_q(func, q, start, mid-1)
    else : 
        if q > func[mid][0] and q < func[mid+1][0] :
            return mid
        elif q == func[mid+1][0] :
            return mid+1
        else :
            return find_index_q(func, q, mid+1, end)
        
     
        
# 시간 복잡도를 어떻게 해결할까
def make_short(func, p, q, short_x, short_y) :
    #short_y = short_f_y + short_g_y
    Maximize = 0
    #v = 0
    m = 0
    n = 0
    #r = 0
    #o = 0
    Max = 0
    if func[0][0] > q :
        short_x.append(0)
        short_y.append(0)
        return short_x, short_y, Maximize, Max
    elif func[len(func)-1][0] < p :
        Maximize = func[len(func)-1][1]
        return [p, q],[Maximize], Maximize, Max
    elif func[0][0] == q :
        short_x = [p, q]
        short_y = [func[0][1]]
        return [p, q], [func[0][1]], Maximize, Max
    else :
        if len(func) == 1 :
            short_x.append(func[0][0])
            short_y.append(func[0][1])
        else :
            m = find_index_p(func, p, 0, len(func)-1)
            #print(m)
            #n = find_index_q(func, q, 0, len(func)-1)
            #print(n)
            if func[m][0] <= p and func[m+1][0] > p :
                short_x.append(p)
                short_y.append(func[m][1])
                Max = func[m][1]
                m = m+1
            for s in range(m, len(func)) :
                if func[s][0] > q :
                    break
                if s == 0 :
                    short_x.append(func[s][0])
                    short_y.append(func[s][1])
                    Max = func[s][1]

                elif s == n :
                    if func[s][0] == func[s-1][0] :
                        if Max > func[s][1] :
                            short_y.append(Max)
                        else :
                            Max = func[s][1]
                            short_y_.append(Max)
                    else :
                        if Max > func[s][1] :
                            short_x.append(func[s][0])
                            short_y.append(Max)
                        else :
                            short_x.append(func[s][0])
                            Max = func[s][1]
                            short_y.append(Max)

                else :
                    if func[s][0] == func[s-1][0] :
                        if Max > func[s][1] :
                            short_y.append(Max)
                        else :
                            Max = func[s][1]
                            short_y.pop()
                            short_y.append(Max)
                    elif func[s][0] == func[s+1][0] :
                        short_x.append(func[s][0])
                        if Max > func[s][1] :
                            short_y.append(Max)
                        else :
                            Max = func[s][1]
                            short_y.append(Max)
                    else :
                        short_x.append(func[s][0])
                        if Max > func[s][1] :
                            short_y.append(Max)
                        else :
                            Max = func[s][1]
                            short_y.append(Max)

    
    
    #print(short_x)
    #print(short_y)
    return short_x, short_y, Maximize, Max
        

def find_result(short_x, short_y, p, q, Maximize, func, Max) :
    diff = 0   
    result = 0
    if Maximize != 0 :
        result = Maximize * (q - p) + Maximize
        return result
    if short_y == [0] :
        result = 0
        return result
    if func[0][0] == q :
        result = func[0][1]
        return result
    elif func[0][0] > q :
        result = 0
        return result
    elif func[len(func)-1][0] <= p :
        result = (q-p)*func[len(func)-1][1] + func[len(func)-1][1]
        return result
    height = 0
    for i in range(len(short_x)) :
        if i == len(short_x)-1 :
            break
        diff = short_x[i+1] - short_x[i]
        height = short_y[i]
        #print(diff*height)
        result = result + diff*height
        #print(result)

    result = result + Max
    if short_x[len(short_x)-1] < q :
        result = result + Max
    #result = result + Max
        
        
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
    func = f_func + g_func
    func = quick_sort(func)
    p, q = [int(x) for x in input().split()]
    short_x = []
    short_y = []
    short_x, short_y, Maximize, Max = make_short(func, p, q, short_x, short_y)
    result = find_result(short_x, short_y, p, q, Maximize, func, Max)
    result = result % 10007
    print(result)
    
main()


