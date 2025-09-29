# Problem ID: 2320
# Title: Find All K-Distant Indices in an Array
# Runtime: 131 ms

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        n = len(nums)
        keyIndices = []
        for i,num in enumerate(nums):
            if num == key:
                keyIndices.append(i)
        for i in keyIndices:
            
            res |= set(range(max(0,i-k),min(n,i+k+1)))
        return list(res)
            