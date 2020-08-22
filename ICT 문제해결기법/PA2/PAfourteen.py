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


def make_locate_list(dicts) :
    locate_list = []
    for i in dicts :
        locate_list.append(i)
    locate_list = quick_sort(locate_list)
    return locate_list

def make_people_list(dicts, locate_list) :
    people_list = []
    for i in locate_list :
        people_list.append(dicts[i])
    return people_list

def make_lists_of_tuple(dicts) :
    lists = []
    for i in dicts :
        lists.append((dicts[i], i))
    lists = quick_sort(lists)
    return lists


def find_maxindex(people_list, dicts) :
    sorting_people = quick_sort(people_list)
    c = sorting_people[0] + sorting_people[1]
    k = 2
    while(c > sorting_people[k]) :
            c = c + sorting_people[k]
            k = k+1
            if k ==len(sorting_people) -1 :
                return k, False
        
    return k, True
"""
def Cum(sorting_people, m) :
    sofar = 0
    for i in range(m) :
        sofar = sofar + sorting_people[m]
    return sofar
"""

def getting(locate_list, people_list, distance, k, Logic, lists, dicts) :
    index = len(people_list) - 1
    Max = 0
    #sorting_people = quick_sort(people_list)
    # 누적 k가 존재할 때
    if Logic == True  :
        for j in range(index, 0, -1) :
            cum = people_list[j]
            m = j-1
            while(locate_list[j] - distance <= locate_list[m] + distance) :
                cum = cum + people_list[m]
                m = m-1
                if m == -1 :
                    break
                
            if cum > Max :
                Max = cum
            if people_list[m+1] == people_list[k] :
                break
            if o < index+1 :
                while(locate_list[j] + distance >= locate_list[o] - distance) :
                    cum = cum + people_list[o]
                    o = o + 1
                    if o == index+1 :
                        continue
    """
    if Logic == False :
        lists = quick_sort(lists)
        Massive = lists[index][0]
        for j in range(index, 0, -1) :
            cum = lists[j][0]
            m = j-1
            while(lists[j][1] - distance <= lists[m][1] + distance) :
                cum = cum + lists[m][1]
                m = m - 1
            if cum > Max :
                Max = cum
            if cum < Massive :
                break
    """
    # 누적 k가 존재하지 않을 때
    if Logic == False  :
        Massive = lists[index][0]
        #print(Massive)
        Max_locate = lists[index][1]
        for me in range(len(people_list)) :
            if people_list[me] == Massive :
                break
        #print(me)
        Max = Massive
        arr = []
        # Max의 범위를 포함하는 범위들 누적값 Max누적 구함
        i = me - 1
        p = me + 1
        #q = me
        #r = me
        if (Max_locate - distance < 0 ) :
            while(Max_locate + distance >= locate_list[p]-distance) :
                Max = Max + people_list[p]
                p = p + 1
                arr.append(locate_list[p])
                if p == index + 1 :
                    break
        elif (Max_locate + distance > locate_list[index]) :
            while(Max_locate - distance <= locate_list[i]+distance) :
                Max = Max + people_list[i]
                i = i - 1
                arr.append(locate_list[i])
                if i == -1 :
                    break
        else :
            while(Max_locate - distance <= locate_list[i]+distance) :
                Max = Max + people_list[i]
                i = i - 1
                arr.append(locate_list[i])
                if i == -1 :
                    break
            while(Max_locate + distance >= locate_list[p]-distance) :
                Max = Max + people_list[p]
                p = p + 1
                arr.append(locate_list[p])
                if p == index + 1 :
                    break
        cum = 0
        
        if len(arr) != 0 :
            for a in dicts :
                if a not in arr :
                    cum = cum + dicts[a]
            if cum < Max :
                return Max

        """
        if len(arr) == 0 :
            
            for a in range(index) :
                #print(cum)
                cum = cum + lists[a][0]

            #print(cum)       
        """

        # 마지막의 경우
        
        Max = 0
        cumu = 0
        for n in range(index, 0, -1) :
            cumu = people_list[n]
            m = n-1
            o = n+1
            while(locate_list[n] - distance <= locate_list[m] + distance) :
                cumu = cumu + people_list[m]
                m = m - 1
                if m == -1 :
                    break
            if o < index+1 :
                while(locate_list[n] + distance >= locate_list[o] - distance) :
                    cumu = cumu + people_list[o]
                    o = o + 1
                    if o == index+1 :
                        break
            if cumu > Max :
                Max = cumu

                    
    return Max

def main() :
    data = [int(x) for x in input().split()]
    build_count = data[0]
    distance = data[1]
    dicts = {}
    for i in range(build_count) :
        datas = [int(m) for m in input().split()]
        dicts[datas[1]] = datas[0]
    locate_list = make_locate_list(dicts)
    people_list = make_people_list(dicts, locate_list)
    lists = make_lists_of_tuple(dicts)
    k, Logic = find_maxindex(people_list, dicts)
    result = getting(locate_list, people_list, distance, k, Logic, lists, dicts)
    print(result)
    

main()
