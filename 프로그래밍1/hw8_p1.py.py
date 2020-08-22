"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 이름으로 구성된 주어진 list를 버블 sort의 방법으로 sorting을 해 결과를 출력해주는 프로그램입니다.
"""


# bubble sort를 하는 중, 두 개의 대소(사전순)를 비교해주는 함수, 기쥰ㄴ은 last name의 알파벳 순. 
def cmp_names(x1, x2) :
    x1 = x1.strip()
    x1 = x1.lower()
    x2 = x2.strip()
    x2 = x2.lower()
    x1 = x1.split()
    x2 = x2.split()

    if x1[1] > x2[1] :
        return True
    elif x1[1] < x2[1] :
        return False
    else : 
        if x1[0] > x2[0] :
            return True
        elif x1[0] < x2[0] :
            return False
        else :
            return False

# 버블 소트 시키는 함수
def bubble_sort(L, func) :
    end = len(L)
    for i in range(end-1) :
        for j in range(end-1-i) :
            i1 = (end-1) - (j+1)
            i2 = (end-1) - j
            if func(L[i1], L[i2]) : 
                L[i1], L[i2] = L[i2], L[i1]
    return L


def main() :
    N = ["Daseong Han", "Chris Terman", "Tom Grimson", "Eric Herman", "Joseph Shin", "John Brady"]
    M = bubble_sort(N, cmp_names)
    print(M) # 버블 소트 결과 출력

main()
