def get_list() :
    list1 = []
    h, w = [int(x) for x in input().split()]
    for j in range(h) :
        list1.append([int(x) for x in input().split()])
    return list1


def can_merge_side(list1, list2, n) :
    result = True
    
    
    return result

def can_merge_updown() :
    s


def get_result(N, list1, list2, lst, next_block) :
    i = 0
    if N = 1 :





    elif N = 4 : # 2 이상일수도...
        
        if len(list1) == len(list2) :



        else :
            if len(list1) > len(list2) :


                



            else :
                ## 좌우 결합일때의 if케이스들
                if len(list1) == 1 and len(list2) == 2 :
                    


                elif len(list1) == 1 and len(list2) == 3 :
                    check_list = []
                    check_list2 = []
                    check_list_all = []
                    length_list1 = len(list1[0])
                    length_list2 = len(list2[0])
                    list1[0] = list1[0] + [0]*(length_list2)
                    list2[0] = list2[0] + [0]*(length_list1)
                    list2[1] = list2[1] + [0]*(length_list1)
                    list2[2] = list2[2] + [0]*(length_list1)
                    # 1번째 pair
                    # [0번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list1[i] = list1[0][i] + list2[0][i]
                    check_list_all = check_list
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a] = list2[0][a+1]
                    # [1번째 슬라이싱]
                    for 
                    

                elif len(list1) == 1 and len(list2) == 4 :
                    check_list = []
                    check_list2 = []
                    check_list_all = []
                    length_list1 = len(list1[0])
                    length_list2 = len(list2[0])
                    list1[0] = list1[0] + [0]*(length_list2)
                    list2[0] = list2[0] + [0]*(length_list1)
                    list2[1] = list2[1] + [0]*(length_list1)
                    list2[2] = list2[2] + [0]*(length_list1)
                    list2[3] = list2[3] + [0]*(length_list1)
                    # 1번째 pair
                    # [0번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                    check_list_all = check_list 
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2) - 2, -1, -1) :
                        list2[0][a] = list2[0][a+1]
                    # [1번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                    check_list_all = check_list 
                    if 2 not in check_list_all :
                        list2[1] = check_list
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2) - 2, -1, -1) :
                        list2[1][a] = list2[1][a+1]
                    # [2번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[2][i]
                    check_list_all = check_list 
                    if 2 not in check_list_all :
                        list2[2] = check_list
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2) - 2, -1, -1) :
                        list2[2][a] = list2[2][a+1]
                    # [3번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[3][i]
                    check_list_all = check_list 
                    if 2 not in check_list_all :
                        list2[3] = check_list
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    

                elif len(list1) == 2 and len(list2) == 3 :
                    ## 좌우결합일 때 slicing 합을 통해 적합한 케이스 산출
                    check_list = []
                    check_list2 = []
                    check_list_all = []
                    length_list1 = len(list1[0])
                    length_list2 = len(list2[0])
                    list1[0] = list1[0] + [0]*(length_list2)
                    list1[1] = list1[1] + [0]*(length_list2)
                    list2[0] = list2[0] + [0]*(length_list1)
                    list2[1] = list2[1] + [0]*(length_list1)
                    list2[2] = list2[2] + [0]*(length_list1)
                    # 1번째 pair
                    # [0번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a] = list2[0][a+1]
                        list2[1][a] = list2[1][a+1]
                    # [1번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a] = list2[0][a+1]
                        list2[1][a] = list2[1][a+1]
                    # [2번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a] = list2[0][a+1]
                        list2[1][a] = list2[1][a+1]
                    # 2번째 pair
                    # [0번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a] = list2[1][a+1]
                        list2[2][a] = list2[2][a+1]
                    # [1번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a] = list2[1][a+1]
                        list2[2][a] = list2[2][a+1]
                    # [2번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    

                elif len(list1) == 2 and len(list2) == 4 :
                    ## 좌우결합일 때 slicing 합을 통해 적합한 케이스 산출
                    check_list = []
                    check_list2 = []
                    check_list_all = []
                    length_list1 = len(list1[0])
                    length_list2 = len(list2[0])
                    
                    list1[0] = list1[0] + [0]*(length_list2)
                    list1[1] = list1[1] + [0]*(length_list2)
                    list2[0] = list2[0] + [0]*(length_list1)
                    list2[1] = list2[1] + [0]*(length_list1)
                    list2[2] = list2[2] + [0]*(length_list1)
                    list2[3] = list2[3] + [0]*(length_list1)
                    # 1번째 pair
                    # [0번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a] = list2[0][a+1]
                        list2[1][a] = list2[1][a+1]
                    # [1번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, 0) :
                        list2[0][a] = list2[0][a+1]
                        list2[1][a] = list2[1][a+1]
                    # [2번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, 1) :
                        list2[0][a] = list2[0][a+1]
                        list2[1][a] = list2[1][a+1]
                    # [3번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    # 2번째 pair
                    # [0번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a] = list2[1][a+1]
                        list2[2][a] = list2[2][a+1]
                    # [1번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a] = list2[1][a+1]
                        list2[2][a] = list2[2][a+1]
                    #[2번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, 1) :
                        list2[1][a] = list2[1][a+1]
                        list2[2][a] = list2[2][a+1]
                    # [3번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    # 3번째 pair
                    # [0번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[2][i]
                        check_list2[i] = list1[1][i] + list2[3][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[2] = check_list
                        list2[3] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[2][a] = list2[2][a+1]
                        list2[3][a] = list2[3][a+1]
                    # [1번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[2][i]
                        check_list2[i] = list1[1][i] + list2[3][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[2] = check_list
                        list2[3] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[2][a] = list2[2][a+1]
                        list2[3][a] = list2[3][a+1]
                    #[2번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[2][i]
                        check_list2[i] = list1[1][i] + list2[3][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[2] = check_list
                        list2[3] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, 1) :
                        list2[2][a] = list2[2][a+1]
                        list2[3][a] = list2[3][a+1]
                    # [3번째 슬라이싱]
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[2][i]
                        check_list2[i] = list1[1][i] + list2[3][i]
                    check_list_all = check_list + check_list2
                    if 2 not in check_list_all :
                        list2[2] = check_list
                        list2[3] = check_list2
                        next_block = next_block + 1
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    
                    
    

                elif len(list1) == 3 and len(list2) == 4 :

                # 상하 결합일때의 if 케이스들
                if    
    
    

def main() :
    N = int(input())
    lst = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    for i in range(N) :
        lst.append(get_list())
    if N == 1 :
        list1 = lst[0]
    elif N == 2 :
        list1 = lst[0]
        list2 = lst[1]
    elif N == 3 :
        list1 = lst[0]
        list2 = lst[1]
        list3 = lst[2]
    elif N == 4 :
        list1 = lst[0]
        list2 = lst[1]
        list3 = lst[2]
        list4 = lst[3]
    else :
        list1 = lst[0]
        list2 = lst[1]
        list3 = lst[2]
        list4 = lst[3]
        list5 = lst[4]

    Fianl_list = []
    is_True = True
    if N == 1 :


    elif N == 2 :



    elif N == 3 :



    elif N == 4 :
        next_list = 1
        Final_list, is_True = get_result(list1, list2, lst, next_list)
        


    else :
        
    
main()
        
            
        
