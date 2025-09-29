# Problem ID: 3213
# Title: Count Subarrays Where Max Element Appears at Least K Times
# Runtime: 75 ms

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        l,ans = 0,0
        freqInWindow = 0
        for r in range(len(nums)):
            if nums[r] == mx:
                freqInWindow +=1
            while freqInWindow == k:
                if nums[l] == mx:
                    freqInWindow-=1
                l+=1
            ans+=l
        return ans