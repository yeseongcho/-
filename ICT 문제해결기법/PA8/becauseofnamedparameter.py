mountain = {}
N = int(input())
for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]

Max = 0
accum = 0
index = 0
memo = {}
results = 0
result1 = 0
result2 = 0
result3 = 0
result4 = 0
a = 0
b = 0
c = 0
d = 0
def max_edge(row,index,val,results, memo, a, b, c, d, result1, result2, result3, result4) :
    # 메모리에 있는 경우
    if (row, index) in memo :
        if (row, index) == memo[(row,index)][1] :
            return results
        #print(memo[(row, index)][0])
        results = results + memo[(row,index)][0]
        #print(results)
        row = memo[(row, index)][1][0]
        index = memo[(row, index)][1][1]
        val = mountain[row][index]
        return max_edge(row,index,val,results, memo, a, b, c, d, result1, result2, result3, result4)
    # boundary인 경우를 다루기 위해
    if index != 0 :
        a = val - mountain[row][index-1]
    if index != N-1 :
        b = val - mountain[row][index+1]
    if row != 0 :
        c = val - mountain[row-1][index]
    if row != N-1 :
        d = val - mountain[row+1][index]
    # 더 이상 내려갈 수 없는 경우 -- 종료 케이스
    if max(a, b, c, d) <= 0 :
        memo[(row, index)] = (0, (row, index))
        return results
    if max(a, b, c, d) == a :
        memo[(row, index)] = (a, (row, index-1))
        results = a + results
        #results = a
        result1 = max_edge(row, index-1, mountain[row][index-1], results, memo, a, b, c, d, result1, result2, result3, result4)
        results = 0
    if max(a, b, c, d) == b :
        memo[(row, index)] = (b, (row, index+1))
        #results = b
        results = b + results
        result2 = max_edge(row, index+1, mountain[row][index+1], results, memo, a, b, c, d, result1, result2, result3, result4)
        results = 0
    if max(a, b, c, d) == c :
        memo[(row, index)] = (c, (row-1, index))
        #results = c
        results = c + results 
        result3 = max_edge(row-1, index, mountain[row-1][index], results, memo, a, b, c, d, result1, result2, result3, result4)
        results = 0
    if max(a, b, c, d) == d :
        memo[(row, index)] = (d, (row+1, index))
        #results = d
        results = d + results
        result4 = max_edge(row+1, index, mountain[row+1][index], results, memo, a, b, c, d, result1, result2, result3, result4)
        results = 0

    if max(result1, result2, result3, result4) == result1 :
        #results = results + result1
        #memo[(row, index)] = (result1, (row, index-1))
        return result1
        
    elif max(result1, result2, result3, result4) == result2 :
        #results = result2
        #memo[(row, index)] = (result2, (row, index+1))
        return result2
    elif max(result1, result2, result3, result4) == result3 :
        #results = results + result3
        #memo[(row, index)] = (result3, (row-1, index))
        return result3
    else :
        #results = results + result4
        #memo[(row, index)] = (result4, (row+1, index))
        return result4
    
for row in mountain :
    for val in mountain[row] :
        index = mountain[row].index(val)
        results = 0
        accum = max_edge(row,index,val,results, memo, a, b, c, d, result1, result2, result3, result4)
        #print(accum)
        #print(memo)
        Max = max(accum, Max)
print(Max)
