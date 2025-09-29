# Problem ID: 18
# Title: 4Sum
# Runtime: 502 ms

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                currTarget = target - nums[i] - nums[j]
                l,r = j+1, n-1
                while l<r:
                    if nums[l] + nums[r] == currTarget:
                        temp = (nums[i],nums[j],nums[l],nums[r])
                        ans.add(temp)
                        l+=1
                        r-=1
                    elif nums[l] + nums[r] > currTarget:
                        r-=1
                    else:
                        l+=1
        return list(ans) 