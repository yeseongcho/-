mountain = {}

N = int(input())

for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]

result = (0, 0)
result2 = (0, 0)
result3 = (0, 0)
result4 = (0, 0)
Max = 0
node = (0, 0)

index = 0
memo = {}
def compare(row, val, start, result, result2, result3, result4, memo) :
    index = mountain[row].index(val) 
    if row == 0 :
        if index == 0 :
            # 좌우 이동 가능
            if mountain[row][index] > mountain[row][index+1] :
                # 메모리 안에 있는 경우
                if (row, index+1) in memo :
                    result = memo[(row, index+1)]
                else :
                    result = compare(row, mountain[row][index+1], start, result, result2, result3, result4, memo)
            # 상하 이동 가능
            if mountain[row][index] > mountain[row+1][index] :

                # 메모리 안에 있는 경우
                if (row+1, index) in memo :
                    result2 =  memo[(row+1, index)]
                else :
                    result2 = compare(row+1, mountain[row][index] , start, result, result2, result3, result4, memo)

            if max(result[1], result2[1], mountain[row][index]) == result[1] :
                return result
            elif max(result[1], result2[1], mountain[row][index]) == result2[1] :
                return result2
            else :
                return (row, mountain[row][index])                  
        elif index == N-1 :
            # 좌우 이동 가능
            if mountain[row][index] > mountain[row][index-1] :
                # 메모리 안에 있는 경우
                if (row, index-1) in memo :
                    result =  memo[(row, index-1)]
                else :
                    result =  compare(row, mountain[row][index-1], start, result, result2, result3, result4, memo)
            # 상하 이동 가능
            if mountain[row][index] > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result2 =  memo[(row+1,index)]
                else :
                    result2 =  compare(row+1, mountain[row+1][index], start, result, result2, result3, result4, memo)

            if max(result[1], result2[1], mountain[row][index]) == result[1] :
                return result
            elif max(result[1], result2[1], mountain[row][index]) == result2[1] :
                return result2
            else :
                return (row, mountain[row][index])            
        else :
            # 우측으로 가는 경우
            if mountain[row][index] >  mountain[row][index+1] :
                if (row, index+1) in memo :
                    result =  memo[(row, index+1)]
                else :
                    result = compare(row, mountain[row][index+1], start, result, result2, result3, result4, memo)
            # 좌측으로 가는 경우
            if mountain[row][index] > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result2 =  memo[(row, index-1)]
                else :
                    result2 =  compare(row, mountain[row][index-1], start, result, result2, result3, result4, memo)
            # 아래로 가능 경우
            if mountain[row][index] > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result3 =  memo[(row+1, index)]
                else :
                    result3 =  compare(row+1, mountain[row][index], start,result, result2, result3, result4,  memo)
            # 이동 불가
            if max(result[1], result2[1], result3[1], mountain[row][index]) == result[1] :
                return result

            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result2[1] :
                return result2

            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result3[1] :
                return result3
            else :
                return (row, mountain[row][index])
            
    elif row == N-1 :
        
        if index == 0 :
            # 우측 이동 가능
            if mountain[row][index] >  mountain[row][index+1] :
                if (row, index+1) in memo :
                    result = memo[(row, index+1)]
                else :
                    result = compare(row, mountain[row][index+1], start, result, result2, result3, result4, memo)
            # 위로 이동 가능
            if mountain[row][index] > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row, mountain[row-1][index], start, result, result2, result3, result4, memo)
            

            if max(result[1], result2[1], mountain[row][index]) == result[1] :
                return result

            elif max(result[1], result2[1], mountain[row][index]) == result2[1] :
                return result2

            else :
                return (row, mountain[row][index])

        elif index == 3 :
            # 좌측 이동 가능
            if mountain[row][index] >  mountain[row][index-1] :
                if (row, index-1) in memo :
                    result = memo[(row, index-1)]
                else :
                    result = compare(row, mountain[row][index-1], start, result, result2, result3, result4, memo)
                
            # 위로 이동 가능
            if mountain[row][index] > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row, mountain[row-1][index], start, result, result2, result3, result4, memo)

            if max(result[1], result2[1], mountain[row][index]) == result[1] :
                return result
            elif max(result[1], result2[1], mountain[row][index]) == result2[1] :
                return result2
            else :
                return (row, mountain[row][index])
        else :
            # 우측 이동 가능
            if mountain[row][index] >  mountain[row][index+1] :
                if (row, index+1) in memo :
                    result = memo[(row, index+1)]
                else :
                    result = compare(row, mountain[row][index+1], start, result, result2, result3, result4, memo)
            # 좌측 이동
            if mountain[row][index] >  mountain[row][index-1] :
                if (row, index-1) in memo :
                    result2 = memo[(row, index-1)]
                else :
                    result2 = compare(row, mountain[row][index-1], start, result, result2, result3, result4, memo)

            # 위로 이동
            if mountain[row][index] > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result3 = memo[(row-1, index)]
                else :
                    result3 = compare(row, mountain[row-1][index], start, result, result2, result3, result4, memo)

            if max(result[1], result2[1], result3[1], mountain[row][index]) == result[1] :
                return result
            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result2[1] :
                return result2
            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result3[1] :
                return result3
            else :
                return (row, mountain[row][index])
                
    else :
        if index == 0 :
            if mountain[row][index] > mountain[row][index+1] :
                if (row, index+1) in memo :
                    result = memo[(row, index+1)]
                else :
                    result = compare(row, mountain[row][index+1], start, result, result2, result3, result4, memo)

            if mountain[row][index] > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row-1, mountain[row-1][index], start,result, result2, result3, result4,  memo)
                    
            if mountain[row][index] > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result3 = memo[(row+1, index)]
                else :
                    result3 = compare(row+1, mountain[row+1][index], start, result, result2, result3, result4, memo)

            if max(result[1], result2[1], result3[1], mountain[row][index]) == result[1] :
                return result

            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result2[1] :
                return result2

            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result3[1] :
                return result3

            else :
                return (row, mountain[row][index])
                
        elif index == N-1 :
            if mountain[row][index] > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result = memo[(row, index-1)]
                else :
                    result = compare(row, mountain[row][index-1], start, result, result2, result3, result4, memo)
            if mountain[row][index] > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row-1, mountain[row-1][index], start, result, result2, result3, result4, memo)
            if mountain[row][index] > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result3 = memo[(row+1, index)]
                else :
                    result3 = compare(row+1, mountain[row+1][index], start, result, result2, result3, result4, memo)
            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result[1] :
                return result
            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result2[1] :
                return result2
            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result3[1] :
                return result3
            else :
                return (row, mountain[row][index])
        else :
            if mountain[row][index] > mountain[row][index-1] :
                if (row, index-1) in memo :
                    result = memo[(row, index-1)]
                else :
                    result = compare(row, mountain[row][index-1], start, result, result2, result3, result4, memo)
            if mountain[row][index] > mountain[row-1][index] :
                if (row-1, index) in memo :
                    result2 = memo[(row-1, index)]
                else :
                    result2 = compare(row-1, mountain[row-1][index], start, result, result2, result3, result4, memo)
            if mountain[row][index] > mountain[row+1][index] :
                if (row+1, index) in memo :
                    result3 = memo[(row+1, index)]
                else :
                    result3 = compare(row+1, mountain[row+1][index], start, result, result2, result3, result4, memo)
            if mountain[row][index] > mountain[row][index+1] :
                if (row, index+1) in memo :
                    result4 = memo[(row, index+1)]
                else :
                    result4 = compare(row, mountain[row][index+1], start, result, result2, result3, result4, memo)
            if max(result[1], result2[1], result3[1], mountain[row][index]) == result[1] :
                return result
            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result2[1] :
                return result2
            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result3[1] :
                return result3
            elif max(result[1], result2[1], result3[1], mountain[row][index]) == result4[1] :
                return result4
            else :
                return (row, mountain[row][index])
            
for i in mountain :
    for j in mountain[i] :
        start = j
        node = compare(i, j, start, result, result2, result3, result4, memo)
        Max = max(Max, j - node[1])
        memo[(i, mountain[i].index(j))] = node
        print(memo)

print(Max)
      
        
    
