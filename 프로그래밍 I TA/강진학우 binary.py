def b_search(L, q, low, high):
    if low == high :
        return L[low][0] == q
    mid = (low + high)//2
    #print(L[mid][0])
    if L[mid][0] == q:
        return True
    elif L[mid][0] < q:
        return b_search(L, q, mid+1, high)
    else:
        if low == mid:
            return False
        else:
            return b_search(L, q, low, mid-1)

#merge sort에서 콜 될 함수
def merge(left, right):
    result = []
    i, j = 0,0
    while i < len(left) and j < len(right): 
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left): #오른쪽 원소가 더이상 없을 때
        result.append(left[i])
    while j < len(right): #왼쪽 원소가 더이상 없을 때
        result.append(right[j])
        j += 1
    return result

#국가코드를 비교 키로 사용해서 합치는 함수
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left,right)

file = open("average-latitude-longitude-countries.csv", "r")
file.readline()
info_list1 = []
for line in file :
    line = line.strip("\n")
    elements = line.split(",") #한 국가코드, 국가이름, 위도, 경도가 한 리스트 안에 담겨 큰 리스트에 저장
    code =  elements[0].strip("") #csv 파일에 있는 정보들의 인덱스에 따라 슬라이싱    
    code = str(code)
    elements[1] = elements[1].strip("")
    if len(elements) == 4:
        name = elements[1]
        name = str(name)
        latitude = float(elements[2])
        longitude = float(elements[3])
    else: #한 국가이름이 콤마로 나뉠 경우, 예: Korea, Republic of
        elements[2] = elements[2].strip("" + " ")
        name = elements[2] + " " + elements[1]
        name = str(name)
        latitude = float(elements[3])
        longitude = float(elements[4])
    if latitude > 0: #적도 위에 있는 국가 정보들만 출력하기 위해
        info_list1.append([code, name, latitude, longitude])
file.close()

"""
info_list = []
i = 0
for i in range(180):
    code = info_list1[i][0]
    info_list.append(code)
    i += 1
"""

info_list1 = merge_sort(info_list1)
print(info_list1[0])

lst = []
print(b_search(info_list1, "KR", 0, len(info_list1)-1))
while True:
    ip = input("Type in a country code(two letters), \n or type in 'q' to stop >>>")
    if b_search(info_list1, ip, 0, len(info_list1)-1) :
        print("code = %2s ; name = %s ; latitude = %.1f ; longitude = %.1f" %(lst[0], lst[1], lst[2], lst[3])) 
        #print("code = %2s ; name = %s ; latitude = %.1f ; longitude = %.1f" %(code, name, latitude, longitude))
        
    elif ip == "q":
        break

    else: 
        print("%s is not in the file" %ip)
        continue  
