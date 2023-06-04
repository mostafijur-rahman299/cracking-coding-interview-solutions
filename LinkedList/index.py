class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def print_linked_list_items(self):
        current = self.head
        
        while current:
            print(current.data)
            current = current.next
        
    def prepand_item(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        temp_head = self.head
        self.head = new_node
        new_node.next = temp_head
        
    def append_item(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head.next
        while current.next:
            current = current.next
            
        current.next = new_node
        
    def append_middle_poition(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
                
        current = self.head
        runner = self.head
        
        while current.next and runner.next.next:
            runner = runner.next.next
            current = current.next
            
        middle_next = current.next
        current.next = new_node
        new_node.next = middle_next
        
    def remove_head_node(self):
        if not self.head:
            return
        
        second_item = self.head.next
        self.head = second_item
        
    def remove_last_node(self):
        current = self.head
        previous_node = self.head
        
        while current.next:
            previous_node = current
            current = current.next
        
        if current == self.head:
            self.head = None
        
        previous_node.next = None
        
    def remove_middle_node(self):
        
        current = self.head
        runner = self.head
        middle_previous = self.head
        
        while current and runner.next:
            middle_previous = current
            current = current.next
            runner = runner.next.next
            
        middle_previous.next = current.next
        
    def remove_item(self, data):
        current = self.head
        previous_node = None
        
        while current.next:
            
            if current.data == data:
                break
                
            previous_node = current
            current = current.next
            
        if previous_node and current.next:
            previous_node.next = current.next
        elif previous_node and not current.next:
            previous_node.next = None
        elif not previous_node:
            self.head = None
        
        

list1 = LinkedList()

list1.prepand_item(90)
list1.prepand_item(80)
list1.prepand_item(70)
list1.prepand_item(60)

list1.append_item(100)
list1.append_item(110)
list1.append_item(120)
list1.append_item(130)
list1.append_item(140)
list1.append_item(150)
list1.append_item(160)
list1.append_item(170)

list1.append_middle_poition(75)

list1.remove_head_node()

list1.remove_last_node()

list1.remove_middle_node()

list1.remove_item(120)

list1.print_linked_list_items()
