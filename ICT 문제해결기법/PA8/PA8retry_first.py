mountain = {}
N = int(input())
for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]

Max = 0
index = 0
# 전체 weight별 누적값을 저장해주는 변수
results = 0
# 현재 노드의 max weight
current_weight = 0
# current_wegiht을 저장해주는 메모리
memo = {}

# 노드의 위치 ID
current_locate = (0, 0)

a = 0
b = 0
c = 0
d = 0
def get_result(mountain, row, val, index) :
    if row == 0 :
        if index == 0 :
            if (row, index) in memo :
                results = results + memo[(row, index)][0]
                row = memo[(row, index)][1][0]
                index = memo[(row, index)][1][1]
                val = mountain[row][index]
                return get_result(mountain, row, val, index)
            a = val - mountain[row][index+1]
            b = val - mountain[row+1][index]
            if a > b :
                current_weight = a
                current_locate = (row, index+1)
            elif a < b :
                current_weight = b
                current_locate = (row+1, index)
            # 같은 경우는 어떻게 탐색할까? -- 이 경우가 코드가 길어지겠다..
            elif a == b :
                current_weight = a
                current_locate = (row, index+1)
                memo[(row, index)] = current_weight
                results = results + current_weight
                row = current_loate[0]
                index = current_locate[1]
                val = mountain[row][index]
                return get_result(mountain, row, val, index)
                current_weight = b
                current_locate = (row+1, index)
                memo[(row, index)] = current_weight
                results = results + current_weight
                row = current_loate[0]
                index = current_locate[1]
                val = mountain[row][index]
                return get_result(mountain, row, val, index)
            # 종료조건
            if max(a, b) <= 0 :
                return results
            memo[(row, index)] = (current_weight, current_locate)
            results = results + current_weight
            row = current_loate[0]
            index = current_locate[1]
            val = mountain[row][index]
            return get_result(mountain, row, val, index)
        
        elif index == N-1 : 


        else :
    elif row == N-1 :
        if index = 0 :

        elif index == N-1 :

        else :

    else :
        


# 아주 큰 for문
for row in mountain :
    for val in mountain[row] :
        index = mountain[row].index(val)
        accum = get_result()
        Max = max(accum, Max)
        accum = 0
