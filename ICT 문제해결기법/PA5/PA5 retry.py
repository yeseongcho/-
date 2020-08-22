import math
sqrt = math.sqrt
def get_list() :
    list1 = []
    sums = 0
    h, w = [int(x) for x in input().split()]
    for j in range(h) :
        s = [int(x) for x in input().split()]
        list1.append(s)
        sums = sums + sum(s)
    return list1, sums

def fitted(i, board, Num, num, a, b) :
    #print("try")
    if (board[Num+b][num+a] == 0 ) or (i[1][Num][num] == 0) :
        return True
    else :
        return False
    
def put(i, board, Num, num, a, b) :
    #print("try")
    board[Num+b][num+a] = board[Num+b][num+a] + i[1][Num][num]
    #print(board)

def find_and_try(List, board, a, b, prev_board, success = False) :
    print(success)
    #prev_list = List
    if success : return success, board
    for i in List :
        prev_board[i[0]] = board # 부모 값들은 어디서 갱신시켜주지?
        large_index = len(board) - len(i[1]) + 1
        small_index = len(board[0]) - len(i[1][0]) + 1
        for Num in range(len(i[1])) :
            for num in range(len(i[1][0])) :
                if fitted(i, board, Num, num, a, b) :
                    put(i, board, Num, num, a, b)
                    #print(board)
                else :
                    # 요기는 다른 위치에 끼워보는 과정
                    print(a)
                    a = a + 1
                    if a != small_index :
                        return find_and_try(List, board, a, b, prev_board, len(List)==0), board
                    a = 0
                    b = b + 1
                    if b != large_index :
                        return find_and_try(List, board, a, b, prev_board, len(List)==0), board
                    b = 0
                    a = 0
                    # 아예 이전 블록이 잘못 끼워진 경우 -- 부모의 값으로 다시 갱신하여 test
                    board = prev_board[i[0]]
                    List = prev_list[i[0]]
                    # 다시 넣을 때 a, b 조정 필요 없나?
                    return find_and_try(List, board, a, b, prev_board, len(List)==0), board
                
                    return False, board
        prev_list[i[0]] = List
        
        List = List[1:] # 줄여주는 과정이 필요
        
    return success, board
     
N = int(input())
List = []
Sum = 0
for i in range(N) :
    values, sums = get_list()
    Sum = Sum + sums
    List.append((i, values))

#print(List)
board = []
prev_board = {}
prev_list = {}
for k in range(N) :
    prev_board[k] = board
for m in range(N) :
    prev_list[m] = List

x = 0
x = int(sqrt(Sum))
a = 0
b = 0
if ( x == 1) or (x==4) or ( x==9 ) or (x==16) or (x==25) or (x==36) or (x==49) or (x==64) :
    for i in range(x) :
        board.append([0]*x)
    

    if find_and_try(List, board, a, b, prev_board)[0] :
        for i in range(len(board)) :
            for j in range(len(board[i])) :
                print(board[i][j], end = " ")
            print(" ")
else :
    print("No solution possible")





    
