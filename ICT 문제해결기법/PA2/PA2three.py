def make_locate_list(dicts) :
    locate_list = []
    for i in dicts :
        locate_list.append(i)
    return locate_list


def make_hospital_range(locate_list, distance) :
    hospital_range = []
    for i in locate_list :
        if i < distance :
            if 0 not in hospital_range :
                hospital_range.append(0)
            if distance + i not in hospital_range :
                hospital_range.append(i+distance)
        else :
            if i - distance not in hospital_range :
                hospital_range.append(i-distance)
            if i + distance not in hospital_range :
                hospital_range.append(i+distance)
    return hospital_range

        
def count_people_max(dicts, hospital_range, distance) :
    people_max = 0
    people_cum = 0
    lists = []
    for x in hospital_range :
        people_cum = 0
        for m in dicts :
            if m in range(x-distance, x+distance+1) :
                people_cum = people_cum + dicts[m]
        lists.append(people_cum)
    result = max(lists)
    
            
    return result

def main() :
    data = [int(x) for x in input().split()]
    build_count = data[0]
    distance = data[1]
    dicts = {}
    for i in range(build_count) :
        datas = [int(m) for m in input().split()]
        dicts[datas[1]] = datas[0]
    locate_list = make_locate_list(dicts)
    hospital_range = make_hospital_range(locate_list, distance)
    Final_result = count_people_max(dicts, hospital_range, distance)
    print(Final_result)

main()
            

