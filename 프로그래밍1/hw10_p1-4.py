"""
Name : 조예성
Student ID : 21600685
Description : 과제 1-2, 1-3를 dictionary를 이용해 간단히 만든 프로그램.
            : 적도 위에 있는 나라의 코드네임, 나라의 이름, 위도와 경도를 알파벳 순으로 정렬한 채로 보여주고 사용자로부터 나라의 코드를 입력받으면 해당 나라의 코드네임, 이름, 위도와 경도를 차례로 표시해주는 프로그램입니다.

"""

# Read file and make a list of country's information
def read_file() :
    f = open("average-latitude-longitude-countries.csv", "r")
    f.readline()
    glob = {}
    for line in f :
        line = line.strip('\n')
        elements = line.split(",")
        code = elements[0].strip('"')
        elements[1] = elements[1].strip('"')
        if len(elements) == 4 : # When country name is only one word
            name = elements[1]
            latitude = float(elements[2])
            longitude = float(elements[3])
            code_info = (name, latitude, longitude)
            glob[code] = code_info
        else :  # When country name consists of two part, include ','
            elements[2] = elements[2].strip('"' + " ")
            name = elements[2] + " " + elements[1]
            latitude = float(elements[3])
            longitude = float(elements[4])
            code_info = (name, latitude, longitude) # Make a dictionary of country's information
            glob[code] = code_info
    f.close()
    return glob

# Finally show     
def show_list(glob) :
    for i in glob :
        a = str(glob[i][0])
        b = glob[i][1]
        c = str(glob[i][2])
        x = is_nextline(i, a)
    
        
        if b > 0 :  # Show only north side ( over the equator )
            b = str(glob[i][1])
            print(i+' '+a+' '*x+b+'\t'+c)
            

def is_nextline(x, y) :
    i = len(x)
    j = len(y)
    x = 0
    while True :
        if i + j + x < 100 : # To make same space whether the word is long or not
            x += 1
        else :
            return x
   

def main() :
    glob = read_file()
    show_list(glob)
    while True:
        try :
            check = input("Type in a country code(two letters) or type in 'q' to stop : ")
            check = str(check)
            check = check.strip('\n')
            if check == 'q' :
                break
            else :
                if len(check) != 2 : # when user input more than 2 length words
                    print('%s is not in the file' % check)
                else :
                    if check in glob :
                        name, latitude, longitude = glob[check][0], glob[check][1], glob[check][2]
                        print('code'+' '+ '='+' '+str(check)+' '+';'+' '+'name'+' '+'='+' '+str(name)+' '+';'+' '+'latitude'+' '+'='+' '+str(latitude)+' '+';'+' '+'longitude'+' '+'='+' '+str(longitude))
                    else :
                        print('%s is not in the file' % check)
        except : # when user input non_string data
            print('%s is not in the file' % check)

main()
                        
    


