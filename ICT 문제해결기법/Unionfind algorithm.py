# Disjoint set을 표현할 때 사용하는 알고리즘
# Disjoint set : 서로 중복되지 않는 부분 집합들로 나누어진 원소들에 대한 정보를
# 저장하고 조작하는 자료구조
parent = {}
rank = {}

def MakeSet(v) :
    parent[v] = v
    rank[v] = 0

def Find(v) :
    if parent[v] != v : parent[v] = Find(parent[v])
    return parent[v]

def Union(u, v) :
    x, y = Find(u), Find(v)
    if x == y : return
    if rank[x] > rank[y] :
        parent[y] = x
    elif rank[x] < rank[y] :
        parent[x] = y
    else :
        parent[y] = x
        rank[x] += 1

def print_part(L) :
    print("{", end = " ")
    for i in range(len(L)-1) :
        print(L[i]+",", end = " ")
    print(L[len(L)-1], "}")

def set_current(node) :
    nNode = [node[1]]
    return node[0], nNode

def report_parts(V_set, V_rep) :
    partition = []
    for i in range(len(V_set)) :
        partition.append((V_rep[i], V_set[i]))
    partition.sort()
    cRoot = None
    for i in range(len(partition)) :
        if cRoot == None :
            cRoot, cNode = set_current(partition[i])
        elif cRoot != partition[i][0] :
            print_part(cNode)
            cRoot, cNode = set_current(partition[i])
        else :
            cNode.append(partition[i][1])
    print_part(cNode)

graph = {"v1" : {"v2", "v4"}, "v2":{"v1","v4"}, "v3":{"v5"}, "v4" : {"v1","v2"}, "v5":{"v3"}, "v6":set()}
#graph = {"v1" : {"v2", "v5"}, "v2" : {"v1", "v3"}, "v3" : {"v2", "v4"}, "v4" : {"v5", "v3"}, "v5" : {"v1","v4"}}
def main() :
    V = [v for v in graph]
    for v in V :
        MakeSet(v)
    for vertex in graph :
        for child in graph[vertex] :
            Union(vertex, child)
    vRep = [Find(v) for v in V]
    report_parts(V, vRep)


main()
