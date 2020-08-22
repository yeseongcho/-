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

def make_tuples_and_list(locate_list, distance, dicts) :
    total = []
    for elements in locate_list :
        if elements < distance :
            start = 0
            end = elements + distance
            total.append((start, end, dicts[elements]))

        else :
            start = elements - distance
            end = elements + distance
            total.append((start, end, dicts[elements]))
    
    return total

def comparison(total) :
    cum = total[0][2]
    j = 1
    Max_cum = 0
    for i in range(len(total)-1) :
        cum = 0
        j = 0
        while(total[i+j][0] <= total[i][1] ) :
            cum = cum + total[i+j][2]
            j = j+1
        if Max_cum < cum :
            Max_cum = cum

    return Max_cum
            
def main() :
    data = [int(x) for x in input().split()]
    build_count = data[0]
    distance = data[1]
    dicts = {}
    for i in range(build_count) :
        datas = [int(m) for m in input().split()]
        dicts[datas[1]] = datas[0]
    locate_list = make_locate_list(dicts)
    total = make_tuples_and_list(locate_list, distance, dicts)
    result = comparison(total)
    print(result)

main()
            
