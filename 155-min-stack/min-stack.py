class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_value = float('inf')
        

    def push(self, val: int) -> None:
        self.min_value = min(self.min_value, val)
        self.min_stack.append(self.min_value)
        self.stack.append(val) 
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
            if self.min_stack:
                self.min_value = self.min_stack[-1]
            else:
                self.min_value = float('inf')
        

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