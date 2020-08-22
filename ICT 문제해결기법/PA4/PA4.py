def quick_sort(lists) :
    if len(lists) <= 1 :
        return lists
    pivot = lists[len(lists)//2]
    less_arr, equal_arr, big_arr = [], [], []
    for i in lists :
        if i < pivot :
            less_arr.append(i)
        elif i > pivot :
            big_arr.append(i)
        else :
            equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)


def sub_max(dictionary, i, j, k, M, D, X) :
    
    if dictionary[M][i] > dictionary[D][j] and dictionary[M][i] > dictionary[X][k] :
        return M
    elif dictionary[D][j] > dictionary[M][i] and dictionary[D][j] > dictionary[X][k] :
        return D
    else :
        return X

def sub_max2(dictionary, j, k, M) :
    if M == 1 :
        if dictionary[2][j] > dictionary[3][k] :
            return 2, 3
        elif dictionary[3][k] > dictionary[2][j] :
            return 3, 2
    elif M == 2 :
        if dictionary[1][j] > dictionary[3][k] :
            return 1, 3
        elif dicotionary[3][k] > dictionary[1][j] :
            return 3, 1
    else :
        if dictionary[2][j] > dictionary[1][k] :
            return 2, 1
        elif dictionary[1][k] > dictionary[2][j] :
            return 1, 2



def big_func(dictionary, M, D, X,  i, j, k, count, Final_Max) :
    add = 0
    R = 0
    if M != D :
        if M == 1 :
            ## M이 끝값인가
            if dictionary[M][i] == dictionary[M][len(dictionary[M])-1] :
                if D == 2 :
                    # 못 옮기는 경우
                    X = 3
                    if dictionary[M][i] > dictionary[D][j] and dictionary[D][j] > 0 :
                    
                        return big_func(dictionary, D, X, M, j, k, i, count, Final_Max)
                    # 옮길 수 있는 경우
                    else :
                        count = count + 1
                        if i != 0 :
                            i = i - 1
                        j = j + 1
                        add = dictionary[M].pop()
                        dictionary[D].append(add)
                        # Max가 드러난 경우
                        if len(dictionary[Final_Max]) == 1 :
                            return count
                        # sub_max의 rod를 계산해서 대입해주는 함수 개발해야 할듯
                        R = sub_max(dictionary, i, j, k, M, D, X)
                        if R == 1 :
                            return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)
                        elif R == 2 :
                            return big_func(dictionary, D, D, X, j, j, k, count, Final_Max)
                        else :
                            return big_func(dictionary, X, D, M, k, j, i, count, Final_Max)
                        #return big_func(dictionary, M, D, X, i, j, k, count)
                        
                elif D == 3 : 
                    X = 2
                    if dictionary[M][i] > dictionary[D][j] and dictionary[D][j] > 0 :
                        return big_func(dictionary, D, X, M, j, k, i, count, Final_Max)
                    else :
                        count = count + 1
                        if i != 0 :
                            i = i - 1
                        j = j + 1
                        add = dictionary[M].pop()
                        dictionary[D].append(add)
                        if len(dictionary[Final_Max]) == 1 :
                            return count
                        R = sub_max(dictionary, i, j, k, count, M, D, X)
                        if R == 1 :
                            #X = 2
                            return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)
                        elif M == 2 :
                            #X = 3
                            return big_func(dictionary, X, D, M, k, j, i, count, Final_Max)
                        else :
                            #X = 1
                            return big_func(dictionary, D, D, X, j, j, k, count, Final_Max)

            # M이 끝값이 아닌가
            else :
                if i != len(dictionary[M]) - 1 :
                    i = i + 1
                if j != len(dictionary[D]) - 1 :
                    j = j + 1
                if k != len(dictionary[X]) - 1 :
                    k = k + 1
                return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)

        elif M == 2 :
            if dictionary[M][i] == dictionary[M][len(dictionary[M])-1] :
                if D == 1 :
                    X = 3
                    if dictionary[M][i] > dictionary[D][j] and dictionary[D][j] > 0 :
                        return big_func(dictionary, D, X, M, j, k, i, count, Final_Max)
                    else :
                        count = count + 1
                        if i != 0 :
                            i = i - 1
                        j = j + 1
                
                        add = dictionary[M].pop()
                        dictionary[D].append(add)
                        if len(dictionary[Final_Max]) == 1 :
                            return count
                        R = sub_max(dictionary, i, j, k, M, D, X)
                        if R == 1 :
                            return big_func(dictionary, D, D, X, j, j, k, count, Final_Max)
                        elif R == 2 :
                            return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)
                        else :
                            return big_func(dictionary, X, D, M, k, j, i, count, Final_Max)
                        
                elif D == 3 :
                    X = 1
                    if dictionary[M][i] > dictionary[D][j] and dictionary[D][j] > 0 :
                        return big_func(dictionary, D, X, M, j, k, i, count, Final_Max)
                    else :
                        count = count + 1
                        if i != 0 :
                            i = i - 1
                        j = j + 1
                        add = dictionary[M].pop()
                        dictionary[D].append(add)
                        if len(dictionary[Final_Max]) == 1 :
                            return count
                        R = sub_max(dictionary, i, j, k, count, M, D, X)
                        if R == 1 :
                            return big_func(dictionary, X, D, M, k, j, i, count, Final_Max)

                        elif R == 2 :
                            return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)
                    
                        else :
                            return big_func(dictionary, D, D, X, j, j, k, count, Final_Max)
                        #return big_func(dictionary, M, D, X, i, j, k, count)
            else :
                if i != len(dictionary[M]) - 1 :
                    i = i + 1
                if j != len(dictionary[D]) - 1 :
                    j = j + 1
                if k != len(dictionary[X]) - 1 :
                    k = k + 1
                return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)
                    


        else :
            if dictionary[M][i] == dictionary[M][len(dictionary[M])-1] :
                if D == 1 :
                    X = 2
                    if dictionary[M][i] > dictionary[D][j] and dictionary[D][j] > 0 :
                        return big_func(dictionary, D, X, M, j, k, i, count, Final_Max)
                    else :
                        count = count + 1
                        if i != 0 :
                            i = i - 1
                        j = j + 1
                        add = dictionary[M].pop()
                        dictionary[D].append(add)
                        if len(dictionary[Final_Max]) == 1:
                            return count
                        R = sub_max(dictionary, i, j, k, M, D, X)
                        if R == 1 :
                            return big_func(dictionary, D, D, X, j, j, k, count, Final_Max)
                        elif R == 2 :
                            return big_func(dictionary, X, D, M, k, j, i, count, Final_Max)
                        else :
                            return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)
                        #return big_func(dictionary, M, D, X, i, j, k, count)


                elif D == 2 :
                    X = 1
                    if dictionary[M][i] > dictionary[D][j] and dictionary[D][j] > 0 :
                        return big_func(dictionary, D, X, M, j, k, i, count, Final_Max)
                    else :
                        count = count + 1
                        if i != 0 :
                            i = i - 1
                        j = j + 1
                        
                        add = dictionary[M].pop()
                        dictionary[D].append(add)
                        if len(dictionary[Final_Max]) == 1 :
                            return count
                        R = sub_max(dictionary, i, j, k, count, M, D, X)
                        if R == 1 :
                            return big_func(dictionary, X, D, M, k, j, i, count, Final_Max)
                        elif R == 2 :
                            return big_func(dictionary, D, D, X, j, j, k, count, Final_Max)
                        else :
                            return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)
                        #return big_func(dictionary, M, D, X, i, j, k, count)
            else :
                if i != len(dictionary[M]) - 1 :
                    i = i + 1
                if j != len(dictionary[D]) - 1 :
                    j = j + 1
                if k != len(dictionary[X]) - 1 :
                    k = k + 1
                return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)


    else :
        if dictionary[M][i] == dictionary[M][len(dictionary[M])-1] :
            if D == 1 :
                R, X = sub_max2(dictionary, j, k, M)
                if R == 2 :
                    return big_func(dictionary, R, D, X, j, i, k, count, Final_Max)
                elif R == 3:
                    return big_func(dictionary, R, D, X, k, i, j, count, Final_Max)
                    
            elif D == 2 :
                R, X = sub_max2(dictionary, j, k, M)
                if R == 1 :
                    return big_func(dictionary, R, D, X, j, i, k, count, Final_Max)
                elif R == 3 :
                    return big_func(dictionary, R, D, X, k, i, j, count, Final_Max)
            else :
                R, X = sub_max2(dictionary, j, k, M)
                if R == 1 :
                    return big_func(dictionary, R, D, X, j, i, k, count, Final_Max)
                elif R == 2:
                    return big_func(dictionary, R, D, X, k, i, j, count, Final_Max)
         

        else :
            if i != len(dictionary[M]) - 1 :
                i = i + 1
            if j != len(dictionay[D]) - 1 :
                j = j + 1
            if k != len(dictionary[X]) - 1 :
                k = k + 1
            return big_func(dictionary, M, D, X, i, j, k, count, Final_Max)

