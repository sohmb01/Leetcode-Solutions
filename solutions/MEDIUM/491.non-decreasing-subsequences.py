# Problem ID: 491
# Title: Non-decreasing Subsequences
# Runtime: 33 ms

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = [[nums[0]]]
        n = len(nums)
        for i in range(1,n):
            temp = []
            for c in ans:
                if c[-1]<=nums[i]:
                    temp.append(c+[nums[i]])
            temp.append([nums[i]])
            ans+=temp
        return [ list(l) for l in {tuple(c) for c in ans} if len(l)!=1 ]

