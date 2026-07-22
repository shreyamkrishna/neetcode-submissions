class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []
        #print("visit history",self.history)
        #print("visit future", self.future)

    def back(self, steps: int) -> str:
        if steps > len(self.history):
            steps = len(self.history)
        for _ in range(steps):
            self.future.append(self.history[-1])
            self.history = self.history[:-1]
            #print("back history",self.history)
            #print("back future", self.future)
        if not self.history:
            self.history.append(self.future[-1])
        return self.history[-1]

    def forward(self, steps: int) -> str:
        if steps > len(self.future):
            steps = len(self.future)
        for _ in range(steps):
            self.history.append(self.future[-1])
            self.future = self.future[:-1]

            #print("forward history",self.history)
            #print("forward future", self.future)
        #print ("forward current", self.history[-1])
        return self.history[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)