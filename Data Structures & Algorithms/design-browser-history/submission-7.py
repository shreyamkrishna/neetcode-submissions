class LinkedNode:
    def __init__(self, val: str, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = LinkedNode(homepage)
        

    def visit(self, url: str) -> None:
        newNode = LinkedNode(url)
        newNode.prev = self.curr
        self.curr.next = newNode
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        i=0
        while i!= steps and self.curr.prev:
            i+=1
            self.curr = self.curr.prev
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        i = 0
        while i!=steps and self.curr.next:
            self.curr = self.curr.next
            i += 1
        
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)