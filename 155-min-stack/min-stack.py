class MinStack:

    def __init__(self):
        self.stack = [] # default stack for regular stack operations
        self.min_stack = [] # default stack for special min operations
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack :
            self.min_stack.append(val)
        else :
            val = min(self.min_stack[-1], val)
            self.min_stack.append(val)     

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()