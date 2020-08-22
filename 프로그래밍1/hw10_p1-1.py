"""
Name : 조예성
Student ID : 21600685
Description : 나라의 코드네임, 나라의 이름, 위도와 경도를 알파벳 순으로 정렬한 채로 보여주는 프로그램입니다.(큰 화면으로 보시는 것이 더 정확합니다)
"""



# Read file and make a list of country's information
def read_file() :
    f = open("average-latitude-longitude-countries.csv", "r")
    f.readline()
    glob = []
    for line in f :
        line = line.strip('\n')
        elements = line.split(",")
        code = elements[0].strip('"')
        elements[1] = elements[1].strip('"')
        if len(elements) == 4 : # When country name is only one word
            name = elements[1]
            latitude = float(elements[2])
            longitude = float(elements[3])
            glob.append((code, name, latitude, longitude))
        else : # When country name consists of two part, include ','
            elements[2] = elements[2].strip('"' + " ")
            name = elements[2] + " " + elements[1]
            latitude = float(elements[3])
            longitude = float(elements[4])
            glob.append((code, name, latitude, longitude)) # Make a list of country's information
    f.close()
    return glob

# Sotring list by merging
def merge_sort(G) : # To divide by two part
    if len(G) < 2 :
        return G[:]
    mid = len(G)//2
    left = merge_sort(G[:mid])
    right = merge_sort(G[mid:])
    return merge(left, right)

# To merge two list by sorting alphabetical order
def merge(L, R) :
    result = []
    i, j = 0, 0
    while i <len(L) and j < len(R) :
        if L[i][0] < R[j][0] :
            result.append(L[i])
            i += 1
        else :
            result.append(R[i])
            j += 1
    while i < len(L) :
        result.append(L[i])
        i += 1
    while j < len(R) :
        result.append(R[j])
        j += 1
    return result

# Finally show 
def show_list(glb) :
    for i in glb :
        a = str(i[0])
        b = str(i[1])
        c = str(i[2])
        d = str(i[3])
        x = is_nextline(a, b) # To arrange line
        print(a+' '+b+' '*x+c+'\t'+d)
            
        
def is_nextline(x, y) :
    i = len(x)
    j = len(y)
    x = 0
    while True :
        if i + j + x < 100 : # To make same space whether the word is long or not.
            x += 1
        else :
            return x



def main() :
    glob = read_file()
    glb = merge_sort(glob)
    show_list(glb)
    
main()
            
            
            
