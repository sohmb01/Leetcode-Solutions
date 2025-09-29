# Problem ID: 2170
# Title: Count Number of Maximum Bitwise-OR Subsets
# Runtime: 235 ms

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        n = len(nums)

        for num in nums :
            maxOr = maxOr | num

        res = [0]
        def bt(i, curr):
            if i == n:
                if curr == maxOr:
                    res[0]+=1
                return
            bt(i+1,curr|nums[i])
            bt(i+1,curr)
        bt(0,0)
        return res[0]

                
