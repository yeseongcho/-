

def God_with_you(dictionary, X, D, M, i, j, k, n, count, order) :
    n = n + 1
    if order[n] in dictionary[1] :
        M = 1
    elif order[n] in dictionary[2] :
        M = 2
    else :
        M = 3

    if M != D :
        if M == 1 :
            i = i + 1
            if D == 2 :
                X = 3
                if max(dictionary[M][i], dictionary[D][j], dictionary[X][k]) == dictionary[X][k] :
                    count = count + 2
                    #### indexing에 대한 조건을 걸어줄 필요 농후
                    if i != len(dictionary[M]) :
                        i = i + 1
                    if j != len(dictionary[D]) :
                        j = j + 1
                    if k != len(dictionary[X]) :
                        k = k + 1
                    if i == len(dictionary[M]) and j == len(dictionary[D]) and k == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                elif min(dictionary[M][i], dictionary[D][j], dictionary[X][k]) == dictionary[X][k] :
                    count = count + 5
                    if i != len(dictionary[M]) :
                        i = i + 1
                    if j != len(dictionary[D]) :
                        j = j + 1
                    if k != len(dictionary[X]) :
                        k = k + 1
                    if i == len(dictionary[M]) and j == len(dictionary[D]) and k == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                else :
                    count = count + 7
                    if i != len(dictionary[M]) :
                        i = i + 1
                    if j != len(dictionary[D]) :
                        j = j + 1
                    if k != len(dictionary[X]) :
                        k = k + 1
                    if i == len(dictionary[M]) and j == len(dictionary[D]) and k == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)


            elif D == 3 :
                X = 2
                if max(dictionary[M][i], dictionary[D][k], dictionary[X][j]) == dictionary[X][j] :
                    count = count + 2
                    if i != len(dictionary[M]) :
                        i = i + 1
                    if k != len(dictionary[D]) :
                        k = k + 1
                    if j != len(dictionary[X]) :
                        j = j + 1
                    if i == len(dictionary[M]) and k == len(dictionary[D]) and j == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                elif min(dictionary[M][i], dictionary[D][k], dictionary[X][j]) == dictionary[X][j] :
                    count = count + 5
                    if i != len(dictionary[M]) :
                        i = i + 1
                    if k != len(dictionary[D]) :
                        k = k + 1
                    if j != len(dictionary[X]) :
                        j = j + 1
                    if i == len(dictionary[M]) and k == len(dictionary[D]) and j == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                else :
                    count = count + 7
                    if i != len(dictionary[M]) :
                        i = i + 1
                    if k != len(dictionary[D]) :
                        k = k + 1
                    if j != len(dictionary[X]) :
                        j = j + 1
                    if i == len(dictionary[M]) and k == len(dictionary[D]) and j == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)


        elif M == 2 :
            if D == 1 :
                X = 3
                if max(dictionary[M][j], dictionary[D][i], dictionary[X][k]) == dictionary[X][k] :
                    count = count + 2
                    if j != len(dictionary[M]) :
                        j = j + 1
                    if i != len(dictionary[D]) :
                        i = i + 1
                    if k != len(dictionary[X]) :
                        k = k + 1
                    if j == len(dictionary[M]) and i == len(dictionary[D]) and k == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                elif min(dictionary[M][j], dictionary[D][i], dictionary[X][k]) == dictionary[X][k] :
                    count = count + 5
                    if j != len(dictionary[M]) :
                        j = j + 1
                    if i != len(dictionary[D]) :
                        i = i + 1
                    if k != len(dictionary[X]) :
                        k = k + 1
                    if j == len(dictionary[M]) and i == len(dictionary[D]) and k == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                else :
                    count = count + 7
                    if j != len(dictionary[M]) :
                        j = j + 1
                    if i != len(dictionary[D]) :
                        i = i + 1
                    if k != len(dictionary[X]) :
                        k = k + 1
                    if j == len(dictionary[M]) and i == len(dictionary[D]) and k == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)

            elif D == 3 :
                X = 1
                if max(dictionary[M][j], dictionary[D][k], dictinary[X][i]) == dictionary[X][i] :
                    count = count + 2
                    if j != len(dictionary[M]) :
                        j = j + 1
                    if k != len(dictionary[D]) :
                        k = k + 1
                    if i != len(dictionary[X]) :
                        i = i + 1
                    if j == len(dictionary[M]) and k == len(dictionary[D]) and i == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                elif min(dictionary[M][j], dictionary[D][k], dictionary[X][i]) == dictionary[X][i] :
                    count = count + 5
                    if j != len(dictionary[M]) :
                        j = j + 1
                    if k != len(dictionary[D]) :
                        k = k + 1
                    if i != len(dictionary[X]) :
                        i = i + 1
                    if j == len(dictionary[M]) and k == len(dictionary[D]) and i == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                else :
                    count = count + 7
                    if j != len(dictionary[M]) :
                        j = j + 1
                    if k != len(dictionary[D]) :
                        k = k + 1
                    if i != len(dictionary[X]) :
                        i = i + 1
                    if j == len(dictionary[M]) and k == len(dictionary[D]) and i == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)



        elif M == 3 :
            if D == 2 :
                X = 1
                if max(dictionary[M][k], dictionary[D][j], dictionary[X][i]) == dictionary[X][i] :
                    count = count + 2
                    if k != len(dictionary[M]) :
                        k = k + 1
                    if j != len(dictionary[D]) :
                        j = j + 1
                    if i != len(dictionary[X]) :
                        i = i + 1
                    if k == len(dictionary[M]) and j == len(dictionary[D]) and i == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                elif min(dictionary[M][k], dictionary[D][j], dictionary[X][i]) == dictionary[X][i] :
                    count = count + 5
                    if k != len(dictionary[M]) :
                        k = k + 1
                    if j != len(dictionary[D]) :
                        j = j + 1
                    if i != len(dictionary[X]) :
                        i = i + 1
                    if k == len(dictionary[M]) and j == len(dictionary[D]) and i == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                else :
                    count = count + 7
                    if k != len(dictionary[M]) :
                        k = k + 1
                    if j != len(dictionary[D]) :
                        j = j + 1
                    if i != len(dictionary[X]) :
                        i = i + 1
                    if k == len(dictionary[M]) and j == len(dictionary[D]) and i == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
            

            elif D == 1 :
                X = 2
                if max(dictionary[M][k], dictionary[D][i], dictionary[X][j]) == dictionary[X][j] :
                    count = count + 2
                    if k != len(dictionary[M]) :
                        k = k + 1
                    if i != len(dictionary[D]) :
                        i = i + 1
                    if j != len(dictionary[X]) :
                        j = j + 1
                    if k == len(dictionary[M]) and i == len(dictionary[D]) and j == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                elif min(dictionary[M][k], dictionary[D][i], dictionary[X][j]) == dictionary[X][j] :
                    count = count + 5
                    if k != len(dictionary[M]) :
                        k = k + 1
                    if i != len(dictionary[D]) :
                        i = i + 1
                    if j != len(dictionary[X]) :
                        j = j + 1
                    if k == len(dictionary[M]) and i == len(dictionary[D]) and j == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
                else :
                    count = count + 7
                    if k != len(dictionary[M]) :
                        k = k + 1
                    if i != len(dictionary[D]) :
                        i = i + 1
                    if j != len(dictionary[X]) :
                        j = j + 1
                    if k == len(dictionary[M]) and i == len(dictionary[D]) and j == len(dictionary[X]) :
                        return count
                    return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
            


    ### 이 경우를 한번 생각해보자!
    elif M == D :
        if M == 1 :
            i = i + 1
            return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
        elif M == 2 :
            j = j + 1
            return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
        else :
            k = k + 1
            return God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
        

            
    















def main() :
    N, D = [int(x) for x in input().split()]
    R1 = [int(x) for x in input().split()]
    R1_i = R1.pop(0)
    R2 = [int(x) for x in input().split()]
    R2_i = R2.pop(0)
    R3 = [int(x) for x in input().split()]
    R3_i = R3.pop(0)
    order = sorted(R1+R2+R3, reverse = True)
    R1.append(0)
    R2.append(0)
    R3.append(0)
    #print(order)
    #print(R1)
    #print(R2)
    #print(R3)
    dictionary = {}
    dictionary[1] = R1
    dictionary[2] = R2
    dictionary[3] = R3
    dictionary[0] = [0]
    
    i = 0
    j = 0
    k = 0
    n = -1
    X = 0 # 아직 정해지지 않는 경우를 대비 X를 초기화
    M = 0
    count = 0
    
    count = God_with_you(dictionary, X, D, M, i, j, k, n, count, order)
    
    print(count)

main()

