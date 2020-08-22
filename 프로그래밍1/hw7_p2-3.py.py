"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 word파일에 있는 단어 중 a로 시작에 z로 끝나는 단어와 그 수를  출력하는 함수입니다.
"""


f = open("./words.txt", "r")

# a로 시작해 z로 끝나는 지를 판별하는 함수
def is_atz(str) :
    if str[0] == "a" and str[-1] == "z" :
        return True
    else :
        return False

def main():
    count = 0
    for word in f : # 파일에 있는 단어를 줄 별로 읽음
        wrd=word.strip()
        if is_atz(wrd) :
            print(wrd)
            count += 1

    print("no.of count : ", count)

main()

f.close()
