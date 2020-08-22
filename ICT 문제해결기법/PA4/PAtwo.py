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
    return quick_sort(big_arr) + equal_arr + quick_sort(less_arr)


def find_result(dictionary, D, order, i, count, M) :
   
    #i = i + 1
    if M == D :
        #i = i + 1
        if order[i+1] in dictionary[1] :
            R = 1
        
        elif order[i+1] in dictionary[2] :
            R = 2
        
        else :
            R = 3
            
        if R == D :
            if i == len(order) - 1 :
                return count
            i = i + 1
            return find_result(dictionary, D, order, i, count, M)

        else :
            if i == len(order) - 1 :
                return count
            count = count + 2**len(order[i+1:])
            i = i + 1
            return f
        ind_result(dictionary, D, order, i, count, M)

    else :
        if i == len(order) - 1 : 
            return count
        count = count + 2**len(order[i+1:])
        print(count)
        i = i + 1
        return find_result(dictionary, D, order, i, count, M)

def main() :
    N, D = [int(x) for x in input().split()]
    R1 = [int(x) for x in input().split()]
    R1_i = R1.pop(0)
    R2 = [int(x) for x in input().split()]
    R2_i = R2.pop(0)
    R3 = [int(x) for x in input().split()]
    R3_i = R3.pop(0)
    order = quick_sort(R1+R2+R3)
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
    count = 0
    count = find_result(dictionary, D, order, i, count, M)
    if M != D :
        count = count + 1
    print(count)

main()
