"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 처음에 만들어놓은 list를 가장 메달이 많은 나라 순으로 다시 분류하기 위한 프로그램입니다.
"""





# (나라이름, 금, 은, 동)으로 구성된 list구성
def create_list() :
    countries = ["Canada", "Germany", "United States", "Norway", "Korea", "Swiss", "Sweden", "China", "Austria", "Netherland"]
    golds = [14, 10, 9, 9, 6, 6, 5, 5, 4, 4]
    silvers = [7, 13, 15, 8, 6, 0, 2, 2, 6, 1]
    bronzes = [5, 7, 13, 6, 2, 3, 4, 4, 6, 3]
    medals = []
    for i in range(10) :
        medals.append((countries[i], golds[i], silvers[i], bronzes[i]))
    
    
    return medals

# sort함수의 key값으로 금, 은, 동의 합을 취해주는 함수
def key_building(item) :
    return sum(item[1:]) 

 # 위에서 구한 합을 가지고 sort를 해주는 함수 구성
def sorting_medals(medals) : 
    medals.sort(key=key_building, reverse=True) 
    return medals

# 나라의 이름, 총 메달갯수, (금, 은, 동 메달 수)를 순차적으로 열을 맞추어 보여주는 함수를 만든다.
def print_medals(medals) :
    for i in range(10) : 
        a = medals[i][1] + medals[i][2] + medals[i][3] 
        if i == 0 : # 미국의 경우 문장 길이가 길어 tab를해도 열이 일치하지않기때문에 따로 구함. 나라 이름과 메달 수 간의 간격을 더 좁게 해줌
            print(str(medals[i][0])+" "+ "\t" +  str(a) + str((medals[i][1], medals[i][2], medals[i][3])))
        else :
            print(str(medals[i][0])+"     "+ "\t" +  str(a) + str((medals[i][1], medals[i][2], medals[i][3]))) 





# main함수 실행
def main() :
    medals = create_list() 
    mdals = sorting_medals(medals) # 여기서 우리가 mdals = medals.sort() 이런식으로 바로 할 수 있을까? nono. sort한 거는! return값이 없다 따로... pop도 return값이 따로 없다!
    print_medals(mdals)
    

main()
