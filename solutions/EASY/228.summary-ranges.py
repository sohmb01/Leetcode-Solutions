# Problem ID: 228
# Title: Summary Ranges
# Runtime: 32 ms

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        n=len(nums)
        i=0
        while i<n:
            a=nums[i]
            j=i+1
            while j<n and nums[j]==nums[j-1]+1:
                j+=1
            j-=1
            if j==i:
                ans.append(str(nums[i]))
            else:
                b=str(nums[i])+"->"+str(nums[j])
                ans.append(b)
            i=j+1
        return ans