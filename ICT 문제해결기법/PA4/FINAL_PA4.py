def get_result(dictionary, dictionary_i, order, i, count, M) :
    if M == 1:
        if order[i] in dictionary[1] :
            i = i + 1
            if i == len(order) :
                return count
            return get_result(dictionary, dictionary_i, order, i, count, M)
        elif order[i] in dictionary[2] :
            count = count + 2**(len(order[i+1:]))-1+1
            i = i + 1
            M = 3
            if i == len(order) :
                return count
            return get_result(dictionary, dictionary_i, order, i, count, M)
        elif order[i] in dictionary[3] :
            count = count + 2**(len(order[i+1:]))-1+1
            i = i + 1
            M = 2
            if i == len(order) :
                return count
            return get_result(dictionary, dictionary_i, order, i, count, M)
    elif M == 2 :
        if order[i] in dictionary[1] :
            count = count + 2**(len(order[i+1:]))-1+1
            
            i = i + 1
            M = 3
            if i == len(order) :
                return count
            return get_result(dictionary, dictionary_i, order, i, count, M)
        elif order[i] in dictionary[2] :
            i = i + 1
            if i == len(order) :
                return count
            return get_result(dictionary, dictionary_i, order, i, count, M)
        elif order[i] in dictionary[3] :
            count = count + 2**(len(order[i+1:]))-1+1
            i = i + 1
            M = 1
            if i == len(order) :
                return count
            return get_result(dictionary, dictionary_i, order, i, count, M)
    elif M == 3 :
        if order[i] in dictionary[1] :
            count = count + 2**(len(order[i+1:]))-1+1
            i = i + 1
            if i == len(order) :
                return count
            M = 2
            return get_result(dictionary, dictionary_i, order, i, count, M)
        elif order[i] in dictionary[2] :
            count = count + 2**(len(order[i+1:]))-1+1
            i = i + 1
            M = 1
            if i == len(order) :
                return count
            return get_result(dictionary, dictionary_i, order, i, count, M)
        elif order[i] in dictionary[3] :
            i = i + 1
            if i == len(order) :
                return count
            return get_result(dictionary, dictionary_i, order, i, count, M)
        
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
    #print(dictionary)
    order = sorted(R1+R2+R3, reverse = True)
    dictionary_i = {}
    if D == 1 :
        dictionary_i[1] = order
        dictionary_i[2] = []
        dictionary_i[3] = []
    elif D == 2 :
        dictionary_i[1] = []
        dictionary_i[2] = order
        dictionary_i[3] = []
    elif D == 3 :
        dictionary_i[1] = []
        dictionary_i[2] = []
        dictionary_i[3] = order
    i = 0
    count = 0
    if order[0] in dictionary_i[1] :
        M = 1
    elif order[0] in dictionary_i[2] :
        M = 2
    elif order[0] in dictionary_i[3] :
        M = 3
    count = get_result(dictionary, dictionary_i, order, i, count, M)
    print(count)

main()
