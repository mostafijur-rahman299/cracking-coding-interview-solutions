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
        
    def add_node_in_last_position(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = Node(value)
        
    def add_node_in_first_position(self, value):
        node = Node(value) # Make node instance
        
        head = self.head
        self.head = node
        node.next = head
        
    def add_node_in_middle_position(self, value):
        node = Node(value)
        a = self.head
        b = self.head.next
        
        if b:
            while b.next:
                a = a.next
                if b.next.next:
                    b = b.next.next
                else:
                    b = b.next
        
        next_node = a.next
        a.next = node
        node.next = next_node
        
    def insert_node(self, position, value):
        node = Node(value)
        
        current = self.head
        current_position = 0
        
        while current:
            if current_position + 1 == position:
                next_node = current.next
                current.next = node
                node.next = next_node
                break
                
            elif position == 0:
                current = self.head
                self.head = node
                node.next = current
                break
            
            current = current.next
            current_position += 1
            
    def delete_node(self, value):
        current = self.head
        
        if current.data == value:
            self.head = current.next
            return
        
        while current:
            if current.data == value:
                break
                
            prev = current
            current = current.next
            
        prev.next = current.next
            
        
            
list1 = LinkedList()
list1.add_node_in_last_position(4)
list1.add_node_in_last_position(5)
list1.add_node_in_last_position(6)
list1.add_node_in_last_position(9)
list1.add_node_in_first_position(10)
list1.add_node_in_last_position(93)
list1.add_node_in_last_position(19)
list1.add_node_in_last_position(34)
list1.add_node_in_last_position(95)

list1.add_node_in_middle_position(900)

list1.insert_node(0, 989898989)

list1.delete_node(95)

list1.print_nodes()

