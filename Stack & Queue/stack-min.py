class Stack:
    def __init__(self):
        self.local_min = -1
        self.stack_list = []
        
    def push(self, value):
        if len(self.stack_list) == 0:
            self.local_min = value
        elif value < self.local_min:
            self.local_min = value
            
        stack = StackItem(value, self.local_min)
        self.stack_list += [stack]
        
    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack !!")
            
        self.stack_list.pop()
        
        if not self.is_empty():
            self.local_min = self.stack_list[len(self.stack_list)-1].local_min
        else:
            self.local_min = -1
            
    def peek(self):
        if self.is_empty():
            raise Exception("Empty stack !!")
        return self.stack_list[len(self.stack_list)-1]
    
    
    def minimum(self):
        return self.peek().local_min
            
    def is_empty(self):
        return not bool(self.stack_list)
    

class StackItem:
    def __init__(self, value, local_min):
        self.value = value
        self.local_min = local_min
        
        
stk = Stack()

stk.push(100)
stk.push(2)
stk.push(33)
stk.push(100)
stk.push(23)
stk.push(3)
stk.push(100)
stk.push(23)
stk.push(33)
stk.push(100)
stk.push(23000)
stk.push(33)

stk.pop()


stk.minimum()




class Stack:
    def __init__(self):
        self.stack = []
        self.stack_min_item = []
        
    def push(self, value):
        if len(self.stack) == 0:
            self.stack_min_item += [value]
        elif self.stack_min_item[len(self.stack_min_item) - 1] >= value:
            self.stack_min_item += [value]
            
        self.stack += [value]
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty !!")
            
        remove_item = self.stack[len(self.stack)-1]
        local_min = self.stack_min_item[len(self.stack_min_item)-1]
        if remove_item == local_min:
            self.stack_min_item.pop()
        self.stack.pop()
        
    def print_stack(self):
        print("stacks=====", self.stack)
        print("min items====", self.stack_min_item)
        
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty !!")
        return self.stack[len(self.stack) - 1]
    
    def min_item(self):
        if self.is_empty():
            raise Exception("Stack is empty !!")
        print(self.stack_min_item[len(self.stack_min_item) - 1])
            
    
    def is_empty(self):
        return not bool(self.stack)
    

stack = Stack()

stack.push(109)
stack.push(105)
stack.push(7)
stack.push(139)
stack.push(200)
stack.push(890)
stack.push(90)
stack.push(102)
stack.push(77)
stack.push(77)
stack.push(7)
stack.push(1)
stack.push(7)

stack.print_stack()
stack.min_item()

stack.pop()
stack.pop()

stack.min_item()




