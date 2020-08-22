def bfs_iterative(graph, start) :
    queue, path = [start], []
    while queue :
        vertex = queue.pop(0)
        if vertex in path :
            continue
        path.append(vertex)
        for neighbor in graph[vertex] :
            queue.append(neighbor)
    return path

input_graph = {'A':['B', 'C'],
               'B' : ['A', 'D', 'E'],
               'C' : ['A', 'F'],
               'D' : ['B'], 'E' : ['B', 'F'],
               'F' : ['C', 'E']}
print(bfs_iterative(input_graph, "A"))

