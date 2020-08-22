"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 입력받은 년도의 환율의 평균, 최대, 최소값을 전체 데이터를 다 탐색해서 구하는 것이 아닌 해당 년도의 데이터만 효율적으로 분석해서 결과를 내는 프로그램입니다.
"""


years = range(1994, 2010) # 년도 변수 설정

# int형으로 년도를 변환하고 1$당 원화의 가치로 환산한 것을 list of tuple로 갖는 list형성하는 함수
def read_year(yr,data) :
    fname = "data/%d.txt" % yr # 년도별 파일 이름 형성
    print(fname)
    f = open(fname, "r")
    for line in f :
        date1, value1 = line.split() # 리스트 형성해서 unpacking
        value = float(value1)
        value = int(1.0/value) # 1$당 \가치로 변환
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

# 평균과 최대, 최소를 구할 때 리스트를 전부 다 search하는 것이 아니라, 해당 index만 탐색하기 위해 index list 설정
def create_ind_tb(data) :
    yr = 1994
    inx_tb = [0]*16
    for i in range(len(data)) :
        date, rate = data[i]
        year = date//10000
        if year != yr :
            inx_tb[year - 1994] = i
            yr = year
    return inx_tb


def average(data, yr, inx_tb) :
    sum = 0
    count = 0
    start = yr*10000
    end = (yr+1)*10000 
    if yr < 2009 : # index의 list에는 2009년 1월 1일 것 까지의 index만이 list에 들어있으므로 2009년것은 별도로 계산
        for m in range(inx_tb[yr-1994], inx_tb[(yr+1)-1994]) : # 주어진 year의 1월1일부터 12월 31일것 까지만 비교하는 반복문 구성, 전체를 다 search하지 않는다.
            if start < data[m][0] < end :
                sum += data[m][1]
                count += 1
    else : # 2009년의 경우, 2009년 1월1일의 index값이 5479이고 그 마지막 index의 값까지가 2009년의 데이터이므로 그 경우를 계산.
        for m in range(inx_tb[yr-1994], len(data)) :
            if start < data[m][0] < end :
                sum += data[m][1]
                count += 1
    
    return round(sum/count)
# 주어진 년도만 비교하여 해당 년도 최소값을 산출하는 함수
def find_min(data, yr, inx_tb) :
    vm = 99999
    dm = None
    if yr<2009 : # 이 경우도 2009년은 별도 취급
        for m in range(inx_tb[yr-1994], inx_tb[(yr+1)-1994]) :
            if data[m][1] < vm :
                vm = data[m][1]
    else :
        for m in range(inx_tb[yr-1994], len(data)) :
            if data[m][1] < vm :
                vm = data[m][1]
    return vm
# 주어진 년도만 비교하여 해당 년도 최대값을 산출하는 함수
def find_max(data, yr, inx_tb):
    vm = 0
    dm = None
    if yr<2009 :
        for m in range(inx_tb[yr-1994], inx_tb[(yr+1)-1994]) :
            if data[m][1] > vm :
                vm = data[m][1]
    else :
        for m in range(inx_tb[yr-1994], len(data)) :
            if data[m][1] > vm :
                vm = data[m][1]
    return vm


# 'More yearly data(y/n)?' 질문에서 대답에 따라 다른 결과값을 양성하는 함수
def check_answer(answer) :
    if answer == 'n' : # 함수 종료
        return True
    elif answer != 'n' and answer != 'y' : # y와 n이 아닌 다른 값들을 입력할 때, 제대로 된 값을 입력할 때 까지 계속 검정하는 recursive 함수 구성
        print("Write right answer down")
        ans = input("More yearly data(y/n)?")
        if check_answer(ans) :
            return True
    else : # y값을 입력할 경우 계속 프로그램 실행
        return False



def main() :
    data = create_list_with_files()
    inx_tb = create_ind_tb(data)
    while True :
        try :
            annual = input("What year?: ")
            annuals = int(annual)
            if 1994 <= annuals <= 2009 : # 제대로 된 년도를 입력할 경우
                minimum = int(find_min(data, annuals, inx_tb))
                maximum = int(find_max(data, annuals, inx_tb))
                avg = int(average(data, annuals, inx_tb))
                if annuals == 2009 : # 2009년의 경우 별도로, No of items.를 구하기 위한 inx_tb값에서 2010데이터가 없기에
                    print("Year:", annuals, "Min =", minimum, "Max =", maximum, "Average =", avg, "No of items. =", len(data)-inx_tb[annuals-1994])
                else :
                    print("Year:", annuals, "Min =", minimum, "Max =", maximum, "Average =", avg, "No of items. =", inx_tb[(annuals+1)-1994]-inx_tb[annuals-1994])
                answer = input("More yearly data?(y/n)") 
                if check_answer(answer) : # 올바른 값을 입력했는지 판별
                    break
            
            else :
                print(str(annuals)+"?" +"Type in a year between 1994 and 2009") # 1994~2009 밖을 벗어나는 수를 입력했을 경우
        except :
            print(str(annual)+"?"+"Enter again") # 애초에 수를 아닌 엉뚱한 값을 입력했을 경우                
    
    
main()
