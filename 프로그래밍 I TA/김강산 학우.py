def main1():
    value, count = fast_fib(7)
    print ("result =", value, "count =", count)
    
def fast_fib(n, memo = {}, count = 0, level = 0):
    if n in memo: #memo 체크
        display(n, level, flag = True)
        return memo[n]
    display(n, level)
    if n == 1 or n == 2: #base case
        return 1, count
    count += 1
    r1, count = fast_fib(n-1, memo, count, level+1)
    r2, count = fast_fib(n-2, memo, count, level+1)
    result = r1+ r2
    memo[n] = result
    return result, count

def display(n, level, flag = False):
    if flag:
        print (" " * 4 * level + "fib("+str(n)+")" + "Already solved")
    else:
        print (" " * 4 * level + "fib("+str(n)+")")


main1()
