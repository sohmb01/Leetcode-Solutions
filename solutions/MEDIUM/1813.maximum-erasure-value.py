# Problem ID: 1813
# Title: Maximum Erasure Value
# Runtime: 199 ms

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        currSum = 0
        mxSum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                currSum-=nums[left]
                seen.remove(nums[left])
                left+=1
            currSum+=nums[right]
            seen.add(nums[right])
            mxSum = max(mxSum,currSum)
        return mxSum
                    