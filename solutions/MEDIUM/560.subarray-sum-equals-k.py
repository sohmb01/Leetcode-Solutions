# Problem ID: 560
# Title: Subarray Sum Equals K
# Runtime: 39 ms

class Solution:
    from collections import defaultdict
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        ans = 0
        mp = defaultdict(int)
        mp [0] = 1
        for num in nums:
            s += num
            ans+= mp[s-k]
            mp[s]+=1 

            
        return ans