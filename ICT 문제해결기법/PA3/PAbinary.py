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


def find_index_p(func, p) :
    
    if p <= func[len(func)//2][0] :
        for i in range(len(func)//2) :
            if p >= func[i][0] and p <= func[i+1][0] :
                return i
        return 0
    elif p >= func[len(func)//2][0] :
        for i in range(len(func)-1, len(func)//2) :
            if p >= func[i][0] and p <= func[i+1][0] :
                return i
        return len(func)-1
def find_index_q(func, q) :
    
    if q <= func[len(func)//2][0] :
        for i in range(len(func)//2) :
            if q >= func[i][0] and q <= func[i+1][0] :
                return i
        return 0
    elif q >= func[len(func)//2][0] :
        for i in range(len(func)//2, len(func)) :
            if q >= func[i][0] and q <= func[i+1][0] :
                return i
        return len(func)-1
                
                
                

# 시간 복잡도를 어떻게 해결할까
def make_short(f_func, g_func, p, q, short_f_x, short_f_y, short_g_x, short_g_y) :
    #short_y = short_f_y + short_g_y
    Maximize = 0
    v = 0
    p_index = 0
    q_index = 0
    if f_func[0][0] > q and g_func[0][0] > q :
        short_f_x.append(0)
        short_g_x.append(0)
        short_f_y.append(0)
        short_g_y.append(0)
        return short_f_x, short_f_y, short_g_x, short_g_y, Maximize
    elif f_func[len(f_func)-1][0] < p and g_func[len(g_func)-1][0] < p :
        Maximize = max(f_func[len(f_func)-1][1], g_func[len(g_func)-1][1])
       return [p], [Maximize], [q], [Maximize], Maximize


    
    if f_func[0][0] != q and f_func[len(f_func)-1][0] != p :
        if len(f_func) == 1 :
            short_f_x.append(f_func[0][0])
            short_f_y.append(f_func[0][1])
        else :
            p_index = find_index_p(f_func, p)
            q_index = find_index_q(f_func, q)
            for m in range(p_index, q_index+1) :
                
                
        
        

        
    else :
        if f_func[0][0] == q :
            short_f_x = [q]
            short_f_y = [f_func[0][1]]
        elif f_func[len(f_func)-1][0] == p :
            short_f_x = [p, q]
            short_f_y = [f_func[len(f_func)-1][1]]

        
    
    

    



    
    find_index(f_func, p, q)
                













    

    for j in g_func :

        if j == g_func[0] :
            for s in range(len(g_func)-1):
                if g_func[s][0] <= p and g_func[s+1][0] > p :
                    short_g_x.append(p)
                    short_g_y.append(g_func[s][1])
                    break
                else :
                    break

        if j[0] > q :
            break
                    
        if j[0] >= p and j[0] <= q :
            if j[0] >= f_func[v][0] and j[1] < f_func[v][1] : # 지배 케이스
                continue
            if j[0] >= f_func[v][0] and j[1] >= f_func[v][1] and v <= len(f_func)-2:
                v = v + 1
            if j[0] not in short_g_x :
                short_g_x.append(j[0])
            if j[1] not in short_g_y :
                short_g_y.append(j[1])
        
        
    if len(short_f_x) == 0 and f_func[len(f_func)-1][0] < p :
        short_f_x.append(g_func[len(g_func)-1][0])
        short_f_y.append(f_func[len(f_func)-1][1])
    if len(short_g_x) == 0 and g_func[len(g_func)-1][0] < p :
        short_g_x.append(f_func[len(f_func)-1][0])
        short_g_y.append(g_func[len(g_func)-1][1])
    

    return short_f_x, short_f_y, short_g_x, short_g_y, Maximize
        
## 시간 복잡도...    
def make_quarter(short_f_x, short_g_x, p, q):
    quarter = [p]
    for i in short_f_x :
        if i not in quarter :
            if i <= q :
                quarter.append(i)
            else :
                break
            
    for j in short_g_x :
        if j not in quarter :
            if j <= q :
                quarter.append(j)
            else :
                break
        
    
    quarter = quick_sort(quarter)
    if q != quarter[len(quarter)-1] :
        if q not in quarter :
            quarter.append(q)
    
    return quarter

def find_result(short_f_x, short_g_x, short_f_y, short_g_y, quarter, p, q, Maximize) :
    m = 0
    n = 0
    cum = 0
    cum2 = 0
    diff = 0
    pre = 0
    Max = 0
    index = 0
    result = 0
    pres = 0
    if Maximize != 0 :
        result = Maximize * (q - p) + Maximize
        return result
    if short_f_y == [0] and short_g_y == [0] :
        result = 0
        return result
    for i in range(len(quarter)) :
        cum = 0
        cum2 = 0
        if m < len(short_f_x)-1 :
            if quarter[i] >= short_f_x[m] and quarter[i] < short_f_x[m+1] :
                cum = short_f_y[m]
            elif quarter[i] >= short_f_x[m+1] : # 예외 케이스로 하면 조금 더 빠르지 않을까.. 하지만 아닐 수도 있는 가능성
                m = m + 1
                if quarter[i] == short_f_x[m] : # 꼭 '==' 이거여야 하는가
                    cum = short_f_y[m]
        elif m == len(short_f_x) - 1 and m != 0: # 예외 케이스로 하면 조금 더 빠르지 않을까.. 하지만 아닐 수도 있는 가능성
            cum = short_f_y[len(short_f_y)-1]
        
        ## f의 길이가 1인 케이스 필요
        elif len(short_f_x) -1 == 0 and m == 0: # 예외 케이스로 하면 조금 더 빠르지 않을까.. 하지만 아닐 수도 있는 가능성
            if quarter[i] >= short_f_x[m] :
                cum = short_f_y[m]
        
        
 
        if n < len(short_g_x)-1 :
            
            if quarter[i] >= short_g_x[n] and quarter[i] < short_g_x[n+1] :
                cum2 = short_g_y[n]

            elif quarter[i] >= short_g_x[n+1] :
                n = n + 1
                if quarter[i] == short_g_x[n] :
                    cum2 = short_g_y[n]
        elif n == len(short_g_x)-1 and n != 0 :
            cum2 = short_g_y[len(short_g_y)-1]
            #if m != len(short_f_x) - 1 and n != len(short_g_x) - 1 :
             #   if quarter[i] >= short_f_x[m+1] and quarter[i] >= short_g_x[n+1] :
              #      i = i - 1
               #     continue

        ## g의 길이가 1인 케이스 필요
        elif len(short_g_x) - 1 == 0 and n == 0:
            if quarter[i] >= short_g_x[n] :
                cum2 = short_g_y[n]

        if quarter[i] == quarter[0] :
            pre = max(cum, cum2)
            index = quarter[i]
            continue

        if cum == cum2 :
            diff = quarter[i] - index
            result = result + diff*pre 
            
            # 이전 값 저장
            
            index = quarter[i]
            #pres = pre
            pre = cum
            
    
        if cum != cum2 :
            Max = max(cum, cum2)
            if cum == 0 :
                cum = pre
            if cum2 == 0 :
                cum2 = pre
            
            diff = quarter[i] - index
            # 이전 값 저장
            result = result + diff*pre
            #print(result)
            index = quarter[i]
            #pres = pre
            pre = Max
    
        
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
    #f_func = quick_sort(f_func)
    #g_func = quick_sort(g_func)  ## sorting이 되어서 들어오는 건가? 아니면 우리가 sorting을 해주어야 하는가?
    p, q = [int(x) for x in input().split()]
    short_f_x = []
    short_f_y = []
    short_g_x = []
    short_g_y = []
    short_f_x, short_f_y, short_g_x, short_g_y, Maximize = make_short(f_func, g_func, p, q, short_f_x, short_f_y, short_g_x, short_g_y)
    #print(short_f_x)
    #print(short_f_y)
    #print(short_g_x)
    #print(short_g_y)
    quarter = make_quarter(short_f_x, short_g_x, p, q)
    #print(quarter)
    result = find_result(short_f_x, short_g_x, short_f_y, short_g_y, quarter, p, q, Maximize)
    result = result % 10007
    print(result)
    
main()

