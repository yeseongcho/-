
def plea(dictionary, M, D, X, i, j, k, count, order, n) :
    s = 0
    r = 0

    if dictionary[D] == [0] and dictionary[X] == [0] :
        count = 2**(len(order)) - 1
        return count
    if M != D :
        if M == 1 :
           
            i = i + 1
             
            if D == 2 :
                X = 3
                if max(dictionary[M][i], dictionary[D][j], dictionary[X][k]) == dictionary[X][k] :
                    count = count + 2
                    if i == len(dictionary[M]) -1 and j == len(dictionary[D])-1 :
                        return count
                elif min(dictionary[M][i], dictionary[D][j], dictionary[X][k]) == dictionary[X][k] :
                    count = count + 5
                    if i == len(dictionary[M]) -1 and j == len(dictionary[D])-1 :
                        return count
                else :
                    count = count + 7
                    if i == len(dictionary[M]) -1 and j == len(dictionary[D])-1 :
                        return count
                ### j+1, k+1 의 경우 한 디스크만 있는 경우는 indexing에 문제가 생긴다
                dictionary[M].pop()
                dictionary[D].pop()
                dictionary[X].pop()
                s = len(dictionary[M][i+1:]) + len(dictionary[D][j+1:]) + len(dictionary[X][k+1:])
                count = count + 2**s - 1 + 1 
                #print(s)
                r = len(dictionary[M][i:]) + len(dictionary[D][j:]) + len(dictionary[X][k:])
                #print(r)
                count = count + 2**r - 1
                #print(count)
                return count
                
    
            elif D == 3 :
                X = 2
                if max(dictionary[M][i], dictionary[D][k], dictionary[X][j]) == dictionary[X][j] :
                    count = count + 2
                    if i == len(dictionary[M])-1 and k == len(dictionary[D]) - 1 :
                        return count


                elif min(dictionary[M][i], dictionary[D][k], dictionary[X][j]) == dictionary[X][j] :
                    count = count + 5
                    if i == len(dictionary[M])-1 and k == len(dictionary[D]) - 1 :
                        return count
                else :
                    count = count + 7
                    if i == len(dictionary[M])-1 and k == len(dictionary[D]) - 1 :
                        return count
                dictionary[M].pop()
                dictionary[D].pop()
                dictionary[X].pop()

                s = len(dictionary[M][i+1:]) + len(dictionary[D][k+1:]) + len(dictionary[X][j+1:])
                count = count + 2**s - 1 + 1
                r = len(dictionary[M][i:]) + len(dictionary[D][k:]) + len(dictionary[X][j:])
                count = count + 2**r - 1
                return count       
        elif M == 2 :
            #if j != len(dictionary[2]) - 1 :
             #   j = j + 1
            j = j + 1
            #print(i)
            #print(j)
            #print(k)
            if D == 1 :
                X = 3
                if max(dictionary[M][j], dictionary[D][i], dictionary[X][k]) == dictionary[X][k] :
                    count = count + 2
                    if i == len(dictionary[D])-1 and j == len(dictionary[M])-1 :
                        return count
                elif min(dictionary[M][j], dictionary[D][i], dictionary[X][k]) == dictionary[X][k] :
                    count = count + 5
                    if i == len(dictionary[D])-1 and j == len(dictionary[M])-1 :
                        return count
                else :
                    count = count + 7
                    if i == len(dictionary[D])-1 and j == len(dictionary[M])-1 :
                        return count
                #print(count)
                dictionary[M].pop()
                dictionary[D].pop()
                dictionary[X].pop()
                s = len(dictionary[M][j+1:]) + len(dictionary[D][i+1:]) + len(dictionary[X][k+1:])
                #print(s)
                count = count + 2**s - 1 + 1
                #print(count)
                r = len(dictionary[M][j:]) + len(dictionary[D][i:]) + len(dictionary[X][k:])
                #print(r)
                count = count + 2**r - 1
                #print(count)
                return count
                    
            elif D == 3  :
                X = 1
                if max(dictionary[M][j], dictionary[D][k], dictionary[X][i]) == dictionary[X][i] :
                    count = count + 2
                    if j == len(dictionary[M]) -1 and k == len(dictionary[D])-1 :
                        return count
                elif min(dictionary[M][j], dictionary[D][k], dictionary[X][i]) == dictionary[X][i] :
                    count = count + 5
                    if j == len(dictionary[M]) - 1 and k == len(dictionary[D]) -1 :
                        return count
                else :
                    count = count + 7
                    if j == len(dictionary[M]) - 1 and k == len(dictionary[D]) -1 :
                        return count
                dictionary[M].pop()
                dictionary[D].pop()
                dictionary[X].pop()
                s = len(dictionary[M][j+1:]) + len(dictionary[D][k+1:]) + len(dictionary[X][i+1:])
                count = count + 2**s - 1 + 1
                r = len(dictionary[M][j:]) + len(dictionary[D][k:]) + len(dictionary[X][i:])
                count = count + 2**r - 1
                return count
        else :
           # if k != len(dictionary[3]) - 1 :
            #    k = k + 1
            k = k + 1
            if D == 1 :
                X = 2
                if max(dictionary[M][k], dictionary[D][i], dictionary[X][j]) == dictionary[X][j] :
                    count = count + 2
                    if k == len(dictionary[M]) - 1 and i == len(dictionary[D]) -1 :
                        return count
                elif min(dictionary[M][k], dictionary[D][i], dictionary[X][j]) == dictionary[X][j] :
                    count = count + 5
                    if k == len(dictionary[M]) - 1 and i == len(dictionary[D]) -1 :
                        return count
                else :
                    if k == len(dictionary[M]) - 1 and i == len(dictionary[D]) -1 :
                        return count
                    count = count + 7
                dictionary[M].pop()
                dictionary[D].pop()
                dictionary[X].pop()
                s = len(dictionary[M][k+1:]) + len(dictionary[D][i+1:]) + len(dictionary[X][j+1:])
                count = count + 2**s - 1 + 1
                r = len(dictionary[M][k:]) + len(dictionary[D][i:]) + len(dictionary[X][j:])
                count = count + 2**r - 1
                return count
            elif D == 2 :
                X = 1
                if max(dictionary[M][k], dictionary[D][j], dictionary[X][i]) == dictionary[X][i] :
                    count = count + 2
                    if k == len(dictionary[M]) - 1 and j == len(dictionary[D]) -1 :
                        return count
                elif min(dictionary[M][k], dictionary[D][j], dictionary[X][i]) == dictionary[X][i] :
                    count = count + 5
                    if k == len(dictionary[M]) - 1 and j == len(dictionary[D]) -1 :
                        return count
                else :
                    count = count + 7
                    if k == len(dictionary[M]) - 1 and j == len(dictionary[D]) -1 :
                        return count
                dictionary[M].pop()
                dictionary[D].pop()
                dictionary[X].pop()
                s = len(dictionary[M][k+1:]) + len(dictionary[D][j+1:]) + len(dictionary[X][i+1:])
                count = count + 2**s - 1 + 1
                r = len(dictionary[M][k:]) + len(dictionary[D][j:]) + len(dictionary[X][i:])
                count = count + 2**r - 1
                return count

        

    else :
        n = n + 1
        if M == 1 :
            #if i != len(dictionary[1])-1 :
             #   i = i + 1
            i = i + 1
            if order[n] in dictionary[M] :
                return plea(dictionary, M, D, X, i, j, k, count, order, n)

            elif order[n] in dictionary[2] :
                M = 2
                D = 1
                X = 3                
                return plea(dictionary, M, D, X, i, j, k, count, order, n)
            else :
                M = 3
                D = 1
                X = 2
                return plea(dictionary, M, D, X, i, j, k, count, order, n)
        elif M == 2 :
            #if j != len(dictionary[2])-1 :
             #   j = j + 1
            j = j + 1
            if order[n] in dictionary[1] :
                M = 1
                D = 2
                X = 3
                return plea(dictionary, M, D, X, i, j, k, count, order, n)
            elif order[n] in dictionary[M] :
                return plea(dictionary, M, D, X, i, j, k, count, order, n)


            else :
                M = 3
                D = 2
                X = 1
                return plea(dictionary, M, D, X, i, j, k, count, order, n)


        else :
           # if k != len(dictionary[3])-1 :
            #    k = k + 1
            k = k + 1
            if order[n] in dictionary[1] :
                M = 1
                D = 3
                X = 2
                return plea(dictionary, M, D, X, i, j, k, count, order, n)
            elif order[n] in dictionary[2] :
                M = 2
                D = 3
                X = 1
                return plea(dictionary, M, D, X, i, j, k, count, order, n)
            else :
                return plea(dictionary, M, D, X, i, j, k, count, order, n)



def main() :
    N, D = [int(x) for x in input().split()]
    R1 = [int(x) for x in input().split()]
    R1_i = R1.pop(0)
    R2 = [int(x) for x in input().split()]
    R2_i = R2.pop(0)
    R3 = [int(x) for x in input().split()]
    R3_i = R3.pop(0)
    order = sorted(R1+R2+R3)
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
    n = 0
    X = 0 # 아직 정해지지 않는 경우를 대비 X를 초기화
    if order[n] in dictionary[1] :
        M = 1
    elif order[n] in dictionary[2] :
        M = 2
    else :
        M = 3
    if M == 1 and D == 2 :
        X = 3
    elif M == 1 and D == 3 :
        X = 2
    elif M == 2 and D == 3 :
        X = 1
    elif M == 2 and D == 1 :
        X = 3
    elif M == 3 and D == 1 :
        X = 2
    elif M == 3 and D == 2 :
        X = 1
    count = 0
    
    
    count = plea(dictionary, M, D, X, i, j, k, count, order, n)
    print(count)

main()
