"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 년도별 날짜를 8자리 수로 전환하고 1\당 환율을 1$당 환율로 전환해 이 두 요소를 tuple element로 갖는 리스트를 구성하는 함수입니다.
"""



years = range(1994, 2010) # 년도 변수 설정

# int형으로 년도를 변환하고 1$당 원화의 가치로 환산한 것을 list of tuple로 갖는 list형성하는 함수
def read_year(yr, data) :
    fname = "data/%d.txt" % yr # 년도별 파일 이름 형성
    print(fname)
    f = open(fname, "r")
    for line in f :
        date1, value1 = line.split() # 리스트 형성해서 unpacking
        value = float(value1)
        value = round(1.0/value) # 1$당 \가치로 변환
        ys, ms, ds = date1.split("/") 
        date = 10000*int(ys) + 100*int(ms) + int(ds) # 날짜를 8자리 수로 환산
        data.append((date, value))
    f.close()
    return data

def create_list_with_files() :
    data = [] 
    for yr in years : # 년도별 리스트를 만들기위한 반복문 구성
        data = read_year(yr, data)
    return data

def main() :
    data = create_list_with_files()
main()
