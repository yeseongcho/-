
def please(dictionary, i, j, k, M, D, X, count) :
    s = 0
    if M == D :
        i = i + 1
        if M == 1 :
            if max(dictionary[M][i], dictionary[2][j], dictionary[3][k]) == dictionary[M][i] :
                return please(dictionary, i, j, k, M, D, X, count)
            elif max(dictionary[M][i], dictionary[2][j], dictionary[3][k]) == dictionary[2][j] :
                M = 2
                X = 3
                return please(dictionary, j, i, k, M, D, X, count)
            else :
                M = 3
                X = 2
                return please(dictionary, k, i, j, M, D, X, count)

        elif M == 2 :
            if max(dictionary[M][i], dictionary[1][j], dictionary[3][k]) == dictionary[1][j] :
                M = 15
                X = 3
                return please(dictionary, j, i, k, M, D, X, count)
            elif max(dictionary[M][i], dictionary[1][j], dictionary[3][k]) == dictionary[M][i] :
                
                return please(dictionary, i, j, k, M, D, X, count)
            else :
                M = 3
                X = 1
                return please(dictionary, k, j, i, M, D, X, count)
        else :
            if max(dictionary[M][i], dictionary[1][j], dictionary[2][k]) == dictionary[1][j] :
                M = 1
                X = 2
                return please(dictionary, j, i, k, M, D, X, count)
            elif max(dictionary[M][i], dictionary[1][j], dictionary[2][k]) == dictionary[2][k] :
                M = 2
                X = 1
                return please(dictionary, k, i, j, M, D, X, count)
            else :
                return please(dictionary, i, j, k, M, D, X, count)
            
            

    else :
        if dictionary[D] == [0] and dictionary[X] == [0] :
            count = 2**(len(dictionary[M][:])) - 1
            return count
        i = i + 1
        if max(dictionary[M][i:], dictionary[D][j:], dictionary[X][k:]) == dictionary[X][k:]  :
         
            count = count + 2
        elif min(dictionary[M][i:], dictionary[D][j:], dictionary[X][k:]) == dictionary[X][k:] :
            count = count + 5
        else :
            count = count + 7
    
        s = len(dictionary[M][i+1:]) + len(dictionary[D][j+1:]) + len(dictionary[D][k+1:])
        count = count + 2**s - 1 + 1
        r = len(dictionary[M][i-1:]) + len(dictionary[D][j:]) + len(dictionary[X][k:])
        count = count + 2**r - 1
        return count

def main() :
    N, D = [int(x) for x in input().split()]
    R1 = [int(x) for x in input().split()]
    R1_i = R1.pop(0)
    R2 = [int(x) for x in input().split()]
    R2_i = R2.pop(0)
    R3 = [int(x) for x in input().split()]
    R3_i = R3.pop(0)

    dictionary = {}
    dictionary[1] = R1
    dictionary[2] = R2
    dictionary[3] = R3
    if dictionary[1] == [] :
        dictionary[1] = [0]
    if dictionary[2] == [] :
        dictionary[2] = [0]
    if dictionary[3] == [] :
        dictionary[3] = [0]
    i = 0
    j = 0
    k = 0
    M = 0
    X = 0
    if max(dictionary[1][0], dictionary[2][0], dictionary[3][0]) == dictionary[1][0] :
        M = 1
        if D == 1 :
            if max(dictionary[1][1], dictionary[2][1], dictionary[3][1]) == dictionary[1][1]:
                X = 1
            elif max(dictionary[1][1], dictionary[2][1], dictionary[3][1]) == dictionary[2][1] :
                X = 2
            else :
                X = 3
        elif D == 2 :
            X = 3
        elif D == 3 :
            X = 2
    elif max(dictionary[1][0], dictionary[2][0], dictionary[3][0]) == dictionary[2][0] :
        M = 2
        if D == 1 :
            X = 3
        elif D == 2 :
            if max(dictionary[1][1], dictionary[2][1], dictionary[3][1]) == dictionary[1][1] :
                X = 1
            elif max(dictionary[1][1], dictionary[2][1], dictionary[3][1]) == dictionary[2][1] :
                X = 2
            else :
                X = 3
        elif D == 3 :
            X = 1
    else :
        M = 3
        if D == 1 :
            X = 2
        elif D == 2 :
            X = 1
        else :
            if max(dictionary[1][1], dictionary[2][1], dictionary[3][1]) == dictionary[1][1] :
                X = 1
            elif max(dictionary[1][1], dictionary[2][1], dictionary[3][1]) == dictionary[2][1] :
                X = 2
            else :
                X = 3
    count = 0
    count = please(dictionary, i, j, k, M, D, X, count)
    print(count)
main()
