import collections
import operator
import math

def b_search(L, U) :
    Mid = (U+L)//2
    return Mid

def can_buffer(fake_dic, date_dic, day, ranges, d, rest ,criteria) :
    if rest > ranges :
        criteria = criteria + 1
        if criteria > d :
            return False, fake_dic
        fake_dic[day] = ranges
        rest = rest-ranges
        if rest > ranges :
            if day == max(date_dic.keys()) :
                return False, fake_dic
            if day+criteria > max(date_dic.keys()) :
                return False, fake_dic
            #print(day+criteria)
            if day+criteria not in fake_dic :
                fake_dic[day+criteria] = 0
            fake_dic[day+criteria] = ranges + fake_dic[day+criteria]
            print(fake_dic)
            #rest = rest - ranges
            return can_buffer(fake_dic, date_dic, day, ranges, d, rest ,criteria)
        else :
            if day == max(date_dic.keys()) :
                return False, fake_dic
            if day+criteria > max(date_dic.keys()) :
                return False, fake_dic
            #print(day+criteria)
            if day+criteria not in fake_dic :
                fake_dic[day+criteria] = 0
            fake_dic[day+criteria] = rest + fake_dic[day+criteria]
            rest = fake_dic[day+1]
            print(fake_dic)
            criteria = 0
            return can_buffer(fake_dic, date_dic, day+1, ranges, d, rest, criteria)
    else :
        return True, fake_dic

def can_accomodate(fake_dic, date_dic, ranges, d, out_day) :
    for day in out_day :
        criteria = 0
        rest = fake_dic[day]
        #boolean, dic = can_buffer(fake_dic, date_dic, day, ranges, d, rest ,criteria)[0]
        if can_buffer(fake_dic, date_dic, day, ranges, d, rest ,criteria)[0] :
            fake_dic = can_buffer(fake_dic, date_dic, day, ranges, d, rest ,criteria)[1]
            continue
        else :
            return False
    return True

def ceil_search(L, U) :
    mid = math.ceil((L+U)/2)
    return mid

def round_search(L, U) :
    mid = round((L+U)/2)
    return mid

def main() :
    n = 0
    d = 0
    m = 0
    n, d, m = [int(x) for x in input().split()]

    date = [int(x) for x in input().split()]

    # 날짜별 환자 수 데이터 저장
    date_dic = dict(collections.Counter(date))

    # 시뮬레이션을 돌리기 위한 짝퉁 dictionary 설정
    fake_dic = date_dic

    dic = {}

    # binary search 범위 지정 L, U 설정
    U = max(date_dic.values())

    L = min(date_dic.values())

    # 가장 많은 환자가 신청한 날짜
    max_day = max(date_dic.items(), key = operator.itemgetter(1))[0]

    # 가장 적은 환자가 신청한 날짜
    min_day = min(date_dic.items(), key = operator.itemgetter(1))[0]
    
    ranges = b_search(L, U)

    # 정렬이 되어있어야 하지 않나...?
    out_day = [key for key in date_dic if date_dic[key] > ranges]

    #print(ranges)
    #print(out_day)
    rest = 0

    criteria = 0
    boolean = False

    Min = 9999999999

    while not boolean :
        boolean = can_accomodate(fake_dic, date_dic, ranges, d, out_day)
        if not boolean :
            fake_dic = date_dic
            ranges = b_search(ranges+1, L)
        else :
            Min = min(ranges, Min) # Min 값 저장
            fake_dic = date_dic

    new_L = L
 
    new_U = Min

    ranges = round_search(new_L, new_U)
    fake_dic = date_dic

    print(date_dic)
    print("##")
    print(fake_dic)

    can = []

    while new_U != ranges :
        if can_accomodate(fake_dic, date_dic, ranges, d, out_day) :
            fake_dic = date_dic
            Min = min(ranges, Min) # 갱신
            if Min not in can :
                can.append(Min)
            ranges = round_search(new_L, Min)
            if ranges in can :
                ranges = round_search(new_L, Min-1)
        else :
            fake_dic = date_dic # 얘는 항상 can_accomodate를 해줄때마다 갱신을 해주어야 한다.
            ranges = ceil_search(ranges, new_U)
            if ranges in can :
                ranges = ceil_search(ranges+1, new_U)

    print(Min)

main()

    
