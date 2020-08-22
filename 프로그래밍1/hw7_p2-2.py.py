"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 각 알파벳이 대칭을 이루는 단어와 그 수를 출력하는 함수입니다.
"""




f = open("./words.txt", "r")


# 단어가 대칭인지 판별하는 함수
def is_symmetry(str) :
    count = 0
    for i in range(len(str)) :
        if str[i] == str[-(i+1)] :
            count += 1
            if count == len(str) :
                
                return True
        else :
            return False


def main() :
    c = 0
    for word in f :
        wrd = word.strip()
        if is_symmetry(wrd) : # 대칭이면 카운트하고 출력
            print(wrd)
            c += 1
        
    print("no.of words : ", c)


main()
f.close() 
        
