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
    #for j in range(len(locate_list)) :
        #print(locate_list[j])
    return locate_list

def make_people_list(dicts, locate_list) :
    people_list = []
    for i in locate_list :
        people_list.append(dicts[i])
    #for j in range(len(people_list)) :
        #print(people_list[j])
    return people_list

def getting(locate_list, people_list, distance) :
    index = len(people_list)-1
    Max = 0
    for j in range(index, 0, -1) :
        cum = people_list[j]
        m = j-1
        while(locate_list[j] - distance <= locate_list[m]+distance) :
            cum = cum + people_list[m]
            #if cum > Max :
                #Max = cum
            m = m - 1
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
    result = getting(locate_list, people_list, distance)
    print(result)

main()
