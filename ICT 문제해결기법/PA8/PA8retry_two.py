mountain = {}
N = int(input())
for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]

Max = 0
accum = 0
index = 0
# 전체 weight별 누적값을 저장해주는 변수 - recursive는 4번의 case가 있으므로 총 4개의 결과값
result1 = 0
result2 = 0
result3 = 0
result4 = 0
# 최종값
results = 0
# weight을 저장해주는 메모리
memo = {}
a = 0
b = 0
c = 0
d = 0
def get_result(mountain, row, val, index, results, a=0, b=0, c=0, d=0, result1= 0, result2=0,result3=0,result4=0) :
    if (row, index) in memo :
        results = results + memo[(row, index)][0]
        row = memo[(row, index)][1][0]
        index = memo[(row, index)][1][1]
        val = mountain[row][index]
        return get_result(mountain, row, val, index, results)
    # 위쪽
    if row != 0 :
        a = val - mountain[row-1][index]
    # 아래쪽
    if row != N-1 :
        b = val - mountain[row+1][index]
    # 왼쪽
    if index != 0 :
        c = val - mountain[row][index-1]
    if index != N-1 :
        d = val - mountain[row][index+1]
    # 더 이상 내려갈 수 없는 종료 조건
    if max(a, b, c, d) <= 0 :
        memo[(row, index)] = (0, (row, index))
        return results
    if max(a, b, c, d) == a :
        results = a
        result1 = get_result(mountain, row-1, mountain[row-1][index], index, results)

    if max(a, b, c, d) == b :
        results = b
        result2 = get_result(mountain, row+1, mountain[row+1][index], index, results)

    if max(a, b, c, d) == c :
        results = c
        result3 = get_result(mountain, row, mountain[row][index-1], index-1, results)

    if max(a, b, c, d) == d :
        results = d
        result4= get_result(mountain, row, mountain[row][index+1], index+1, results)

    if max(result1, result2, result3, result4) == result1 :
        results = results + a
        memo[(row, index)] = (a, (row-1, index))
        return get_result(mountain, row-1, mountain[row-1][index], index, results)
    elif max(result1, result2, result3, result4) == result2 :
        results = results + b
        memo[(row, index)] = (b, (row+1, index))
        return get_result(mountain, row+1, mountain[row+1][index], index, results)
    elif max(result1, result2, result3, result4) == result3 :
        results = results + c
        memo[(row, index)] = (c, (row, index-1))
        return get_result(mountain, row, mountain[row][index-1], index-1, results)
    else :
        results = results + d
        memo[(row, index)] = (d, (row, index+1))
        return get_result(mountain, row, mountain[row][index+1], index+1, results)
    
for row in mountain :
    for val in mountain[row] :
        index = mountain[row].index(val)
        accum = get_result(mountain, row, val, index, results)
        Max = max(accum, Max)
        accum = 0
