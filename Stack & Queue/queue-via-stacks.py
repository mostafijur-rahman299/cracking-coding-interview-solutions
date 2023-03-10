class QueueOfStacks:
    def __init__(self):
        self.entry_point_data = []
        self.exit_point_data = []
        
    def enqueue(self, value):
        self.entry_point_data.append(value)
        
    def entry_stack_data_to_queue(self):
        if not self.exit_point_data:
            while self.entry_point_data:
                self.exit_point_data.append(self.entry_point_data.pop())
                
    def dequeue(self):
        self.entry_stack_data_to_queue()
        if self.is_empty():
            raise Exception("Queue is empty !!")
        self.exit_point_data.pop()
        
    def peek(self):
        self.entry_stack_data_to_queue()
        if self.is_empty():
            raise Exception("Queue is empty !!")
        return self.exit_point_data[len(self.exit_point_data)-1]
        
    def is_empty(self):
        return not bool(self.exit_point_data)
        
        
    def print_stacks(self):
        print("entry pint======", self.entry_point_data)
        print("exit point=====", self.exit_point_data)
        
        
queue = QueueOfStacks()
queue.enqueue(109)
queue.enqueue(9)
queue.enqueue(90)
queue.enqueue(94)
queue.enqueue(87)

queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.print_stacks()

print(queue.peek())

        