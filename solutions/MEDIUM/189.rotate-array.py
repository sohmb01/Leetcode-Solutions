# Problem ID: 189
# Title: Rotate Array
# Runtime: 783 ms

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        for i in range(n-k):
            nums.append(nums[i])
        for i in range(n-k):
            nums.pop(0)