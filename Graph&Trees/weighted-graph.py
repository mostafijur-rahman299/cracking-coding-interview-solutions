import heapq
class Graph:
    def __init__(self, n, edges):
        self.graph = {}
        
        # Initialize graph
        for node in range(n):
            self.graph[node] = []
            
        # Initialize edges
        for edge in edges:
            self.graph[edge[0]].append((edge[1], edge[2]))
            
    def addEdge(self, edge):
        if not self.graph:
            self.graph[edge[0]] = []
        self.graph[edge[0]].append((edge[1], edge[2]))
        print(self.graph)
        
    def sortestPath(self, node1, node2):
        distances = {vertex: float('infinity') for vertex in self.graph}
        
        queue = [self.graph[node1]]
        current_node = node1
        distances[node1] = 0
        
        while queue:
            nodes = queue.pop(0)
            
            min_distance = 0
            min_distance_node = 0
            
            for node in nodes:
                distance = distances[current_node] + node[1]
                distances[node[0]] = distance
                
                if distance < min_distance:
                    min_distance_node = node
                    
            queue.append(self.graph[min_distance_node])
            
        print(distances)

        # If the destination node is not reachable from the source
        return  -1
            
g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);

g.addEdge([1, 3, 4])
g.sortestPath(3, 2)