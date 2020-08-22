### 새롭게 디밸롭한 아이디어로 문제를 풀어보자!!

def new(dictionary, M, D, X, order, count, i) :
    
    if M == D :
        i = i + 1
        if i == len(order) :
            return count
        return new(dictionary, M, D, X, order, count, i)
    
    else :
        if i == len(order) - 1 :
            return count
        if i == len(order) - 2 :
            count = count + 2**(len(order[i+1:])) - 1
            return count
        count = count + 2**(len(order[i+1:]))
        i = i + 1
        if i == len(order) :
            return count
        if order[i] in dictionary[1] :
            M = 1
        elif order[i] in dictionary[2] :
            M = 2       
        else :
            M = 3
        if M == 1 and D == 2 :
            X = 3
        elif M == 2 and D == 1 :
            X = 3
        elif M == 3 and D == 2 :
            X = 1
        elif M == 2 and D == 3 :
            X = 1
        elif M == 1 and D == 3 :
            X = 2
        elif M == 3 and D == 1 :
            X = 2
            
        return new(dictionary, M, D, X, order, count, i)


def main() :
    N, D = [int(x) for x in input().split()]
    R1 = [int(x) for x in input().split()]
    R1_i = R1.pop(0)
    R2 = [int(x) for x in input().split()]
    R2_i = R2.pop(0)
    R3 = [int(x) for x in input().split()]
    R3_i = R3.pop(0)
    order = sorted(R1+R2+R3)
    #print(order)
    dictionary = {}
    dictionary[1] = R1
    dictionary[2] = R2
    dictionary[3] = R3
    #First_Max = 0
    i = 0
    if order[i] in dictionary[1] :
        M = 1
    elif order[i] in dictionary[2] :
        M = 2       
    else :
        M = 3
    if M == 1 and D == 2 :
        X = 3
    elif M == 2 and D == 1 :
        X = 3
    elif M == 3 and D == 2 :
        X = 1
    elif M == 2 and D == 3 :
        X = 1
    elif M == 1 and D == 3 :
        X = 2
    elif M == 3 and D == 1 :
        X = 2
    elif M == 1 and D == 1 :
        if order[i+1] in dictionary[1] :
            X = 1
        elif order[i+1] in dictionary[2] :
            X = 2       
        else :
            X = 3
    elif M == 2 and D == 2 :
        if order[i+1] in dictionary[1] :
            X = 1
        elif order[i+1] in dictionary[2] :
            X = 2       
        else :
            X = 3
    elif M == 3 and D == 3 :
        if order[i+1] in dictionary[1] :
            X = 1
        elif order[i+1] in dictionary[2] :
            X = 2       
        else :
            X = 3
    
    count = 0
    count = new(dictionary, M, D, X, order, count, i)
    print(count)


main()
