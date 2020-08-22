"""
Name : 조예성
Student ID : 21600685
Description : tpmon 이라는 텍스트파일로부터 년도와 여름, 겨울 평균 기온을 구하여 정렬한 채로 산출해주는 프로그램입니다.
"""


# Read file in text
def read_file() :
    f = open("tpmon.txt", "r")
    f.readline()
    temperature = []
    for line in f :
        line = line.strip("\n")
        line = line.strip(" ")
        element = line.split(" "*2) # split by double blank
        winter = (float(element[0])+float(element[1]))/2 # Calculate by averaging of January and February
        summer = (float(element[6])+float(element[7]))/2 # Calculate by averaging of July and August
        temperature.append((winter, summer))

    f.close()
    return temperature

def show_temper(temperature) :
    year = 1723
    for i in temperature :
        print("%d : %10.2f/%.2f" % (year, i[0], i[1])) # Show information by format string
        year += 1
def main() :
    temperature = read_file()
    show_temper(temperature)

main()
        
    
    
