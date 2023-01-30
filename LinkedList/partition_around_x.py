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
        
    def partition_linkedlist_around_x(self, x):
        list_greater_than_x = LinkedList()
        list_less_than_x = LinkedList()
        
        current = self.head
        while current:
            if current.data >= x:
                list_greater_than_x.add_node(current.data)
            else:
                list_less_than_x.add_node(current.data)
                
            current = current.next
            
        
        combine_list = list_less_than_x.head
        while combine_list.next:
            combine_list = combine_list.next
                        
        combine_list.next = list_greater_than_x.head
        
        hc = list_less_than_x.head
        while hc:
            print(hc.data)
            hc = hc.next
    
        
linkedList = LinkedList()
linkedList.add_node(3)
linkedList.add_node(5)
linkedList.add_node(8)
linkedList.add_node(5)
linkedList.add_node(10)
linkedList.add_node(2)
linkedList.add_node(1)

        
linkedList.print_nodes()
linkedList.partition_linkedlist_around_x(5)



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def partition(self, x):
        less_head = less_tail = Node(0)
        equal_head = equal_tail = Node(0)
        greater_head = greater_tail = Node(0)

        current = self.head
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = current
            elif current.val == x:
                equal_tail.next = current
                equal_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
            current = current.next

        greater_tail.next = None
        equal_tail.next = greater_head.next
        less_tail.next = equal_head.next

        self.head = less_head.next
