"""
Name: 조예성
Student ID : 21600685
Description : 이 함수는 년도별 환율의 평균값, 최대, 최소값을 산출해주는 프로그램입니다.
"""



years = range(1994, 2010) # 년도 변수 설정

# int형으로 년도를 변환하고 1$당 원화의 가치로 환산한 것을 list of tuple로 갖는 list형성하는 함수
def read_year(yr, data) :
    fname = "data/%d.txt" % yr # 년도별 파일 이름 형성
    f = open(fname, "r")
    for line in f :
        date1, value1 = line.split()  # 리스트 형성해서 unpacking
        value = float(value1)
        value = int(1.0/value) # 1$당 \가치로 변환
        ys, ms, ds = date1.split("/")
        date = 10000*int(ys) + 100*int(ms) + int(ds)  # 날짜를 8자리 수로 환산
        data.append((date, value))
    f.close()
    return data

def create_list_with_files() :
    data = []
    for yr in years : # 년도별 리스트를 만들기위한 반복문 구성
        data = read_year(yr, data)
    return data

# 년도별 환율의 평균값을 구하는 함수
def average(data, yr) :
    sum = 0
    count = 0
    start = yr*10000
    end = (yr+1)*10000 
    for d, v in data:
        if start < d < end :
            sum += v # 환율의 데이터 합
            count += 1 
    return round(sum/count)

def find_min(data) :
    vm = 99999 # 큰 임의의 값 설정
    dm = None
    for d, v in data :
        if v < vm :
            dm = d
    return dm, vm

def find_max(data) :
    vm = 0
    dm = None
    for d, v in data :
        if v > vm : 
            vm = v 
            dm = d 
    return dm, vm

def main() :
    data = create_list_with_files()
    print("Maximum : ", find_max(data))
    print("Minimum : ", find_min(data))
    for yr in years : 
        avg = average(data, yr) # 년도별 평균 산출
        print("%-6d %4d" % (yr, int(avg+0.5)))

main()
