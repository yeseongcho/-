def b_search(List2, j, low, high) :
    mid = (low+high)//2

    if List2[mid] == j :
        return mid

    elif List2[mid] < j :
        return b_search(List2, j, mid+1, high)

    elif List2[mid] > j :
        return b_search(List2, j, low, mid-1)



def main() :
    List = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 12 , 13]
    threshold = [5, 6]
    index = []
    for j in threshold :
        b = b_search(List, j, 0, len(List)-1)
        index.append(b)
    print(index)

main()
    
