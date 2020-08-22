import heapq

queue = []
graph_data = [[2, 'A'], [5, 'B'], [3, 'C']]

#for edge in graph_data:
#    heapq.heappush(queue, edge)
heapq.heapify(graph_data)
#print(queue)
for index in range(len(queue)):
    print (heapq.heappop(queue))

print (queue)
