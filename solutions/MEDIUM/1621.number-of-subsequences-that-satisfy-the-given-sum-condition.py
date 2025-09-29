# Problem ID: 1621
# Title: Number of Subsequences That Satisfy the Given Sum Condition
# Runtime: 6715 ms

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        def binSearch(l,r, target):
            while l<r:
                mid = l + (r-l+1)//2
                if nums[mid] <= target:
                    l = mid
                elif nums[mid] > target:
                    r = mid-1
            return l

        mod = 10**9 + 7
        ans = 0
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            if nums[i]>=target:
                break
            j = binSearch(i,n-1,target - nums[i])
            if nums[i]+nums[j] > target:
                continue
            
            ans = (ans + 2**max(0,j-i))%mod
        return ans
