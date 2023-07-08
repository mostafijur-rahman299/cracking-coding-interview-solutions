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
        if self.head == None:
            self.head = Node(value)
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = Node(value)
        
    def print_kth_to_last_with_recursive(self, head, k):
        if head is None:
            return 0
        index = self.print_kth_to_last_with_recursive(head.next, k) + 1
        if index == k:
            print(f"{k} th to last node is {head.data}")
        return index
    
    def print_kth_to_last(self, k):
        p1 = self.head
        p2 = self.head
        
        i = 0
        while i < k:
            p1 = p1.next
            i += 1
            
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        print(p2.data)
        
linkedList = LinkedList()
linkedList.add_node(4)
linkedList.add_node(3)
linkedList.add_node(7)
linkedList.add_node(1)
linkedList.add_node(5)
linkedList.add_node(9)
linkedList.add_node(11)

        
linkedList.print_nodes()

linkedList.print_kth_to_last_with_recursive(linkedList.head, 3)
linkedList.print_kth_to_last_with_recursive(3)
