"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 숫자 3개를 입력받아 삼각형을 만들 수 있는 지를 판별하는 프로그램입니다
"""


def take_a_number() : # 숫자를 받는 함수 구성
    while True: # 제대로 된 숫자를 입력할 때 까지 계속 입력받는 반복문 구성
        try:
            in_num = input("Enter a number : ")
            value = float(in_num) 
            
            return value
        except :
            print(in_num + "? Please enter a number.") # 제대로 숫자 값을 입력 못했을 경우 산출하는 문장


# x, y, z = tuple로 취하기 위한 구성!!! - 이런 아이디어가 필요하다. 함수를 새로 만드는 연습!
def take_numbers() :
    x = take_a_number()
    y = take_a_number()
    z = take_a_number()
    return x, y, z
    


def check_inequalities(a, b, c) : # 삼각형을 만들 수 있는 지 여부를 판단하는 함수
    if a+b>c and b+c>a and a+c>b :
        return True
    else :
        return False


while True : # 사용자가 원할 때까지 입력받게 하기위한 반복문 구성
    # 숫자 3개를 입력받음
    x, y, z = take_numbers() #unpacking
    if check_inequalities(x, y, z) :
        print(x, y, z, "a valid triangle") # 삼각형을 만들 수 있을 때
    else :
        print(x, y, z, "a invalid triangle") # 삼각형을 만들 수 없을 때
    if input("Go for a more check?") != "yes" : # 사용자가 더 프로그램을 이용하길 원하는지 묻는 문장
        break #사용자가 원치 않을 때 반복문 탈출


