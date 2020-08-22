"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 세 개의 같은 알파벳이 연속으로 나오는 단어와 그 수를 출력하는 프로그램입니다.
"""


f = open("./words.txt", "r")

# 3개의 연달아 같은 알파벳이 나오는 지 판별하는 함수
def is_triple(wrd) :
    for i in range(len(wrd)-2) :
        if wrd[i] == wrd[i+1] and wrd[i+1] == wrd[i+2] and wrd[i] == wrd[i+2] :
            return True

    return False

def main() :
    count = 0
    for word in f : # 줄 별로 파일의 단어들을 읽음
        wrd = word.strip()
        if is_triple(wrd) :
            print(wrd)
            count += 1
            

    print("These word's number is : ", count)

main()
f.close()



