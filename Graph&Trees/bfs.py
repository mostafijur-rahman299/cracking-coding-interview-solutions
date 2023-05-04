graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

def graph_bfs(bfs, start):
    visited = list()
    stack = [start]
    while stack:
        vertex = stack.pop(0)
        visited.append(vertex)
        for child in graph[vertex]:
            if child not in visited:
                stack.append(child)
                
    print(visited)
                
graph_bfs(graph, 'A')
