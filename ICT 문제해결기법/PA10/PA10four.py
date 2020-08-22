parent = {}
rank = {}
conflict = {}

N = int(input())

M = int(input())
v1 = 0
v2 = 0
v3 = 0
v4 = 0
r1 = 0
r2 = 0

def Find(v) :
    if parent[v] != v : parent[v] = Find(parent[v])
    return parent[v]

def Union(r1, r2) :
    if r1 == r2 : return
    if rank[r1] > rank[r2] :
        parent[r2] = r1
    elif rank[r1] < rank[r2] :
        parent[r1] = r2
    else :
        parent[r1] = r2
        rank[r2] += 1
result = 0

# Make Set
for n in range(1, N+1) :
    parent[n] = n
    rank[n] = 0
    conflict[n] = None

for m in range(1, M+1) :
    result = result + 1
    v1, v2 = [int(x) for x in input().split()]
    v3 = conflict[v1]
    v4 = conflict[v2]
    #if v3 == v4 and (v3 != None) :
    #    break
    if v3 == None :
        conflict[v1] = v2
    else :
        #if conflict[v2] == None :
        #    conflict[v2] = v1
        r1 = Find(v2)
        r2 = Find(v3)
        #print(conflict[r1])
        if conflict[r1] == r2 :
            break
        else :
            Union(r1, r2)
    if v4 == None :
        conflict[v2] = v1
    else :
        #if conflict[v1] == None :
        #    conflict[v1] = v2
        r1 = Find(v1)
        r2 = Find(v4)
        if conflict[r1] == r2 :
            break
        else :
            Union(r1, r2)

print(result)
