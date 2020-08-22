import collections
import operator
import math
import random

n = 0
d = 0
m = 0

n, d, m = [int(x) for x in input().split()]

# 날짜별 환자 수 데이터 저장
date = [int(x) for x in input().split()]
sums = len(date)

date_dic = dict(collections.Counter(date))
fake_dic = dict(collections.Counter(date))

# 시뮬레이션을 돌리기 위한 짝퉁 dictionary 설정

#print(date_dic)
#print(d)

# binary search 범위 지정 L, U 설정
U = max(date_dic.values())

L = min(date_dic.values())

# 가장 많은 환자가 신청한 날짜
#max_day = max(date_dic.items(), key = operator.itemgetter(1))[0]

# 가장 적은 환자가 신청한 날짜
#min_day = min(date_dic.items(), key = operator.itemgetter(1))[0]


def b_search(L, U) :
    Mid = (U+L)//2
    return Mid

ranges = b_search(L, U)

# 정렬?
# 우선, 이 부분이 상당히 시간을 잡아먹을 것 같다
out_day = [key for key in date_dic if date_dic[key] > ranges]


rest = 0
criteria = 0

# 메인 알고리즘..!
def can_buffer(fake_dic, day, ranges, d, rest ,criteria) :
    
    if rest > ranges :
        criteria = criteria + 1
        if criteria > d :
            return False, fake_dic
        fake_dic[day] = ranges
        rest = rest-ranges
        if rest > ranges :
            #if day == max(date_dic.keys()) :
            #    return False, fake_dic
            if day+criteria not in fake_dic :
                fake_dic[day+criteria] = 0
            if day+criteria > max(fake_dic.keys()) :
                return False, fake_dic
            fake_dic[day+criteria] = ranges + fake_dic[day+criteria]
            return can_buffer(fake_dic, day, ranges, d, rest ,criteria)
        else :
            #if day == max(date_dic.keys()) :
            #    return False, fake_dic
            if day+criteria not in fake_dic :
                fake_dic[day+criteria] = 0
            if day+criteria > max(fake_dic.keys()) :
                #print("###")
                return False, fake_dic
            fake_dic[day+criteria] = rest + fake_dic[day+criteria]
            rest = fake_dic[day+1]
            criteria = 0
            return can_buffer(fake_dic, day+1, ranges, d, rest, criteria)
    else :
        return True, fake_dic
        
        

boolean = True

#수용 가능 여부 확인...!
def can_accomodate(fake_dic, date_dic, ranges, d, out_day, sums) :
    # huristic
    if ranges*n < sums :
        return False
    for day in out_day :
        criteria = 0
        rest = fake_dic[day]
        boolean, dic = can_buffer(fake_dic, day, ranges, d, rest, criteria)
        if boolean :
            fake_dic = dic
            #continue
        else :
            return False
    return True

Min = 9999999999

boolean = False

# 가장 큰 과정
while not boolean :
    boolean = can_accomodate(fake_dic, date_dic, ranges, d, out_day, sums)
    if not boolean :
        fake_dic = dict(collections.Counter(date))
        ranges = b_search(ranges+1, L)
    else :
        Min = min(ranges, Min) # Min 값 저장
        fake_dic = dict(collections.Counter(date))

# 값을 하나 찾아주고 난 다음 더 적합한 값이 있는 지를 binary search를 통해 탐색

new_L = L

new_U = Min

def ceil_search(L, U) :
    mid = math.ceil((L+U)/2)
    return mid

def round_search(L, U) :
    mid = round((L+U)/2)
    return mid

ranges = round_search(new_L, new_U)
#print(ranges)
fake_dic = dict(collections.Counter(date))

possible = {}

while new_U != ranges :
    
    if can_accomodate(fake_dic, date_dic, ranges, d, out_day, sums) :
        possible[ranges] = True
        fake_dic = dict(collections.Counter(date))
        Min = min(ranges, Min) # 갱신
        ranges = round_search(new_L, ranges)
        if ranges in possible :
            if possible[ranges] == True :
                ranges = round_search(new_L, ranges)
                if ranges == new_L :
                    break
            else :
                ranges = ceil_search(ranges, new_U)
        
       
    else :
        #if ranges == new_L :
        #    break
        possible[ranges] = False
        fake_dic = dict(collections.Counter(date)) # 얘는 항상 can_accomodate를 해줄때마다 갱신을 해주어야 한다.
        ranges = ceil_search(ranges, new_U)
        if ranges in possible :
            if possible[ranges] == True :
                ranges = round_search(new_L, ranges)
                if ranges == new_L :
                    break
            else :
                ranges = ceil_search(ranges, new_U)
        


print(Min)
