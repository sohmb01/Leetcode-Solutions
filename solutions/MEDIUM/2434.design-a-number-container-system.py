# Problem ID: 2434
# Title: Design a Number Container System
# Runtime: 140 ms

class NumberContainers:

    def __init__(self):
        self.indices_numbers = {}
        self.numbers_indices = defaultdict(list)


    def change(self, index: int, number: int) -> None:
        if index in self.indices_numbers:
            n = self.indices_numbers[index]
            if number == n:
                return
        self.indices_numbers[index] = number
        heappush(self.numbers_indices[number],index)
        

    def find(self, number: int) -> int:
        if not len(self.numbers_indices[number]):
            return -1
        while len(self.numbers_indices[number]) and self.indices_numbers[self.numbers_indices[number][0]]!= number:
            heappop(self.numbers_indices[number])
        return self.numbers_indices[number][0] if len(self.numbers_indices[number]) else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)