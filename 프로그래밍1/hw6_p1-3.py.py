"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 나라 별 메달의 갯수를 3단위의 범위(0~2개, 3~5개 식으로)로 지정해 각 범위에 해당하는 나라 수만큼 "*"표시로 표시해주는 프로그램입니다.
"""

def create_list() : # p1-1, p1-2에서 사용한 list를 그대로 사용해준다.
    countries = ["Canada", "Germany", "United States", "Norway", "Korea", "Swiss", "Sweden", "China", "Austria", "Netherland"]
    golds = [14, 10, 9, 9, 6, 6, 5, 5, 4, 4]
    silvers = [7, 13, 15, 8, 6, 0, 2, 2, 6, 1]
    bronzes = [5, 7, 13, 6, 2, 3, 4, 4, 6, 3]
    medals = []
    for i in range(10) :
        medals.append((countries[i], golds[i], silvers[i], bronzes[i]))
    
    
    return medals

# 각 나라별 메달의 합을 보여주는 리스트를 만드는 함수
def sums_medals(medals) :
    su = [] 
    for item in medals : 
        
        su.append(sum(item[1:])) 

    return su 

# 최종적으로 만들어진 것을 보여주기 위한 함수
def show_list(t) :
    for i in range(13) : # 메달의 갯수의 max가 37이므로 0~2, 3~5... 36~38까지 총 13개의 범위
        print(str(3*i) + "~" + str(3*i+2) + "\t" + "*"*t[i]) 
        
def main() :
    medals = create_list()
    sumlist = sums_medals(medals) 
    t = [0]*13 # [0, 0, ..., 0 ] # '*'를 몇개 찍어낼 것인지 나타내는 리스트 ( 즉, 나라의 수 )
    for i in range(10) :
        
        t[sumlist[i]//3] += 1 # 해당 범위에 속한 나라의 수를 하나씩 증가

    show_list(t) 


main()
