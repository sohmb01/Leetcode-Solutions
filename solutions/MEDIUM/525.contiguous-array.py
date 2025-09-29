# Problem ID: 525
# Title: Contiguous Array
# Runtime: 103 ms

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        idx = {0:-1}
        for i in range(len(nums)):
            if nums[i]:
                cnt+=1
            else:
                cnt-=1
            if cnt in idx:
                res = max(res,i-idx[cnt])
            else:
                idx[cnt] = i
        return res
            

        
