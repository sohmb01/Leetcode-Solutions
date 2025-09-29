# Problem ID: 3241
# Title: Divide Array Into Arrays With Max Difference
# Runtime: 83 ms

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        arrs = n//3
        i = 0
        res = []
        while i<n-2:
            if nums[i+2]-nums[i]>k:
                return []
            res.append(nums[i:i+3])
            i+=3
        return res