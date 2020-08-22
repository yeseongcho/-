def fitted(m,square,x,y,seq):
    auxil = square
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==1 and m[i][j]-square[i+y][j+x]!=1:
                return False, square
            if m[i][j]==1 and m[i][j]-square[i+y][j+x]==1:
                auxil[i+y][j+x] = seq
    return True, auxil

def subtract(m,square,x,y,seq):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==1 and square[i+y][j+x]==seq:
                square[i+y][j+x] = 0
    return square

def confirm(lst, square, k=1, success = False):
    x, y = -1, -1
    if len(lst)==0:
        return True
    m, remLst = lst[:1], lst[1:]
    m=m[0]
    is_empty = len(remLst) == 0
    h, w = len(m), len(m[0])
    for i in range(len(square)):
        y+=1
        x=-1
        if h+y>len(square):
            continue
        for j in range(len(square)):
            x+=1
            if w+x>len(square):
                continue
            is_fitted, square = fitted(m, square, x, y, k)
            if is_fitted:
                success = confirm(remLst, square, k+1)
            if success==False:
                square = subtract(m,square,x,y,k)
                continue
    return success

n = int(input())
summ, square, poly = 0, [1,2,3,4,5,6,7,8], [[] for x in range(n)]

for i in range(n):
    auxil = [int(x) for x in input().split()]
    for j in range(auxil[0]):
        poly[i].append([int(x) for x in input().split()])
        summ+=poly[i][j].count(1)
summ=int(summ**(1/2))

if square.count(summ) == 0:
    print("No solution possible")
    
else:
    square = [int(0) for x in range(summ)]
    for i in range(summ):
        square[i] = [int(0) for x in range(summ)]
    last = confirm(poly, square)
    if last == False:
        print("No solution possible")
    elif last == True:
        for i in range(summ):
            for j in range(len(square[i])):
                print(square[i][j],end=' ')
            print()
