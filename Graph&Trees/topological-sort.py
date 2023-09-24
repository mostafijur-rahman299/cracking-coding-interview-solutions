adjacency_list = [[1,4],[2,4],[3,1],[3,2]]

graph = {}
indegree = {}
queue = []
ans = []

# make a graph from list
for preq, course in adjacency_list:
    if preq in graph:
        graph[preq].append(course)
    else:
        graph[preq] = [course]

# Find indegree from adjancency list
for edge in adjacency_list:
    from_node, to_node = edge
    indegree[from_node] = 0
    indegree[to_node] = 0
    
for edge in adjacency_list:
    _, to_node = edge
    indegree[to_node] += 1
    
for key, value in indegree.items():
    if value == 0:
        queue.append(key)
        
while queue:
    node = queue.pop(0)
    ans.append(node)
    
    if graph.get(node):
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    

print(indegree)
