def merge_sort(L) :
    if len(L) <2 :
        return L[:]
    mid = len(L)//2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)

def merge(left, right) :
    result = []
    i, j = 0, 0
    while i <len(left) and j <len(right) :
        if left[i] < right[j] :
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    while i <len(left) : # 더 이상 right에 항목이 없는 경우
        result.append(left[i])
        i += 1
    while j < len(right) : # 더 이상 left에 항목이 없는 경우. ex) [2, 3, 6, 9, 10, 11, 12, 13]
        result.append(right[j])
        j += 1
    return result

def main() :
    M = [23, 2, 8, 6, 17, 11, 20, 7]
    M = merge_sort(M) # 얘만 시행해주면 된다. 이 안에 이미 merge함수가 있기에!!
    print(M)

main()
    
