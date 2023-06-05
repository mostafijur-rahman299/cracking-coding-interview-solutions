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
        
    def reverse_list(self):
        current = self.head
        reverse_list = LinkedList()
        
        while current:
            reverse_list.add_node(current.data)
            current = current.next
        return reverse_list
    
    def check_palindrome(self):
        reverse_list = self.reverse_list()
        current = self.head
        
        pointer_2 = self.head.next # Loop through half of the list because if first half of the list is equal of it's reverse then last half of the lis the list must equal
        current2 = reverse_list.head
        
        while pointer_2:
            if current.data != current2.data:
                print("Not a palindrome")
                break
            
            current = current.next
            current2 = current2.next
            pointer_2 = pointer_2.next.next
            
        print("Yeah!! Palindrome")
        

        

list1 = LinkedList()

list1.add_node(0)
list1.add_node(1)
list1.add_node(2)
list1.add_node(1)
list1.add_node(0)

list1.print_nodes()
reverse_list = list1.reverse_list()
reverse_list.print_nodes()

list1.check_palindrome()

