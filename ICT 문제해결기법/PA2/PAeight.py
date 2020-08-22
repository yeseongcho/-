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
    #people_list = sorted(people_list)
    return people_list


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


def getting(locate_list, people_list, distance, k, Logic) :
    index = len(people_list) - 1
    Max = 0
    if Logic == True :
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

    if Logic == False :
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
    result = getting(locate_list, people_list, distance, k, Logic)
    print(result)
    

main()
