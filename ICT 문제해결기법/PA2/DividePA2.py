def finding(dicts, distance) :
    locate_list = []
    for i in dicts :
        locate_list.append(i)
    mid = len(locate_list)//2
    MaxL = peoples_by_locates_left(locate_list, distance, dicts, mid)
    print('##########')
    MaxR = peoples_by_locates_right(locate_list, distance, dicts, mid)
    print('##########')
    MaxM = peoples_by_locates_mid(locate_list, distance, dicts, mid)
    return max(MaxL, MaxR, MaxM)

def peoples_by_locates_mid(locate_list, distance, dicts, mid) :
    peoples_by_locate = {}
    if locate_list[mid] < distance :
        for j in range(locate_list[mid] - distance, locate_list[mid] + distance+1) :
            if j in peoples_by_locate :
                peoples_by_locate[j] = peoples_by_locate[j] + dicts[locate_list[mid]]
            else :
                peoples_by_locate[j] = dicts[locate_list[mid]]
    else :
        for k in range(locate_list[mid] - distance, locate_list[mid] + distance+1) :
            if k in peoples_by_locate :
                peoples_by_locate[k] = peoples_by_locate[k] + dicts[locate_list[mid]]
            else :
                peoples_by_locate[k] = dicts[locate_list[mid]]
    Max = 0
    for i in peoples_by_locate :
        if peoples_by_locate[i] > Max :
            Max = peoples_by_locate[i]

    for a in peoples_by_locate :
        print(a)
        print(peoples_by_locate[a])
        print('\n')

    return Max
            
            

        

def peoples_by_locates_left(locate_list, distance, dicts, mid) :
    peoples_by_locate = {}
    for i in locate_list[:mid] :
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
    Max = 0
    for i in peoples_by_locate :
        if peoples_by_locate[i] > Max :
            Max = peoples_by_locate[i]

    for a in peoples_by_locate :
        print(a)
        print(peoples_by_locate[a])
        print('\n')

    return Max
    
def peoples_by_locates_right(locate_list, distance, dicts, mid) :
    peoples_by_locate = {}
    for i in locate_list[mid:] :
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
    Max = 0
    for i in peoples_by_locate :
        if peoples_by_locate[i] > Max :
            Max = peoples_by_locate[i]

    for a in peoples_by_locate :
        print(a)
        print(peoples_by_locate[a])
        print('\n')

    return Max
   

def main() :
    data = [int(x) for x in input().split()]
    build_count = data[0]
    distance = data[1]
    dicts = {}
    for i in range(build_count) :
        datas = [int(m) for m in input().split()]
        dicts[datas[1]] = datas[0]
    print(finding(dicts, distance))

main()
                
                
               

