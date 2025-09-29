# Problem ID: 225
# Title: Implement Stack using Queues
# Runtime: 0 ms

class MyStack:

    def __init__(self):
        self.q = deque()
        self.rq = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        while len(self.q)>1:
            self.rq.append(self.q.popleft())
        ret = self.q.popleft()
        self.q,self.rq = self.rq,self.q
        return ret

    def top(self) -> int:
        while len(self.q)>1:
            self.rq.append(self.q.popleft())
        ret = self.q[0]
        self.rq.append(self.q.popleft())
        self.q,self.rq = self.rq,self.q
        return ret


    def empty(self) -> bool:
        return not len(self.q)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()