# 이중 dictionary로 graph 구성
graph = { "a" : {"b" : 7, "c" : 9, "f" : 14},
          "b" : {"c":10, "d":15},
          "c" : {"f": 2, "d":11},
          "d" : {"e":6},
          "e":{},
          "f":{"e":9}
          }

T = []
final_D = []

F = []
D = []
prev = {}

visited = {}

# 초기 방문값 visited 초기화
for v in graph :
    visited[v] = False


def append_to_T(vertex, distance) :
    T.append(vertex)
    final_D.append(distance)
    print(T)
    print(final_D)

def append_to_F(vertex, parent, value = None) :
    F.append(vertex)
    prev[vertex] = parent
    if value == None :
        D.append(graph[parent][vertex])
    else :
        D.append(value)

    visited[vertex] = True

# Tree로 산출될 애들 뽑고 Fringe 축소
def remove_from_F() :
    min_d = min(D)
    k = get_k(D, min_d)
    vertex = F.pop(k)
    D.pop(k)
    return vertex, min_d

def get_k(S, d) :
    return S.index(d)

# 최단 거리 갱신
def update_D(vertex, parent, value) :
    k = get_k(F, vertex)
    if value < D[k] :
        D[k] = value
        prev[vertex] = parent

def dijkstra(graph, start) :
    # step 0 ############ start point의 finge 설정
    prev[start] = None
    append_to_T(start, 0)
    for v in graph[start] :
        append_to_F(v, start)
    while F != [] : 
        # step 1 ################# 최단 경로를 tree로 삽입
        current, min_val = remove_from_F()
        append_to_T(current, min_val)

        # step 2 ################# 루트 중 가장 짧은 루트
        for v in graph[current] :
            new_dist = min_val + graph[current][v] # 새로운 dist 색출
            if not visited[v] : 
                append_to_F(v, current, new_dist) # 비 방문 노드 새로운 fringe 설정
            else :
                update_D(v, current, new_dist) # 최단 거리 갱신

# 최단 경로 산출
def print_shortest_path(target) :
    path = []
    k = get_k(T, target)
    while target != None :
        path.append(target)
        target = prev[target]
    path.reverse()
    print(path, final_D[k])


dijkstra(graph, "a")
print_shortest_path("e")

