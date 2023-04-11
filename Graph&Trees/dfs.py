graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

def graph_dfs(graph, start):
    visited = set()
    stack = [start]
    print("called")
    while stack:
        vertext = stack.pop()
        visited.add(vertext)
        print(vertext)
        for child in reversed(graph[vertext]):
            if child not in visited:
                stack.append(child)
                
graph_dfs(graph, 'A')

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

def graph_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for child in graph[start]:
        if child not in visited:
            graph_dfs(graph, child, visited)
                
graph_dfs(graph, 'A')
