# Problem ID: 2626
# Title: Count the Number of Good Subarrays
# Runtime: 139 ms

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        n = len(nums)
        l, r = 0,-1
        mp = defaultdict(int)
        res = 0
        currPairs = 0 
        while l < n-1:
            while currPairs < k and r < n-1:
                r+=1
                currPairs += mp[nums[r]]
                mp[nums[r]]+=1
            if currPairs >= k:
                res+= n-r
            mp[nums[l]]-=1
            currPairs -= mp[nums[l]]
            l+=1
        return res
