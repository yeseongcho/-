def b_search(L, q, low, high) :
    if low == high :
        return L[low]== q
    mid = (low+high)//2
    if L[mid] == q :
        return True
    elif L[mid] < q :
        return b_search(L, q, mid+1, high)
    else :
        if low == mid : #special case ex) [5, 7]
            return False
        else :
            return b_search(L, q, low, mid-1)

def main() :
    L = [1, 2, 6, 8, 11, 19, 23]
    
    if b_search(L, 12, 0, 3) == True :
        print("Yes")
    else :
        print("No")

main()
