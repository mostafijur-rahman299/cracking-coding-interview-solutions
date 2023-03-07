class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [None] * (stack_size * 3)
        self.tops = [-1, -1, -1]  # pointers to the tops of the three stacks
    
    def push(self, stack_num, value):
        if self.is_full():
            raise Exception("Stack is full")
        if stack_num < 0 or stack_num > 2:
            raise ValueError("Invalid stack number")
        self.tops[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value
    
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = None
        self.tops[stack_num] -= 1
        return value
    
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        return self.array[self.index_of_top(stack_num)]
    
    def is_empty(self, stack_num):
        return self.tops[stack_num] == -1
    
    def is_full(self):
        return self.tops[2] == self.stack_size - 1
    
    def index_of_top(self, stack_num):
        
        return stack_num * self.stack_size + self.tops[stack_num]
    
    def print_arr(self):
        print(self.array)


stk = ThreeStacks(10)
# stk.print_arr()

stk.push(2, 100)
stk.push(2, 100)
stk.push(2, 100)
stk.push(2, 100)
stk.push(2, 100)
stk.push(2, 100)
stk.push(2, 100)
# stk.push(2, 100)
# stk.push(2, 100)
# stk.push(2, 100)
# stk.push(2, 100)
# stk.push(2, 100)
# stk.print_arr()

stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
stk.push(1, 90)
# stk.print_arr()

stk.push(0, 101)
stk.push(0, 101)
stk.push(0, 101)
stk.push(0, 101)

stk.peek(1)


stk.print_arr()

