graph = {
    '5': ['2', '3'],
    '2': ['1', '0'],
    '3': ['7', '9'],
    '7': ['10']
}


class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, node):
        pass
        

class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        
        visited.add(node)
        if graph.get(node, None):
            
            # Create linkedList
            linked_list = LinkedList()
            lnode = Node(node)
            linked_list.add(lnode)
        
            for child in reversed(graph.get(node, None)):
                if child not in visited:
                    stack.append(child)
                    lnode = Node(node)
                    linked_list.add(lnode)
                

dfs(graph, '5')
