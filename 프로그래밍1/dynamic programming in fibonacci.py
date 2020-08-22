def fast_fib(n, memo={}) :
    if n in memo :
        return memo[n]
    if n==1 or n==2 :
        return 1
    result = fast_fib(n-1, memo) + fast_fib(n-2, memo)
    memo[n] = result
    return result

print(fast_fib(120))


# 만약 fast_fib(n, memo)여기서의 시간복잡성은
# O(n)에 비례해 증가하게 된다.
