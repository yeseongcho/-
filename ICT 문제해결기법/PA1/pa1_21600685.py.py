# 9진수와 변형된 9진수의 차이를 활용

def get_diff(x, n) :
    diff = 0
    while(n >= 0) :
        if int(x/10**n) > 4 :
            diff = diff + (10**n)
        x = x - (10**n)*int((x/10**n))
        n = n-1
        
    return diff

def count(x) :
    n = 1
    while(x >= 10**n) :
        n = n+1
    return n-1
        
def get_tenth(ninth, m) :
    result = 0
    while(m >=0 ) :
        result += int((ninth/10**m)) * 9**m
        ninth = ninth - 10**m*int((ninth/10**m))
        m -= 1
    return result

def main() :
    x = int(input())
    n = count(x)
    diff = get_diff(x, n)
    ninth = x - diff
    m = count(ninth)
    result = get_tenth(ninth, m)
    print(result)

main()

# 시간 복잡도의 경우 T(n) = O(n/10**x)로 자릿수에 따른다
# 공간 복잡도는 O(1)
