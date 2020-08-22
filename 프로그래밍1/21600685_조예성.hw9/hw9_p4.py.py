"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 해당 년도 월별 환율의 정도를 그래프로 나타내는 함수입니다.
"""



import cs1media

# 그래프를 가시성이 좋게 그리기 위해 단위 조정. ( 1개월당 5pixel, 1원당 0.5pixel )
x_step = 5
y_step = 0.5
# 그래프 안에 환율이 다 나오기 위해 최대 최소 설정. 모든 환율은 이 범위 안에 다 들어간다.
min_y = 700 
max_y = 2000

years = range(1994, 2010) # 년도 변수 설정

# int형으로 년도를 변환하고 1$당 원화의 가치로 환산한 것을 list of tuple로 갖는 list형성하는 함수
def read_year(yr) :
    fname = "data/%d.txt" % yr # 년도별 파일 이름 형성
    f = open(fname, "r")
    data = []
    for line in f :
        date1, value1 = line.split() # 리스트 형성해서 unpacking
        value = float(value1)
        value = int(1.0/value) # 1$당 \가치로 변환
        ys, ms, ds = date1.split("/")
        date = 10000*int(ys) + 100*int(ms) + int(ds) # 날짜를 8자리 수로 환산
        data.append((date, value))
    f.close()
    return data


# 주어진 년도의 월별 환율의 최대, 최소값을 구하는 함수
def find_minmax(yr) :
    minmax = [(9999,0)]*12 # 최대, 최소를 구하기 위한 초기 임의의 값 설정
    data = read_year(yr) 
    for d, v in data :
        month = (d//100)%100-1 
        minr, maxr = minmax[month] # minmax unpacking
        if v < minr :
            minr = v
        if v > maxr :
            maxr = v
        minmax[month] = minr, maxr
    return minmax

def main() :
    w = len(years)*12*x_step # 16개의 년도의 12개월을 1개월당 5달씩 차지하는 단위로 width설정
    h = int((max_y - min_y)*y_step) #  총 1300의 단위를 0.5로 나누어 1원당 0.5를 차지하는 단위로 hieght설정
    p = cs1media.create_picture(w, h, cs1media.Color.white)

    # 수직선 그리드 라인 그리기
    for yr in years :
        x = (yr-years[0])*12*x_step
        for y in range(h) :
            p.set(x, y, cs1media.Color.gray)

    # 수평선 그리드 라인 그리기
    for won in range(min_y, max_y, 100) :
        y = int((won-min_y)*y_step)
        for x in range(w) :
            p.set(x, y, cs1media.Color.gray)
    
    # 월별 최대 최소 표시하는 반복문
    for yr in years :
        minmax = find_minmax(yr) # 월별 최대 최소 데이터 가져옴
        for m in range(12) :
            x = ((yr-years[0])*12+m) * x_step # 월별로 x축 지정
            y1 = int((minmax[m][0] - min_y)*y_step) # y1에 최소값 지정
            y2 = int((minmax[m][1] - min_y)*y_step) # y2에 최대값 지정
            for y in range(h-y2, h-y1+1) : # y축기준, 위에서 아래로 갈수록 값이커지는 게 아닌, 통상적으로 아래에서 위로갈수록 값이 커지게끔 범위 조정

                # 달 별로 값의 차가 크므로 바로 옆에 같은 거 하나 더 표시해 굵기를 굵게해줌
                p.set(x, y, cs1media.Color.red)
                p.set(x+1, y, cs1media.Color.red)
    p.show()
    p.save_as("krw.png")

main()
