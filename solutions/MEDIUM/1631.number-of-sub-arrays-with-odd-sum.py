# Problem ID: 1631
# Title: Number of Sub-arrays With Odd Sum
# Runtime: 85 ms

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = []
        last = 0
        mod = (10 ** 9) + 7
        for num in arr:
            prefix.append(num+last)
            last += num
        even, odd, ans = 0, 0, 0
        for p in prefix:
            if p%2:
                odd+=1
                ans+=even
            else:
                even+=1
                ans+=odd
        ans+=odd
        return ans%mod
            
            