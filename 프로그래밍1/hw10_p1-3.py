"""
Name : 조예성
Student ID : 21600685
Description : 사용자로부터 나라의 코드를 입력받으면 해당 나라의 코드네임, 이름, 위도와 경도를 차례로 표시해주는 프로그램입니다.
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
# Sorting list by merging
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

# To find information about what user input 
def binary_search(G,x,low,high) :
    if low == high : # base case
        return G[low][0] == x
    mid = (low+high)//2
    if G[mid][0] == x : # when mid code is user's input country code
        return True
    elif G[mid][0] < x : # when user's input country code is over than mid data
        return binary_search(G, x, mid+1, high)
    else : # when user's input country code is lower than mid data
        if low == mid : # Special case when list consists of only two element
            return False
        else :
            return binary_search(G, x, low, mid-1)

# To get information of user's input country code
def this_is_check(G, x, low, high) :
    if low == high : # base case
        if G[low][0] == x : 
            return G[low][1], G[low][2], G[low][3] # get information
        else :
            return False
    mid = (low+high)//2
    if G[mid][0] == x :
        return G[mid][1], G[mid][2], G[mid][3] # get information
    elif G[mid][0] < x :
        return this_is_check(G, x, mid+1, high) # recursive case
    else :
        if low == mid :
            return False
        else :
            return this_is_check(G, x, low, mid-1) # recursive case
    
    


def main() :
    glob = read_file()
    glb = merge_sort(glob)
    while True :
        try :
            check = input("Type in a country code(two letters) or type in 'q' to stop : ")
            check = str(check)
            check = check.strip("\n")
            if check == 'q' :
                break
            else :
                if len(check) != 2 : # when user input more than 2 length words
                    print('%s is not in the file' % check)
                else :
                    if binary_search(glb, check, 0, len(glb)-1) :
                        name, latitude, longitude = this_is_check(glb, check, 0, len(glb)-1)
                        print('code'+' '+ '='+' '+str(check)+' '+';'+' '+'name'+' '+'='+' '+str(name)+' '+';'+' '+'latitude'+' '+'='+' '+str(latitude)+' '+';'+' '+'longitude'+' '+'='+' '+str(longitude))
                    else : 
                        print('%s is not in the file' % check)
                        
        except : # when user input non_string data
            print('%s is not in the file' % check)
            

            
                        
main()
