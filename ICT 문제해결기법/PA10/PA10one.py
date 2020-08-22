parent = {}
conflict = {}

N = int(input())

M = int(input())

v1 = 0
v2 = 0
v3 = 0
v4 = 0

def check_another(conflict, v, u) :
    if conflict[v] == [] : return None
    get_me = 0
    for i in conflict[v] :
        # 같은 경우 말구
        if i == u :
            continue
        else :
            # 이거 맞는겨?
            get_me = i
            break
    return get_me

def Find(v) :
    if parent[v] != v : parent[v] = Find(parent[v])
    return parent[v]

def check_conflict(conflict, v, u) :

    return (v not in conflict[u]) and (u not in conflict[v])
   
# Make Set
for i in range(1, N+1) :
    parent[i] = i
    conflict[i] = []
print(conflict)
results = 0
for m in range(1, M+1) :
    v1, v2 = [int(x) for x in input().split()]
    
    v3 = check_another(conflict, v1, v2)
    v4 = check_another(conflict, v2, v1)

    conflict[v1].append(v2)
    conflict[v2].append(v1)
    
    if v3 != None :
        if not check_conflict(conflict, v3, v2) :
            results = m 
            break
    if v4 != None :
        if not check_conflict(conflict, v4, v1) :
            results = m
            break
            
print(results)

