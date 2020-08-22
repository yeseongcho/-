"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 words메모장 파일에 있는 단어들 중, palindromes인 단어들의 길이, 그 갯수와 그 단어 리스트를 나란히 정렬된 채로 출력해주는 프로그램입니다.
"""

# palinndrome인 경우 True값을 리턴해주는 함수, 재귀적으로 추적
def palin(word) :
    if len(word) <= 1 :
        return True
    else :
        return (word[0] == word[-1]) and palin(word[1:-1])


# words메모장 파일에 있는 단어들 중 palindrome인 녀석들의 길이와 그 단어를 tuple element로 갖는 리스트를 만드는 함수
def create_list() :
    f = open("words.txt", "r")
    words = []
    for word in f :
        word = word.strip().lower()
        if palin(word) :
            words.append((len(word), word))
    
    f.close()
    return words

# 한 줄당 단어들과 공백들이 차지하는 공간이 일정 수치를 넘기는 지를 판별하는 함수
def new_line(length, m, n) :
    
    if length*m + n >= 35 :
        return True
    

# 단어들의 길이, 빈도 수, 단어들을 출력하는 함수
def display(lst, length) :
    a = str(length)
    b = str(len(lst))
    print(" "*3 + a + " "*7 + b+ "\t"+" "*2, end=" ") # 빈도수와 길이 출력
    m = 0 # 단어로 구성된 리스트 안에 있는 단어의 수
    n = 0 # 단어로 구성된 리스트 안에 있는 공백의 수
    for i in lst :
        if not new_line(length, m, n) : # 아직 일정 공간을 넘기지 않는 경우 
            print(i, end = " ")
            m += 1 # 단어 하나 추가
            n += 1 # 해당 여백 추가
            if new_line(length, m, n) : # 일정 공간을 넘기는 경우
                if i == lst[-1] : # 만약, 일정 공간을 넘었으나 더 이상 다음 라인에 출력해줄 리스트의 값이 없을 경우, 반복문 탈출
                    break
                else : # 일정 공간을 넘었으나 출력해줄 것이 있는 경우
                    print(" ") # 줄 바꿈
                    print(" "*18, end = " ") # palindrome열에 해당하게 위치시키기 위함.
                    m = 0 # 열이 바뀜으로 이 둘도 초기화
                    n = 0
                
        
        
    print(" ") # length값이 변할 때 열을 바꾸어주기 위해

# 리스트 안에 있는 palindrome을 그 길이, 빈도수, 그 단어들을 나란히 출력해주는 함수
def print_summary(palind) :
    length = 0
    print("Length  Frequency  Palindroms")
    
    flag = True
    for lw, word in palind : 
        if length != lw : 
            if flag == True :
                flag = False
            else : # length값이 변하게 되면, 그 때 변하기 전까지 length에 해당하는 단어들의 빈도 수와 단어들 출력.
                display(lst, length)
            lst = [word]
            length = lw
        else :
            lst.append(word)
    display(lst, length) # length가 마지막으로 한번 더 변하고 나서 그 마지막 것까지 보여주기 위해
    




def main() :
    pal_list = create_list()
    pal_list.sort(reverse = True)
    print_summary(pal_list)
    
    
main()
