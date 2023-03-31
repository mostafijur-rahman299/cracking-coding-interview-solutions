def has_route_dfs(graph, start_node, end_node):
    queue = [start_node]
    visited = set()
    
    while queue:
        start_node = queue.pop(0)
        visited.app(start_node)
        
        if start_node == end_node:
            return True
        
        for child in graph[start_node]:
            if child no in visited:
                queue.append(child)
        
    return False
    

graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []}

has_route_dfs(graph, 'B', 'E')


from collections import deque

def has_route_bfs(graph, start, end):
    """
    Determines whether there is a route between two nodes in a directed graph using BFS.
    
    Parameters:
    graph (dict): A dictionary representing the directed graph.
    start: The starting node.
    end: The ending node.
    
    Returns:
    bool: True if there is a route between the two nodes, False otherwise.
    """
    # Initialize a queue to store the nodes to be visited.
    queue = deque([start])
    
    # Initialize a set to store the visited nodes.
    visited = set()
    
    # Traverse the graph using BFS.
    while queue:
        # Get the next node from the queue.
        node = queue.popleft()
        
        # Check if the node has already been visited.
        if node in visited:
            continue
        
        # Add the node to the visited set.
        visited.add(node)
        
        # Check if the ending node has been reached.
        if node == end:
            return True
        
        # Add the neighbors of the node to the queue.
        neighbors = graph.get(node, [])
        for neighbor in neighbors:
            queue.append(neighbor)
    
    # If no route is found, return False.
    return False

graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []}

has_route_bfs(graph, 'B', 'E')

