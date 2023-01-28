class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def print_nodes(self):
        current = self.head
        data = []
        while current.next != None:
            data.append(current.data)
            current = current.next
        data.append(current.data)
        
        print(data)
        
    def add_node(self, value):
        node = Node(value)
        
        head = self.head
        self.head = node
        node.next = head
        
        
    def remove_duplicate_nodes(self):
        current = self.head
        unique_data = []
        
        unique_data.append(current.data)
        previous = current
        
        while current:
            
            prev = previous
            current = current.next
            
            if current:
                if current.data in unique_data:
                    prev.next = current.next
                    continue

                unique_data.append(current.data)
                
            previous = current
            
        print(unique_data)
            

list1 = LinkedList()

list1.add_node(34)
list1.add_node(19)
list1.add_node(34)
list1.add_node(19)
list1.add_node(19)
list1.add_node(19)
list1.add_node(19)
list1.add_node(34)
list1.add_node(34)
list1.add_node(34)
list1.add_node(19)
list1.add_node(4)
list1.add_node(4)
list1.add_node(4)
list1.add_node(4)
list1.add_node(0)


list1.remove_duplicate_nodes()

list1.print_nodes()

