# 산 정보 구축
mountain = {}

N = int(input())

for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]

memo = {}
# start point와 end point를 저장해주는 결과값 리스트
result = [0, 0]
Max_get = 0
def get_max(mountain, i, j) :
    # 층의 special case
    if i == 0 :
        # 이동 가능 case 1 down
        if mountain[i+1][mountain[i].index(j)] < j :
            if (i+1, mountain[i+1][mountain[i].index(j)] ) in memo :
                return memo[(i+1, mountain[i+1][mountain[i].index(j)] )]
            result = get_max(mountain, i+1, mountain[i+1][mountain[i].index(j)])
            Max_get = max(result, Max_get)

        # 이동 가능 case2
        # 가장 좌측열의 경우
        if j == 0 :
            if mountain[i][mountain[i].index(j)+1] < j :
                if (i, mountain[i][mountain[i].index(j)+1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)+1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)+1])
                Max_get = max(result, Max_get)
            return Max_get 

        # 가장 우측 열의 경우
        elif j == 3 :
            if mountain[i][mountain[i].index(j)-1] < j :
                if (i, mountain[i][mountain[i].index(j)-1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)-1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)-1])
                Max_get = max(result, Max_get)

            return Max_get
        else :
            # 우측 애랑 비교
            if mountain[i][mountain[i].index(j)+1] < j :
                if (i, mountain[i][mountain[i].index(j)+1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)+1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)+1])
                Max_get = max(result, Max_get)
            # 좌측 애랑 비교
            elif mountain[i][mountain[i].index(j)-1] < j :
                if (i, mountain[i][mountain[i].index(j)-1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)-1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)-1])
                Max_get = max(result, Max_get)
            return Max_get


    # 층의 special case
    elif i == 3 :
        # 이동 가능 case 1 up
        if mountain[i-1][mountain[i].index(j)] < j :
            # 이미 메모리에 있는 경우
            if (i-1, mountain[i-1][mountain[i].index(j)]) in memo :
                return memo[(i-1, mountain[i-1][mountain[i].index(j)])]

            # 인자 바꾸어서 search 지속
            result = get_max(mountain, i-1, mountain[i-1][mountain[i].index(j)])
            Max_get = max(result, Max_get)
        # 이동 가능 case3
        # 가장 좌측열의 경우
        if j == 0 :
            if mountain[i][mountain[i].index(j)+1] < j :
                if (i, mountain[i][mountain[i].index(j)+1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)+1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)+1] )
                Max_get = max(result, Max_get)
            return Max_get
        # 가장 우측 열의 경우
        elif j == 3 :
            if mountain[i][mountain[i].index(j)-1] < j :
                if (i, mountain[i][mountain[i].index(j)-1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)-1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)-1])
                Max_get = max(result, Max_get)
            return Max_get
        else :
            # 우측 애랑 비교
            if mountain[i][mountain[i].index(j)+1] < j :
                if (i, mountain[i][mountain[i].index(j)+1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)+1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)+1] )
                Max_get = max(result, Max_get)
            # 좌측 애랑 비교
            elif mountain[i][mountain[i].index(j)-1] < j :
                if (i, mountain[i][mountain[i].index(j)-1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)-1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)-1])
                Max_get = max(result, Max_get)

            return Max_get
        

    else :
        # 이동 가능 case 1 up
        if mountain[i-1][mountain[i].index(j)] < j :
            # 이미 메모리에 있는 경우
            if (i-1, mountain[i-1][mountain[i].index(j)]) in memo :
                return memo[(i-1, mountain[i-1][mountain[i].index(j)])]

            # 인자 바꾸어서 search 지속
            result = get_max(mountain, i-1, mountain[i-1][mountain[i].index(j)])
            Max_get = max(result, Max_get)

        # 이동 가능 case2 down
        elif mountain[i+1][mountain[i].index(j)] < j :
            if (i+1, mountain[i+1][mountain[i].index(j)] ) in memo :
                return memo[(i+1, mountain[i+1][mountain[i].index(j)] )]
            result = get_max(mountain, i+1, mountain[i+1][mountain[i].index(j)])
            Max_get = max(result, Max_get)

        # 이동 가능 case3
        # 가장 좌측열의 경우
        if j == 0 :
            if mountain[i][mountain[i].index(j)+1] < j :
                if (i, mountain[i][mountain[i].index(j)+1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)+1] )]
                result = get_max(mountain, i,  mountain[i][mountain[i].index(j)+1] )
                Max_get = max(result, Max_get)
            return Max_get
        # 가장 우측 열의 경우
        elif j == 3 :
            if mountain[i][mountain[i].index(j)-1] < j :
                if (i, mountain[i][mountain[i].index(j)-1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)-1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)-1])
                Max_get = max(result, Max_get)
            return Max_get
        else :
            # 우측 애랑 비교
            if mountain[i][mountain[i].index(j)+1] < j :
                if (i, mountain[i][mountain[i].index(j)+1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)+1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)+1] )
                Max_get = max(result, Max_get)
            # 좌측 애랑 비교
            elif mountain[i][mountain[i].index(j)-1] < j :
                if (i, mountain[i][mountain[i].index(j)-1] ) in memo :
                    return memo[(i, mountain[i][mountain[i].index(j)-1] )]
                result = get_max(mountain, i, mountain[i][mountain[i].index(j)-1] )
                Max_get = max(result, Max_get)

            return Max_get
            
# 우선 큰 반복문을 구축한다
Max = 0
for i in mountain :
    for j in mountain[i] :
        # 이 recursion을 구성하는 것이 핵심일 것으로 보인다.
        result = get_max(mountain, i, j)
        # 메모리에 저장해준다. dynamic programming
        memo[(i, j)] = result
        Max = max(result, Max)

print(Max)
