from random import randint
import math

sqrt = math.sqrt

def fitted(plm,x,y,n) :
    h = len(plm)
    w = len(plm[0])
    for a in range(h) :
        for b in range(w) :
            if plm[a][b]-board[a+y][b+x] != 1 and plm[a][b] == 1 :
                return False
    return True
            
def put_plm(plm, x, y, n) :
    h = len(plm)
    w = len(plm[0])
    for a in range(h) :
        for b in range(w) :
            if plm[a][b] - board[a+y][b+x] == 1 and plm[a][b] == 1 :
                board[a+y][b+x] = n

def undo_plm(plm, x, y, n) :
    h = len(plm)
    w = len(plm[0])
    for a in range(h) :
        for b in range(w) :
            if plm[a][b] == 1 and board[a+y][b+x] == n :
                board[a+y][b+x] = 0


def find_and_try(plm_lst, success = False, n=1) :
    if success : return success
    for i in plm_lst :
        x = -1
        y = -1
        plm, remLst = plm_lst[0], plm_lst[1:]
        for j in range(square) :
            y += 1
            x = -1
            if len(plm)+y > len(board) :
                continue
            for k in range(square) :
                x += 1
                if len(plm[0])+x> len(board) :
                    continue
                if fitted(plm,x,y,n) :
                    put_plm(plm, x, y, n)
                    success = find_and_try(remLst, len(remLst)==0, n+1)
                    if success : return success
                    else : undo_plm(plm,x,y,n)
        return success

N = int(input())
sums = 0
data = []
for i in range(N) :
    info = [int(x) for x in input().split()]
    height = info[0]
    width = info[1]
    data.append([])
    for j in range(height) :
        data[i].append([int(x) for x in input().split()])
        sums += sum(data[i][j])

if sqrt(sums) != 1 and sqrt(sums) != 2 and sqrt(sums) != 3 and sqrt(sums) != 4 and sqrt(sums) != 5 and sqrt(sums) != 6 and sqrt(sums) != 7 and sqrt(sums) != 8 :
    print("No solution possible")

else :
    square = int(sqrt(sums))
    board = [[0]*square for i in range(square)]
    
    if find_and_try(data) :
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                print(board[i][j], end=' ')
            print('')

    else :
        print("No solution possible")


