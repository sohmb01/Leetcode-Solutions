# Problem ID: 2856
# Title: Count Complete Subarrays in an Array
# Runtime: 7 ms

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(int)
        l = 0
        res = 0
        distinct = len(set(nums))
        for r in range(n):
            mp[nums[r]] += 1
            while distinct == len(mp):
                res += n - r
                
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    del mp[nums[l]]
                l+=1
        return res