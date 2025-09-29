# Problem ID: 155
# Title: Min Stack
# Runtime: 56 ms

class MinStack:
    min_stack=[]
    stack=[]
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack=[]
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack)<1 or self.min_stack[-1]>=x:
            self.min_stack.append(x)
    def pop(self) -> None:
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack)<1:
            return 0
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()