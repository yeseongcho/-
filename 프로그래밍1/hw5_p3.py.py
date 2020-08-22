"""
Name : 조예성
Student Id : 21600685
Description : 이 함수는 3개의 변을 입력받아 삼각형을 이룰 수 있는지 판별하는 프로그램입니다.
"""


def take_length(side) : # 길이를 입력받는 함수 
    while True :
        try :
            msg = "Enter the length side %1d : " % side # side1, side2, side3에 대한 언급 (19, 20, 21번째줄에 side를 1, 2, 3입력 받음 ) 
            num = input(msg) # 각각 side1, 2, 3에 대해 입력값 받음
            cord = float(num) # 올바르게 입력했는지 판별해 올바른 숫자면 cord값 리턴하고 그렇지 않으면 except로 넘어감
            return cord
        except :
            print(num + "?" + "Please enter a number.") # 숫자를 재입력하라는 문구를 띄우고 while문 반복
# 내 과제 4의 감점 요인 - 나는 main함수에서 쟤를 tuple로 받기 위해, while반복문에서 3 변수를 취했는데, 얘는 함수를 따로 만들어서 시행했네.. 이러면 문자를 입력하고 다시 숫자를 입력해도 이어서 프로그램이 진행될 수 있잖아..
def take_numbers() :
    x = take_length(1) 
    y = take_length(2) 
    z = take_length(3) 
    return x, y, z # 각각 입력받은 x, y, z값을 tuple로 리턴함

def check_inequalities(x1, x2, x3) : # 삼각형을 이루는 지 판별하는 함수
    if x1+x2 > x3 and x2+x3>x1 and x3+x1>x2 :
        return True
    else :
        return False

def main() :
    while(True) : # 사용자가 원할 때까지 계속해서 프로그램을 실시하기 위해 무한 반복문 구성
        a, b, c = take_numbers() # tuple값 unpacking
        if check_inequalities(a, b, c) :
            print(a, b, c, "a valid triangle") 
        else :
            print(a ,b, c, "invalid triangle")
        if input("Go for a more check? Type 'yes'if you do. ") != "yes" : # 프로그램을 계속 시행할 것인지 묻는 문구, yes가 아니면 while문을 빠져나온다.
            break

main() # main함수 실행
