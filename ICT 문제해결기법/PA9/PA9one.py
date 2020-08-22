import collections
import operator

n = 0
d = 0
m = 0
n, d, m = [int(x) for x in input().split()]

date = [int(x) for x in input().split()]

# 날짜별 환자 수 데이터 저장
date_dic = dict(collections.Counter(date))

# 시뮬레이션을 돌리기 위한 짝퉁 dictionary 설정
fake_dic = date_dic

# binary search 범위 지정 L, U 설정
U = max(date_dic.values())

L = min(date_dic.values())

# 가장 많은 환자가 신청한 날짜
max_day = max(date_dic.items(), key = operator.itemgetter(1))[0]

# 가장 적은 환자가 신청한 날짜
min_day = min(date_dic.items(), key = operator.itemgetter(1))[0]

# 이진 탐색 결과에 넘어가는 날을 반환해줌 -- time limit의 가능성 농후

p = 0
l = 0
i = 0
Mid = 0
def b_search(L, U) :
    Mid = (U+L)//2
    return Mid
    

# 수용 가능한 지 직접 확인
def can_buffer(fake_dic, date_dic, day, ranges, i, d, p) :
    #fake_dic[day+i] = ranges
    print(fake_dic)
    p = fake_dic[day+i] - ranges

    i = i + 1

    if i == d+1 :
        return False

    if day + i not in fake_dic :
        fake_dic[day+i] = 0

    fake_dic[day+i-1] = fake_dic[day+i-1] - p
    fake_dic[day+i] = fake_dic[day+i] + p
    

    if fake_dic[day+i] > ranges :
    
        return can_buffer(fake_dic, date_dic, day, ranges, i, d, p)

    return True


# buffer로 넘겨주어 수용이 가능한 지 여부 확인
def can_accomodate(fake_dic, date_dic, ranges, i, d, out_day) :
    for day in out_day :
        if can_buffer(fake_dic, date_dic, day, ranges, i, d, p) :
            continue
        else :
            return False
    return True


ranges = b_search(L, U)
print(L)
print(U)
print(ranges)
out_day = [key for key in date_dic if date_dic[key] > ranges]
print(out_day)
Min = 9999999999999999

while ranges != L :
    if can_accomodate(fake_dic, date_dic, ranges, i, d, out_day) :
        Min = min(ranges, Min)
    fake_dic = date_dic
    print("##")
    i = 0
    ranges = b_search(L, ranges-1)

print(ranges)
    

        
    



