def get_list() :
    list1 = []
    h, w = [int(x) for x in input().split()]
    for j in range(h) :
        list1.append([int(x) for x in input().split()])
    return list1
def get_result(lists, lst, next_block, List,a, prev) :
    large_index = len(List) - len(lists) +1
    small_index = len(List[0]) - len(lists[0]) + 1
    #print(large_index)
    #print(small_index)
    #print(List)
    #print(prev)
    for k in range(large_index) :
        for n in range(len(lists)) :
            for b in range(len(lists[0])) :
                if List[n+k][b+a] ==1 and  lists[n][b] == 1 :
                    a = a + 1
                    List = prev
                    print(List)
                    if len(lists) == 1 :
                        if a == small_index :
                            if next_block > 0 :
                                a = 0
                                return get_result(lst[next_block-1], lst, next_block, List, a ,prev)
                        return get_result(lists, lst, next_block, List, a, prev) 
                        
                    else :
                        if a == small_index+1 :
                            #next_block = next_block + 1
                            if next_block > 0 :
                                a = 0
                                return get_result(lst[next_block-1], lst, next_block, List, a, prev)
                        return get_result(lists, lst, next_block, List, a, prev)    
                List[n+k][b+a] = List[n+k][b+a] + lists[n][b]
                print(List)
        #prev = List
        #next_block = next_block + 1
        #if next_block == len(lst) :
        #    return List
        #a = 0
        #return get_result(lst[next_block], lst, next_block, List, a, prev)
    prev = List
    next_block = next_block + 1
    if next_block == len(lst) :
        return List
    a = 0
    return get_result(lst[next_block], lst, next_block, List, a, prev)        
                    
                    
           

def main() :
    N = int(input())
    lst = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    L = []
    List = []
    sums = 0
    for i in range(N) :
        lst.append(get_list())
    ### 이 경우는 바로 정사각형 여부 판단해주면 됨
    if N == 1 :
        list1 = lst[0]
        
    elif N == 2 :
        list1 = lst[0]
        list2 = lst[1]
        for i in list1 :
            sums = sums + sum(i)
        for i in list2 :
            sums = sums + sum(i)
        if sums == 4 :
            puzzle_length = 2
        elif sums == 9 :
            puzzle_length = 3
        elif sums == 16 :
            puzzle_length = 4
        elif sums == 25 :
            puzzle_length = 5
        elif sums == 36 :
            puzzle_length = 6
        elif sums == 49 :
            puzzle_length = 7
        elif sums == 64 :
            puzzle_length = 8
        for i in range(puzzle_length) :
            L = [0]*(puzzle_length)
            List.append(L)    
    elif N == 3 :
        list1 = lst[0]
        list2 = lst[1]
        list3 = lst[2]
        for i in list1 :
            sums = sums + sum(i)
        for i in list2 :
            sums = sums + sum(i)
        for i in list3 :
            sums = sums + sum(i)
        if sums == 4 :
            puzzle_length = 2
        elif sums == 9 :
            puzzle_length = 3
        elif sums == 16 :
            puzzle_length = 4
        elif sums == 25 :
            puzzle_length = 5
        elif sums == 36 :
            puzzle_length = 6
        elif sums == 49 :
            puzzle_length = 7
        elif sums == 64 :
            puzzle_length = 8
        for i in range(puzzle_length) :
            L = [0]*(puzzle_length)
            List.append(L)
    elif N == 4 :
        list1 = lst[0]
        list2 = lst[1]
        list3 = lst[2]
        list4 = lst[3]
        for i in list1 :
            sums = sums + sum(i)
        for i in list2 :
            sums = sums + sum(i)
        for i in list3 :
            sums = sums + sum(i)
        for i in list4 :
            sums = sums + sum(i)
        if sums == 4 :
            puzzle_length = 2
        elif sums == 9 :
            puzzle_length = 3
        elif sums == 16 :
            puzzle_length = 4
        elif sums == 25 :
            puzzle_length = 5
        elif sums == 36 :
            puzzle_length = 6
        elif sums == 49 :
            puzzle_length = 7
        elif sums == 64 :
            puzzle_length = 8
        #puzzle_length = max(len(list1), len(list2), len(list3), len(list4)) + max(len(list1[0]), len(list2[0]), len(list3[0]), len(list4[0]))
        for i in range(puzzle_length) :
            L = [0]*(puzzle_length)
            List.append(L)
    else :
        list1 = lst[0]
        list2 = lst[1]
        list3 = lst[2]
        list4 = lst[3]
        list5 = lst[4]
        for i in list1 :
            sums = sums + sum(i)
        for i in list2 :
            sums = sums + sum(i)
        for i in list3 :
            sums = sums + sum(i)
        for i in list4 :
            sums = sums + sum(i)
        for i in list5 :
            sums = sums + sum(i)
        if sums == 4 :
            puzzle_length = 2
        elif sums == 9 :
            puzzle_length = 3
        elif sums == 16 :
            puzzle_length = 4
        elif sums == 25 :
            puzzle_length = 5
        elif sums == 36 :
            puzzle_length = 6
        elif sums == 49 :
            puzzle_length = 7
        elif sums == 64 :
            puzzle_length = 8
    
        for i in range(puzzle_length) :
            L = [0]*(puzzle_length)
            List.append(L)
    next_block = 0
    lists = lst[0]
    prev = []
    prev = List
    a = 0
    List = get_result(lists, lst, next_block, List,a, prev)
    print(List)
    
   
main()
