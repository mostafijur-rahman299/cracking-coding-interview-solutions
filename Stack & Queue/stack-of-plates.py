class StackOfPlates:
    def __init__(self, stack_size):
        self.stacks = []
        self.stack_size = stack_size
        
    def push(self, value):
        
        # Added new stack
        if (len(self.stacks)-1)< self.index_of_push_able_stack():
            self.stacks += [[]]
            
        self.stacks[self.index_of_push_able_stack()] += [value]
        
    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack !!")
            
        self.stacks[len(self.stacks)-1].pop()
        
        if len(self.stacks[len(self.stacks)-1]) == 0:
            self.stacks.pop(len(self.stacks)-1)
            
    def peek(self):
        if self.is_empty():
            raise Exception("Empty Stack !!")
            
        stack = self.stacks[len(self.stacks)-1]
        print(stack[len(stack)-1])
        
    
    def is_empty(self):
        return not bool(self.stacks)
        
    def print_stacks(self):
        print(self.stacks)
        
    def index_of_push_able_stack(self):
        index_number = 0
        for stack in self.stacks:
            if len(stack) != self.stack_size:
                return index_number
            index_number += 1
        
        return index_number
        
        
    
stack = StackOfPlates(2)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)
stack.push(80)
stack.push(0)
stack.push(90)
stack.push(100)
stack.push(50)
stack.push(60)
stack.push(80)


stack.print_stacks()

stack.pop()
stack.pop()
stack.pop()

stack.print_stacks()

stack.peek()