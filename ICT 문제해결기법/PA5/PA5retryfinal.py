import math
sqrt = math.sqrt
def get_list() :
    list1 = []
    sums = 0
    count = 0
    h, w = [int(x) for x in input().split()]
    for j in range(h) :
        s = [int(x) for x in input().split()]
        list1.append(s)
        sums = sums + sum(s)
    return list1, sums

def fitted(lists, board, Num, num, a, b, next_block) :
    if next_block == 0 :
        return True
    elif board[Num+b][num+a] + lists[1][Num][num] >= 2 :
        return False
    else :
        return True
    
    
def put(lists, board, Num, num, a, b, next_block) :
    
    if lists[1][Num][num] != 0 :
        board[Num+b][num+a] = board[Num+b][num+a] + lists[0] + 1 
    



def find_and_try(lists, board, a, b, prev_board, next_block, when_a, when_b, List) :
    
    large_index = len(board) - len(lists[1]) + 1
    small_index = len(board[0]) - len(lists[1][0]) + 1
    for Num in range(len(lists[1])) :
        for num in range(len(lists[1][0])) :
            if fitted(lists, board, Num, num, a, b, next_block) :
                put(lists, board, Num, num, a, b, next_block)
            else :
                # 요기는 다른 위치에 끼워보는 과정
                board = prev_board[lists[0]]
                a = a + 1
                #print(a)
                if a != small_index :
                    return find_and_try(lists, board, a, b, prev_board, next_block, when_a, when_b, List), board
                a = 0
                board = prev_board[lists[0]]
                b = b + 1
                if b != large_index :
                    return find_and_try(lists, board, a, b, prev_board, next_block, when_a, when_b, List), board
                b = 0
                a = 0
                # 왜 c블록에서 부모값이 변형되지??
                board = prev_board[lists[0]-1]
                #print(lists[0]-1)
                #print(prev_board[lists[0]-1])
               
                a = when_a[lists[0]-1] + 1
                
                if a != small_index :
                    return find_and_try(List[next_block-1], board, a, b, prev_board, next_block, when_a, when_b, List), board
                a = 0
                board = prev_board[lists[0]-1]
                b = when_b[lists[0]-1] + 1
                if b != large_index :
                    return find_and_try(List[next_block-1], board, a, b, prev_board, next_block, when_a, when_b, List), board
                
                return False, board
    #print("#")
    prev_board[lists[0]+1] = board
    #print("##")
    #print(lists[0]+1)
    #print(prev_board[lists[0]+1])
    when_a[lists[0]] = a
    when_b[lists[0]] = b
    next_block += 1
    #print(next_block)
    if next_block == len(List) :
        return True, board
    
    return find_and_try(List[next_block], board, a, b, prev_board, next_block, when_a, when_b, List), board

def main() :
    N = int(input())
    List = []
    Sum = 0
    for i in range(N) :
        values, sums = get_list()
        Sum = Sum + sums
        List.append((i, values))

    board = []
    prev_board = {}
    when_a = {}
    when_b = {}

    x = 0
    x = int(sqrt(Sum))
    a = 0
    b = 0
    next_block = 0
    if ( x == 1) or (x==4) or ( x==9 ) or (x==16) or (x==25) or (x==36) or (x==49) or (x==64) :
        for i in range(x) :
            board.append([0]*x)
        for k in range(N) :
            prev_board[k] = board

        if find_and_try(List[next_block], board, a, b, prev_board, next_block, when_a, when_b, List)[0] :
            for i in range(len(board)) :
                for j in range(len(board[i])) :
                    print(board[i][j], end = " ")
                print(" ")
    else :
        print("No solution possible")



main()
