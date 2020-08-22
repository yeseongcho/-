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
def make_short(f_func, g_func, p, q, short_f_x, short_f_y, short_g_x, short_g_y) :
    #short_y = short_f_y + short_g_y
    Maximize = 0
    v = 0
    m = 0
    n = 0
    r = 0
    o = 0
    if f_func[0][0] > q and g_func[0][0] > q :
        short_f_x.append(0)
        short_g_x.append(0)
        short_f_y.append(0)
        short_g_y.append(0)
        return short_f_x, short_f_y, short_g_x, short_g_y, Maximize
    elif f_func[len(f_func)-1][0] < p and g_func[len(g_func)-1][0] < p :
        Maximize = max(f_func[len(f_func)-1][1], g_func[len(g_func)-1][1])
        return [p], [Maximize], [q], [Maximize], Maximize
    
    elif f_func[0][0] == q :
        short_f_x = [q]
        short_f_y = [f_func[0][1]]
    elif f_func[0][0] > q :
        short_f_x = [q]
        short_f_y = [0]
    
    elif f_func[len(f_func)-1][0] <= p :
        short_f_x = [p]
        short_f_y = [f_func[len(f_func)-1][1]]

    else :
        if len(f_func) == 1 :
            short_f_x.append(f_func[0][0])
            short_f_y.append(f_func[0][1])
        else :
            m = find_index_p(f_func, p, 0, len(f_func)-1)
            #print(m)
            n = find_index_q(f_func, q, 0, len(f_func)-1)
            #print(n)
            if f_func[m][0] <= p and f_func[m+1][0] > p :
                short_f_x.append(p)
                short_f_y.append(f_func[m][1])
                m = m+1
            for s in range(m, n+1) :
               # if f_func[s][0] <= p and f_func[s+1][0] > p :
                #    short_f_x.append(p)
                 #   short_f_y.append(f_func[s][1])
                  #  continue
                #if f_func[s][0] > q :
                 #   break
                if f_func[s][0] >= p and f_func[s][0] <= q :
                    short_f_x.append(f_func[s][0])
                    short_f_y.append(f_func[s][1])
                    #if f_func[s][0] not in short_f_x :
                     #   short_f_x.append(f_func[s][0])
                    #if f_func[s][1] not in short_f_y :
                     #   short_f_y.append(f_func[s][1])            

    if g_func[0][0] == q :
        short_g_x = [q]
        short_g_y = [g_func[0][1]]
    elif g_func[0][0] > q :
        short_g_x = [q]
        short_g_y = [0]
    elif g_func[len(g_func)-1][0] <= p :
        short_g_x = [p]
        short_g_y = [g_func[len(g_func)-1][1]]
        
    else :
        if len(g_func) == 1 :
            short_g_x.append(g_func[0][0])
            short_g_y.append(g_func[0][1])
        else :
            r = find_index_p(g_func, p, 0, len(g_func)-1)
            o = find_index_q(g_func, q, 0, len(g_func)-1)
            if g_func[r][0] <= p and g_func[r+1][0] > p :
                short_g_x.append(p)
                short_g_y.append(g_func[r][1])
                r = r+1
            for j in range(r, o+1) :
                #if g_func[j][0] <= p and g_func[j+1][0] > p :
                 #   short_g_x.append(p)
                  #  short_g_y.append(g_func[j][1])
                   # continue
                #if g_func[j][0] > q :
                 #   break
                if g_func[j][0] >= p and g_func[j][0] <= q :
                    if g_func[j][0] >= f_func[v][0] and g_func[j][1] < f_func[v][1] :
                        continue
                    if g_func[j][0] >= f_func[v][0] and g_func[j][1] >= f_func[v][1] and v <= len(f_func)-2 :
                        v = v+1
                    short_g_x.append(g_func[j][0])
                    short_g_y.append(g_func[j][1])
                   # if g_func[j][0] not in short_g_x :
                    #    short_g_x.append(g_func[j][0])
                    #if g_func[j][1] not in short_g_y :
                     #   short_g_y.append(g_func[j][1])
                    
    #print(short_g_y)        
    if len(short_f_x) == 0 and f_func[len(f_func)-1][0] < p :
        short_f_x.append(g_func[len(g_func)-1][0])
        short_f_y.append(f_func[len(f_func)-1][1])
    if len(short_g_x) == 0 and g_func[len(g_func)-1][0] < p :
        short_g_x.append(f_func[len(f_func)-1][0])
        short_g_y.append(g_func[len(g_func)-1][1])
    
    #print(short_g_y)
    return short_f_x, short_f_y, short_g_x, short_g_y, Maximize
        
