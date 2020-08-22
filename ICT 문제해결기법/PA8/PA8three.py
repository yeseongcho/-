mountain = {}
root = {}
N = int(input())

for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]
        

Max = 0

roots = 0 # 현재 가리키는 노드의 root값

start = 0 # 자신의 시작점

# 각 recurisve 수행 시 root 정보
root1 = (0, 0)

root2 = (0 ,0)

root3 = (0 ,0)

root4 = (0, 0)

true_root = 0

## root값의 판을 초기화해주는 효과적인 방법이 없을까?

# root값 추적, 이렇게 dynamic programming을 짜주면 되지 않나?
def Find(node, root) :
    if node in root :
        node = root[node]
        Find(node, root)
    root[node] = node
    return node

def compare(row, val, start, root1, root2, root3, root4, root={}) :
    # 우선 값을 초기화, key error 방지를 위해
    #root[mountain[row][mountain[row].index(val)]] = val
    if row == 0 :
        if mountain[row][mountain[row].index(val)] == 0 :
            if val < mountain[row][mountain[row].index(val)+1] :
                root1 = Find((row, mountain[row][mountain[row].index(val)+1]), root)

            if val < mountain[row+1][mountain[row].index(val)] :
                
                root2 = Find((row, mountain[row+1][mountain[row].index(val)]), root)

            true_root = max(root1[1]-start, root2[1]-start, start)
            return true_root

        elif mountain[row][mountain[row].index(val)] == 3 :
            if val < mountain[row][mountain[row].index(val)-1] :
                print(val)
                print(mountain[row][mountain[row].index(val)-1])
                print(root)
                root1 = Find((row, mountain[row][mountain[row].index(val)-1]), root)

            if val < mountain[row+1][mountain[row].index(val)] :
                root2 = Find((row, mountain[row+1][mountain[row].index(val)]) , root)

            true_root = max(root1[1]-start, root2[1]-start, start)
            return true_root    
            
        else :
            if val < mountain[row][mountain[row].index(val)+1] :
                root1 = Find((row, mountain[row][mountain[row].index(val)+1]), root)
                
            if val < mountain[row][mountain[row].index(val)-1] :
                root2 = Find((row,  mountain[row][mountain[row].index(val)-1]), root)

            if val < mountain[row+1][mountain[row].index(val)] :
                root3 = Find((row, mountain[row+1][mountain[row].index(val)] ), root)
            true_root = max(root1[1]-start, root2[1]-start, root3[1]-start, start)
            return true_root
    elif row == 3 :
        if mountain[row][mountain[row].index(val)] == 0 :
            if val <  mountain[row][mountain[row].index(val)+1] :
                root1 = Find((row, mountain[row][mountain[row].index(val)+1]), root)

            if val <  mountain[row-1][mountain[row].index(val)] :
                root2 = Find((row,  mountain[row-1][mountain[row].index(val)]), root)

            true_root = max(root1[1]-start, root2[1]-start, start)
            return true_root
        elif mountain[row][mountain[row].index(val)] == 3 :
            if val < mountain[row][mountain[row].index(val)-1] :
                root1 = Find((row, mountain[row][mountain[row].index(val)-1]), root)

            if val < mountain[row-1][mountain[row].index(val)] :
                root2 = Find((row, mountain[row-1][mountain[row].index(val)] ), root)
            true_root = max(root1[1]-start, root2[1]-start, start)
            return true_root
        else :
            if val < mountain[row][mountain[row].index(val)-1] :
                root1 = Find((row, mountain[row][mountain[row].index(val)-1]), root)

            if val < mountain[row][mountain[row].index(val)+1] :
                root2 = Find((row, mountain[row][mountain[row].index(val)+1] ), root)

            if val < mountain[row-1][mountain[row].index(val)] :
                root3 = Find((row, mountain[row-1][mountain[row].index(val)] ), root)
            true_root = max(root1[1]-start, root2[1]-start, root3[1]-start, start)
            return true_root
    else :
        if mountain[row][mountain[row].index(val)] == 0 :
            if val < mountain[row][mountain[row].index(val)+1] :
                root1 = Find((row, mountain[row][mountain[row].index(val)+1]), root)

            if val < mountain[row-1][mountain[row].index(val)] :
                root2 = Find((row, mountain[row-1][mountain[row].index(val)]), root)

            if val < mountain[row+1][mountain[row].index(val)] :
                root3 = Find((row, mountain[row+1][mountain[row].index(val)]), root)
            true_root = max(root1[1]-start, root2[1]-start, root3[1]-start, start)
            return true_root
        elif mountain[row][mountain[row].index(val)] == 3 :
            if val < mountain[row][mountain[row].index(val)-1] :
                root1 = Find((row, mountain[row][mountain[row].index(val)-1]), root)

            if val < mountain[row-1][mountain[row].index(val)] :
                root2 = Find((row, mountain[row-1][mountain[row].index(val)]), root)

            if val < mountain[row+1][mountain[row].index(val)] :
                root3 = Find((row, mountain[row+1][mountain[row].index(val)]), root)
            true_root = max(root1[1]-start, root2[1]-start, root3[1]-start, start)
            return true_root
        else :
            if val < mountain[row][mountain[row].index(val)-1] :
                root1 = Find((row, mountain[row][mountain[row].index(val)-1]), root)

            if val < mountain[row][mountain[row].index(val)+1] :
                root2 = Find((row, mountain[row][mountain[row].index(val)+1]), root)

            if val < mountain[row+1][mountain[row].index(val)] :
                root3 = Find((row,  mountain[row+1][mountain[row].index(val)] ), root)

            if val < mountain[row-1][mountain[row].index(val)] :
                root4 = Find((row, mountain[row-1][mountain[row].index(val)]), root)
            true_root = max(root1[1]-start, root2[1]-start, root3[1]-start, root4[1]-start, start)
            return true_root
for i in mountain :
    for j in mountain[i] :
        # 비교 함수
        start = j
        roots = compare(i, j, start, root1, root2, root3, root4)
        Max = max(Max, roots)
        #roots[(i, j)] = roots # root 한번 더 갱신

print(Max)        

