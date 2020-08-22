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
r3 = 0
r4 = 0

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
    r1 = Find(v1)
    r2 = Find(v2)
    if r1 == r2 :
        break
    v3 = conflict[v1]
    v4 = conflict[v2]
    if v3 == None :
        conflict[v1] = v2
    else :
        r3 = Find(v3)
        Union(r2, r3)
    if v4 == None :
        conflict[v2] = v1
    else :
        r4 = Find(v4)
        Union(r1, r4)

print(result)

