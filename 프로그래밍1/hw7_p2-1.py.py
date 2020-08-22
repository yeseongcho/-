"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 words파일에 있는 단어 중 길이가 18을 넘는 단어를 출력하고 그 갯수를 보여주는 함수입니다.
"""
# 파일을 읽어옴
f = open("./words.txt", "r")
count = 0
# 파일에 있는 단어를 라인별로 읽음
for word in f :
    wrd = word.strip()
    if len(wrd) > 18 :
        count += 1
        print(wrd)
print("no. of words = ", count)
f.close() # 실행 완료하고 파일 닫음
