# Problem ID: 565
# Title: Array Nesting
# Runtime: 80 ms

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        res = 0
        for num in nums:
            cnt = 0
            if num in visited:
                continue
            temp = num
            while temp not in visited:
                cnt+=1
                visited.add(temp)
                temp = nums[temp]
            res = max(cnt,res)
        return res