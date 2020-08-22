# main - 이름을 bubble sort
def main():
    N = ['Chris Terman','Daseong Han', 'Tom Grimson','Eric Herman', 'Joseph Shin','John Brady']
    bubble_sort(N,cmp_names)
    print(N)
    
# bubble sort 방식으로 first name 기준 정렬하는 함수 
def bubble_sort(L,func): 
    end = len(L)
    for i in range(end-1):
        for j in range(end-1-i):
            i1 = (end-1) -(j+1)
            i2 = (end -1) -j
            # cmp_names 함수 호출 -- 정렬 기준 제공
            if func(L[i1],L[i2]):
                L[i1],L[i2] = L[i2],L[i1]
    return L


# first name 정렬 기준 제공 함수
def cmp_names(n1,n2): 
    n1 = n1.split(' ')
    n2 = n2.split(' ')
    # first name 동일 시 second name 기준  
    if n1[1].lower() == n2[1].lower():
        return n1[0].lower()> n2[0].lower()
    else:
        return n1[1].lower()> n2[1].lower()
    

main() 
