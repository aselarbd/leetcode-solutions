from collections import deque

class MyStack:

    def __init__(self):
        self.primary =  deque([])
        self.secoundary =  deque([])
        

    def push(self, x: int) -> None:
        self.primary.appendleft(x)
        

    def pop(self) -> int:
        while self.primary and len(self.primary) > 1:
             self.secoundary.appendleft(self.primary.pop())
        value =  self.primary.pop()
        self.primary, self.secoundary = self.secoundary, self.primary
        return value
        

    def top(self) -> int:
        return self.primary[0]
        

    def empty(self) -> bool:
        return not self.primary
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()