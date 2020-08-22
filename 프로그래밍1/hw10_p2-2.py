"""
Name : 조예성
Student ID : 21600685
Description : tpmon 텍스트 파일로부터 정보를 읽어들여 csv파일을 만드는 프로그램입니다.
"""

# Read file in text
def read_file() :
    f = open("tpmon.txt", "r")
    f.readline()
    temperature = []
    for line in f :
        line = line.strip("\n")
        line = line.strip(" ")
        lists = line.split(" "*2) # split by double blank
        
        temperature.append(lists)
    f.close()
    return temperature
# To make a csv file
def create_file(temperature) :
    print(temperature[0])
    f = open("tpmon.csv", "w")
    year = 1723
    for i in temperature :

        f.write(str(year)+',') # To write year

        for j in range(12) :
            
            f.write(i[j]+',') # To write monthly temperature ','
        f.write('\n') # To make another line
        year += 1
    f.close()

def main() :
    temperature = read_file()
    create_file(temperature)

main()
