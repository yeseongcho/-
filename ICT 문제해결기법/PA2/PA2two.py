def make_locate_list(dicts) :
    locate_list = []
    for i in dicts :
        locate_list.append(i)
    return locate_list


def peoples_by_locates(locate_list, distance, dicts) :
    peoples_by_locate = {}
    for i in locate_list :
        if i < distance :
            for j in range(0, i+distance+1) :
                if j in peoples_by_locate :
                    peoples_by_locate[j] = peoples_by_locate[j] + dicts[i]
                else :
                    peoples_by_locate[j] = dicts[i]
        else :
            for k in range(i-distance, i+distance+1) :
                if k in peoples_by_locate :
                    peoples_by_locate[k] = peoples_by_locate[k] + dicts[i]
                else :
                    peoples_by_locate[k] = dicts[i]

    return peoples_by_locate

def find(peoples_by_locate) :
    Max = 0
    for i in peoples_by_locate :
        if peoples_by_locate[i] > Max :
            Max = peoples_by_locate[i]
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
    peoples_by_locate = peoples_by_locates(locate_list, distance, dicts)
    Max = find(peoples_by_locate)
    print(Max)
    
main()
                
