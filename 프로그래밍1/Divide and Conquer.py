def comp_MaxML(low, high, X) :
    sum = 0
    MaxML = 0
    for i in range(high, low-1, -1) :
        sum = sum + X[i]
        if sum > MaxML :
            MaxML = sum
    return MaxML

def comp_MaxMR(low, high, X) :
    sum = 0
    MaxMR = 0
    for i in range(low, high+1) :
        sum = sum + X[i]
        if sum > MaxMR :
            MaxMR = sum
    return MaxMR

def max_sub(X, lower, upper) :
    if lower == upper :
        return max(0, X[lower])
    m = (lower + upper)//2
    MaxL = max_sub(X, lower, m)
    MaxR = max_sub(X, m+1, upper)
    MaxML = comp_MaxML(0, m-1, X)
    MaxMR = comp_MaxMR(m, upper, X)
    MaxM = max(0, MaxML+MaxMR)
    return max(MaxL, MaxR, MaxM)

def main() :
    X = [1, -1, 2, -4, 51, -6, 2, -45, 25, 31, -21]
    print(max_sub(X, 0, len(X)-1))

main()
