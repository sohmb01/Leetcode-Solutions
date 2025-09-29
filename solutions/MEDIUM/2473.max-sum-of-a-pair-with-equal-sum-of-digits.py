# Problem ID: 2473
# Title: Max Sum of a Pair With Equal Sum of Digits
# Runtime: 319 ms

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def sumOfDigits(num):
            s = 0
            while num:
                s+= num%10
                num = num // 10
            return s
        ans = -1
        mp = defaultdict(int)
        for num in nums:
            s = sumOfDigits(num)
            if mp[s]:
                ans = max(ans,mp[s]+num)
                mp[s] = max(mp[s],num)
            else:
                mp[s] = num
            
        return ans