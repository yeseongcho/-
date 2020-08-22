"""
Name : 조예성
Student ID  : 21600685
Description : 네이버 날씨에서 오늘, 내일과 그 이후 날짜의 오전, 오후 기온을 보여주는 프로그램입니다.
"""

# To use url information
import urllib.request
url = "http://weather.naver.com/rgn"+"/cityWetrCity.nhn?cityRgnCd=CT007023"
fname = "./montp.html"
dates = []
min_tp = []
max_tp = []

# Make webpages code readable string 
def process_webpage() :
    webpage = urllib.request.urlopen(url)
    out = open(fname, "w")
    for line in webpage :
        line = str(line) # Convert string data
        out.write(line.strip() + "\n") # write new file
    webpage.close()
    out.close()

def print_weather() :
    f = open('montp.html', "r")
    min_flag = True # Indicator which says it is morning or afternoon
    for line in f :
        if '<th scope="col"' in line : # To take today and tomorrow date
            wdate = extract_date(line)
            dates.append(wdate)
        elif '<th scope="row"' in line : # To take the day after tomorrow and after date
            wdate = extract_date(line)
            dates.append(wdate)
        elif '<li class="nm">' in line : # To take temperature information
            temp = extract_temperature(line)
            if min_flag == True : # If it is moring
                min_tp.append(temp)
                min_flag = False # To take afternoon temperature
            else : # If it is afternoon
                max_tp.append(temp)
                min_flag = True # To take next day's morning temperature
    for i in range(len(dates)) :
        print("%s : \t%5s ~ %5s" % (dates[i], min_tp[i], max_tp[i]))

    f.close()

# To take date
def extract_date(line) :
    if "<span>(" in line : # If data in the day after tomorrow and after date
        tdate = line[line.find("(") + 1 : line.find(")")] # Find date information
    else : # if data in today and tomorrow
        skip_len = len("<span>") 
        start_idx = line.find("<span>") + skip_len
        tdate = line[start_idx : line.find("<", start_idx)] # Find date information
        tdate = tdate.strip(".")
        tdate = tdate.replace(".", "/")
    return tdate

def extract_temperature(line) : # To take temperature information
    skip_len = len('<span class="temp">')
    start_idx = line.find('<span class="temp">') + skip_len
    end_idx = line.find("<", start_idx)
    temp = line[start_idx : end_idx] # Find temperature information
    return temp

def main() :
    process_webpage()
    print_weather()

main()
    