def main() :
    N, D = [int(x) for x in input().split()]
    R1 = [int(x) for x in input().split()]
    R1_i = R1.pop(0)
    R2 = [int(x) for x in input().split()]
    R2_i = R2.pop(0)
    R3 = [int(x) for x in input().split()]
    R3_i = R3.pop(0)
    order = quick_sort(R1+R2+R3)
    i = 0
    j = 0
    k = 0
    dictionary = {}
    dictionary[1] = R1
    dictionary[2] = R2
    dictionary[3] = R3
    count = 0
    M = 0
    M1 = 0
    M2 = 0
    M3 = 0
     # 이 알고리즘이 어려운 이유... indexing문제 및 케이스..
    
    M1 = max(dictionary[1])
    M2 = max(dictionary[2])
    M3 = max(dictionary[3])
    if max(M1, M2, M3) == M1 :
        M = 1
        X = 3
    elif max(M1, M2, M3) == M2 :
        M = 2
        X = 3
    else :
        M = 3
        X = 1
    Final_Max = M
    #print(dictionary)
    #print(M)
    #print(D)
    #print(X)
    count = 0
    count = big_func(dictionary, M, D, X, i, j, k, count, Final_Max)
    #print(count)
    count = count + 1 # Max moving
    n = len(R1) + len(R2) + len(R3) 
    count = 2**(n-1) - 1
    #print(count)

main()



