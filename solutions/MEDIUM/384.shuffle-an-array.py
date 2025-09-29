# Problem ID: 384
# Title: Shuffle an Array
# Runtime: 39 ms

class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.arr = nums

    def reset(self) -> List[int]:
        self.arr = self.original
        self.original = list(self.original)
        return self.arr

    def shuffle(self) -> List[int]:
        for i in range(len(self.arr)):
            randomIdx = random.randrange(i, len(self.arr))
            self.arr[i], self.arr[randomIdx] = self.arr[randomIdx], self.arr[i]
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()