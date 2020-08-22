def make_locate_list(dicts) :
    locate_list = []
    for i in dicts :
        locate_list.append(i)
    locate_list = sorted(locate_list)
    return locate_list

def make_people_list(dicts) :
    people_list = []
    for i in dicts :
        people_list.append(dicts[i])
    people_list = sorted(people_list)
    return people_list


def find_maxindex(people_list, dicts) :
    sorting_people = sorted(people_list)
    c = people_list[0] + people_list[1]
    k = 2
    while(c > people_list[k]) :
            c = c + people_list[k]
            k = k+1
            if k ==len(people_list) -1 :
                return k, False
        
    return k, True


def getting(locate_list, people_list, distance, k, Logic) :
    index = len(people_list)-1
    Max = 0
    if Logic == True :
        for j in range(index, 0, -1) :
            cum = people_list[j]
            m = j-1
            while(locate_list[j] - distance <= locate_list[m]+distance) :
                cum = cum + people_list[m]
                
                m = m - 1
                if m == -1 :
                    break
            if cum > Max :
                    Max = cum
            
            if people_list[j-1] == people_list[k] :
                break
        
     if Logic == False :
         for j in range(index, 0, -1) :
             cum = people_list[j]
             m = j-1
             while(locate_list[j] - distance <= locate_list[m]+distance) :
                 cum = cum + people_list[m]
                 
            
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
    people_list = make_people_list(dicts)
    k, Logic = find_maxindex(people_list, dicts)
    result = getting(locate_list, people_list, distance, k, Logic)
    print(result)
    

main()
