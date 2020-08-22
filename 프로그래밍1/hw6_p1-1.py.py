"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 나라별 메달의 총 수 와 각 금,은,동 별 메달의 수를 보기 좋게 정렬하기 위한 프로그램입니다
"""






# (나라의 이름, 금, 은, 동 )순으로 기록된 list를 만들어준다.
def create_list() :
    countries = ["Canada", "Germany", "United States", "Norway", "Korea", "Swiss", "Sweden", "China", "Austria", "Netherland"]
    golds = [14, 10, 9, 9, 6, 6, 5, 5, 4, 4]
    silvers = [7, 13, 15, 8, 6, 0, 2, 2, 6, 1]
    bronzes = [5, 7, 13, 6, 2, 3, 4, 4, 6, 3]
    medals = []
    for i in range(10) :
        medals.append((countries[i], golds[i], silvers[i], bronzes[i]))
    
    
    return medals


# 나라의 이름, 총 메달갯수, (금, 은, 동 메달 수)를 순차적으로 열을 맞추어 보여주는 함수를 만든다.
def print_medals(medals) :
    for i in range(10) : 
        a = medals[i][1] + medals[i][2] + medals[i][3] 
        if i == 2 : # 미국의 경우 문장 길이가 길어 tab를해도 열이 일치하지않기때문에 따로 구함. 나라 이름과 메달 수 간의 간격을 더 좁게 해줌
            print(str(medals[i][0])+" "+ "\t" +  str(a) + str((medals[i][1], medals[i][2], medals[i][3]))) 
        else :
            print(str(medals[i][0])+"     "+ "\t" +  str(a) + str((medals[i][1], medals[i][2], medals[i][3]))) 

    

# main함수 정의
def main() :
    
    medals = create_list()
    
    print_medals(medals)
    

main()







