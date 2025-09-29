# Problem ID: 689
# Title: Maximum Sum of 3 Non-Overlapping Subarrays
# Runtime: 184 ms

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = [sum(nums[:k])]
        n = len(nums)
        for i in range(k,n):
            s = sums[-1] + nums[i] - nums[i-k]
            sums.append(s)
        
        memo = {}
        def getMaxSum(i,cnt):
            if cnt==3 or i>n-k:
                return 0
            
            if (i,cnt) in memo:
                return memo[(i,cnt)]
            #include i
            include = sums[i] + getMaxSum(i+k,cnt+1)
            #skip i
            skip =  getMaxSum(i+1,cnt)
            memo[(i,cnt)] = max(include,skip)
            return memo[(i,cnt)]

        ans = []
        i = 0
        while i <= n-k and len(ans)<3:
            include = sums[i] + getMaxSum(i+k,len(ans)+1)
            skip = getMaxSum(i+1,len(ans))
            if include>=skip:
                ans.append(i)
                i+=k
            else:
                i+=1
        return ans