## 시간 복잡도...    
def make_quarter(short_f_x, short_g_x, p, q):
    quarter=[]
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

def find_result(short_f_x, short_g_x, short_f_y, short_g_y, quarter, p, q, Maximize, f_func, g_func) :
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
    if f_func[0][0] == q and g_func[0][0] == q :
        result = max(f_func[0][1], g_func[0][1])
        return result
    elif f_func[0][0] > q and g_func[0][0] == q :
        result = g_func[0][1]
        return result
    elif f_func[0][0] == q and g_func[0][0] > q :
        result = f_func[0][1]
        return result
    elif f_func[len(f_func)-1][0] <= p and g_func[len(g_func)-1][0] <= p :
        result = max(f_func[len(f_func)-1][1], g_func[len(g_func)-1][1]) * (q - p) + max(f_func[len(f_func)-1][1], g_func[len(g_func)-1][1])
        return result

    for i in range(len(quarter)) :
        cum = 0
        cum2 = 0
        if m < len(short_f_x)-1 :
            if quarter[i] >= short_f_x[m] and quarter[i] < short_f_x[m+1] :
                cum = short_f_y[m]
            elif quarter[i] >= short_f_x[m+1] : # 예외 케이스로 하면 조금 더 빠르지 않을까.. 하지만 아닐 수도 있는 가능성
                m = m + 1
                cum = short_f_y[m]
                #if quarter[i] == short_f_x[m] : # 꼭 '==' 이거여야 하는가
                 #   cum = short_f_y[m]
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
                cum2 = short_g_y[n]
                #if quarter[i] == short_g_x[n] :
                 #   cum2 = short_g_y[n]
        elif n == len(short_g_x)-1 and n != 0 :
            cum2 = short_g_y[len(short_g_y)-1]
            #if m != len(short_f_x) - 1 and n != len(short_g_x) - 1 :
                #if quarter[i] >= short_f_x[m+1] and quarter[i] >= short_g_x[n+1] :
                    #i = i - 1
                    #continue

        ## g의 길이가 1인 케이스 필요
        elif len(short_g_x) - 1 == 0 and n == 0:
            if quarter[i] >= short_g_x[n] :
                cum2 = short_g_y[n]


        if quarter[i] == quarter[0] :
            pre = max(cum, cum2)
            index = quarter[i]
            continue

        elif cum == cum2 :
            diff = quarter[i] - index
            result = result + diff*pre 
            
            # 이전 값 저장
            
            index = quarter[i]
            #pres = pre
            pre = cum
            
    
        elif cum != cum2 :
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
    #print(result)
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
    if (f_func[0][0] >= q and g_func[0][0] >= q) or (f_func[len(f_func)-1][0] <= p and g_func[len(g_func)-1][0] <= p):
        quarter = []
        result = find_result(short_f_x, short_g_x, short_f_y, short_g_y, quarter, p, q, Maximize, f_func, g_func)
        result = result % 10007
        print(result)
    else :
        quarter = make_quarter(short_f_x, short_g_x, p, q)
        result = find_result(short_f_x, short_g_x, short_f_y, short_g_y, quarter, p, q, Maximize, f_func, g_func)
        result = result % 10007
        print(result)
    
main()

