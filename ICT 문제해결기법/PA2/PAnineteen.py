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


def find_maxindex(people_list, dicts) :
    #sorting_people = quick_sort(people_list)
    #c = sorting_people[0] + sorting_people[1]
    c = people_list[0] + people_list[1]
    k = 2
    while(c > people_list[k]) :
        c = c + people_list[k]
        k = k+1
        if k == len(people_list) -1 :
            return k, False
    return k, True

def find_maxindex2(people_list, dicts) :
    #sorting_people = quick_sort(people_list)
    #c = sorting_people[len(sorting_people)-1] + sorting_people[len(sorting_people)-2]
    c = people_list[len(people_list)-1] + people_list[len(people_list)-2]
    r = len(people_list)-3
    while( c > people_list[r]) :
        c = c + people_list[r]
        r = r - 1
        if r == 0 :
            return r, False
    return r, True


def getting(locate_list, people_list, distance, k, Logic, r, Logic2) :
    index = len(people_list) - 1
    Max = 0
    if((Logic == True) and (Logic2 == False)):
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
    elif((Logic == False) and (Logic2 == True)) :
        for j in range(0, index+1) :
            cum = people_list[j]
            o = j + 1
            while(locate_list[j] + distance >= locate_list[o] - distance) :
                cum = cum + people_list[o]
                o = o + 1
                if o == index + 1 :
                    break
            if cum > Max :
                Max = cum
            if people_list[o-1] == people_list[r] :
                break
    else :
        for j in range(index, 0, -1) :
            cum = people_list[j]
            m = j-1
            o = j+1
            while(locate_list[j] - distance <= locate_list[m] + distance) :
                cum = cum + people_list[m]
                m = m-1
                if m == -1 :
                    break
            if o < index + 1 :
                while(locate_list[j] + distance >= locate_list[o] - distance) :
                    cum = cum + people_list[o]
                    o = o + 1
                    if o == index + 1 :
                        break
            if cum > Max :
                Max = cum
    
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
    k, Logic = find_maxindex(people_list, dicts)
    r, Logic2 = find_maxindex2(people_list, dicts)
    result = getting(locate_list, people_list, distance, k, Logic, r, Logic2)
    print(result)
    

main()
