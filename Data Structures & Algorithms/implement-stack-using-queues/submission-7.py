class MyStack:

    def __init__(self):
        self.ins = deque()
        self.outs = deque()
        

    def push(self, x: int) -> None:
        self.ins.append(x)
        self.outs.append(x)
        

    def pop(self) -> int:
        _ = self.ins.popleft()
        return self.outs.pop()

    def top(self) -> int:
        return self.outs[-1]

    def empty(self) -> bool:
        return True if not self.ins else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()