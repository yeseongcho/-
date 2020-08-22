def dfs_iterative(graph, start) :
    stack, path = [start], []
    while stack :
        vertex = stack.pop()
        if vertex in path :
            continue
        path.append(vertex)
        for neighbor in reversed(graph[vertex]) :
            stack.append(neighbor)
    return path

input_graph = {'A':['B', 'C'],
               'B' : ['A', 'D', 'E'],
               'C' : ['A', 'F'],
               'D' : ['B'], 'E' : ['B', 'F'],
               'F' : ['C', 'E']}

print(dfs_iterative(input_graph, 'A'))

