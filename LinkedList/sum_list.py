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
    
    @staticmethod   
    def sum_list(list1, list2):
        current = list1.head
        current2 = list2.head
        results = LinkedList()
        
        value = 0
        carry = 0
        
        while current and current2:
            carry = value // 10
            value = carry + current.data + current2.data
            
            results.add_node(value % 10)
            
            current = current.next
            current2 = current2.next
            
        
        current_results = results.head
        while current_results:
            print(current_results.data)
            current_results = current_results.next
            
    @staticmethod
    def sum_list_recursively(list1, list2, carry, results):
        if not list1 or not list2: return
        
        value = carry + list1.data + list2.data
        results.add_node(value % 10)
        
        carry = value // 10
        
        current = results.head
        print(current.data, results)
        
        LinkedList.sum_list_recursively(list1.next, list2.next, carry, results)
        
        

list1 = LinkedList()

list1.add_node(6)
list1.add_node(1)
list1.add_node(7)

list1.print_nodes()

list2 = LinkedList()

list2.add_node(2)
list2.add_node(9)
list2.add_node(5)

list2.print_nodes()

results = LinkedList()
LinkedList.sum_list_recursively(list1.head, list2.head, 0, results)
