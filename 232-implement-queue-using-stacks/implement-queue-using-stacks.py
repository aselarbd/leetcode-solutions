class MyQueue:

    def __init__(self):
        self.ins = []
        self.outs = []
        

    def push(self, x: int) -> None:
        while self.outs:
            self.ins.append(self.outs.pop())
        self.ins.append(x)
        
        

    def pop(self) -> int:

        while self.ins:
            self.outs.append(self.ins.pop())
        return self.outs.pop()
        

    def peek(self) -> int:
        while self.ins:
            self.outs.append(self.ins.pop())
        return self.outs[-1]
        

    def empty(self) -> bool:
        return not self.ins and not self.outs
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()