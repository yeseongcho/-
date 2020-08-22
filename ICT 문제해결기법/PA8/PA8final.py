mountain = {}
N = int(input())
for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]

Max = 0
accum = 0
index = 0
memo = {}

def max_val(row, index, memo, a=0, b=0, c=0, d=0, result1=0, result2=0, result3=0, result4=0) :
    if (row, index) in memo :
        return memo[(row, index)]
    if index != 0 :
        a = mountain[row][index] - mountain[row][index-1]
    if index != N-1 :
        b = mountain[row][index] - mountain[row][index+1]
    if row != 0 :
        c = mountain[row][index] - mountain[row-1][index]
    if row != N-1 :
        d = mountain[row][index] - mountain[row+1][index]
    if max(a, b, c, d) <= 0 :
        memo[(row, index)] = 0
        return 0
    # 내려갈 수 있는 경우
    if a > 0 :
        #memo[(row, index)] = a
        result1 = max_val(row, index-1, memo) + a
        memo[(row, index)] = result1
    if b > 0 :
        #memo[(row, index)] = b
        result2 = max_val(row, index+1, memo) + b
        memo[(row, index)] = result2
    if c > 0 :
        #memo[(row, index)] = c
        result3 = max_val(row-1, index, memo) + c
        memo[(row, index)] = result3
    if d > 0 :
        #memo[(row, index)] = d
        result4 = max_val(row+1, index, memo) + d
        memo[(row, index)] = result1

    memo[(row, index)] = max(result1, result2, result3, result4)
    return memo[(row, index)]

for row in range(N) :
    for index in range(N) :
        accum = max_val(row, index, memo)
        Max = max(accum, Max)

print(Max)
