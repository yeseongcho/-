"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 주어진 해의 월별 환율의 최대, 최소를 산출하는 함수입니다.
"""


years = range(1994, 2010) # 년도 변수 설정

# int형으로 년도를 변환하고 1$당 원화의 가치로 환산한 것을 list of tuple로 갖는 list형성하는 함수
def read_year(yr) :
    fname = "data/%d.txt" % yr  # 년도별 파일 이름 형성
    f = open(fname, "r")
    data = []
    for line in f :
        date1, value1 = line.split()  
        value = float(value1)
        value = int(1.0/value) # 1$당 \가치로 변환
        ys, ms, ds = date1.split("/")
        date = 10000*int(ys) + 100*int(ms) + int(ds) # 날짜를 8자리 수로 환산
        data.append((date, value))
    f.close()
    return data
# 주어진 년도의 월별 환율의 최대, 최소값을 구하는 함수
def find_minmax(yr) :
    minmax = [(9999, 0)]*12 # 최대, 최소를 구하기 위한 초기 임의의 값 설정
    data = read_year(yr) 
    for d, v in data :
        month = (d//100)%100-1 # 월별 minmax의 element를 구성하기 위한 식, 1월의 경우 이 값이 0이 되어, minmax[0]이 1월의 최대 최소 정보를 갖게 됨.
        minr, maxr = minmax[month] # minmax unpacking
        if v < minr : 
            minr = v 
        if v > maxr : 
            maxr = v 
        minmax[month] = minr, maxr
    return minmax

def main() :
    for yr in years : 
        print("%4d:" % yr, end=" " )
        minmax = find_minmax(yr) # 주어진 해의 월별 최대 최소 구하기
        for m in range(12) :
            print("%4d/%-4d" % minmax[m], end=" ") 
        print(" ") # 한 줄씩 더 공백이 생기는 것을 막기 위해

main()
