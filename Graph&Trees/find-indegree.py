graph = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}

indegree = {node: 0 for node in graph}

for ns in graph.values():
    for n in ns:
        indegree[n] += 1
        
        
print(indegree)

adjacency_list = [[0,1], [1,2], [3,4], [5,6]]

indegree = {}

for edge in adjacency_list:
    from_node, to_node = edge
    indegree[from_node] = 0
    indegree[to_node] = 0
    
for edge in adjacency_list:
    _, to_node = edge
    indegree[to_node] += 1
    
print(indegree)


