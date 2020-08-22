def get_list() :
    list1 = []
    h, w = [int(x) for x in input().split()]
    for j in range(h) :
        list1.append([int(x) for x in input().split()])
    return list1






### 모든 리스트 슬라이싱 결과가 2인 경우!! --- 결합가능한 special case

### 완성된 마지막 결과에서 끝에서부터의 0은 모두 제거해주어야한다 ----- 이 경우도 경우를 잘 생각해야한다. 아직 여기 수정 안됨..!!!
### 2와 0만 있는 경우가 더해진 경우 --- 1이 없는 경우로 하자
def get_result() :
    if len(list1) < len(list2) :
        if len(list1) == 1 and len(list2) == 2 :
            check_list = []
            check_list_all = []
            length_list1 = len(list1)
            length_list2 = len(list2[0])
            list1 = list1 + [0]*(length_list2)
            list2[0] = list2[0] + [0]*(length_list1)
            list2[1] = list2[1] + [0]*(length_list1)
            
            if len(list1) > len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block+1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    if 1 not in check_list_all :
                        
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        next_block = next_block+1
                        if next_block == len(lst) :
                            return list1, list2
                        return get+result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a+1] = list2[1][a]                


            elif len(list1) < len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list1[a+1] = list1[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list1[a+1] = list1[a]

        
            elif len(list1) == len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list1[a+1] = list1[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list1[a+1] = list1[a]
                        
                


        elif len(list1) == 1 and len(list2) == 3 :
            check_list = []
            check_list_all = []
            length_list1 = len(list1)
            length_list2 = len(list2[0])
            list1 = list1 + [0]*(length_list2)
            list2[0] = list2[0] + [0]*(length_list1)
            list2[1] = list2[1] + [0]*(length_list1)
            list2[2] = list2[2] + [0]*(length_list1)
            
            if len(list1) > len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list_all
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list_all
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a+1] = list2[1][a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[2] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[2][a+1] = list2[2][a]
                
        
            elif len(list1) < len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1) -2, -1, -1) :
                        list1[a+1] = list1[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1) -2, -1, -1) :
                        list1[a+1] = list1[a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1) -2, -1, -1) :
                        list1[a+1] = list1[a]
                        




            elif len(list1) == len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1) -2, -1, -1) :
                        list1[a+1] = list1[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1) -2, -1, -1) :
                        list1[a+1] = list1[a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1) -2, -1, -1) :
                        list1[a+1] = list1[a]
                
                
            




        elif len(list1) == 1 and len(list2) == 4 :
            check_list = []
            check_list_all = []
            length_list1 = len(list1)
            length_list2 = len(list2[0])
            list1 = list1 + [0]*(length_list2)
            list2[0] = list2[0] + [0]*(length_list1)
            list2[1] = list2[1] + [0]*(length_list1)
            list2[2] = list2[2] + [0]*(length_list1)
            list2[3] = list2[3] + [0]*(length_list1)
            
            if len(list1) > len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a+1] = list2[1][a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[2] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[2][a+1] = list2[2][a]
                # 4 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[3][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[3] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[3][a+1] = list2[3][a]
                

            elif len(list1) < len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[a+1] = list1[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[a+1] = list1[a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[2] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[a+1] = list1[a]
                # 4 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[3][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[3] = check_list
                        next_block = next_block + 1
                        if next_block = len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[a+1] = list1[a]
                        


            elif len(list1) == len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        next_block = next_block + 1
                        if next_block = len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[a+1] = list1[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list2[1] = check_list
                        next_block = next_block + 1
                        if next_block = len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[a+1] = list1[a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[2] = check_list
                        next_block = next_block + 1
                        if next_block = len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[a+1] = list1[a]
                # 4 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[i] + list2[3][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[3] = check_list
                        next_block = next_block + 1
                        if next_block = len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[a+1] = list1[a]
                        
                




        elif len(list1) == 2 and len(list2) == 3 :
            check_list = []
            check_list2 = []
            check_list_all = []
            length_list1 = len(list1[0])
            length_list2 = len(list2[0])
            list1[0] = list1[0] + [0]*(length_list2)
            list1[1] = list1[1] + [0]*(length_list2)
            list2[0] = list2[0] + [0]*(length_list1)
            list2[1] = list2[1] + [0]*(leng1h_list1)
            list2[2] = list2[2] + [0]*(length_list1)
            if len(list1[0]) > len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                        list2[1][a+1] = list2[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a+1] = list2[1][a]
                        list2[2][a+1] = list2[2][a]
            

            elif len(list1[0]) < len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]


            elif len(list1[0]) == len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                



        elif len(list1) == 2 and len(list2) == 4 :
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
            if len(list1[0]) > len(list2[0]) :
                # 자체적으로 이 큰 for문을 통해 4번 슬라이싱을 해주는 것 같은데??
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                        list2[1][a+1] = list2[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a+1] = list2[1][a]
                        list2[2][a+1] = list2[2][a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[2][i]
                        check_list2[i] = list1[1][i] + list2[3][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[2] = check_list
                        list2[3] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[2][a+1] = list2[2][a]
                        list2[3][a+1] = list2[3][a]
                

            elif len(list1[0]) < len(list2[0]) :
                 # 자체적으로 이 큰 for문을 통해 4번 슬라이싱을 해주는 것 같은데??
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[2][i]
                        check_list2[i] = list1[1][i] + list2[3][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[2] = check_list
                        list2[3] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]



            elif len(list1[0]) == len(list2[0]) :
                # 자체적으로 이 큰 for문을 통해 4번 슬라이싱을 해주는 것 같은데??
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        list2[1] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[1][i] + list2[2][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list2[1] = check_list
                        list2[2] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1+length_list2) :
                        check_list[i] = list1[0][i] + list2[2][i]
                        check_list2[i] = list1[1][i] + list2[3][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[2] = check_list
                        list2[3] = check_list2
                        next_block = next_block + 1
                        ## 종료 케이스가 필요할듯
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                

        elif len(list1) == 3 and len(list2) == 4 :
            check_list = []
            check_list2 = []
            check_list3 = []
            check_list_all = []
            length_list1 = len(list1[0])
            length_list2 = len(list2[0])
            list1[0] = list1[0] + [0]*(length_list2)
            list1[1] = list1[1] + [0]*(length_list2)
            list1[2] = list1[2] + [0]*(length_list2)
            list2[0] = list2[0] + [0]*(length_list1)
            list2[1] = list2[1] + [0]*(length_list1)
            list2[2] = list2[2] + [0]*(length_list1)
            list2[3] = list2[3] + [0]*(length_list1)
            if len(list1[0]) > len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                        check_list3[i] = list1[2][i] + list2[2][i]
                    check_list_all = check_list + check_list2 + check_list3
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        list2[1] = check_list1
                        list2[2] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                        list2[1][a+1] = list2[1][a]
                        list2[2][a+1] = list2[2][a]
                # 2 pair 여기 짜야함!! -- 여기만 짜고 all 2 케이스 분석해보자
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[0][i] + list2[2][i]
                        check_list3[i] = list1[0][i] + list2[3][i]
                    check_list_all = check_list + check_list2 + check_list3
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        list2[2] = check_list2
                        list2[3] = check_list3
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list2[1][a+1] = list2[1][a]
                        list2[2][a+1] = list2[2][a]
                        list2[3][a+1] = list2[3][a]
                        


            elif len(list1[0]) < len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                        check_list3[i] = list1[2][i] + list2[2][i]
                    check_list_all = check_list + check_list2 + check_list3
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        list2[1] = check_list1
                        list2[2] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                        list1[2][a+1] = list1[2][a]
                # 2 pair 여기 짜야함!! -- 여기만 짜고 all 2 케이스 분석해보자
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[0][i] + list2[2][i]
                        check_list3[i] = list1[0][i] + list2[3][i]
                    check_list_all = check_list + check_list2 + check_list3
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        list2[2] = check_list2
                        list2[3] = check_list3
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                        list1[2][a+1] = list1[2][a]
                



            elif len(list1[0]) == len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                        check_list3[i] = list1[2][i] + list2[2][i]
                    check_list_all = check_list + check_list2 + check_list3
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[0] = check_list
                        list2[1] = check_list1
                        list2[2] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                        list1[2][a+1] = list1[2][a]
                # 2 pair 여기 짜야함!! -- 여기만 짜고 all 2 케이스 분석해보자
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[1][i]
                        check_list2[i] = list1[0][i] + list2[2][i]
                        check_list3[i] = list1[0][i] + list2[3][i]
                    check_list_all = check_list + check_list2 + check_list3
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list2[1] = check_list
                        list2[2] = check_list2
                        list2[3] = check_list3
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list2, lst[next_block], lst, next_block)
                    for a in range((length_list2)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                        list1[2][a+1] = list1[2][a]
                
            
        

###### 여기까지 했는데 이거는 최후의 보루로 놓자. 다른 아이디어를 생각하자!
    elif len(list1) > len(list2) :
        if len(list1) == 2 and len(list2) == 1 :
            check_list = []
            check_list_all = []
            length_list1 = len(list1[0])
            length_list2 = len(list2)
            list1[0] = [0]*(length_list2)
            list1[1] = [0]*(length_list2)
            list2 = [0]*(length_list1)
            if len(list1[0]) > len(list2) :
               # 1 pair
               for j in range(length_list1 + length_list2) :
                   for i in range(length_list1 + length_list2) :
                       check_list[i] = list2[i] + list1[0][i]
                   check_list_all = check_list
                   if not(1 in check_list_all and 2 in check_list_all) :
                       list1[0] = check_list
                       #list1[1] = check_list2
                       next_block = next_block+1
                       if next_block == len(lst) :
                           return list1, list2
                       return get_result(N, list1, lst[next_block], lst, next_block)
                   for a in range((length_list1) -2, -1, -1) :
                       list2[a+1] = list2[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                   for i in range(length_list1 + length_list2) :
                       check_list[i] = list2[i] + list1[1][i]
                   check_list_all = check_list
                   if not(1 in check_list_all and 2 in check_list_all) :
                       list1[0] = check_list
                       list1[1] = check_list2
                       next_block = next_block+1
                       if next_block == len(lst) :
                           return list1, list2
                       return get_result(N, list1, lst[next_block], lst, next_block)
                   for a in range((length_list1) -2, -1, -1) :
                       list2[a+1] = list2[a]


            elif len(list1[0]) < len(list2) :
                # 1 pair
               for j in range(length_list1 + length_list2) :
                   for i in range(length_list1 + length_list2) :
                       check_list[i] = list2[i] + list1[0][i]
                   check_list_all = check_list
                   if not(1 in check_list_all and 2 in check_list_all) :
                       list1[0] = check_list
                       #list1[1] = check_list2
                       next_block = next_block+1
                       if next_block == len(lst) :
                           return list1, list2
                       return get_result(N, list1, lst[next_block], lst, next_block)
                   for a in range((length_list1) -2, -1, -1) :
                       list1[0][a+1] = list1[0][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                   for i in range(length_list1 + length_list2) :
                       check_list[i] = list2[i] + list1[1][i]
                   check_list_all = check_list
                   if not(1 in check_list_all and 2 in check_list_all) :
                       list1[0] = check_list
                       list1[1] = check_list2
                       next_block = next_block+1
                       if next_block == len(lst) :
                           return list1, list2
                       return get_result(N, list1, lst[next_block], lst, next_block)
                   for a in range((length_list1) -2, -1, -1) :
                       list1[1][a+1] = list1[1][a]

            elif len(list1[0]) == len(list2) :
                # 1 pair
               for j in range(length_list1 + length_list2) :
                   for i in range(length_list1 + length_list2) :
                       check_list[i] = list2[i] + list1[0][i]
                   check_list_all = check_list
                   if not(1 in check_list_all and 2 in check_list_all) :
                       list1[0] = check_list
                       #list1[1] = check_list2
                       next_block = next_block+1
                       if next_block == len(lst) :
                           return list1, list2
                       return get_result(N, list1, lst[next_block], lst, next_block)
                   for a in range((length_list1) -2, -1, -1) :
                       list2[a+1] = list2[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                   for i in range(length_list1 + length_list2) :
                       check_list[i] = list2[i] + list1[1][i]
                   check_list_all = check_list
                   if not(1 in check_list_all and 2 in check_list_all) :
                       list1[0] = check_list
                       list1[1] = check_list2
                       next_block = next_block+1
                       if next_block == len(lst) :
                           return list1, list2
                       return get_result(N, list1, lst[next_block], lst, next_block)
                   for a in range((length_list1) -2, -1, -1) :
                       list2[a+1] = list2[a]

                


        elif len(list1) == 3 and len(list2) == 1 :
            check_list = []
            check_list_all = []
            length_list1 = len(list1[0])
            length_list2 = len(list2)
            list1[0] = list1[0] + [0]*(length_list2)
            list1[1] = list1[1] + [0]*(length_list2)
            list1[2] = list1[2] + [0]*(length_list2)
            list2 = list2 + [0]*(length_list1)
            
            if len(list1[0]) > len(list2) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[a+1] = list2[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[a+1] = list2[a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[2] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[a+1] = list2[a]
                                       
            elif len(list1[0]) < len(list2) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[1][a+1] = list1[1][a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[2] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[2][a+1] = list1[2][a]



            elif len(list1[0]) == len(list2) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[0][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[0] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[a+1] = list2[a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[1][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[1] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[a+1] = list2[a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2 + list1[2][i]
                    check_list_all = check_list
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[2] = check_list
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[a+1] = list2[a]
                


        elif len(list1) == 3 and len(list2) == 2 :
            check_list = []
            check_list2 = []
            check_list_all = []
            length_list1 = len(list1[0])
            length_list2 = len(list2[0])
            list1[0] = list1[0] + [0]*(length_list2)
            list1[1] = list1[1] + [0]*(length_list2)
            list1[2] = list1[2] + [0]*(length_list2)
            list2[0] = list2[0] + [0]*(length_list1)
            list2[1] = list2[1] + [0]*(length_list1)
            if len(list1[0]) > len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[0] = check_list
                        list1[1] = check_list2
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                        list2[1][a+1] = list2[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[1][i] + list2[0][i]
                        check_list2[i] = list1[2][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[1] = check_list
                        list1[2] = check_list2
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[1][a+1] = list2[0][a]
                        list2[2][a+1] = list2[1][a]
            elif len(list1[0]) < len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[0] = check_list
                        list1[1] = check_list2
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[1][i] + list2[0][i]
                        check_list2[i] = list1[2][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[1] = check_list
                        list1[2] = check_list2
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[1][a+1] = list1[1][a]
                        list1[2][a+1] = list1[2][a]
            elif len(list1[0]) == len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[0][i] + list2[0][i]
                        check_list2[i] = list1[1][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[0] = check_list
                        list1[1] = check_list2
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                        list2[1][a+1] = list2[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list1[1][i] + list2[0][i]
                        check_list2[i] = list1[2][i] + list2[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[1] = check_list
                        list1[2] = check_list2
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list2[0][a+1] = list2[0][a]
                        list2[1][a+1] = list2[1][a]
                


        ### 여기부터 해야한다!!
        elif len(list1) == 4 and len(list2) == 1 :
            check_list = []
            check_list_all = []
            length_list1 = len(list1[0])
            length_list2 = len(list2[0])
            list1[0] = list1[0] + [0]*(length_list2)
            list1[1] = list1[1] + [0]*(length_list2)
            list1[2] = list1[2] + [0]*(length_list2)
            list1[3] = 
            list2
            for j in range(length_list1 + length_list2) :
                for i in range(length_list1 + length_list2) :
                    check_list[i] = list1[0]
                check_list_all = check_list
                if not(1 in check_list_all and 2 in check_list_all) :
                    list1

       
        elif len(list1) == 4 and len(list2) == 2 :
            check_list = []
            check_list2 = []
            check_list_all = []

            length_list1 = len(list1[0])
            length_list2 = len(list2[0])
            list1[0] = list1[0] + [0]*(length_list2)
            list1[1] = list1[1] + [0]*(length_list2)
            list1[2] = list1[2] + [0]*(length_list2)
            list1[3] = list1[3] + [0]*(length_list2)
            list2[0] = list2[0] + [0]*(length_list1)
            list2[1] = list2[0] + [0]*(length_list1)
            if len(list1[0]) > len(list2[0]):
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2[0][i] + list1[0][i]
                        check_list2[i] = list2[1][i] + list1[1][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list1[0] = check_list
                        list1[1] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2[0][i] + list1[1][i]
                        check_list2[i] = list2[1][i] + list1[2][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list1[1] = check_list
                        list1[2] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[1][a+1] = list1[1][a]
                        list1[2][a+1] = list1[2][a]
                # 3 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2[0][i] + list1[1][i]
                        check_list2[i] = list2[1][i] + list1[2][i]
                    check_list_all = check_list + check_list2
                    if not(1 in check_list_all and 2 in check_list_all) :
                        list1[1] = check_list
                        list1[2] = check_list2
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[1][a+1] = list1[0][a]
                        list1[2][a+1] = list1[1][a]



            elif len(list2[0]) > len(list1[0]) :






            elif len(list2[0]) == len(list1[0]) :
                
                



        elif len(list1) == 4 and len(list2) == 3 :
            check_list = []
            check_list2 = []
            check_list3 = []
            check_list_all = []
               
            length_list1 = len(list1[0])
            length_list2 = len(list2[0])
            list1[0] = list1[0] + [0]*(length_list2)
            list1[1] = list1[1] + [0]*(length_list2)
            list1[2] = list1[2] + [0]*(length_list2)
            list1[3] = list1[3] + [0]*(length_list2)
            list2[0] = list2[0] + [0]*(length_list1)
            list2[1] = list2[1] + [0]*(length_list1)
            list2[2] = list2[2] + [0]*(length_list1)
           
            if len(list1[0]) > len(list2[0]) :
                # 1 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2[0][i] + list1[0][i]
                        check_list2[i] = list2[1][i] + list1[1][i]
                        check_list3[i] = list2[2][i] + list1[2][i]
                    check_list_all = check_list + check_list2 + check_list_all
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list1[0] = check_list
                        list1[1] = check_list2
                        list1[2] = check_list3
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[0][a+1] = list1[0][a]
                        list1[1][a+1] = list1[1][a]
                        list1[2][a] = list1[2][a+1]
                # 2 pair
                for j in range(length_list1 + length_list2) :
                    for i in range(length_list1 + length_list2) :
                        check_list[i] = list2[0][i] + list1[1][i]
                        check_list2[i] = list2[1][i] + list1[2][i]
                        check_list3[i] = list2[2][i] + list1[3][i]
                    check_list_all = check_list + check_list2 + check_list_all
                    if not(1 in check_list_all and 2 in check_list_all)  :
                        list1[1] = check_list
                        list1[2] = check_list2
                        list1[3] = check_list3
                        next_block = next_block + 1
                        if next_block == len(lst) :
                            return list1, list2
                        return get_result(N, list1, lst[next_block], lst, next_block)
                    for a in range((length_list1)-2, -1, -1) :
                        list1[1][a+1] = list1[1][a]
                        list1[2][a+1] = list1[2][a]
                        list1[3][a] = list1[3][a+1]



            elif len(list1[0]) < len(list2[0]) :
                


        


    elif len(list1) == len(list2) :
        if len(list1) == 1 and len(list2) == 1 :


        elif len(list1) == 2 and len(list2) == 2 :

        elif len(list1) == 3 and len(list2) == 3 :


        elif len(list1) == 4 and len(list2) == 4 :
            
        







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


