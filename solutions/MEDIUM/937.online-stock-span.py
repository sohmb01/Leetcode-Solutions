# Problem ID: 937
# Title: Online Stock Span
# Runtime: 220 ms

class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        if not self.st:
            self.st.append((price,1))
            return 1
        ind = self.st[-1][1] + 1
        while self.st and self.st[-1][0] <= price:
            self.st.pop()
        if self.st:
            ans = ind - self.st[-1][1] 
        else:
            ans = ind
        self.st.append((price,ind))
        print(self.st)
        return ans



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)