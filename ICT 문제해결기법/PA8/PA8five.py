
## TA님 코드가 너무 길어 죄송합니다..ㅠㅠ

## 예제 케이스는 풀었다...!! 어느 경우가 안되는 걸까...??

# 산의 정보를 담은 딕셔너리
mountain = {}
N = int(input())
maxs = 0
max_dic = {}
# 산의 정보 담음
for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]
    maxs = max(mountain[floor])
    max_dic[floor] = (maxs, mountain[floor].index(maxs))

## 위쪽, 아래쪽, 왼쪽, 오른쪽을 탐색하는 recursion 값 저장하기 위한 값들
result1 = ( )

result2 = ( )

result3 = ( )

result4 = ( )

Max = 0

# 최종 다다른 노드
node = (0, 0)

# 최종 노드 값을 저장하는 메모리 -- 이를 통해 dynamic programming 구
memo = {}

def compare(row, val, start, result1, result2, result3, result4, memo) :
    index = mountain[row].index(val)
    if row == 0 :
        if index == 0 :
            if val > mountain[row][index+1] :
                if (row, index+1) in memo :
                    result1 = memo[(row, index+1)]
                else :
                    result1 = compare(row, mountain[row][index+1], start, result1, result2, result3, result4, memo)
            if val > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result2 = memo[(row+1, index)]
                else :
                    result2 = compare(row+1, mountain[row+1][index], start, result1, result2, result3, result4, memo)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])
                

            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            else :
                #memo[(row, index)] = (row, index)
                return (row, index)

        elif index == N-1 :
            if val > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result1 = memo[(row, index-1)]
                else :
                    result1 = compare(row, mountain[row][index-1], start, result1, result2, result3, result4, memo)

            if val > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result2 = memo[(row+1, index)]
                else :
                    result2 = compare(row+1, mountain[row+1][index], start, result1, result2, result3, result4, memo)
            
            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            
            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            else :
                #memo[(row, index)] = (row, index)
                return (row, index)

        else :
            if val > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result1 = memo[(row, index-1)]
                else :
                    result1 = compare(row, mountain[row][index-1], start, result1, result2, result3, result4, memo)
         
            if val > mountain[row][index+1] :
                if (row, index+1) in memo :
                    result2 = memo[(row, index+1)]
                else :
                    result2 = compare(row, mountain[row][index+1], start, result1, result2, result3, result4, memo)

            if val > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result3 = memo[(row+1, index)]
                else :
                    result3 = compare(row+1, mountain[row+1][index], start, result1, result2, result3, result4, memo)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])

                    
            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result3[0]][result3[1]] :
                #memo[(row, index)] = result3
                return result3
            else :
                #memo[(row, index)] = (row, index)
                return (row, index)
            


    elif row == N-1 :
        if index == 0 :
            if val > mountain[row][index+1] :
                if (row, index+1) in memo :
                    result1 = memo[(row, index+1)]
                else :
                    result1 = compare(row, mountain[row][index+1], start, result1, result2, result3, result4, memo)
            if val > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row-1, mountain[row-1][index], start, result1, result2, result3, result4, memo)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            

            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            else :
                #memo[(row, index)] = (row, index)
                return (row, index)


        elif index == N-1 :
            if val > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result1 = memo[(row, index-1)]
                else :
                    result1 = compare(row, mountain[row][index-1], start, result1, result2, result3, result4, memo)
            if val > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row-1, mountain[row-1][index], start, result1, result2, result3, result4, memo)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])


            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            else :
                #memo[(row, index)] = (row, index)
                return (row, index)

        else :
            if val > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result1 = memo[(row, index-1)]
                else :
                    result1 = compare(row, mountain[row][index-1], start, result1, result2, result3, result4, memo)
            
            if val > mountain[row][index+1] :
                if (row, index+1) in memo :
                    result2 = memo[(row, index+1)]
                else :
                    result2 = compare(row, mountain[row][index+1], start, result1, result2, result3, result4, memo)
            if val > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result3 = memo[(row-1, index)]
                else :
                    result3 = compare(row-1, mountain[row-1][index], start, result1, result2, result3, result4, memo)
            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])



            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result3[0]][result3[1]] :
                #memo[(row, index)] = result3
                return result3
            else :
                return (row, index)

    else :
        if index == 0 :
            if val > mountain[row][index+1] :
                if (row, index+1) in memo :
                    result1 = memo[(row, index+1)]
                else :
                    result1 = compare(row, mountain[row][index+1], start, result1, result2, result3, result4, memo)
            if val > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row-1, mountain[row-1][index], start, result1, result2, result3, result4, memo)
            if val > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result3 = memo[(row+1, index)]
                else :
                    result3 = compare(row+1, mountain[row+1][index], start, result1, result2, result3, result4, memo)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])


            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result3[0]][result3[1]] :
                #memo[(row, index)] = result3
                return result3
            else :
                #memo[(row, index)] = (row, index)
                return (row, index)
                
        elif index == N-1 :
            if val > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result1 = memo[(row, index-1)]
                else :
                    result1 = compare(row, mountain[row][index-1], start, result1, result2, result3, result4, memo)
            if val > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row-1, mountain[row-1][index], start, result1, result2, result3, result4, memo)
            if val > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result3 = memo[(row+1, index)]
                else :
                    result3 = compare(row+1, mountain[row+1][index], start, result1, result2, result3, result4, memo)
            
            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])

            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val) == mountain[result3[0]][result3[1]] :
                #memo[(row, index)] = result3
                return result3
            else :
                #memo[(row, index)] = (row, index)
                return (row, index)



        else :
            if val > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result1 = memo[(row, index-1)]
                else :
                    result1 = compare(row, mountain[row][index-1], start, result1, result2, result3, result4, memo)
            if val > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row-1, mountain[row-1][index], start, result1, result2, result3, result4, memo)
            if val > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result3 = memo[(row+1, index)]
                else :
                    result3 = compare(row+1, mountain[row+1][index], start, result1, result2, result3, result4, memo)

            if val > mountain[row][index+1] :
                if (row, index+1) in memo :
                    result4 = memo[(row, index+1)]
                else :
                    result4 = compare(row, mountain[row][index+1], start, result1, result2, result3, result4, memo)


            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])

            if result4 == () :
                result4 = (row, max_dic[row][1])

            if min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], mountain[result4[0]][result4[1]], val) == mountain[result1[0]][result1[1]] :
                #memo[(row, index)] = result1
                return result1
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], mountain[result4[0]][result4[1]], val) == mountain[result2[0]][result2[1]] :
                #memo[(row, index)] = result2
                return result2
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], mountain[result4[0]][result4[1]], val) == mountain[result3[0]][result3[1]] :
                #memo[(row, index)] = result3
                return result3
            elif min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], mountain[result4[0]][result4[1]], val) == mountain[result4[0]][result4[1]] :
                #memo[(row, index)] = result4
                return result4
            else :
                #memo[(row, index)] = (row, index)
                return (row, index)            

# 이중 for loop를 통해 하나씩 searching...!
for row in mountain :
    for val in mountain[row] :
        start = val
        index = mountain[row].index(val)
        node = compare(row, val, start, result1, result2, result3, result4, memo)
        print(node)
        Max = max(Max, val - mountain[node[0]][node[1]])
        memo[(row, index)] = node

print(Max)
