"""
Name: 조예성
Student ID : 21600685
Description : 피보나치 함수를 구하기 위해 함수가 실행 될때, 프로그램이 현재 어느 부분을 실행하고 있는 지를 실시간으로 보여주기 위한 함수입니다. 메모리를 활용한 경우와 활용하지 않은 경우 두 가지를 다 보여주는 함수입니다.
"""



# 피보나치 함수
def fib(n, count=0, level = -1) :
    level += 1 # fib함수가 recursive하게 호출될 때마다 level을 늘려줌. 깊이가 깊어질수록 우측으로 이동해 표시하게 해주기 위함.
    if n==1 or n==2 : # Base case
        #level = -1
        print(" "*4*level, "fib(", n,")")
        return 1, count
    count += 1 # recrusive case의 경우 count 1 늘려줌
    print(" "*4*level, "fib(", n, ")")
    # recursive case
    r1, count = fib(n-1, count, level) # 깊이 우선 탐색, 이 쪽부터 recursive
    r2, count = fib(n-2, count, level) # 위에 것이 base case에 도착한 뒤에, 하나씩 실행
    level -= 1 # Base case까지 간 뒤, 하나씩 return값들을 취할때, level을 낮추기 위함
    return r1+r2, count

# 메모리를 활용한 피보나치 함수
def fast_fib(n, memo={}, count=0, level = -1) :
    level += 1 # fib함수가 recursive하게 호출될 때마다 level을 늘려줌. 깊이가 깊어질수록 우측으로 이동해 표시하게 해주기 위함.
    if n in memo : # 해당 recursive case가 이미 memory에 저장되어있는 경우
        print(" "*4*level, "fib(", n, "), Already Computed") 
        return memo[n], count 
    if n==1 or n==2 : # Base case
        print(" "*4*level, "fib(", n, ")")
        return 1, count
    count += 1 # recrusive case
    print(" "*4*level, "fib(", n, ")")
    r1, count = fast_fib(n-1, memo, count, level) # 깊이 우선 탐색, 이 쪽부터 recursive
    r2, count = fast_fib(n-2, memo, count, level) # 위에 것이 base case에 도착한 뒤에, 하나씩 실행
    level -= 1 # base case이후 하나씩 다시 올라가는 경우를 display해야할 때, level을 낮추어야 하므로 recrusive이후에 위치
    result = r1+r2 # 메모리에 저장할 recursive 결과 값
    memo[n] = result
    return result, count


def main() :

    value, count = fib(7) # 피보나치 함수 실행
    print('\n')
    print("result=", value, "count=", count)

    value, count = fast_fib(7) # 메모리를 활용한 피보나치 함수 실행
    print('\n')
    print("result=", value, "count=", count)
main()    

