# https://www.fun-coding.org/Chapter20-prim-live.html
# heap 자료구조랑 collections 자료구조에 대한 설명이랑 같이 공부를 하면 좋을 듯

# 1. 기본 프림 알고리즘
from collections import defaultdict

from heapq import *

def prim(start_node, edges) :
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges :
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list :
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes :
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2] :
                if edge[2] not in connected_nodes :
                    heappush(candidate_edge_list, edge)
    return mst
myedges = [
    (1, 'B', 'E'), (2, 'A', 'D'),
    (2, 'B', 'C'), (3, 'A', 'E'), (3, 'C', 'F'),
    (4, 'E', 'F'),
    (5, 'A', 'B'), (10, 'D', 'E')
]
result = []
result = prim('A', myedges)
print(result)
