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

#date_dic = dict(collections.Counter(date))
fake_dic = dict(collections.Counter(date))

# binary search 범위 지정 L, U 설정
U = max(fake_dic.values())

L = min(fake_dic.values())

def b_search(L, U) :
    Mid = round((U+L)/2)
    return Mid

ranges = b_search(L, U)

# 우선, 이 부분이 상당히 시간을 잡아먹을 것 같다
out_day = [key for key in fake_dic if fake_dic[key] > ranges]

#print(ranges)
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
            #print(fake_dic)
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
            #print(fake_dic)
            criteria = 0
            return can_buffer(fake_dic, day+1, ranges, d, rest, criteria)
    else :
        return True, fake_dic
        
        

boolean = True

#수용 가능 여부 확인...!
def can_accomodate(fake_dic, ranges, d, out_day, sums) :
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
    if max(fake_dic.values()) <= ranges :
        return True
    else :
        return False

Min = 9999999999

boolean = False

# 가장 큰 과정
while not boolean :
    boolean = can_accomodate(fake_dic, ranges, d, out_day, sums)
    if not boolean :
        # 이 다시 초기화해주는 과정에서 너무 time cost가 크게 작용하는 것 같다...
        fake_dic = dict(collections.Counter(date))
        ranges = b_search(ranges+1, L)
        # 이 과정은?
        out_day = [key for key in fake_dic if fake_dic[key] > ranges]
    else :
        Min = min(ranges, Min) # Min 값 저장
        fake_dic = dict(collections.Counter(date))

# 값을 하나 찾아주고 난 다음 더 적합한 값이 있는 지를 binary search를 통해 탐색

#print(Min)

new_L = L

new_U = Min

def ceil_search(L, U) :
    mid = math.ceil((L+U)/2)
    return mid

def round_search(L, U) :
    mid = math.floor((L+U)/2)
    return mid

ranges = round_search(new_L, new_U)
#print(ranges)
fake_dic = dict(collections.Counter(date))

can = []

# critical point!! : 1) range가 바뀔 때 마다 다시 fake_dic을 초기화해주어야 하는 부분과 out_day를 초기화해주어야 하는 부분...!
# critical point!! : 2) binary search의 범위를 줄여주는 과정을 어떻게 구현해 주어야 할까? --  ranges를 1씩 깎아주는 과정이 필요한가..?
# ex) ranges(new_L, Min-1)
while new_U != ranges :
    
    if can_accomodate(fake_dic, ranges, d, out_day, sums) :
        fake_dic = dict(collections.Counter(date))
        Min = min(ranges, Min) # 갱신
        if Min not in can :
            can.append(Min)
        
        #possible[ranges] = True

        ranges = round_search(new_L, Min)
        
            
        #if ranges == new_L : break -- run error 발생 이유 무엇?
        
        if ranges in can :
            ranges = round_search(new_L, Min)
        
    else :
       
        fake_dic = dict(collections.Counter(date)) # 얘는 항상 can_accomodate를 해줄때마다 갱신을 해주어야 한다. 
        #possible[ranges] = False
        ranges = ceil_search(ranges, new_U)
        
        #if ranges == new_L : break -- run error 발생 이유 무엇?
    
        if ranges in can :
            ranges = ceil_search(ranges, new_U)


print(Min)
